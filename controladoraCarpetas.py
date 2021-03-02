"""
Esto controla todo lo referente a la creacion de carpetas 
y verificacion de que las carpetas existan
"""

import os
from os import scandir

class ControladoraCarpetas(object):
    def __init__(self, tiempo, rutaDelProyecto):
        self.tiempo = tiempo
        self.rutaDelProyecto = rutaDelProyecto

    def crearYVerificarCarpetas(self):
        if not os.path.isdir(self.rutaDelProyecto+"\\DATA"): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA")

        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\DIARIO"): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\DIARIO")
        
        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\DIARIO\\"+str(self.tiempo.año())): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\DIARIO\\"+str(self.tiempo.año()))

        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\SENTIMIENTOS"): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\SENTIMIENTOS")

        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\SENTIMIENTOS\\"+str(self.tiempo.año())): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\SENTIMIENTOS\\"+str(self.tiempo.año()))

        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\NOTAS"): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\NOTAS")

        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\RESULTADOANUAL"): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\RESULTADOANUAL")

        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\ACTIVIDADES"): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\ACTIVIDADES")

        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\ACTIVIDADES\\"+str(self.tiempo.año())): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\ACTIVIDADES\\"+str(self.tiempo.año()))

        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\ECONOMIA"): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\ECONOMIA")

        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\ECONOMIA\\"+str(self.tiempo.año())): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\ECONOMIA\\"+str(self.tiempo.año()))

        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\ECONOMIA\\CAJA"): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\ECONOMIA\\CAJA")

        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\DISTRIBUCIONTIEMPO"): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\DISTRIBUCIONTIEMPO")

        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO"): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO")

        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\"+str(self.tiempo.año())): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\"+str(self.tiempo.año()))

        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\HORARIO"): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\HORARIO")

        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\HORARIO\\"+str(self.tiempo.año())): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\HORARIO\\"+str(self.tiempo.año()))

        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\DECICIONES"): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\DECICIONES")

        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\PERFIL"): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\PERFIL")
        

    def listarTodosLosArchivosdeCarpeta(self, ruta, extension):
        """
        Retorna el nombre de todos los archivos.extension de una carpeta
        """
        nombreArchivos = []
        for i in scandir(ruta):
            if i.is_file():
                if extension in i.name:
                    nombreArchivos.append(i.name)
        return nombreArchivos

    def listarAñosDeRegistroSentimientos(self):
        """
        Retorna ['año', 'año', 'año' ...]
        de los años que hay registrados en DATA/SENTIMIENTOS
        """
        años = []
        #self.rutaDelProyecto+"\\DATA\\SENTIMIENTOS"
        for i in scandir("DATA\\SENTIMIENTOS"):
            if i.is_dir():   
                años.append(i.name)
        return años

    def listarAñosDeEconomia(self):
        años = []
        #self.rutaDelProyecto+"\\DATA\\SENTIMIENTOS"
        for i in scandir("DATA\\ECONOMIA"):
            if i.is_dir() and i.name != "CAJA":   
                años.append(i.name)
        return años

    

    def cargarEstadosEmocionanes(self):
        """
        Se retorna el contenido de  RECURSOS/estadosEmocionales.txt
        En caso de error se retornan las emociones basicas
        """
        try:
            
            estadosEmocionales = []
            f = open(self.rutaDelProyecto+"\\RECURSOS\\estadosEmocionales.txt", 'r', encoding="UTF-8")
            for i in f.read().split("\n"):
                if i.split() != "":
                    estadosEmocionales.append(i)
            
            return estadosEmocionales
        except:
            return ['tristeza', 'tranquilidad', 'ira', 'miedo', 'hostilidad', 'desesperanza', 'frustración', 'odio', 'culpa', 'celos', 'felicidad', 'alegría', 'amor', 'gratitud', 'esperanza', 'Asco', 'Suicida']


    def cargarActividades(self):
        """
        Se retorna el contenido de RECURSOS/actividades.txt
        en caso de error se retornan las basicas
        """
        try:
            actividades = []
            f = open(self.rutaDelProyecto+"\\RECURSOS\\actividades.txt", 'r', encoding="UTF-8")
            for i in f.read().split("\n"):
                if i.split() != "":
                    actividades.append(i)
            
            return actividades

        except:
            return ['dormir', 'trabajar', 'deporte']

    def crearCarpetaEnDeciociones(self, txt):
        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\DECICIONES\\"+str(txt)): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\DECICIONES\\"+str(txt))
            return True
        else:
            return False
