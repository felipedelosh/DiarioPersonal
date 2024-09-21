"""
Esto controla todo lo referente a la creacion de carpetas 
y verificacion de que las carpetas existan
"""

import os
import json
from os import scandir
from StringProcessor import *

class ControladoraCarpetas(object):
    def __init__(self, tiempo, rutaDelProyecto, env):
        self.stringProcessor = StringProcessor(env)
        self.tiempo = tiempo
        self.rutaDelProyecto = rutaDelProyecto

    def crearYVerificarCarpetas(self):
        carpetas = [
            "DATA",
            "DATA\\DIARIO", 
            f"DATA\\DIARIO\\{self.tiempo.año()}",
            "DATA\\DREAMS",
            f"DATA\\DREAMS\\{self.tiempo.año()}",
            "DATA\\PEOPLE",
            "DATA\\SENTIMIENTOS",
            f"DATA\\SENTIMIENTOS\\{self.tiempo.año()}",
            "DATA\\NOTAS",
            "DATA\\RESULTADOANUAL",
            "DATA\\ACTIVIDADES",
            f"DATA\\ACTIVIDADES\\{self.tiempo.año()}",
            "DATA\\ECONOMIA",
            f"DATA\\ECONOMIA\\{self.tiempo.año()}",
            "DATA\\ECONOMIA\\CAJA",
            "DATA\\DISTRIBUCIONTIEMPO",
            "DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO",
            f"DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\{self.tiempo.año()}",
            "DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\HORARIO",
            f"DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\HORARIO\\{self.tiempo.año()}",
            "DATA\\PERFIL",
            "DATA\\NEURONAS",
            "DATA\\USOS",
            "DATA\\DRUGS",
            f"DATA\\DRUGS\\{self.tiempo.año()}",
            "DATA\\WORK"
        ]

        for carpeta in carpetas:
            ruta_completa = os.path.join(self.rutaDelProyecto, carpeta)
            if not os.path.isdir(ruta_completa):
                os.mkdir(ruta_completa)


    def saveDiaryPage(self, path, txt):
        try:
            txt = self.stringProcessor.enigmaMachineEncrypt(txt)
            with open(path, "a", encoding="UTF-8") as f:
                f.write(txt)

            return True
        except:
            return False

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
    

    def listALLFolderInPath(self, path):
        """
        Enter a x/y/z and return ['Folder1',... 'FolderN']
        """
        folders = []

        try:
            for i in scandir(path):
                if i.is_dir():
                    folders.append(i.name)
        except:
            pass

        return folders
    

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
    
    def listOfAllYearsInDrugs(self):
        """
        Return all yers to the user register DRUGS
        """
        YYYY = []
        _path = f"{self.rutaDelProyecto}\\DATA\\DRUGS"

        for i in scandir(_path):
            try:
                if i.is_dir() and int(i.name) > 0:
                    YYYY.append(i.name)
            except:
                pass

        return YYYY

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

        _sep = self.getSimbolikPathSeparator()

        path = f"{self.rutaDelProyecto}{_sep}DATA{_sep}PEOPLE"
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

    def getAllYearsOfDrugs(self):
        """
        Return [YYYY, YYYY, YYYY] in DATA\DRUGS
        """
        YYYY = []
        for i in scandir(f"{self.rutaDelProyecto}\\DATA\\DRUGS"):
            try:
                if i.is_dir() and int(i.name) > 0:   
                    YYYY.append(i.name)    
            except:
                pass

        return YYYY

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
        """
        return [YYYY, ...YYYY]
        GET ALL YYYY folder names in \\DATA\\ECONOMIA
        """
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
        
    def loadIndexOfActivity(self, activity):
        """
        Enter a activity:str and return the index # of this activity
        """
        allActivities = self.cargarActividades()
        counter = 0
        for i in allActivities:
            if i == activity:
                return counter

            counter = counter + 1

        return None


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
        

    def getAllDrugs(self):
        """
        Load RECURSOS\drugs.txt and return all drugs
        """
        drugs = []
        try:
            path = self.rutaDelProyecto + "\\RECURSOS\\drugs.txt"

            temp = self.getTextInFile(path)
            for i in temp.split("\n"):
                drugs.append(i)
        except:
            pass
        

        return drugs
    
    def saveDrug(self, drug_title, drug_detonate, drug_feel):
        try:
            YYYY = self.tiempo.año()

            path = self.rutaDelProyecto + "\\DATA\\DRUGS\\" + str(YYYY) + "\\" + drug_title + " - " + self.tiempo.estampaDeTiempo() + ".txt"

            # Exists ???
            data = ""
            try:
                with open(path, 'r', encoding="UTF-8") as f:
                    data = f.read()
            except:
                pass
            
            with open(path, 'w', encoding="UTF-8") as f:
                f.write(drug_detonate + "\n\n\n" + drug_feel + "\n" + self.tiempo.hora() + "\n" + data)    

            return True
        except:
            return False
        
    def saveWork(self, args):
        try:
            _PATH = self.rutaDelProyecto+"\\DATA\\WORK\\"

            # Create foldername Exists?
            _nameFoler = str(args['nameOfWork']).lower()

            if not os.path.isdir(_PATH+_nameFoler):
                os.mkdir(_PATH+_nameFoler)

            with open(_PATH+_nameFoler+"\\PO.txt", 'w', encoding="UTF-8") as f:
                f.write(args['nameOfProductOwner'])

            _bool_description = self.appendTextInFile(_PATH+_nameFoler+"\\description.txt",args['description'])
            _bool_tools = self.appendTextInFile(_PATH+_nameFoler+"\\tools.txt",args['tools'])
            

            with open(_PATH+_nameFoler+"\\deliveryEND.txt", 'w', encoding="UTF-8") as f:
                f.write(args['deliveryEND'])

            with open(_PATH+_nameFoler+"\\costPeerHour.txt", 'w', encoding="UTF-8") as f:
                f.write(args['costPeerHour'])

            with open(_PATH+_nameFoler+"\\status.txt", 'w', encoding="UTF-8") as f:
                f.write("open")

            return _bool_description and _bool_tools
        except:
            return False
        

    def loadSpecifyWork(self, folderName):
        """
        Read DATA/WORK/* and return all information in dic
        """
        try:
            path = self.rutaDelProyecto+"\\DATA\\WORK\\"+folderName

            if not os.path.isdir(path):
                return False
            
            _projectName = folderName

            _productOwner = ""
            with open(path+"\\PO.txt", "r", encoding="UTF-8") as f:
                _productOwner = f.read()

            _status = ""
            with open(path+"\\status.txt", "r", encoding="UTF-8") as f:
                _status = f.read()         
            
            return {
                "project_name" : _projectName,
                "product_owner" : _productOwner,
                "status":_status
            }
        except:
            return False


    def saveIncOfWork(self, concept, hours, projectName):
        try:
            _path = f"{self.rutaDelProyecto}\\DATA\\WORK\\{projectName}"

            # Save the concept of work
            conceptWork = ""
            try:
                with open(_path+"\\concept.txt", 'r', encoding="UTF-8") as f:
                    conceptWork = f.read()
            except:
                pass

            # Save the concept
            with open(_path+"\\concept.txt", 'w', encoding="UTF-8") as f:
                if conceptWork != "":
                    f.write(f"{conceptWork}\n{concept}")
                else:
                    f.write(f"{concept}")            

            # Load previuos hours worked
            dataHours = ""
            try:
                with open(_path+"\\hours.txt", 'r', encoding="UTF-8") as f:
                    dataHours = f.read()
            except:
                pass

            # Save this hours
            with open(_path+"\\hours.txt", 'w', encoding="UTF-8") as f:
                if dataHours != "":
                    f.write(f"{dataHours}\n{hours}")
                else:
                    f.write(f"{hours}")
            
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


    def getTextInFileDecrypt(self, path):
        """
        Enter a path to open file and return text
        """
        data = "Newfags can't read it"

        try:
            with open(path, encoding="UTF-8") as f:
                data = f.read()
                data = self.stringProcessor.enigmaMachineDecript(data)
        except:
            pass

        return data


    def appendTextInFile(self, path, data):
        """
        Enter a path and append the text if exits or create ig not exists
        """
        try:

            _original_data = ""

            try:
                with open(path, 'r', encoding="UTF-8") as f:
                    _original_data = f.read()
            except:
                pass

            _save_data = ""
            if not _original_data == "":
                _save_data = _original_data + "\n" + data
            else:
                _save_data = data


            with open(path, 'w', encoding="UTF-8") as f:
                f.write(_save_data)

            return True
        except:
            return False


    def getSimbolikPathSeparator(self):
        """
        In Some SO usages / or \ to separates folder PATH
        """
        _simbolikSep = "\\"

        if _simbolikSep not in self.rutaDelProyecto:
            _simbolikSep = "/"

        return _simbolikSep
