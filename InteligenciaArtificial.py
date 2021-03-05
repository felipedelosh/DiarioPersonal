"""
2020 automata pilar

FelipedelosH

Neurona: Es una estructura de nodos interconectados que se mueve un punetero por
medio de simbolos, 


"""
# -⁻- coding: UTF-8 -*-
import os
import threading
import time
from tiempo import *


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
        self.medidor = [] # aqui se guardan los contadores "idContador" : #valor
        self.puntero = "" # aqui se guarda el pivote
        self.haceCuantoFuiActivada = "" # Aqui se guarda la fecha año mes dia
        self.conjuntoDeReglas = {} # Esto indica como deben de moverse los medidores


        self.inizializar()

    def inizializar(self):
        self.simbolos = self.cargarElementos("simbolos.txt")
        self.nodo = self.cargarElementos("nodos.txt")
        self.puntero = self.nodo[0]
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

        medidor = self.cargarElementos("medidores.txt")


        for i in medidor:
            if i.strip() != "":
                self.medidor.append((i.split(":")[0], int(i.split(":")[1])))


        self.haceCuantoFuiActivada = self.cargarElementos("haceCuantoFuiActivada.txt")[0]

        conjuntoDeReglas = self.cargarElementos("conjuntoDeReglas.txt")

        for i in conjuntoDeReglas:
            if i.strip() != "":
                nodo = i.split(":")[0]
                # Se guarda la conexion {nodo:[medidor1, medidor2, medidor3]}
                self.conjuntoDeReglas[nodo] = [int(i.split(":")[1]), int(i.split(":")[2]), int(i.split(":")[3]), int(i.split(":")[4])]

    def realizarMovimiento(self, simbolo, tiempo):
        """
        Entra un simbolo y el pivote se mueve y ejecuta las reglas
        luego de ello se actualiza la informacion de activaion

        """
        for i in self.aristras[self.puntero]:
            if i[1] == simbolo:
                # Se hace el salto
                self.puntero = i[0]
                # Se aplica la regla:
                contador = 0
                for j in self.conjuntoDeReglas[self.puntero]:
                    temp = self.medidor[contador][0], self.medidor[contador][1] + j
                    self.medidor[contador] = temp
                    contador = contador + 1
                break

        print(self.puntero)
        print(self.medidor)
    
    
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

    def actualizarElemento(self, elento, valor):
        
        try:
            pass
        except:
            pass
        


        








class Cerebro:
    """
    Es un conjunto de neuronas, desde aqui son controladas.
    El cerebro ejecuta el conjunto de reglas de cada neurona
    """
    def __init__(self):
        self.tiempo = Tiempo() # El cerebro tiene que saber la fecha y hora para trabajar
        self.neuronaMonitoreadoraDeSueño = NeuronaContadora("MonitoreadoraDeSueño")


        self.hilo = threading.Thread(target=self.actividadNeuronal)
        self.hilo.start()


    def actividadNeuronal(self):
        """
        Si una neurona no se activa en x tiempo... se activa de nuevo
        """
        while True:
            # Verificar el Estados

            # Verificar la neurona que lee el sue+o
        
            print("estoy vivo")
            if not self.tiempo.estampaDeTiempo() != self.neuronaMonitoreadoraDeSueño.haceCuantoFuiActivada:
                print("Neurona Monitora de sue+o activada")
                self.neuronaMonitoreadoraDeSueño.realizarMovimiento("1", self.tiempo.estampaDeTiempo())
                self.neuronaMonitoreadoraDeSueño.realizarMovimiento("0", self.tiempo.estampaDeTiempo())
                self.neuronaMonitoreadoraDeSueño.realizarMovimiento("1", self.tiempo.estampaDeTiempo())
                self.neuronaMonitoreadoraDeSueño.realizarMovimiento("0", self.tiempo.estampaDeTiempo())
                self.neuronaMonitoreadoraDeSueño.realizarMovimiento("0", self.tiempo.estampaDeTiempo())
            time.sleep(5)




c = Cerebro()


       