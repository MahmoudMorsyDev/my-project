class GrammarStats:
    def __init__(self):
        self.checks = []
        pass

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if text[0].isupper() and text[-1] == '.':
            self.checks.append(1)
            return True
        else:
            self.checks.append(0)
            return False    

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        return int((sum(self.checks) / len(self.checks)) * 100)