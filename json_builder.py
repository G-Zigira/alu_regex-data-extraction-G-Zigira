"""
    thuis file as the name suggests builds the final structured JSON
    the function ensures that both threats and extracted data appear
    in an oragnised manner
    
    """
    
    
def building_final_json(extracted_data: dict, threats: dict) -> dict:
    
    #this segment arranges the threats

    ordered_threats = {
        "list of path traversal": threats.get("path_traversal", []),
        "list of xss": threats.get("xss", []),
        "listr of sql_injection": threats.get("sql_injection", [])
    }
    # this is just to arrange the extracted data
    ordered_data = {
        "list of emails": extracted_data.get("emails", []),
        "list of credit cards": extracted_data.get("credit_cards", []),
        "list of urls": extracted_data.get("urls", []),
        "list of times": extracted_data.get("times", []),
        "list of hashtags": extracted_data.get("hashtags", []),
        "list of currency": extracted_data.get("currency", [])
    }
    
    # thus return function builds and returns the final json stucture
    return {
        "Number of threats found": sum(len(v) for v in ordered_threats.values()),
        "threats": ordered_threats,
        "count of extracted data found": sum(len(v) for v in ordered_data.values()),
        "extracted data": ordered_data
    }
