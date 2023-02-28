"""
FelipedelosH
2023

Create to proccess text in Spañish to computate words
"""
class StringProcessor:
    def __init__(self) -> None:
        self.articles = ['el', 'la', 'lo', 'del', 'los', 'las', 'un', 'uno', 'una', 'unas']
        self.prepositions = ['a', 'ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde', 'durante', 'en', 'entre', 'hacia', 'hasta', 'mediante', 'para', 'por', 'según', 'sin', 'so', 'sobre', 'tras', 'versus', 'vía']
        self.adverbs_site = ['aquí', 'allí', 'ahí', 'allá', 'acá', 'arriba', 'abajo', 'cerca', 'lejos', 'adelante', 'delante', 'detrás', 'encima', 'debajo', 'enfrente', 'atrás', 'alrededor']
        self.adverbs_time = ['antes', 'después', 'luego', 'pronto', 'tarde', 'temprano', 'todavía', 'aún', 'ya', 'ayer', 'hoy', 'mañana', 'anteayer', 'siempre', 'nunca', 'jamás', 'próximamente', 'prontamente', 'anoche', 'enseguida', 'ahora', 'anteriormente']
        self.excludeWord = ['y', 'que', 'se', 'es', 'muy']
        self.strangerCharacters = ['.', ':', "\\", '(', ')', "\'", '$', '>', '-', '[', ']', '+']

    def cleanWord(self, word):
        if str(word.strip()) == "":
            return ""

        word = str(word).lower()


        for i in self.strangerCharacters:
            word = word.replace(i, '')

        return word

    def isExcludeWord(self, word):
        """
        Return if the word wanna be exclude becos is not rich language
        """
        word = self.cleanWord(word)
        return word in self.articles or word in self.prepositions or word in self.excludeWord
    