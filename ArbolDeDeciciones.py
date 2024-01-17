"""
arbol la toma de deciciones
"""
class Decicion(object):
    def __init__(self, idPadre, id, titulo, quePaso):
        self.idPadre = idPadre # Dice quien es el padre
        self.id = id # marca unica
        self.titulo = titulo
        self.quePaso = quePaso

class Nodo(object):
    def __init__(self, decicion, hijos):
        self.data = decicion
        self.hijos = hijos

class Arbol:
    def __init__(self):
        self.nickName = ""
        self.nroHojas = 0 # Guarda la cantidad total de hojas
        self.raiz = None

    def addDato(self, x):
        if x.idPadre == 0:
            self.raiz = Nodo(x, [])
            self.nroHojas == self.nroHojas + 1
        else:
            self._addDato(self.raiz, x , x.idPadre)
    def _addDato(self, nodo, x, Idpadre):
        if nodo.data.id == Idpadre:
            nodo.hijos.append(Nodo(x, []))
            self.nroHojas == self.nroHojas + 1
        else:
            for i in nodo.hijos:
                self._addDato(i, x, Idpadre)

    def mostrarArbol(self):
        print(self.nickName)
        self._mostrarArbol(self.raiz)
    def _mostrarArbol(self, nodo):
        if nodo != None:
            txt = str(nodo.data.id)+"\n"
            txt = txt+str(nodo.data.idPadre)+","+self.getAllIdHijos(nodo.hijos)+"\n"
            txt = txt + nodo.data.titulo+"\n"
            txt = txt + nodo.data.quePaso
            print(txt)
            print("============")

            for i in nodo.hijos:
                self._mostrarArbol(i)


    def getAllIdHijos(self, hijos):
        h = []
        for i in hijos:
            h.append(i.data.id)

        return str(h)

"""
a = Arbol()
a.nickName = "nada"

d1 = Decicion(0, 1, "A", "")
d2 = Decicion(1, 2, "B", "")
d3 = Decicion(1, 3, "C", "")
d4 = Decicion(1, 4, "D", "")
d5 = Decicion(1, 5, "E", "")

a.addDato(d1)
a.addDato(d2)
a.addDato(d3)
a.addDato(d4)
a.addDato(d5)

d6 = Decicion(4, 6, "G", "")
a.addDato(d6)

d7 = Decicion(4, 7, "F", "")
a.addDato(d7)

d8 = Decicion(7, 8, "END", "")
a.addDato(d8)


a.mostrarArbol()
"""