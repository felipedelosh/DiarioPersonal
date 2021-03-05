"""
2020 automata pilar

FelipedelosH

Neurona: Es una estructura de nodos interconectados que se mueve un punetero por
medio de simbolos, 


"""
import os


class NeuronaContadora(object):
    def __init__(self, nombreNeurona):
        """
        Se constriye una neurona contadora
        """
        self.rutaDelProyecto = str(os.path.dirname(os.path.abspath(__file__))) # En donde estoy padado
        self.nombreNeurona = nombreNeurona
        self.simbolos = [] # Aca se gardan 
        self.nodo = [] # Acá se guardan los IDnodo Ejemplo A,B..Z NO1
        self.aristras = {} # Aca se guandan los caminos (Destino, simbolo)
        self.conjuntoDeSimbolos = []
        self.medidor = {} # aqui se guardan los contadores "idContador" : #valor

        self.inizializar()

    def inizializar(self):
        self.simbolos = self.cargarElementos("simbolos.txt")
        self.nodo = self.cargarElementos("nodos.txt")
        aristas = self.cargarElementos("aristas.txt")
        for i in aristas:
            if i.strip() != "":
                nodo = i.split(":")[0]
                # Se guarda la conexion {nodo:(nodo, simbolo)}
                if nodo in self.aristras:

                    temp = self.aristras[nodo]
                    temp.append((i.split(":")[1], i.split(":")[2]))

                else:
                    self.aristras[nodo] = [(i.split(":")[1], i.split(":")[2])]


    def cargarElementos(self, elemento):
        """
        Entra el nombre de un NERONA/LAqueSeaMierda.txt

        """
        ruta = self.rutaDelProyecto + "\\DATA"  + "\\NEURONAS\\" + self.nombreNeurona + "\\"

        informacion = []

        try:

            f = open(ruta+elemento, "r", encoding="UTF-8")

            for i in f.read().split("\n"):
                if i.strip() != "":
                    informacion.append(i)

            return informacion
        except:
            return informacion
        


        








class Cerebro:
    """
    Es un conjunto de neuronas, desde aqui son controladas.
    """
    def __init__(self):
        self.neuronaMonitoreadoraDeSueño = NeuronaContadora("MonitoreadoraDeSueño")


c = Cerebro()


       