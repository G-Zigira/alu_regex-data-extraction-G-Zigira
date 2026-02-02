import re

"""
    i used this class to just hide  sensitive data from the textfile
    before it is written to output files or logs
    """
    
class datahider:
    
    # the function in question
    def hide_sensitive(self, value: str, category: str) -> str:
        
        # hidres credit card numbers 
        
        if category == "credit_card":
            return re.sub(r"\d", "*", value[:-4]) + value[-4:]
        
        # hides emails

        if category == "email":
            parts = value.split("@")
            if len(parts) == 2:
                name = parts[0]
                masked = name[0] + "*" * (len(name) - 1)
                return f"{masked}@{parts[1]}"
        
        return value
