"""
Esto controla todo lo referente a la creacion de carpetas 
y verificacion de que las carpetas existan
"""

import os
import json
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

        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\DREAMS"): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\DREAMS")

        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\DREAMS\\"+str(self.tiempo.año())): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\DREAMS\\"+str(self.tiempo.año()))

        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\PEOPLE"): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\PEOPLE")

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

        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\NEURONAS"): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\NEURONAS")
        

        if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\USOS"): # No existe la carpera creelas
            os.mkdir(self.rutaDelProyecto+"\\DATA\\USOS")

    def listarTodosLosArchivosdeCarpeta(self, ruta, extension):
        """
        Retorna el nombre de todos los archivos.extension de una carpeta
        """
        nombreArchivos = []
        
        try:
            for i in scandir(ruta):
                if i.is_file():
                    if extension in i.name:
                        nombreArchivos.append(i.name)
        except:
            pass

        return nombreArchivos
    

    def get_all_triggers(self):
        """
        return all .json infolder DATA/TRIGGERS/*.json
        """
        _path = self.rutaDelProyecto + "\\DATA\\TRIGGERS"
        _file_names = self.listarTodosLosArchivosdeCarpeta(_path, ".json")

        data = []
        for i in _file_names:
            try:
                brute_data = self.getTextInFile(_path + "\\" + i)
                data.append(json.loads(brute_data))
            except:
                pass

        return data





    def listOfAllYearWriteInDiary(self):
        """
        return all years to the user write the diary pages in string
        example: [2020,2021...]
        """
        years = []
        path = self.rutaDelProyecto + "\\DATA\\DIARIO"

        for i in scandir(path):
            try:
                if i.is_dir() and int(i.name) > 0:
                     years.append(i.name) 
            except:
                pass

        return years
    

    def listOfAllYearWriteInDreams(self):
        """
        return all years to the user write the dream diary pages in string
        example: [2020,2021...]
        """
        years = []

        path = self.rutaDelProyecto + "\\DATA\\DREAMS"
        for i in scandir(path):
            try:
                if i.is_dir() and int(i.name) > 0:
                     years.append(i.name) 
            except:
                pass

        return years
    
    def getTitlesOfAllDreams(self):
        """
        return [DATE-DREAM, DATE-DREAM, DATE-DREAM,DATE-DREAM ....]
        Get all Titles of Dreams in all 
        """
        _y = self.listOfAllYearWriteInDreams()

        output = []

        for i in _y:
            try:
                path = self.rutaDelProyecto + "\\DATA\\DREAMS\\" + i
                _titles = self.listarTodosLosArchivosdeCarpeta(path, ".txt")
                for x in _titles:
                    output.append(x)
            except:
                pass

        return output
    
    def listOfAllPeople(self):
        """
        return all people in the people folder
        """
        people = []

        path = self.rutaDelProyecto + "\\DATA\\PEOPLE"
        for i in scandir(path):
            try:
                if i.is_dir():
                    people.append(i.name)
            except:
                pass

        return people
    
    def listOfAllPeopleAlias(self):
        """
        return ALL alias in a people folder
        """
        _all_people = []
        data = []

        for i in self.listOfAllPeople():
            path = self.rutaDelProyecto + "\\DATA\\PEOPLE\\" + i + "\\alias.txt"
            _data = self.getTextInFile(path)
            data.append(_data)

        return data
    

    def listOfNamePeopleAndAlias(self):
        """
        return ALL 'Name: alias' in a people folder
        """
        _all_people = []
        data = []

        for i in self.listOfAllPeople():
            path = self.rutaDelProyecto + "\\DATA\\PEOPLE\\" + i + "\\alias.txt"
            _data = self.getTextInFile(path)
            data.append(i+": "+_data)

        return data



    def listarAñosRegistradosDistribucionDeTiempo(self):
        """
        Retorna ['año', 'año', 'año' ...]
        de los años registrados en DATA\DISTRIBUCIONTIEMPO\TIEMPODIARIO
        """
        años = []

        for i in scandir(self.rutaDelProyecto+"\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO"):
            try:
                if i.is_dir() and int(i.name) > 0:   
                    años.append(i.name)    
            except:
                pass

        return años

    def listarAñosDeRegistroSentimientos(self):
        """
        Retorna ['año', 'año', 'año' ...]
        de los años que hay registrados en DATA/SENTIMIENTOS
        """
        años = []
        
        for i in scandir(self.rutaDelProyecto+"\\DATA\\SENTIMIENTOS"):
            if i.is_dir():   
                años.append(i.name)
        return años

    def listarAñosDeEconomia(self):
        años = []


        for i in scandir(self.rutaDelProyecto+"\\DATA\\ECONOMIA"):
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


    def createPeopleFolder(self, nameFoler):
        try:
            # Exists?
            nameFoler = str(nameFoler).lower()
            if not os.path.isdir(self.rutaDelProyecto+"\\DATA\\PEOPLE\\"+nameFoler):
                os.mkdir(self.rutaDelProyecto+"\\DATA\\PEOPLE\\"+nameFoler)
            return True
        except:
            return False
        

    def getTextInFile(self, path):
        """
        Enter a path to open file and return text
        """
        data = ""

        try:
            with open(path, encoding="UTF-8") as f:
                data = f.read()
        except:
            pass

        return data  
