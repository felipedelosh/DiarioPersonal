"""
Esta parte se encargara de la mineria:

Procesamiento de datos en json

1 - Registro de Logros de mi vida
2 - Cosas que hago




"""
# -⁻- coding: UTF-8 -*-
import json

from StringProcessor import *


class ControladoraProcesamientoDeDatos(object):
    def __init__(self, rutaDelProyecto, tiempo):
        self.stringProcessor = StringProcessor()
        self.rutaDelProyecto = rutaDelProyecto
        self.tiempo = tiempo
        """
        Este dicionario guarda los logros mas importantes del a+o
        Año:LogroA, LogroB
        """
        
        self.resultadoAnual = {}
        self.registroActividades = ""
        self.dataSentimientos = {} # Se guardan los sentimientos para ser analizados {"Sentimientos": nro, "Sentimiento":nro...}
        self.dataHorarioSemanal = {} # Se guandan la informacion porcentual de las actividades realizadas
        
        try:
            with open(self.rutaDelProyecto+"\\DATA\\RESULTADOANUAL\\resultadoAnual.txt", 'r', encoding="UTF-8") as file:
                self.resultadoAnual = json.load(file)
        except:
            pass

        try:
            with open(self.rutaDelProyecto+"\\DATA\\ACTIVIDADES\\"+str(self.tiempo.año())+"\\"+str(self.tiempo.estampaDeTiempo())+".txt", 'r', encoding="UTF-8") as file:
                self.registroActividades = json.load(file)
        except:
            pass

    def registrarLogroDeMiVida(self, año, logro):
        """Se hace un backup por si hay mas eventos ese a+o"""
        if str(año) in self.resultadoAnual.keys():
            if logro not in self.resultadoAnual[str(año)]:
                self.resultadoAnual[str(año)].append(logro)

        else:
            self.resultadoAnual[str(año)] = []
            self.resultadoAnual[str(año)].append(logro)

        return self.guardarJsonRegistroLogros()
        
    def guardarJsonRegistroLogros(self):
        try:
            with open(self.rutaDelProyecto+"\\DATA\\RESULTADOANUAL\\resultadoAnual.txt", 'w', encoding="UTF-8") as file:
                json.dump(self.resultadoAnual, file)
            return True
        except:
            return False

    def registrarActividad(self, actividad):
        """Si hay eventos de ese dia se hace backup"""
        try:
            """No se registrar Actividades dobles"""
            if actividad not in self.registroActividades:
                self.registroActividades = self.registroActividades + actividad + "\n"

                with open(self.rutaDelProyecto+"\\DATA\\ACTIVIDADES\\"+str(self.tiempo.año())+"\\"+str(self.tiempo.estampaDeTiempo())+".txt", 'w', encoding="UTF-8") as file:
                    json.dump(self.registroActividades, file)

                return True
            else:
                return False
            
        except:
            return False

    def guardarReporteEconomicoDebeHaber(self, reporte, dia, mes):
        try:
            f = open(self.rutaDelProyecto+"\\DATA\\ECONOMIA\\"+str(self.tiempo.año())+"\\"+mes+" "+dia+".xlsx", "w", encoding="UTF-8")
            f.write(reporte)
            f.close()
            return True
        except:
            return False

    def cargarReporteEconomicoDebeHaber(self, dia, mes):
        try:
            f = open(self.rutaDelProyecto+"\\DATA\\ECONOMIA\\"+str(self.tiempo.año())+"\\"+mes+" "+dia+".xlsx", "r", encoding="UTF-8")
            return f.read()
        except:
            return None

    def procesarDatosSentimientos(self, todosLosSentimientos, listadoSentimientos):
        """
        todosLosSentimientos : [sentimientoA, sentimientoB, sentimientoC ...]
        para preparar el diccionario {'sentimientoA':0, 'sentimientoB':0 ...}

        Entran una lista de sentimientos [feliz, feliz, triste]
        y eso es contado y se retorna {'depre': 0,'feliz':2, 'triste':1}
        """
        # Se reinicia el diccionario
        for i in todosLosSentimientos:
            self.dataSentimientos[str(i)] = 0
        # Se genera el reporte de todos los sentimientos
        for i in listadoSentimientos:
            try:
                temporal = self.dataSentimientos[i]
                temporal = temporal + 1
                self.dataSentimientos[str(i)] = temporal
            except:
                pass
        
        self._cleanZeroFeelings()
        return self.dataSentimientos
    
    def _cleanZeroFeelings(self):
        temp = {}
        for i in self.dataSentimientos:
            try:
                if self.dataSentimientos[i] > 0:
                    temp[i] = self.dataSentimientos[i]
            except:
                pass

        self.dataSentimientos = temp

    def procesarDatosSemanalHorario(self, todasLasActividades, informacion):
        """
        Dadas todas las actividades se crea el diccionario {acticidad:0}
        dada la informacion se calcula
        horas semanales = 168
        cada hora significa 0.5952%
        """
        # Se reinicia el diccionario
        for i in todasLasActividades:
            self.dataHorarioSemanal[str(i)] = 0

        for i in informacion:
            try:
                temporal = self.dataHorarioSemanal[str(i)] 
                temporal = temporal + 0.5952
                self.dataHorarioSemanal[str(i)] = round(temporal, 4)
            except:
                pass

        return self.dataHorarioSemanal

    def procesarReporteEconomigo(self, data):
        """

        Se procesa los datos y se hace el reporte asi

        los datos son un vector de informacion de tipo [a;0;0\nb;0;0]

        reporte = {Entradas:+, Salidas:-}


        
        """

        reporte = {}

        for i in data:
            for j in str(i).split("\n"):
                # Cada j contiene Etiqueta;+0,-0

                key = j.split(";") # Separo la etiqueta de la informacion

                if key != ['']: # Descarto lo que no tenga informacion
                    if key[0] in reporte: # Se actualiza la informacion
                        
                        vartemp = reporte[key[0]] # Se guarda la informacion de cuanto contenia el registro

                        try: # Se trabaja solo con informacion numerica

                            if int(key[1]) > 0:
                                vartemp = vartemp + int(key[1])
                            else:
                                vartemp = vartemp - int(key[2])


                            reporte[key[0]] = vartemp # Se actualiza la informacion

                        except:
                            pass



                    else:
                        reporte[key[0]] = 0 # Se pone la etiqueta

                        try: # Se trabaja solo con numeros
                            
                            if int(key[1]) > 0:
                                reporte[key[0]] = int(key[1])
                            else:
                                reporte[key[0]] = -int(key[2])
                        except:
                            pass


        return reporte
    

    def getFullReport(self, data):
        """
        retrun a  sumary of {diary:str, dreams:str, people:str, economy:str, time:str, feelings:str, app use:str}
        """
        information = {}
        try:
            self._getDiarySummary(information, data)
            self._getDreamSumary(information, data)

        except:
            pass

        return information
    
    def _getDiarySummary(self, information, data):
        """
        Process all Diary data and get sumary
        """
        try:
            txt = ""
    
            top_titles = self._getCounterWriterWords(data["diary_titles"])
            top_titles = self._shorterDic(top_titles)

            if top_titles != None:
                txt = txt + "\nLo que más vives es: \n\n" + self._apendTopTitlesInTxt(top_titles) + "\n"

            top_words = {}
            top_date = {}
            for i in data["diary"]:
                self._getMostWriteWordInText(top_words, top_date, i)

            top_words = self._shorterDic(top_words)
            if top_words != None:
                txt = txt + "\nAquello que más escribes es: \n\n" + self._apendTopWordsInTxt(top_words) + "\n"
                

            top_date = self._shorterDic(top_date)
            if top_date != None:
                txt = txt + "\nLos días en que más escribes son: \n\n" + self._apendTopDaysInTxt(top_date) + "\n"

            # Add total write
            txt = txt + "\nEscribiste un total de: " + str(len(data["diary"])) + " Veces"
            information["diary"] = txt
        except:
            pass


    def _getCounterWriterWords(self, str_vec):
        """
        Enter a vector [str, str, str, str]
        and return a {str(word):int(#), str(word):int(#), str(word):int(#) ...}
        """
        top_words = {}

        for i in str_vec:
            clean_txt = self.stringProcessor.cleanWord(i)
            for j in clean_txt.split(" "):
                if j != "" and not self.stringProcessor.isExcludeWord(j):
                    if j in top_words:
                        top_words[j] = top_words[j] + 1
                    else:
                        top_words[j] = 1

        return top_words

    def _getMostWriteWordInText(self, top_words, top_date, txt):
        """
        Enter a TXT and add
        top_words" = "str", #frecuency, "str", #frecuency, "str", #frecuency
        top_date = "day", #count
        """
        data = txt.split("\n")
        rich_text = data[0:len(data)-3]
        date_text = data[-3]
        

        self._countADayInDate(date_text, top_date)
        

        for i in rich_text:
            for j in str(i).split(" "):
                if str(j).strip() != "" and not self.stringProcessor.isExcludeWord(j):
                    word = self.stringProcessor.cleanWord(j)
                    if j in top_words:
                        top_words[word] = top_words[word] + 1
                    else:
                        top_words[word] = 1


    def _countADayInDate(self, txtTimeStamp, top_date):
        """
        Enter a str: txtTimeStamp if is a date save count  day: MON, TUE... in top_date
        """
        days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

        date = txtTimeStamp.split(" ")
        day = date[0]


        if str(day).lower() in days:
            if day in top_date:
                top_date[day] = top_date[day] + 1
            else:
                top_date[day] = 1

    def _getDreamSumary(self, information, data):
        """
        Process all Dreams data and get sumary
        """
        try:
            txt = ""

            top_titles = self._getCounterWriterWords(data["dreams_titles"])
            top_titles = self._shorterDic(top_titles)

            if top_titles != None:
                txt = txt + "\nLo que más sueñas es: \n\n" + self._apendTopTitlesInTxt(top_titles) + "\n"

            top_words = {}
            top_date = {}
            for i in data["dreams"]:
                self._getMostWriteWordInText(top_words, top_date, i)

            top_words = self._shorterDic(top_words)
            if top_words != None:
                txt = txt + "\nAquello que más ves en tus sueños es: \n\n" + self._apendTopWordsInTxt(top_words) + "\n"

            top_date = self._shorterDic(top_date)
            if top_date != None:
                txt = txt + "\nLos días en que más sueñas son: \n\n" + self._apendTopDaysInTxt(top_date) + "\n"

            # Add total write
            txt = txt + "\nSoñaste un total de: " + str(len(data["dreams"])) + " Veces"
            information["dreams"] = txt
        except:
            pass
    

    def _apendTopTitlesInTxt(self, vec_titles):
        """
        Enter a vec=[] and return 7 titles in str
        """
        str_top_tiles = "" 
        if vec_titles != None and len(vec_titles) > 0:
            if len(vec_titles) >= 7:
                for i in vec_titles[0:7]:
                    str_top_tiles = str_top_tiles + "\n *  " + str(i[0])
            else:
                for i in vec_titles:
                    str_top_tiles = str_top_tiles + "\n *  " + str(i[0])
        else:
            pass

        return str_top_tiles
    

    def _apendTopWordsInTxt(self, vec_word):
        """
        Enter a vec
        """
        str_top_words = ""

        if len(vec_word) >= 15:
            for i in vec_word[0:15]:
                str_top_words = str_top_words + "\n *  " + str(i[0])
        else:
            for i in vec_word:
                str_top_words = str_top_words + "\n *  " + str(i[0])

        return str_top_words 
    

    def _apendTopDaysInTxt(self, vec_day):
        """
        
        """
        str_top_date  = ""

        if len(vec_day) > 3:
                for i in vec_day[0:3]:
                    str_top_date = str_top_date + "\n *  " + self._translateDay(str(i[0]))
        else:
            for i in vec_day:
                str_top_date = str_top_date + "\n *  " + self._translateDay(str(i[0]))

        return str_top_date 


            

    def _shorterDic(self, dic):
        """
        Enter a Dic {key:str, value:int}
        and order via bubbleshort
        """
        all_data = []
        # Copy all data in vect of tuples
        for i in dic:
            all_data.append((i, dic[i]))



        # Bubble Short
        n = len(all_data)
        swapped = False
        for i in range(n-1):
            for j in range(0, n-i-1):
                if all_data[j][1] < all_data[j + 1][1]:
                    swapped = True
                    all_data[j], all_data[j+1] = all_data[j+1], all_data[j]

                
            if not swapped:
                return all_data

        return all_data
    

    def _translateDay(self, keyDay):
        """
        Enter a Key of day and return spanish name
        if enter mon output : lunes
        """
        _t = {'Mon': 'Lunes', 'Tue': 'Martes', 'Wed': 'Miercoles', 'Thu': 'Jueves', 'Fri': 'Viernes', 'Sat': 'Sabado', 'Sun':'Domingo'}

        try:
            return _t[keyDay]
        except:
            return keyDay
