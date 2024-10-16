"""
FelipedelosH
2024

Create to proccess text in Spañish to computate words
"""
class StringProcessor(object):
    def __init__(self, env) -> None:
        self.alphabet = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚabcdefghijklmnñopqrstuvwxyzáéíóú")
        self.shift = 13
        try:
            self.shift = self.calculateShift(env) % len(self.alphabet)
        except:
            pass
        self.articles = ['el', 'la', 'lo', 'del', 'los', 'las', 'un', 'uno', 'una', 'unas']
        self.prepositions = ['a', 'ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde', 'durante', 'en', 'entre', 'hacia', 'hasta', 'mediante', 'para', 'por', 'según', 'sin', 'so', 'sobre', 'tras', 'versus', 'vía']
        self.adverbs_site = ['aquí', 'allí', 'ahí', 'allá', 'acá', 'arriba', 'abajo', 'cerca', 'lejos', 'adelante', 'delante', 'detrás', 'encima', 'debajo', 'enfrente', 'atrás', 'alrededor']
        self.adverbs_time = ['antes', 'después', 'luego', 'pronto', 'tarde', 'temprano', 'todavía', 'aún', 'ya', 'ayer', 'hoy', 'mañana', 'anteayer', 'siempre', 'nunca', 'jamás', 'próximamente', 'prontamente', 'anoche', 'enseguida', 'ahora', 'anteriormente']
        self.excludeWord = ['al', 'y', 'como','o','le', 'que', 'se', 'ese', 'su', 'es', 'me', 'muy', 'te', 'fue', 'xq', 'más', 'mas', 'tan', 'pero']
        self.strangerCharacters = ['.txt', ',', '?', '*', ':', "\\", '\n', '(', ')', "\'", '$', '>', '-', '[', ']', '+', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def cleanWord(self, word):
        """
        Enter a txt and clean stranger things
        """
        if str(word.strip()) == "":
            return ""

        word = str(word).lower()

        for i in self.strangerCharacters:
            word = word.replace(i, '')

        word = word.lstrip()
        word = word.rstrip()

        return word

    def isExcludeWord(self, word):
        """
        Return if the word wanna be exclude becos is not rich language
        """
        return word in self.articles or word in self.prepositions or word in self.excludeWord


    def groupTextByWords(self, txt):
        data = {}

        for i in str(txt).split(" "):
            _w = self.cleanWord(i)
            if not self.isExcludeWord(_w):
                if _w not in data.keys():
                    data[_w] = 0
                data[_w] = data[_w] + 1


        return data
    
    def calculateShift(self, env):
        return int(env, 16)
    
    def enigmaMachineEncrypt(self, plain_text):
        "'TIP: 1942 HH"
        encrypted_text = ''
        for char in plain_text:
            if char in self.alphabet:
                index = (self.alphabet.index(char) + self.shift) % len(self.alphabet)
                encrypted_text += self.alphabet[index]
            else:
                encrypted_text += char
        return encrypted_text
    

    def enigmaMachineDecript(self, encrypted_text):
        """
        Remeber: NEW FAGOT CAN'T READ IT
        """
        decrypted_text = ''
        for char in encrypted_text:
            if char in self.alphabet:
                index = (self.alphabet.index(char) - self.shift) % len(self.alphabet)
                decrypted_text += self.alphabet[index]
            else:
                decrypted_text += char
        return decrypted_text
