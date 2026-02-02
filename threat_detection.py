#importing all the libraries
import re
from collections import defaultdict
from typing import Dict, List


"""
    this class is used for identifying the malicious patterns
    and threats in input text
    """
    
class threatdetective:
    

    def __init__(self):
        

        # pattern used to detect SQL injections
        self.sql_pattern = re.compile(
            r"(?:--|;|'|\"|\bOR\b|\bAND\b|\bDROP\b|\bDELETE\b|\bINSERT\b|\bUPDATE\b|\bSELECT\b).*(?:TABLE|FROM|WHERE)",
            re.IGNORECASE,
        )

        #this is the pattern used to detec XSS 
        self.xss_pattern = re.compile(
            r"<script|javascript:|onerror=|onload=|onclick=|<iframe|eval\(|document\.|window\.",
            re.IGNORECASE,
        )

        #pattern used to detect directory traversal attempts
        self.traversal_pattern = re.compile(r"\.\./|\.\.\\|/etc/passwd|/etc/shadow")

       #checks whether a given string contains any known malicious patterns
       
    def is_safe(self, content: str) -> bool:


        #checks for SQL injection patterns
        
        if self.sql_pattern.search(content):
            return False



        #check for XSS attack patterns

        if self.xss_pattern.search(content):
            return False

        # check for path traversal patterns
        
        if self.traversal_pattern.search(content):
            return False

       
        return True


    """
        this function scans the entire input text 
        and extracts all detected threat patterns
        """
        
    def scan_threats(self, content: str) -> Dict[str, List[str]]:
       
        findings = defaultdict(list)

       
        for match in self.sql_pattern.finditer(content):
            findings["sql_injection"].append(match.group().strip())

       
        for match in self.xss_pattern.finditer(content):
            findings["xss"].append(match.group().strip())

        
        for match in self.traversal_pattern.finditer(content):
            findings["path_traversal"].append(match.group().strip())

        return dict(findings)
