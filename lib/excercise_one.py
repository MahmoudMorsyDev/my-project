
def estimate_reading_time(text, words_per_minute):
    """calculates the times in minutes the user needs to read the given text 
    Parameters: 
        text: a string containing the text that the user wants to calculate the reading time for 
        words_per_minute: rate at which the user reads (words/minute) 
    Returns: 
        a string describing the time required to read the given text
    Side Effects:
        this function doesn't have any side effects     
    """
    if type(text) == str:
        estimate_time = len(text.split(" "))/words_per_minute
        return f'Your estimate time is {round(estimate_time, 2)} minutes'
    else: 
        raise Exception("Text given should be a string!")