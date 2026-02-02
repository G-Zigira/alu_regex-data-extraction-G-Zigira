# importing all the libraries the file needs 
import re
import json
from typing import Dict, List
from collections import defaultdict
from threat_detection import threatdetective
from data_hider import datahider
from json_builder import building_final_json


class FileScanner:
    """
    This class is responsible for scanning a text file and extracting
    structured data using regular expressions while applying security checks.
    """

    def __init__(self):
        
        self.threat_checker = threatdetective()
        self.masker = datahider()

        # this section contains the regular expressions used to loctate specific data patterns
        self.email_regex = re.compile(r"\b[a-zA-Z0-9][a-zA-Z0-9._-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b")
        
        self.url_regex = re.compile(r"https?://[^\s]+")
        
        self.card_regex = re.compile(r"\b(?:\d{4}[-\s]?){3}\d{4}\b")
        
        self.time_regex = re.compile(r"\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?(?:AM|PM))?\b")
        
        self.tag_regex = re.compile(r"<[a-zA-Z][^>]*>")
        
        self.hashtag_regex = re.compile(r"#[a-zA-Z][a-zA-Z0-9_]*\b")
        
        
        self.money_regex = re.compile(r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?\b")


    """
        this function extracts valid data from the given text using regex patterns and
        each extracted value is checked for malicious content before being stored
        """
    def extract_and_validate(self, content: str) -> Dict[str, List[str]]:
       
        output = defaultdict(list)

        #extracts and hides email addresses
        for match in self.email_regex.finditer(content):
            email = match.group()
            
            if self.threat_checker.is_safe(email):
                masked = self.masker.hide_sensitive(email, "email")
                output["emails"].append(masked)
                

        # extracts and hides credit card numbers
        for match in self.card_regex.finditer(content):
            card = match.group()
            if self.threat_checker.is_safe(card):
                masked = self.masker.hide_sensitive(card, "credit_card")
                output["credit_cards"].append(masked)

        # extracts URLs
        for match in self.url_regex.finditer(content):
            url = match.group()
            if self.threat_checker.is_safe(url):
                output["urls"].append(url)

        # extracts time values
        for match in self.time_regex.finditer(content):
            output["times"].append(match.group())


        #extracts HTML tags
        for match in self.tag_regex.finditer(content):
            tag = match.group()
            if self.threat_checker.is_safe(tag):
                output["html_tags"].append(tag)
                

        #extracts hashtags
        for match in self.hashtag_regex.finditer(content):
            output["hashtags"].append(match.group())

        #extract currency
        for match in self.money_regex.finditer(content):
            output["currency"].append(match.group())

        return dict(output)


"""
    this is the main function of the program which reads the file
    processes its contents, and saves the results as JSON
    """
    
def main():
    
    file_name = "dummyinput.txt"

    try:
        
        with open(file_name, "r", encoding="utf-8") as f:
            raw_text = f.read()


        extractor = FileScanner()

        extracted = extractor.extract_and_validate(raw_text)


        threats = extractor.threat_checker.scan_threats(raw_text)


        final_output = building_final_json(extracted, threats)

        with open("ResultsofScanning.json", "w", encoding="utf-8") as out:
            json.dump(final_output, out, indent=2)

        print("The scanning is complete the outputs were saved to the JSON")

    except FileNotFoundError:
        print("Input error the file was not found")
    except Exception as err:
        print(f"Unexpected error: {err}")


if __name__ == "__main__":
    main()
