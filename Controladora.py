# -⁻- coding: UTF-8 -*-
"""
Esta es la controladora del diario

controladoraDeCarpetas
controladoraProcesamientoDatos
tiempo

control de archivos de imagenes de fondo, imagenes de botonos y sonidos.
"""
import os # TO get path project
import json
from Femputadora import *
from tiempo import * 
from controladoraCarpetas import *
from controladoraProcesamientoDeDatos import *
from GraphicsController import *
from tkMagicColorByLoko import *
from AudioMixer import *
import random


class Controladora:
    def __init__(self):
        self.env = self._setENV()
        self.rutaDelProyecto = str(os.path.dirname(os.path.abspath(__file__))) # En donde estoy padado
        self.audioMixer = AudioMixer() # Reproductor de sonido
        self.tiempo = Tiempo() # Metodos personalizados de tiempo
        self.controladoraCarpetas = ControladoraCarpetas(self.tiempo, self.rutaDelProyecto, self.env) # Para crear y aceder a informacion
        self.controladoraProcesamientoDeDatos = ControladoraProcesamientoDeDatos(self.rutaDelProyecto, self.tiempo, self.controladoraCarpetas, self.env) # Aca se hace la mineria de datos
        self.graphicsController = GraphicsController()
        self.estadoDeLasCarpetas = self.crearCarpetasDelSistema()
        self.coloresParaGraficos = MagicColor() # Color
        self.coloresParaGraficoCircular = [] # Color que le va a corresponder al grafico circular
        self.arbolDeDecicionListo = False # Me dice si se cargo o creo el arbol
        self.questionsChatbot = self.loadQuestions()
        self.femputadora = Femputadora(self.questionsChatbot)
        self.triggers = self._updateTriggers() # Always Refresh When the program is RUN
        self.femputadora_triggers = Femputadora(self.triggers)
        self.codenamePopularDrug = ""
        """
        Se procede a saludar al usuario
        """
        self.saludarAlUsuario()
        # The user use program and registe
        self.saveUseRunAPP()


    def _setENV(self):
        "NEW FAGOT CANT READ MY DIARY"
        "Chismoso PUTO primero deja de ser bruto y podras leer mi diario"
        # Advertencia: bruto = idiota que en frances significa 'ligeramente afeminado'
        try:
            with open(".env", "r", encoding="UTF-8") as f:
                return f.read()
        except:
            pass

        return "TU ERES UN MARICA SIN CEREBRO"


    def _updateTriggers(self):
        """
        Read a folder DATA/TRIGGERS and gell all [Question, ...]
        """
        _json_triggers = self.controladoraCarpetas.get_all_triggers()

        triggers = []
        for i in _json_triggers:
            q_t = Question(**i)
            triggers.append(q_t)
        
        return triggers
        

    def crearCarpetasDelSistema(self):
        """
        Se procede a acceder al disco duro y verificar si las carpetas de trabajo existen
        carpeta de trabajo>Es donde se almacena y se saca la informacion
        """
        try:
            self.controladoraCarpetas.crearYVerificarCarpetas()
            return True
        except:
            return False


    def projPATH(self):
        return self.rutaDelProyecto
    
    
    def returnIMGRnBtnRousourceX(self, resource):
        """
        Read a img in folder: RECURSOS/img/btns/<Resource>/<ResourceFile> + rnd + .gif 
        And you rtrn rnd img
        """
        return self.graphicsController.returnIMGRnBtnRousourceX(self.rutaDelProyecto, resource)
    
    
    def returnIMGBtnPeople(self):
        """
        Read all quantity of pleople you conect...
        retrun a representative image
        """
        qty_people = len(self.controladoraCarpetas.listOfAllPeople())
        return self.graphicsController.getIMGPeople(self.rutaDelProyecto,qty_people)

    def retrunIMGBtnFeelings(self):
        """
        Read all .gif images in folder: RECURSOS/img/btns/feelings/real/*.gif
        if the emotion is the most popular render a imagen of feeling
        if the feeling dont exits retrun random feeling
        """
        try:
            _sep = self.controladoraCarpetas.getSimbolikPathSeparator()

            path = f"{self.rutaDelProyecto}{_sep}RECURSOS{_sep}img{_sep}btns{_sep}feelings{_sep}real" 
            _files_img_emotions = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(path, '.gif')
            
            #get current year
            YYYY = self.tiempo.año()

            # Read the most feeling in year
            data_feelings = self.procesarDatosSentimientos(YYYY)
            if len(data_feelings) == 0 or not data_feelings:
                return self.returnIMGRnBtnRousourceX("feelings")
            else:
                data = self.controladoraProcesamientoDeDatos._shorterDic(data_feelings) # [(a, #), ... (z, #)]
                
                if data[0][0] + ".gif" in _files_img_emotions:
                    return self.graphicsController.getPhotoImageFromRouteX(f"{path}{_sep}{data[0][0]}.gif")
                return self.returnIMGRnBtnRousourceX("feelings")
        except:
            return self.returnIMGRnBtnRousourceX("feelings")
        

    def returnIMGBtnDRUGS(self):
        """
        Read all drugs in current year and return a img > moda
        """
        try:
            YYYY = self.tiempo.año()
            path = self.rutaDelProyecto + "\\RECURSOS\\img\\btns\\drugs\\"

            _files_img_drugs = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(path, '.gif')
            #Get the most popular DRUG
            path = self.rutaDelProyecto + "\\DATA\\DRUGS\\" + str(YYYY)
            _files_names_drugs_yyyy = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(path, '.txt')

            # Get TOP
            dic_count = {}
            for i in _files_names_drugs_yyyy:
                _drug = str(i.split("-")[0]).strip()
                if _drug not in dic_count.keys():
                    dic_count[_drug] = 0
                dic_count[_drug] = dic_count[_drug] + 1

            # Order
            dic_count = self.controladoraProcesamientoDeDatos._shorterDic(dic_count)

            if dic_count[0][0]  + '.gif'  in _files_img_drugs:
                self.codenamePopularDrug = dic_count[0][0]
                return self.projPATH() + f"/RECURSOS/img/btns/drugs/{dic_count[0][0]}.gif"
            else:
                return self.projPATH()+'/RECURSOS/img/weed.gif'

        except:
            pass

        return self.projPATH()+'/RECURSOS/img/weed.gif'
    
    def getDescriptionOfPopularDrug(self):
        try:
            _data = f"{self.codenamePopularDrug}"

            if self.codenamePopularDrug != "":
                _path = f"{self.rutaDelProyecto}\\RECURSOS\\drugs\\{self.codenamePopularDrug}.txt"
                _data = self.controladoraCarpetas.getTextInFile(_path)
                return _data

            return "The Drug Description 404 :("
        except:
            return "ERROR 508 :X"

    def retornarRutaImagenDeFondo(self):
        """
        En la carpeta RECURSOS/img/bg hay fotos.gif
        con id [0-9] se retorna por randon
        """
        return self.graphicsController.getBackgroundImage(self.rutaDelProyecto)

    def guardarPaginaDiario(self, palabraMagica, texto):
        try:
            """Se genera la ruta del disco duro donde va a estar el archivo"""
            _sep = self.controladoraCarpetas.getSimbolikPathSeparator()
            rutaDiario = f"{self.rutaDelProyecto}{_sep}DATA{_sep}DIARIO{_sep}{self.tiempo.año()}"
            _path = f"{rutaDiario}{_sep}{self.tiempo.estampaDeTiempo()} - {palabraMagica}.txt"
            if(len(str(palabraMagica).strip()) > 0):
                # Write a page diary
                texto = texto + "\n\n" + self.tiempo.hora() + "\n\n"
                # AutoEncrypted
                status = self.controladoraCarpetas.saveDiaryPage(_path, texto)
                if not status:
                   return False

                # Save user usages Diary
                self.saveUseWrite("diary")

                # Femputadora analize a words
                try:
                    # Erase a timestamps
                    txt = str(texto).split("\n")
                    txt = txt[0:-4]
                    # Reconstrucut
                    sms = ""
                    for x in txt:
                        sms = sms + " " + x 
                    
                    sms = sms.lstrip()
                    sms = sms.rstrip()

                    # Execute_action
                    action = self.femputadora_triggers.getResponse(sms)
                    self.execute_trigger_event(action)
                except:
                    pass

                return True
            else:
                return False
                
        except:
            return False

    def cargarpaginaDeDiario(self, palabraMagica):
        _sep = self.controladoraCarpetas.getSimbolikPathSeparator()

        rutaDiario = f"{self.rutaDelProyecto}{_sep}DATA{_sep}DIARIO{_sep}{self.tiempo.año()}"
        archivo = f"{rutaDiario}{_sep}{self.tiempo.estampaDeTiempo()} - {palabraMagica}.txt" 

        return self.controladoraCarpetas.getTextInFile(archivo)

    def loadDiaryPageBypath(self, path):
        """
        Enter a path to open file and return page text
        """
        data = ""

        try:
            with open(path, encoding="UTF-8") as f:
                data = f.read()
        except:
            pass

        return data

    def loadFilePageByPath(self, path):
        """
        Enter a path to open file and return page text
        """
        data = ""

        try:
            with open(path, encoding="UTF-8") as f:
                data = f.read()
        except:
            pass

        return data     

    def loadDiaryDataFilterByLetter(self, letter):
        """
        Enter a letter and return all titles to start of this letter
        retrun a [{title:abc, text:abc}, {title:abc, text:abc}, {title:abc, text:abc}, {title:abc, text:abc}]
        """
        information = []
        

        years = self.controladoraCarpetas.listOfAllYearWriteInDiary()


        for y in years:
            try:
                path = self.rutaDelProyecto + "\\DATA\\DIARIO\\" + y
                data = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(path, '.txt')
                self._loadDiaryDataFilterTitleByLetter(letter, path, data, information)
            except:
                pass

        return information

    def _loadDiaryDataFilterTitleByLetter(self, letter, path, data, information):
        for i in data:
            try:
                title = i
                title = title.split("-")[1]
                title = title.strip()[0]

                if letter == ".":
                    newData = {}
                    newData["title"] = i
                    txt = self.controladoraCarpetas.getTextInFileDecrypt(path+"\\"+i)
                    newData["text"] = txt
                    information.append(newData)

                elif letter == "#":
                    if title in "0123456789":
                        newData = {}
                        newData["title"] = i
                        txt = self.controladoraCarpetas.getTextInFileDecrypt(path+"\\"+i)
                        newData["text"] = txt
                        information.append(newData)
                else:

                    if str(title).upper() == letter:
                        newData = {}
                        newData["title"] = i
                        txt = self.controladoraCarpetas.getTextInFileDecrypt(path+"\\"+i)
                        newData["text"] = txt
                        information.append(newData)
            except:
                pass


    def loadDreamsDataFilterByLetter(self, letter):
        """
        Enter a letter and return all titles to start of this letter
        retrun a [{title:abc, text:abc}, {title:abc, text:abc}, {title:abc, text:abc}, {title:abc, text:abc}]
        """
        information = []

        years = self.controladoraCarpetas.listOfAllYearWriteInDreams()

        for y in years:
            try:
                path = self.rutaDelProyecto + "\\DATA\\DREAMS\\" + y
                data = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(path, '.txt')
                self._loadDreamsDataFilterByLetter(letter, path, data, information)
            except:
                pass

        return information


    def _loadDreamsDataFilterByLetter(self, letter, path, data, information):
        for i in data:
            try:
                title = i
                title = title.split("-")[1]
                title = title.strip()[0]

                if letter == ".":
                    newData = {}
                    newData["title"] = i
                    newData["text"] = self.loadFilePageByPath(path+"\\"+i)
                    information.append(newData)

                elif letter == "#":
                    if title in "0123456789":
                        newData = {}
                        newData["title"] = i
                        newData["text"] = self.loadFilePageByPath(path+"\\"+i)
                        information.append(newData)
                else:

                    if str(title).upper() == letter:
                        newData = {}
                        newData["title"] = i
                        newData["text"] = self.loadFilePageByPath(path+"\\"+i)
                        information.append(newData)
            except:
                pass


    def savePeopleDescription(self, name, alias, description, qualification):
        if self.controladoraCarpetas.createPeopleFolder(name):
            path = self.rutaDelProyecto + "\\DATA\\PEOPLE\\" + str(name).lower() + "\\"
            try:
                with open(path+"name.txt", 'w', encoding="UTF-8") as f:
                    f.write(name)
                    f.close()

                if alias != None and alias != "":
                    with open(path+"alias.txt", 'w', encoding="UTF-8") as f:
                        f.write(alias)
                        f.close()

                date = self.tiempo.estampaDeTiempo()
                hour = str(self.tiempo.hora()).split(" ")[3]
                hour = str(hour).replace(":", " ")

                desc = "description-" + str(date) + "-" + hour + ".txt"

                with open(path+desc, 'w', encoding="UTF-8") as f:
                    f.write(description + "\n" +str(qualification))
                    f.close()

                self.saveUseWrite("people")
            except:
                return False
            return True
        else:
            return False
        

    def _getEmojiPeopleEmotionalValue(self, emotionalValue):
        """
        Get value in string [0,100] and return emoji
        """
        return self.controladoraProcesamientoDeDatos._rtnEmotional(emotionalValue)

    def guardarNota(self, palabraMagica, texto):
        """
        las notas son como un diccionario:

        la nota se va a guardar en 

        """
        try:
            archivo = self.rutaDelProyecto + "\\DATA\\NOTAS\\"+ palabraMagica + ".txt"

            if(len(palabraMagica.strip()) > 0):
                texto = texto + "\n\n" + self.tiempo.hora() + "\n\n"
                f = open(archivo, "a", encoding="UTF-8")
                f.write(texto)
                f.close()
                self.saveUseWrite("note")
                return True
            else:
                return False
        except:
            return False

    def cargarNotas(self, letra):
        """
        Entra un letra y luego se retornan todas las notas que empiecen por esa letra
        """
        try:
            informacion = {}

            ruta = self.rutaDelProyecto+"\\DATA\\NOTAS"
            lista = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(ruta, ".txt")

            if letra == "#":
                print("Epa")
            else:
                for i in lista:
                    if i[0] == letra:
                        f = open(ruta+"\\"+i, "r", encoding="UTF-8")
                        informacion[i] = f.read()
                        f.close()

            return informacion
        except:
            return {}

    def loadNotesDataFilterByLetter(self, letter):
        """
        Enter a letter and return all titles to start of this letter
        retrun a [{title:abc, text:abc}, {title:abc, text:abc}, {title:abc, text:abc}, {title:abc, text:abc}]
        """
        information = []

        path = self.rutaDelProyecto + "\\DATA\\NOTAS\\"
        files_path = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(path, '.txt')
        self._loadNotesDataFilterByLetter(letter, path, files_path, information)

        return information


    def _loadNotesDataFilterByLetter(self, letter, path, files_names, information):
        for i in files_names:
            try:
                initial_letter = i[0]
                newData = {}
                if letter == ".":
                    newData["title"] = i
                    newData["text"] = self.loadFilePageByPath(path+"\\"+i)
                    information.append(newData)
                elif letter == "#":
                    if initial_letter in "0123456789":
                        newData["title"] = i
                        newData["text"] = self.loadFilePageByPath(path+"\\"+i)
                        information.append(newData)
                else:
                    if str(letter).upper() == str(initial_letter).upper():
                        newData["title"] = i
                        newData["text"] = self.loadFilePageByPath(path+"\\"+i)
                        information.append(newData)
            except:
                pass



    def saveDreamDiaryPage(self, keyword, text):
        try:
            path = self.rutaDelProyecto + "\\DATA\\DREAMS\\" + str(self.tiempo.año())
            file_path = path + "\\"+self.tiempo.estampaDeTiempo() + " - " + keyword + ".txt"
            if(len(keyword.strip()) > 0):
                text = text + "\n\n" + self.tiempo.hora() + "\n\n"
                with open(file_path, "a", encoding="UTF-8") as f:
                    f.write(text)
                    f.close()

                self.saveUseWrite("dream")
                return True
            else:
                return False
        except:
            return False

    def loadDreamDiarypage(self, keyword):
        data = ""

        try:
            path_file = self.rutaDelProyecto + "\\DATA\\DREAMS\\" + str(self.tiempo.año())
            path_file = path_file + "\\" + self.tiempo.estampaDeTiempo() + " - " + keyword + ".txt"

            with open(path_file, 'r', encoding="UTF-8") as f:
                data = f.read()

        except:
            return None

        return data


    def guardarSentimiento(self, sentimiento):
        try:
            if sentimiento != "":
                rutaDiario = self.rutaDelProyecto + "\\DATA\\SENTIMIENTOS\\" + str(self.tiempo.año())
                archivo = rutaDiario+"\\"+self.tiempo.estampaDeTiempo()+".txt"
                f = open(archivo, 'w', encoding="UTF-8")
                f.write(sentimiento)
                f.close()
                self.saveUseWrite("feeling")
                return True
            else:
                return False
        except:
            return False

    def procesarDatosSentimientos(self, año):
        """
        Entra un a+o luego se leen todos los sentimientos de ese a+o y se entregan 
        los datos para ser graficados.
        """
        # Se llaman todos los nombre archivos de ese a+o
        ruta = self.rutaDelProyecto+"\\DATA\\SENTIMIENTOS\\"+str(año)
        listadoNombreArchivoSentimientos = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(ruta, ".txt")
        sentimientos = []
        # Se abren los archivos y se guardan en una lista
        for i in listadoNombreArchivoSentimientos:
            try:
                f = open(ruta+"\\"+i ,'r', encoding="UTF-8")
                sentimientos.append(f.read())
                f.close()
            except:
                pass 

        # Todos esos sentimientos se los mando a la procesadora de datos
        dataSentimientos = self.controladoraProcesamientoDeDatos.procesarDatosSentimientos(self.controladoraCarpetas.cargarEstadosEmocionanes(),sentimientos)
        return dataSentimientos
    

    def processDataDrugs(self, YYYY):
        """
        DATA/DRUGS/YYYY
        Group data and show
        """
        return self.controladoraProcesamientoDeDatos.proccesDrugsDataByYYYY(YYYY)
    

    def loadTodayTimeInversion(self):
        """
        get date today and return {hour:activity, ...hour:activity}
        """
        _data = {}
        YYYY = self.tiempo.año()
        MM = self.tiempo.mes()
        DD = self.tiempo.diaNumero()

        _fileName = self.rutaDelProyecto + f"\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\{YYYY}\\{YYYY} {MM} {DD}.txt"
        _temp = self.controladoraCarpetas.getTextInFile(_fileName)

        for i in _temp.split("\n"):
            if str(i).strip() != "":
                d = str(i).split(":")
                _data[d[0]] = d[1]

        return _data
    

    def guardarDistribucionTiempoDiario(self, reporte):
        """
        reporte : ['Hora:Actividad', 'Hora:Actividad', ...]
        eso se guarda en DATA/DISTRTIEMP/TDIA/A+o/estampadetiempo.txt
        """
        try:
            txt = ""
            for i in reporte:
                txt = txt + i + "\n"
            ruta = self.rutaDelProyecto+"\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\"+str(self.tiempo.año())+"\\"+str(self.tiempo.estampaDeTiempo())+".txt"
            f = open(ruta, 'w', encoding="UTF-8")
            f.write(txt)
            f.close()
            return True
        except:
            return False

    def procesarInformacionSemanal(self, informacion):
        """
        el metodo de horario semanal 
        {actividad : %, actividad : %, ...}
        """
        dataHorario = self.controladoraProcesamientoDeDatos.procesarDatosSemanalHorario(self.controladoraCarpetas.cargarActividades(), informacion)
        # Se acualizan los colores para el grafico circular
        contador = 0
        for i in dataHorario:
            if dataHorario[i] != 0:
                contador = contador + 1
        
        self.coloresParaGraficoCircular = self.retornarColores(contador)
        return dataHorario
    

    def processDiaryActivitiesInWeek(self):
        """
        Cacth the current year and return all things to do 24h in the year peer only WEEK
        """
        data = 0
        YYYY = self.tiempo.año()
        path = self.rutaDelProyecto + f"\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\{YYYY}"
        
        # Get all data via name of week
        data = self.controladoraProcesamientoDeDatos.getSumaryYYYYAllActivities24HPerDayOfWeek(path)

        # Get Only Unique Values
        _temp = {}
        for i in data:
            try:
                if i not in _temp.keys():
                    _temp[i] = {}
                for j in data[i]:
                    if j not in _temp[i].keys():
                        _temp[i][j] = ""
                    #is unique value? 
                    _qtyActivities = len(data[i][j])
                    if _qtyActivities == 1:
                        test_dict = data[i][j]
                        _activity = str(list(test_dict.keys())[0])
                        _temp[i][j] = _activity
                    elif _qtyActivities > 1:
                        # In the future put here if you hav more of 2 activities
                        _top = self.controladoraProcesamientoDeDatos._shorterDic(data[i][j]) # [('A', x), ('B', y)]  x > y
                        _top = _top[0][0]
                        _temp[i][j] = _top
            except:
                pass



        data = _temp
        return data
    
    def vizualizeHistogramData(self, data, title):
        self.graphicsController.showHistogramGraphic(data, title)


    def drawTimeLife(self):
        """
        data["YYYY"] = [all years registred]
        data["MERTADATA"] = [MAX, MIN, COUNT]
        """
        data = {"YYYY":[], "DATA":{}, "METADATA":{}}
        _maxIN = 0
        _maxOUT = 0

        # Get economy data
        _YYYY = self.controladoraCarpetas.listarAñosDeEconomia()
        if _YYYY:
            data["YYYY"] = sorted(_YYYY)
            for i in data["YYYY"]:
                _tempDic = self.controladoraProcesamientoDeDatos.getFormatedEconomyReportByYear(i)
                data["DATA"].update(_tempDic["DATA"])
                if _tempDic["METADATA"]["maxin"] > _maxIN:
                    _maxIN = _tempDic["METADATA"]["maxin"]
                if _tempDic["METADATA"]["maxout"] >_maxOUT:
                    _maxOUT = _tempDic["METADATA"]["maxout"]

            data["METADATA"]["maxin"] = _maxIN
            data["METADATA"]["maxout"] = _maxOUT

        # Get time distribution 24h data
        _YYYY = self.controladoraCarpetas.listarAñosRegistradosDistribucionDeTiempo()
        if _YYYY:
            _YYYY = sorted(_YYYY)
            for i in _YYYY:
                if i not in data["YYYY"]:
                    data["YYYY"].append(i)

                _tempDic = self.controladoraProcesamientoDeDatos.getFormatedTimeDistributionReportByYear(i)
                for x in _tempDic["DATA"]:
                    if x in data["DATA"]:
                        data["DATA"][x].update(_tempDic["DATA"][x])
                    else:
                        data["DATA"][x] = _tempDic["DATA"][x]
                        
        self.graphicsController.drawTimeLife(data)


    def retornarColores(self, cantidad):
        """
        deacuerdo a la cantidad retorna un vector [color, color, color, ....]
        """
        colores = []

        for _ in range(0, cantidad):
            colores.append(self.coloresParaGraficos.colorAleatoreo())
        
        # Try to return equals colors in journaly
        # Find a BUG always paint -1 elemetns
        #print(self.coloresParaGraficos.returnStaticColors(cantidad))

        return colores
    

    def guardarHorario(self, informacion):
        """
        Se guarda el horario y la copia
        """
        try:
            # Se guarda el original
            ruta = self.rutaDelProyecto+"\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\HORARIO\\horario.txt"
            h = open(ruta, 'w', encoding="UTF-8")
            h.write(informacion)
            h.close()

            # Se guarda la copia
            ruta = self.rutaDelProyecto+"\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\HORARIO\\"+str(self.tiempo.año())+"\\"+str(self.tiempo.estampaDeTiempo())+".txt"
            bk = open(ruta, 'w', encoding="UTF-8")
            bk.write(informacion)
            bk.close()
            
            return True
        except:
            return False

    def cargarHorario(self):
        """
        Se abre DATA/DDT/HORARIO/horario.txt
        """
        try:
            informacion = ""
            ruta = self.rutaDelProyecto+"\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\HORARIO\\horario.txt"

            h = open(ruta, 'r', encoding="UTF-8")
            informacion = h.read()
            return informacion

        except:
            return None

    def cargarDatosFechasInformacionEconomica(self):
        valuesComboBox = []
        # Se cargan los a+os disponibles
        añosDisponbibles = self.controladoraCarpetas.listarAñosDeEconomia()
        # Se retornan los meses disponibles.
        mesesDisponibles = self.tiempo.meses[0:self.tiempo.mes()]

        valuesComboBox = valuesComboBox + añosDisponbibles + mesesDisponibles

        if valuesComboBox:
            valuesComboBox = ["ALL"] + valuesComboBox

        return valuesComboBox


    def arbolDeDecicionEstaListo(self):
        """
        Si el arbol esta listo para trabajar : True or false
        """
        return self.arbolDeDecicionListo


    def retornarInformacionEconomica(self, _filter):
        """
        GET information in DATA/ECONOMIA
        _filter = ALL | YYYY | MM
        """
        isYYYY = False
        try:
            isYYYY = int(_filter) > 0
        except:
            pass

        _path = ""
        _filesPath = [] # [_path]
        data = [] # Save economic info []
        if isYYYY: 
            _path = f"{self.rutaDelProyecto}\\DATA\\ECONOMIA\\{_filter}"
            arch = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(_path, ".xlsx")

            for i in arch:
                _filesPath.append(f"{_path}\\{i}")

        elif _filter == "ALL":
            _path = f"{self.rutaDelProyecto}\\DATA\\ECONOMIA\\"

            _allYYYY = self.controladoraCarpetas.listarAñosDeEconomia()

            for i in _allYYYY:
                arch = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(f"{_path}\\{i}", ".xlsx")
                for j in arch:
                    _filesPath.append(f"{_path}\\{i}\\{j}")
        else:
            _path = f"{self.rutaDelProyecto}\\DATA\\ECONOMIA\\{self.tiempo.año()}"
            arch = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(_path, ".xlsx")

            for i in arch:
                if _filter in i: #ONLY MM
                    _filesPath.append(f"{_path}\\{i}")

        if _filesPath:
            for i in _filesPath:
                data.append(self.controladoraCarpetas.getTextInFile(i))

        return self.controladoraProcesamientoDeDatos.procesarReporteEconomigo(data)
    
    def getTAccountsInformationFilterByKeyWord(self, keyword):
        _data = {}

        try:
            _data = self.controladoraProcesamientoDeDatos.getTAccountsReportByKeyWord(keyword)
        except:
            pass
        
        return _data

    def guardarEstadoCajaMayor(self, monto):
        """
        Si el monto es un numero se procede a guardar
        Se guarda una copia en el final del txt \\DATA\\ECONOMIA\\CAJA\\cajaMayor(año).txt
        """
        ruta = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\CAJA\\cajaMayor.txt"
        try:
            txtM = int(monto)
            f = open(ruta, "w", encoding="UTF-8")
            f.write(monto)
            f.close()

            try:
                rutaTemp = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\CAJA\\cajaMayor" + str(self.tiempo.año()) + ".txt"
                temp = open(rutaTemp, 'r', encoding="UTF-8")
                k = temp.read() + monto + "\n"
                temp.close()
                temp = open(rutaTemp, 'w', encoding="UTF-8")
                temp.write(k)
                temp.close()

            except:
                rutaTemp = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\CAJA\\cajaMayor" + str(self.tiempo.año()) + ".txt"
                temp = open(rutaTemp, "w", encoding="UTF-8")
                temp.write(monto + "\n")
                temp.close()

            return True
        except:
            return False


    def cargarEstadoCajaMayor(self):
        """
        Se carga el monto contenido en DATA/ECONOMIA/CAJA/cajaMayor.txt

        >Si el txt no existe se crea y se retorna $0
        """
        ruta = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\CAJA\\cajaMayor.txt"
        try:
            f = open(ruta, encoding="UTF-8")
            return f.read()
        except:
            f = open(ruta, "w", encoding="UTF-8")
            f.write("0")
            f.close()
            return 0

    def cargarRecordEstadoCajaMayor(self):
        """
        se cargan los montos contenidos en \\DATA\\ECONOMIA\\CAJA\\cajaMayor(año).txt
        """
        try:
            ruta = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\CAJA\\cajaMayor" + str(self.tiempo.año()) + ".txt"
            f = open(ruta, 'r', encoding="UTF-8")
            valores = []

            for i in f.readlines():
                try:
                    valores.append(int(i))
                except:
                    pass

            return valores
        except:
            return []


    def cargarEstadoCajaMenor(self):
        """
        Se carga el monto contenido en DATA/ECONOMIA/CAJA/cajaMenor.txt

        >Si el txt no existe se crea y se retorna $0
        """
        ruta = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\CAJA\\cajaMenor.txt"
        try:
            f = open(ruta, encoding="UTF-8")
            return f.read()
        except:
            f = open(ruta, "w", encoding="UTF-8")
            f.write("0")
            f.close()
            return 0

    def cargarRecordEstadoCajaMenor(self):
        """
        se cargan los montos contenidos en \\DATA\\ECONOMIA\\CAJA\\cajaMenor(año).txt
        """
        try:
            ruta = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\CAJA\\cajaMenor" + str(self.tiempo.año()) + ".txt"
            f = open(ruta, 'r', encoding="UTF-8")
            valores = []

            for i in f.readlines():
                try:
                    valores.append(int(i))
                except:
                    pass

            return valores
        except:
            return []

    def guardarEstadoCajaMenor(self, monto):
        """
        Si el monto es un numero se procede a guardar
        Se procede a guardar una copia en el final del txt \\DATA\\ECONOMIA\\CAJA\\cajaMenor(año).txt
        """
        ruta = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\CAJA\\cajaMenor.txt"
        try:
            txtM = int(monto)
            f = open(ruta, "w", encoding="UTF-8")
            f.write(monto)
            f.close()

            try:
                rutaTemp = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\CAJA\\cajaMenor" + str(self.tiempo.año()) + ".txt"
                temp = open(rutaTemp, 'r', encoding="UTF-8")
                k = temp.read() + monto + "\n"
                temp.close()
                temp = open(rutaTemp, 'w', encoding="UTF-8")
                temp.write(k)
                temp.close()

            except:
                rutaTemp = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\CAJA\\cajaMenor" + str(self.tiempo.año()) + ".txt"
                temp = open(rutaTemp, "w", encoding="UTF-8")
                temp.write(monto + "\n")
                temp.close()

            return True
        except:
            return False

    def queAñoEs(self):
        """
        Retorna el año en que nos encontramos
        """
        return self.tiempo.año()

    def queMesEs(self):
        """
        Retorna el mes actual
        """
        return self.tiempo.mes()

    def queNumeroDeDiaEs(self):
        """
        Retorna el # dia en que estamos
        """
        return self.tiempo.diaNumero()

    """WORK"""
    """WORK"""
    """WORK"""
    def saveWork(self, args):
        """
        Enter valid args and create folder and files
        """
        return self.controladoraCarpetas.saveWork(args)
    
    def getWorkX(self, nameOfWork):
        """
        Load all files in DATA/WORK/*
        """
        return self.controladoraCarpetas.loadSpecifyWork(nameOfWork)
    
    def getAllWorksNames(self):
        """
        Return all folder names in work folder.
        """
        return self.controladoraCarpetas.listALLFolderInPath(self.rutaDelProyecto+"\\DATA\\WORK")

    def saveIncOfWork(self, concept, hours, projectName):
        """
        Save hours and concept in folder
        """
        return self.controladoraCarpetas.saveIncOfWork(concept, hours, projectName)
    
    def getALlIncOfWork(self, projectName):
        """
        Read folder DATA/WORK/projectName and return:
        costPeerHour.txt
        hours.txt
        """
        _path = f"{self.rutaDelProyecto}\\DATA\\WORK\\{projectName}"
        _data = {}

        _cph = self.controladoraCarpetas.getTextInFile(f"{_path}\\costPeerHour.txt")
        if _cph != "":
            _data['costPeerHour'] = _cph

        _h = self.controladoraCarpetas.getTextInFile(f"{_path}\\hours.txt")
        if _h != "":
            _data['hours'] = _h

        return _data

    """WORK"""
    """WORK"""
    """WORK"""
    
    def getYearsToAPPUse(self):
        """
        Return all Year of user save a files in all types: economy, diary, dreams ...
        [2020, 2021, 2022, ...]
        """
        years = []

        for i in self.controladoraCarpetas.listarAñosDeEconomia():
            years.append(i)

        for i in self.controladoraCarpetas.listarAñosDeRegistroSentimientos():
            if i not in years:
                years.append(i)

        for i in self.controladoraCarpetas.listarAñosRegistradosDistribucionDeTiempo():
            if i not in years:
                years.append(i)

        for i in self.controladoraCarpetas.listOfAllYearWriteInDiary():
            if i not in years:
                years.append(i)

        for i in self.controladoraCarpetas.listOfAllYearWriteInDiary():
            if i not in years:
                years.append(i)

        return years
    

    def getAllDrugs(self):
        """
        read RECURSOS/drugs.txt and return all info
        """
        return self.controladoraCarpetas.getAllDrugs()
    

    def saveDrugs(self, drug_title, drug_detonate, drug_feel):
        """
        save in DATA/DRUGS
        """
        return self.controladoraCarpetas.saveDrug(drug_title, drug_detonate, drug_feel)


    def guardarInformacionPerfil(self, informacion):
        """
        Se guarda la informacion en los txt correspondientes
        """
        try:
            ruta = self.rutaDelProyecto + "\\DATA\\PERFIL\\"
            
            f = open(ruta+"nombreApellido.txt", "w", encoding="UTF-8")
            f.write(informacion[0])
            f.close()

            f = open(ruta+"fechaNacimiento.txt", "w", encoding="UTF-8")
            f.write(informacion[1])
            f.close()

            f = open(ruta+"sexo.txt", "w", encoding="UTF-8")
            f.write(informacion[2])
            f.close()

            f = open(ruta+"edad.txt", "w", encoding="UTF-8")
            f.write(informacion[3])
            f.close()

            f = open(ruta+"username.txt", "w", encoding="UTF-8")
            f.write(informacion[4])
            f.close()

            f = open(ruta+"biografia.txt", "w", encoding="UTF-8")
            f.write(informacion[5])
            f.close()

            return True
        except:
            return False

    def cargarInformacionDelPerfil(self):
        try:
            informacion = []

            ruta = self.rutaDelProyecto + "\\DATA\\PERFIL\\"
            try:
                f = open(ruta+"nombreApellido.txt", "r", encoding="UTF-8")
                informacion.append(f.read())
                f.close()
            except:
                pass


            try:
                f = open(ruta+"fechaNacimiento.txt", "r", encoding="UTF-8")
                informacion.append(f.read())
                f.close()
            except:
                pass

            try:
                f = open(ruta+"sexo.txt", "r", encoding="UTF-8")
                informacion.append(f.read())
                f.close()
            except:
                pass

            try:
                f = open(ruta+"edad.txt", "r", encoding="UTF-8")
                informacion.append(f.read())
                f.close()
            except:
                pass
            
            try:
                f = open(ruta+"username.txt", "r", encoding="UTF-8")
                informacion.append(f.read())
                f.close()
            except:
                pass

            try:
                f = open(ruta+"biografia.txt", "r", encoding="UTF-8")
                informacion.append(f.read())
                f.close()
            except:
                pass


            return informacion
        except:
            return []

    def cargarAñosDeRegistroActividades(self):
        """
        Se cargan los años registrados en "\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\"
        """
        return self.controladoraCarpetas.listarAñosRegistradosDistribucionDeTiempo()

    def cargarActividades(self):
        """
        Se carga toda la informacion contenida RECURSOS/actividades.txt
        """
        try:
            ruta = self.rutaDelProyecto + "\\RECURSOS\\actividades.txt"
            f = open(ruta, "r", encoding="UTF-8")
            return f.read()
        except:
            return "dormir\nalimentacion\nNada"
        
        
    def loadIndexOfActivity(self, activity):
        """
        Return the index of activity x
        """
        index = None
        index = self.controladoraCarpetas.loadIndexOfActivity(activity)
        return index


    def cargarPorcentajesDeActividades(self, año):
        """
        Se carga el % de gasto de cada actividad en el año correspondiente en un dic
        {dormir:0.2, comer:0.1, trabajar:0.5}
        """
        try:
            ruta = self.rutaDelProyecto + "\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\" + str(año)
            data = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(ruta, "txt")


            informacion = {}
            totalHoras = 0  

            # Se lee cada archivo de horario
            for i in data:
                try:
                    f = open(ruta+"\\"+i, "r", encoding="UTF-8")
                    txt = f.read().split("\n")
                    
                    # Se analiza actividad hora por hora
                    for j in txt:
                        if j.strip() != "":
                            key = j.split(":")[1]
                            if key in informacion:
                                temp = informacion[key] + 1
                                informacion[key] = temp
                            else:
                                informacion[key] = 1
                            totalHoras = totalHoras + 1

                except:
                    pass

            # Se pone la informacion en terminos de porcentaje
            for i in informacion:
                informacion[i] = informacion[i]/totalHoras    

            return informacion
        except:
            return {"No data":0.5, "No Data":0.5}
        
    def loadCalendaryReport(self, year, month, day):
        """
        Retrun a String with the date info
        """
        # Diary
        data = {}
        dataDiary = []
        dataDiaryTitles = []
        super_path = self.rutaDelProyecto + "\\DATA\\DIARIO\\"
        self._getDataFilterByDate("diary", dataDiary, dataDiaryTitles, super_path, year, month, day)

        if len(dataDiary) > 0 and len(dataDiaryTitles) > 0:
            data["diary"] = dataDiary
            data["diary_titles"] = dataDiaryTitles
        # End Diary


        # Dreams
        dataDreams = []
        dataDreamsTitles = []
        super_path = self.rutaDelProyecto + "\\DATA\\DREAMS\\"
        self._getDataFilterByDate("dreams", dataDreams, dataDreamsTitles, super_path, year, month, day)

        if len(dataDreams) > 0 and len(dataDreamsTitles) > 0:
            data["dreams"] = dataDreams
            data["dreams_titles"] = dataDreamsTitles
        # End dreams

        # People
        dataPeople = {}
        dataPeopleNames = []
        super_path = self.rutaDelProyecto + "\\DATA\\PEOPLE\\"
        self._getAllDataPeople(dataPeople, dataPeopleNames, super_path, year, month, day)

        if (len(dataPeople) > 0 and len(dataPeopleNames)) > 0:
            data["people"] = dataPeople
            data["people_names"] = dataPeopleNames
        # End people


        # Economy
        dataEconomy = {}
        super_path = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\"
        self._getDataFilterByDate("economy", dataEconomy, [], super_path, year, month, day)

        if len(dataEconomy) > 0:
            data["economy"] = dataEconomy
        # End Economy



        return self.controladoraProcesamientoDeDatos.getFullReport(data)


    def _getDataFilterByDate(self, key, data, data_titles, path, year, month, day):
        """
        Enter this args:

            - key: is a control to filter folder
            - data: is a empty []
            - data_titles: is a empty []
            - path: is a path to examinate a folder.
            - year: is a year to filter
            - month: is a month to filter
            - day: is a day to filter

        all information is save in data and data_titles
        """
        if year == "all":
            # Load ALL years in regs
            try:
                if key == "diary":
                    all_years = self.controladoraCarpetas.listOfAllYearWriteInDiary()

                if key == "dreams":
                    all_years = self.controladoraCarpetas.listOfAllYearWriteInDreams()

                if key == "economy":
                    all_years = self.controladoraCarpetas.listarAñosDeEconomia()
            except:
                return
            # END to load Years

            
            # Charge the Speficy data
            for i in all_years:
                if key != "economy":
                    get_all_files_names = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(path+i, ".txt")
                
                    for j in get_all_files_names:
                        if self._filterDataByIDAndMonth("diary", j, month):
                            data_titles.append(j)
                            file_path = path+i+"\\"+j
                            data.append(self.loadFilePageByPath(file_path))
                else:
                    # Is Economy
                    get_all_files_names = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(path+i, ".xlsx")
                    
                    if i not in data:
                        data[i] = {}

                    for j in get_all_files_names:
                        if self._filterDataByIDAndMonth("economy", j, month):
                            if j not in data[i]:
                                data[i][j] = {}

                            file_path = path+i+"\\"+j
                            data[i][j] = self.loadFilePageByPath(file_path)
            
        else:
            try:
                if key != "economy":
                    get_all_files_names = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(path+year, ".txt")
                    for j in get_all_files_names:
                        if self._filterDataByIDAndMonth("diary", j, month):
                            data_titles.append(j)
                            file_path = path+year+"\\"+j
                            data.append(self.loadFilePageByPath(file_path))
                else:
                    get_all_files_names = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(path+year, ".xlsx")
                    
                    if year not in data:
                        data[year] = {}

                    for i in get_all_files_names:
                        if self._filterDataByIDAndMonth("economy", i, month):
                            file_path = path+year+"\\"+i
                            data[year][i] = self.loadFilePageByPath(file_path)
            except:
                return
            

    def _filterDataByIDAndMonth(self, idData, data, month):
        """
        Enter a idData is a Str id
        data is str a name
        month is a name of month
        """
        if str(month).lower() == "all":
            return True

        try:
            if idData == "diary":
                nroMonth = str(self.tiempo.getMonthNumberByMonthName(month))
                data_nro_month = str(data).split("-")[0]
                data_nro_month = str(data_nro_month).split(" ")[1]
                if data_nro_month == nroMonth:
                    return True

            if idData == "economy":
                data_nro_month = str(data).split(".")[0]
                data_nro_month = str(data).split(" ")[0]

                if data_nro_month == month:
                    return True

            return False
        except:
            return False
  

    def _getAllDataPeople(self, data, data_titles, path, year, month, day):
        """
        Enter args:
         - Data: is {} and save descriptions
         - data_titles: is a name of folder people
         - path: is a path to examinate a folder.
         - year: is a year to filter
         - month: is a month to filter
         - day: is a day to filter
        """
        get_people_folder_names = self.controladoraCarpetas.listOfAllPeople()

        for i in get_people_folder_names:
            if year == "all":
                data_titles.append(i)
                # Create a name
                if i not in data:
                    data[i] = {}

                get_all_files_names = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(path+i, ".txt")


                for j in get_all_files_names:
                    file_path = path + "\\" + i + "\\" + j
                    data[i][j] = self.loadFilePageByPath(file_path)
            else:
                get_all_files_names = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(path+i, ".txt")

                for j in get_all_files_names:
                    if "description-" in j:
                        date_description = j.split("description-")[1]
                        date_description = date_description.split(" ")[0]

                        if year == date_description:
                            if i not in data_titles:
                                data_titles.append(i)

                            # Create a name
                            if i not in data:
                                data[i] = {}

                            file_path = path + "\\" + i + "\\" + j
                            data[i][j] = self.loadFilePageByPath(file_path)

                    

    """
    AUDIO
    AUDIO
    AUDIO
    """
    def saludarAlUsuario(self):
        """
        Play AUDIO only  one times per day
        """
        # When is the last time to APP say HI?
        path = self.rutaDelProyecto + "\\DATA\\USOS\\" + str(self.tiempo.año()) + "-APPsayHI.txt"
        lastTIme = self.controladoraCarpetas.getTextInFile(path)

        if lastTIme != "":
            lastTIme = lastTIme.split("\n")[-1]

        # Get Current TIME
        hour = str(self.tiempo.getOnlyHour())
        time = self.tiempo.estampaDeTiempo() + " " + hour

        # Is not Equal DAY
        lastTIme = lastTIme.split(" ")
        time = time.split(" ") 

        bool_say_hi = False

        if lastTIme[0:3] == time[0:3]:
            # Create a rules to say hi few times to day
            bool_say_hi = False
        else:
            bool_say_hi = True

        if bool_say_hi:
            hora = hour.split(":")[0]
            hora = int(hora)

            if hora >= 20:
                self.audioMixer.line = self.rutaDelProyecto + "\\recursos\\audio\\buenas noches"
                self.audioMixer.playSound()
            else:
                if hora > 12:
                    self.audioMixer.line = self.rutaDelProyecto + "\\recursos\\audio\\buenas tardes"
                    self.audioMixer.playSound()
                else:
                    self.audioMixer.line = self.rutaDelProyecto + "\\recursos\\audio\\buenos dias"
                    self.audioMixer.playSound()

            # Save the usage
            self.saveUseAPPSayHI()
        

    """USOS"""
    """USOS"""
    """USOS"""
    def saveUseRunAPP(self):
        """
        Save a date to the user run APP
        """
        path = self.rutaDelProyecto + "\\DATA\\USOS\\" + str(self.tiempo.año()) + "-run.txt"
        hour = str(self.tiempo.getOnlyHour())

        time = self.tiempo.estampaDeTiempo() + " " + hour
        data = ""
        try:
            with open(path, 'r', encoding="UTF-8") as f:
                data = f.read()
        except:
            pass

        try:
            with open(path, 'w', encoding="UTF-8") as f:
                if data == "":
                    f.write(time)
                else:
                    f.write(data+"\n"+time)
                f.close()
        except:
            pass


    def saveUseWrite(self, _type):
        """
        Save the date to the user write in app.
        _type is a contex for example: diary, dream, economy
        """
        path = self.rutaDelProyecto + "\\DATA\\USOS\\" + str(self.tiempo.año()) + "-" + _type + ".txt"
        hour = str(self.tiempo.getOnlyHour())

        time = self.tiempo.estampaDeTiempo() + " " + hour
        data = ""
        try:
            with open(path, 'r', encoding="UTF-8") as f:
                data = f.read()
        except:
            pass

        try:
            with open(path, 'w', encoding="UTF-8") as f:
                if data == "":
                    f.write(time)
                else:
                    f.write(data+"\n"+time)
                f.close()
        except:
            pass


    def saveUseAPPSayHI(self):
        """
        Save when the APP reproduces HI audio
        * Creates for only say hi 3 times to day
        """
        path = self.rutaDelProyecto + "\\DATA\\USOS\\" + str(self.tiempo.año()) + "-APPsayHI.txt"
        hour = str(self.tiempo.getOnlyHour())

        time = self.tiempo.estampaDeTiempo() + " " + hour
        data = ""
        try:
            with open(path, 'r', encoding="UTF-8") as f:
                data = f.read()
        except:
            pass

        try:
            with open(path, 'w', encoding="UTF-8") as f:
                if data == "":
                    f.write(time)
                else:
                    f.write(data+"\n"+time)
                f.close()
        except:
            pass


    """FEMPUTADORA"""
    """FEMPUTADORA"""
    """FEMPUTADORA"""
    def loadQuestions(self):
        """
        Load all questions to chatbot in folder:
        DATA/QUESTIONS
        """
        path = self.rutaDelProyecto + "\\DATA\\QUESTIONS"

        chatbotQuestions = []
        questions = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(path, ".json")

        for i in questions:
            try:
                brute_data = self.controladoraCarpetas.getTextInFile(path + "\\" + i)
                json_data = json.loads(brute_data)
                q = Question(**json_data)
                chatbotQuestions.append(q)
            except:
                pass

        return chatbotQuestions


    def userInputTXT(self, txt):
        """
        Enter a text to chatbot analizer
        """
        code = self.femputadora.getResponse(txt)
        response = self.executeCodeFemputadora(code)
        self.femputadora.update_chat("FEMPUTADORA", response)

    def executeCodeFemputadora(self, code):
        """
        Enter a Femputadora function code and execute.
        Note: the Femputadora function name see in file : .json
        """
        if code == "unknow()":
            return self.femputadora_unknow()
        elif code == "hi()":
            return self.femputadora_hi()
        elif code == "get_all_dreams()":
            return self.femputadora_get_all_dreams()
        elif code == "how_i_feel()":
            return self.how_i_feel()
        elif code == "get_all_do()":
            return self.get_all_do()
        elif code == "drugs_information()":
            return self.drugs_information()
        elif code == "sleep_information()":
            return self.sleep_information()
        elif code == "help()":
            return self.help_femputadora()
        
        return ":("
        

    def getFemputadoraChatHistorial(self):
        return self.femputadora.conversation
    

    def femputadora_unknow(self):
        if self.femputadora._counter_unkow_questions < 10:
            responses = ['Podrias Repetir?', 'No estoy seguro', 'No tengo esa información', 'no se de lo que hablas']

        else:
            responses = ['Yo no le entiendo ni chimba.', 'Que pasa bobo mrk .l..', 'Perro hijueputa yo que voy a saber', 'Que mierda pues...']

        return responses[random.randint(0, len(responses)-1)]


    def femputadora_hi(self):
        return "Hola"
    
    def femputadora_get_all_dreams(self):
        data = self.controladoraCarpetas.getTitlesOfAllDreams()
        sms = ""
        if data == []:
            sms = "No hay Sueños Aún...\n"
        else:
            sms = "Estos son tus sueños:\n"
            for i in data:
                sms = sms + i + "\n"
            
        return sms
    
    def how_i_feel(self):
        # get current year
        YYYY = str(self.tiempo.año())

        # Get all Feelings
        _all_feelings = self.controladoraCarpetas.cargarEstadosEmocionanes()

        # Get all years of feelings
        _years = self.controladoraCarpetas.listarAñosDeRegistroSentimientos()

        # Top Data Feelings
        _data = {}

        # Prepare final Output
        for i in _years:
            ruta = self.rutaDelProyecto+"\\DATA\\SENTIMIENTOS\\"+str(i)
            _feelings = []
            _all_filenames_in_folder = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(ruta, ".txt")

            for x in _all_filenames_in_folder:
                try:
                    with open(ruta+"\\"+x ,'r', encoding="UTF-8") as f:
                        _feelings.append(f.read())
                except:
                    pass 

            dataSentimientos = self.controladoraProcesamientoDeDatos.procesarDatosSentimientos(_all_feelings, _feelings)
            
            # Save
            _temp = self.controladoraProcesamientoDeDatos._shorterDic(dataSentimientos)

            _rich_data = []
            if len(_temp) >= 3:
                for x in _temp[0:2]:
                    _rich_data.append(f"{str(x[0])} un total de: {str(x[1])} veces")
            else:
                for x in _temp:
                    _rich_data.append(f"{str(x[0])} un total de: {str(x[1])} veces")


            _data[i] = _rich_data
                    
        # Representate a information to user
        sms = f"Lo que más sentiste en {str(YYYY)}:\nfue {str(_data[YYYY][0])}\n\n"

        for i in _data:
            if i != YYYY:
                _sumaryFeels = ""
                for _feel in _data[i]:
                    _sumaryFeels = _sumaryFeels + _feel + "\n"
                sms = sms + f"Lo que más sentiste en {str(i)}:\nes {str(_sumaryFeels)}\n"

        return sms
 

    def get_all_do(self):
        path = self.rutaDelProyecto + "\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO"
        years = self.controladoraCarpetas.listALLFolderInPath(path)
        _count_years = 0

        data = "Lo Que más has hecho es:\n"

        for i in years:
            try:
                if int(i) > 0:
                    _p = path + "\\" + str(i)
                    _d = self.controladoraProcesamientoDeDatos.sumaryALLActivities24H(_p)
                    _d = self.controladoraProcesamientoDeDatos._shorterDic(_d)
                    _temp = ""
                    for j in _d: 
                        _temp = _temp + "Para: " + str(j[0]) + " un total de: " + str(j[1]) + " Horas.\n"
                    data = data + "\nPara el Año: " + str(i) + "\n" + _temp + "\n"
                    _count_years = _count_years + 1
            except:
                pass

        if _count_years == 0:
            data = data + "No Tengo Información de que haces con tu vida."
        elif _count_years == 1:
            data = data + "\nSolo tengo la información de un año."
        elif _count_years > 1:
            data = data + "\nEn " + str(_count_years) + " años."
        
        return data
    
    
    def drugs_information(self):
        _path = f"{self.rutaDelProyecto}\\DATA\\DRUGS\\"
        YYYY = self.controladoraCarpetas.listOfAllYearsInDrugs()

        data = "Sobre las Drogas:\n"

        for i in YYYY:
            try:
                _d = self.controladoraProcesamientoDeDatos.getSumaryOfDrugs(f"{_path}{i}")
                data = data + f"En el año: \"{i}\" consumiste: {len(_d['DRUGSQTY'])} tipos de sustancias, la más consumida es: {_d['DRUGSQTY'][0][0]}\n"
                data = data + "Los días de mayor consumo son: "
                count = 0
                _dayToDrus = ""
                _daysToShow = random.randint(2, 5)
                for j in _d['DRUGSDAYS']:
                    if count == _daysToShow:
                        break
                    _dayToDrus = _dayToDrus + f"{j[0]},"
                    count = count + 1
                _dayToDrus = _dayToDrus[0:-1]
                data = data + _dayToDrus + ".\n\n"

                
            except:
                pass

        return data
    

    def sleep_information(self):
        """
        Get informatión about:
        1 - total sleep hours
        2 - get AVG of hours sleep peer week day
        3 - get total hours register by week day
        """
        path = self.rutaDelProyecto + "\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO"
        years = self.controladoraCarpetas.listALLFolderInPath(path)
        _count_years = 0

        data = "Está es la información de tu ciclo de sueño:\n"
        _data = {}
        _data["total"] = 0

        for i in years:
            try:
                if int(i) > 0:
                    data = data + f"\npara el año {i}:\n"
                    _p = path + "\\" + str(i)
                    _d = self.controladoraProcesamientoDeDatos.sumaryALLSleep24H(_p)
                    _data["total"] = _data["total"] + _d["total"] # count of all hours register in all years

                    # Get information peer week
                    for t in self.tiempo.diasDeLaSemana:
                        data = data + f"El día {t} dormiste un promedio de: {_d[f"avg-{t}"]} horas.\nHay un total de {_d[f"total-{t}"]} horas registradas.\n"
                    
                    _count_years = _count_years + 1
            except:
                pass

        
        if _data:
            # 



            # PUT RICH INFORMATION
            data = data + f"\nTotal horas de sueño registradas: {_data["total"]}\n\n"

        if _count_years == 0:
            data = data + "No Tengo Información en mi sistema sobre tus horas de sueño."
        elif _count_years == 1:
            data = data + "Solo tengo la información de un año."
        elif _count_years > 1:
            data = data + "En " + str(_count_years) + " años."
        
        return data


    def help_femputadora(self):
        _path = f"{self.rutaDelProyecto}\\RECURSOS\\helpFemputadora.txt"
        txt = self.controladoraCarpetas.getTextInFile(_path)
        return txt if txt else "HELLO WORLD"

    """END FEMPUTADORA"""
    """END FEMPUTADORA"""
    """END FEMPUTADORA"""


    """TRIGGERS"""
    """TRIGGERS"""
    """TRIGGERS"""
    def execute_trigger_event(self, code):
        """
        Enter a code 'name of method' and excecute 1 time >24hours Only<
        """
        # Get Trigger Date information
        _path = self.rutaDelProyecto + "\\DATA\\USOS\\"
        _getAllTriggers = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(_path, ".txt")
        triggers_time = {}
        trigger_execute = False

        # Load ALL triggers
        for i in _getAllTriggers:
            if "trigger." in i:
                _file_d_path = _path + i
                _data = self.controladoraCarpetas.getTextInFile(_file_d_path)
                if _data != "":
                    triggers_time[i] = _data

        # -------------------
        # -------------------
        # Talk About Money Problems
        if code == "think_work_money()":
            trigger_execute = self._execute_trigger_event_validate_time(triggers_time, code)

            if trigger_execute:
                self.think_work_money()
        #END  Talk About Money Problems

        # if the user have porn alert
        if code == "porn_alert()":
            trigger_execute = self._execute_trigger_event_validate_time(triggers_time, code)

            if trigger_execute:
                self.porn_alert()
        #END if the user have porn alert

        # -------------------
        # -------------------
        # -------------------
        # Save a Trigger use
        if trigger_execute:
            self.saveUseWrite("trigger."+code)


    def _execute_trigger_event_validate_time(self, triggers_time, code):
        """
        return bool
        Enter a TriggersTimeFile and compare trigger >< date.today
        """
        _time_now = self.tiempo.estampaDeTiempo()

        _last_time = ""

        for x in triggers_time:
            if code in x:
                _last_time = triggers_time[x]
                break

        if _last_time != "":
            _last_time = _last_time.split("\n")[-1]
            _last_time = _last_time.split(" ")
            _last_time = _last_time[0] + " " + _last_time[1] + " " + _last_time[2]

        
        return _last_time != _time_now



    def think_work_money(self):
        audo_path = self.rutaDelProyecto + "\\recursos\\audio\\hablar_trabajo_dinero"
        self.audioMixer.line = audo_path
        self.audioMixer.playSound()

    def porn_alert(self):
        audo_path = self.rutaDelProyecto + "\\recursos\\audio\\porn_alert"
        self.audioMixer.line = audo_path
        self.audioMixer.playSound()

    """TRIGGERS"""
    """TRIGGERS"""
    """TRIGGERS"""


    """AYUDA"""
    """AYUDA"""
    """AYUDA"""
    def retornarMensajePrincipalAyuda(self):
        try:
            ruta = self.rutaDelProyecto + "\\RECURSOS\\manual\\MensajePrincipal.txt"
            f = open(ruta, 'r', encoding="UTF-8")
            return f.read()
        except:
            return "No se pudo abrir ni mierda"

    def retornarListadoDePosibilidades(self):
        try:
            ruta = self.rutaDelProyecto + "\\RECURSOS\\manual\\ListadoDePosibilidades.txt"
            f = open(ruta, 'r', encoding="UTF-8")
            return f.read()
        except:
            return "Error acediendo a HDD"
