class VowelRemover:
    def __init__(self, text):
        "chair"
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]
    def remove_vowels(self):
        i = 0
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i+1:]
            else:
                i +=1
    
        return self.text

# vowel = VowelRemover("aeiou")
# vowel.remove_vowels()
"""
chair -- 
01234

"""