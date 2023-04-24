
def grammar_checker(text):
    """Checks for grammatical mistakes (i.e. First letter is a capital 
        sentence ends with a period). 
    Parameters: 
        text: Text to be checked
    Returns: 
        a boolean stating if the text is grammatically correct
    Side Effects:
        Not all grammar mistakes are checked    
    """
    return text[0].isupper() and text[-1] == "."