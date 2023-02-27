"""
FelipedelosH
2023

Create to proccess text in Spañish to computate words
"""
class StringProcessor:
    def __init__(self) -> None:
        self.articles = ['el', 'la', 'lo', 'del', 'los', 'la', 'un', 'uno', 'una', 'unas']
        self.prepositions = ['a', 'ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde', 'durante', 'en', 'entre', 'hacia', 'hasta', 'mediante', 'para', 'por', 'según', 'sin', 'so', 'sobre', 'tras', 'versus', 'vía']


    def isExcludeWord(self, word):
        """
        Return if the word wanna be exclude becos is not rich language
        """
        word = str(word).lower()
        return word in self.articles or word in self.prepositions
    