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
from ArbolDeDeciciones import *
from AudioMixer import *
import random

class Controladora:
    def __init__(self):
        self.rutaDelProyecto = str(os.path.dirname(os.path.abspath(__file__))) # En donde estoy padado
        self.audioMixer = AudioMixer() # Reproductor de sonido
        self.tiempo = Tiempo() # Metodos personalizados de tiempo
        self.controladoraCarpetas = ControladoraCarpetas(self.tiempo, self.rutaDelProyecto) # Para crear y aceder a informacion
        self.controladoraProcesamientoDeDatos = ControladoraProcesamientoDeDatos(self.rutaDelProyecto, self.tiempo) # Aca se hace la mineria de datos
        self.graphicsController = GraphicsController()
        self.estadoDeLasCarpetas = self.crearCarpetasDelSistema()
        self.coloresParaGraficos = MagicColor() # Color
        self.coloresParaGraficoCircular = [] # Color que le va a corresponder al grafico circular
        self.arbolDeDeDecicion = Arbol() # Es un arbol temporal que guarda las deciciones
        self.arbolDeDecicionListo = False # Me dice si se cargo o creo el arbol
        self.questionsChatbot = self.loadQuestions()
        self.femputadora = Femputadora(self.questionsChatbot)
        """
        Se procede a saludar al usuario
        """
        self.saludarAlUsuario()
        # The user use program and registe
        self.saveUseRunAPP()


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

    def retornarRutaDelProyecto(self):
        return self.rutaDelProyecto

    def retornarRutaImagenDeFondo(self):
        """
        En la carpeta RECURSOS/img/bg hay fotos.gif
        con id [0-9] se retorna por randon
        """
        id = str(random.randint(0, 14))
        return self.rutaDelProyecto+"\\RECURSOS\\img\\bg\\"+id+".gif"

    def guardarPaginaDiario(self, palabraMagica, texto):
        try:
            """Se genera la ruta del disco duro donde va a estar el archivo"""
            rutaDiario = self.rutaDelProyecto + "\\DATA\\DIARIO\\" + str(self.tiempo.año())
            archivo = rutaDiario+"\\"+self.tiempo.estampaDeTiempo() + " - " + palabraMagica + ".txt"
            if(len(palabraMagica.strip()) > 0):
                texto = texto + "\n\n" + self.tiempo.hora() + "\n\n"
                f = open(archivo, "a", encoding="UTF-8")
                f.write(texto)
                f.close()
                self.saveUseWrite("diary")
                return True
            else:
                return False
                
        except:
            return False

    def cargarpaginaDeDiario(self, palabraMagica):
        try:
            rutaDiario = self.rutaDelProyecto + "\\DATA\\DIARIO\\" + str(self.tiempo.año())
            archivo = rutaDiario+"\\"+self.tiempo.estampaDeTiempo() + " - " + palabraMagica + ".txt"

            f = open(archivo, "r", encoding="UTF-8")
            return f.read()
            
        except:
            return None

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
                    newData["text"] = self.loadDiaryPageBypath(path+"\\"+i)
                    information.append(newData)

                elif letter == "#":
                    if title in "0123456789":
                        newData = {}
                        newData["title"] = i
                        newData["text"] = self.loadDiaryPageBypath(path+"\\"+i)
                        information.append(newData)
                else:

                    if str(title).upper() == letter:
                        newData = {}
                        newData["title"] = i
                        newData["text"] = self.loadDiaryPageBypath(path+"\\"+i)
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
                print(desc)

                with open(path+desc, 'w', encoding="UTF-8") as f:
                    f.write(description + "\n" +str(qualification))
                    f.close()

                self.saveUseWrite("people")
            except:
                return False
            return True
        else:
            return False


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
        ruta = self.rutaDelProyecto+"\\DATA\\SENTIMIENTOS\\"+año
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
    
    def vizualizeFeelingsData(self, data):
        self.graphicsController.showFeelingsYearGraphic(data)


    def retornarColores(self, cantidad):
        """
        deacuerdo a la cantidad retorna un vector [color, color, color, ....]
        """
        colores = []

        for i in range(0, cantidad):
            colores.append(self.coloresParaGraficos.colorAleatoreo())

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

        return valuesComboBox


    def crearCarpetaArbolDeDeciciones(self, txt):
        # Se reinicia el arbol
        self.arbolDeDeDecicion = Arbol()
        self.arbolDeDeDecicion.nickName = txt
        return self.controladoraCarpetas.crearCarpetaEnDeciociones(txt)

    def agregarNodoAlArbolDeDecion(self, info):
        # la info es un vector[IDpadre, id, titulo, info]
        """
        1 -> los ID son de tipo numerico
        2 -> agregar al arbol
        """

        try:
            idPadre = int(info[0])
            idNodo = int(info[1])
            d = Decicion(idPadre, idNodo, info[2], info[3])
            self.arbolDeDeDecicion.addDato(d)
            
            return self.guardarNodoEnHDD(d)
        except:
            return False

    def guardarNodoEnHDD(self, decicion):
        """
        Una Decion[idPadre, Id, Titulo, Info]
        va a ser guardada en su carpeta correspondiente (Arbol.nickName)
        como id.txt
        con formato
        <IDPadre>ID</IDpadre>
        <ID>ID</ID>
        <HIJOS>ID,ID,ID</HIJOS>
        <TITULO>TituloDeMierda</TITULO>
        <EVENTO>EventoDeMierda</EVENTO>
        """
        idPadre = "<IDPadre>"+str(decicion.idPadre)+"</IDpadre>\n"
        idNodo = "<ID>" + str(decicion.id) + "</ID>\n"
        hijos = "<HIJOS>" + "</HIJOS>\n"
        titulo = "<TITULO>" +str(decicion.titulo)+ "</TITULO>\n"
        evento = "<EVENTO>\n"+str(decicion.quePaso)+"</EVENTO>"

        data = idPadre + idNodo + hijos + titulo + evento

        # Se guarda en HDD 
        try:
            ruta = self.rutaDelProyecto + "\\DATA\\DECICIONES\\" + str(self.arbolDeDeDecicion.nickName)  + "\\" + str(decicion.id) + ".txt"
            f = open(ruta, "w")
            f.write(data)
            f.close()
            return True
        except:
            return False
        

    def arbolDeDecicionEstaListo(self):
        """
        Si el arbol esta listo para trabajar : True or false
        """
        return self.arbolDeDecicionListo


    def retornarInformacionEconomica(self, tipo):
        """
        Cuando se solicite informacion sobre un año, 
        o un mes en especifico se retornara los conceptos de 
        ingresos o egresos de ese periodo.
        """
        tipoDeVista = None
        
        try: # Si es un año
            tipoDeVista = int(tipo)
            # Se retorna toda la informacion del año

            ruta = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\" + str(tipo) # Obtengo la ruta
            arch = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(ruta, ".xlsx") # Obtengo el nombre de todos los archivos


            data = [] # Aqui se empaqueta toda la informacion para procesarla


            for i in arch:
                rutaTemp = ruta + "\\" + i
                
                f = open(rutaTemp, encoding="UTF-8")
                data.append(f.read())
                f.close()

            # La informacion va a ser procesada
            return self.controladoraProcesamientoDeDatos.procesarReporteEconomigo(data)


        except: # Si es un mes
            
            # Se recupera la informacion del año actual
            ruta = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\" + str(self.tiempo.año()) # Obtengo la ruta
            arch = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(ruta, ".xlsx") # Obtengo el nombre de todos los archivos
            data = [] # Aqui se empaqueta toda la informacion para procesarla
            # Solo empaquetos los archivos que contengan informacion de ese mes
            for i in arch:
                if tipo in i:
                    rutaTemp = ruta + "\\" + i
                
                    f = open(rutaTemp, encoding="UTF-8")
                    data.append(f.read())
                    f.close()

            # La informacion va a ser procesada
            return self.controladoraProcesamientoDeDatos.procesarReporteEconomigo(data)

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

            try:
                if key == "diary":
                    all_years = self.controladoraCarpetas.listOfAllYearWriteInDiary()

                if key == "dreams":
                    all_years = self.controladoraCarpetas.listOfAllYearWriteInDreams()

                if key == "economy":
                    all_years = self.controladoraCarpetas.listarAñosDeEconomia()
            except:
                return

            
            for i in all_years:
                if key != "economy":
                    get_all_files_names = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(path+i, ".txt")
                
                    for j in get_all_files_names:
                        data_titles.append(j)
                        file_path = path+i+"\\"+j
                        data.append(self.loadFilePageByPath(file_path))
                else:
                    get_all_files_names = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(path+i, ".xlsx")
                    
                    if i not in data:
                        data[i] = {}

                    for j in get_all_files_names:
                        if j not in data[i]:
                            data[i][j] = {}

                        file_path = path+i+"\\"+j
                        data[i][j] = self.loadFilePageByPath(file_path)
            
        else:
            try:
                if key != "economy":
                    get_all_files_names = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(path+year, ".txt")
                    for j in get_all_files_names:
                        data_titles.append(j)
                        file_path = path+year+"\\"+j
                        data.append(self.loadFilePageByPath(file_path))
                else:
                    get_all_files_names = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(path+year, ".xlsx")
                    
                    if year not in data:
                        data[year] = {}

                    for i in get_all_files_names:
                        file_path = path+year+"\\"+i
                        data[year][i] = self.loadFilePageByPath(file_path)
            except:
                return
            

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
        Dependiendo de la hora da un saludo
        """
        hora = str(self.tiempo.hora()).split(":")[0]
        hora = hora.split(" ")
        hora = int(hora[len(hora)-1])

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

    def decir(self, palabra):
        """
        Sera dicha una palabra
        """
        self.audioMixer.line = self.rutaDelProyecto + "\\recursos\\audio\\" + palabra
        self.audioMixer.playSound()


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

    """FEMPUTADORA"""
    """FEMPUTADORA"""
    """FEMPUTADORA"""
    def loadQuestions(self):
        """
        Load all questions to chatbot in folder:
        DATA\QUESTIONS
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
        

    def getFemputadoraChatHistorial(self):
        return self.femputadora.conversation
    

    def femputadora_unknow(self):
        responses = ['Podrias Repetir?', 'No estoy seguro', 'No tengo esa información']
        return responses[random.randint(0, len(responses)-1)]


    def femputadora_hi(self):
        return "Hola"


    """END FEMPUTADORA"""
    """END FEMPUTADORA"""
    """END FEMPUTADORA"""


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
