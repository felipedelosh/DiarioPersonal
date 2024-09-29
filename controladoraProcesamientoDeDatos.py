"""
Esta parte se encargara de la mineria:

Procesamiento de datos en json

1 - Registro de Logros de mi vida
2 - Cosas que hago




"""
# -⁻- coding: UTF-8 -*-
import json
import os # TO get path project, read folders
from os import scandir
from StringProcessor import *


class ControladoraProcesamientoDeDatos(object):
    def __init__(self, rutaDelProyecto, tiempo, folderController, env):
        self.stringProcessor = StringProcessor(env)
        self.rutaDelProyecto = rutaDelProyecto
        self.tiempo = tiempo
        self.folderControler = folderController
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

    def getAllFilesNamesxTypeInFolderPath(self, path, fileExtension):
        filesNames = []
        for i in scandir(path):
            try:
                if fileExtension in i.name:   
                    filesNames.append(i.name)    
            except:
                pass

        return filesNames
    

    def getALLFoldersNamesInFolderPath(self, path):
        folderNames = []

        with os.scandir(path) as dir:
            for itterDir in dir:
                if itterDir.is_dir():
                    folderNames.append(itterDir.name)

        return folderNames
    

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
        
        # Dont return 0 information.
        return self._cleanZeroFeelings()
    

    def proccesDrugsDataByYYYY(self, YYYY):
        """
        GET ALL DATA in DATA\DRUGS\YYYY
        group {"DRUG": COUNTER, ..."DRUG": COUNTER}
        """
        _outputData = {}
        _path = f"{self.rutaDelProyecto}\\DATA\\DRUGS\\{YYYY}"

        # get ALL Files names
        filesNames = self.getAllFilesNamesxTypeInFolderPath(_path, ".txt")

        # Group data
        for i in filesNames:
            _id = str(i).split("-")[0]
            _id = _id.lstrip().rstrip()
            if _id not in _outputData.keys():
                _outputData[_id] = 0
            _outputData[_id] = _outputData[_id] + 1
            
        return _outputData
        
    def _cleanZeroFeelings(self):
        temp = {}
        for i in self.dataSentimientos:
            try:
                if self.dataSentimientos[i] > 0:
                    temp[i] = self.dataSentimientos[i]
            except:
                pass

        return temp
    
    def sumaryALLActivities24H(self, path):
        """
        Enter a DATA\DISTRIBUCIONTIEMPO\YYYY 
        and return {"Activity":#, "Activity":#, "Activity":#}
        """
        data = {}

        try:
            for i in self.folderControler.listarTodosLosArchivosdeCarpeta(path, ".txt"):
                _data = self.folderControler.getTextInFile(path + "\\" + str(i))
                for j in _data.split("\n"):
                    if str(j) != "":
                        _act = str(j).split(":")[-1]
                        if _act not in data.keys():
                            data[_act] = 0
                        data[_act] = data[_act] + 1
        except:
            pass

        return data
    

    def sumaryALLSleep24H(self, path):
        """
        Enter a DATA\DISTRIBUCIONTIEMPO\YYYY 
        and return {
                total: # hours all year
                total-by-day: # hours all year in these day
                avg-by-day: avg of this day in these year
            }
        """
        data = {}
        data["total"] = 0

        # Control of days found
        # Save dates in format {MONDAY:["YYYY MM DD.txt", ..."YYYY MM DD.txt"], TH....}
        _control = {}
        for i in self.tiempo.diasDeLaSemana:
            _control[i] = []

        # Put all days of week
        for i in self.tiempo.diasDeLaSemana:
            data[f"total-{i}"] = 0
            data[f"avg-{i}"] = 0


        try:
            for i in self.folderControler.listarTodosLosArchivosdeCarpeta(path, ".txt"):
                _data = self.folderControler.getTextInFile(path + "\\" + str(i))
                for j in _data.split("\n"):
                    if str(j).strip() != "":
                        try:
                            _arr = str(j).split(":")
                            if (_arr[1] == "dormir"):
                                # get time in format YYYY-MM-DD
                                _timeYYYYMMDD = str(i).replace(".txt", "")
                                _timeYYYYMMDD = _timeYYYYMMDD.split(" ")
                                _timeYYYYMMDD = f"{_timeYYYYMMDD[0]}-{_timeYYYYMMDD[1]}-{_timeYYYYMMDD[2]}"
                                
                                _nameOfDay = self.tiempo.getNameOfDayByDateYYYYMMDD(_timeYYYYMMDD)

                                # Control of day register by date
                                if i not in _control[_nameOfDay]:
                                    _control[_nameOfDay].append(i)

                                # Count Hour in total in this day
                                data[f"total-{_nameOfDay}"] = data[f"total-{_nameOfDay}"] + 1

                                # Counter SLEEP ++
                                data["total"] = data["total"] + 1
                        except:
                            pass
        except:
            pass

        # Calcule prom
        for i in _control:
            try:
                sum = data[f"total-{i}"]
                total = len(_control[i])
                data[f"avg-{i}"] = round(sum/total, 2)
            except:
                pass

        return data
    

    def sumaryALLLeisureTime24H(self, path):
        """
        Enter a DATA\DISTRIBUCIONTIEMPO\YYYY 
        and return {
                total: # hours all year
                total-by-day: # hours all year in these day
                avg-by-day: avg of this day in these year
            }
        """
        data = {}
        data["total"] = 0
        data["total-faptime"] = 0
        data["total-tv"] = 0
        data["total-leisure"] = 0
        data["total-social-network"] = 0

        # Control of days found
        # Save dates in format {MONDAY:["YYYY MM DD.txt", ..."YYYY MM DD.txt"], TH....}
        _control = {}
        for i in self.tiempo.diasDeLaSemana:
            _control[i] = []
            _control[f"faptime-{i}"] = []
            _control[f"tv-{i}"] = []
            _control[f"leisure-{i}"] = []
            _control[f"social-network-{i}"] = []

        # Put all days of week
        for i in self.tiempo.diasDeLaSemana:
            # Total peer year
            data[f"total-{i}"] = 0
            data[f"avg-{i}"] = 0

            # Total peer leisure activity
            data[f"total-faptime-{i}"] = 0
            data[f"avg-faptime-{i}"] = 0
            data[f"total-tv-{i}"] = 0
            data[f"avg-tv-{i}"] = 0
            data[f"total-leisure-{i}"] = 0
            data[f"avg-leisure-{i}"] = 0
            data[f"total-social-network-{i}"] = 0
            data[f"avg-social-network-{i}"] = 0


        try:
            for i in self.folderControler.listarTodosLosArchivosdeCarpeta(path, ".txt"):
                _data = self.folderControler.getTextInFile(path + "\\" + str(i))
                for j in _data.split("\n"):
                    if str(j).strip() != "":
                        try:
                            _arr = str(j).split(":")
                            if _arr[1] == "FAPTIME" or _arr[1] == "ocio" or _arr[1] == "televisión" or _arr[1] == "redes sociales":
                                # get time in format YYYY-MM-DD
                                _timeYYYYMMDD = str(i).replace(".txt", "")
                                _timeYYYYMMDD = _timeYYYYMMDD.split(" ")
                                _timeYYYYMMDD = f"{_timeYYYYMMDD[0]}-{_timeYYYYMMDD[1]}-{_timeYYYYMMDD[2]}"
                                
                                _nameOfDay = self.tiempo.getNameOfDayByDateYYYYMMDD(_timeYYYYMMDD)

                                # General day of week control
                                _control[_nameOfDay].append(j)

                                # Count Hour in total in this day
                                data[f"total-{_nameOfDay}"] = data[f"total-{_nameOfDay}"] + 1

                                if _arr[1] == "FAPTIME":
                                    _control[f"faptime-{_nameOfDay}"].append(j)
                                    data[f"total-faptime-{_nameOfDay}"] = data[f"total-faptime-{_nameOfDay}"] + 1
                                    data["total-faptime"] = data["total-faptime"] + 1

                                if _arr[1] == "ocio":
                                    _control[f"leisure-{_nameOfDay}"].append(j)
                                    data[f"total-leisure-{_nameOfDay}"] = data[f"total-leisure-{_nameOfDay}"] + 1
                                    data["total-leisure"] = data["total-leisure"] + 1

                                if _arr[1] == "televisión":
                                    _control[f"tv-{_nameOfDay}"].append(j)
                                    data[f"total-tv-{_nameOfDay}"] = data[f"total-tv-{_nameOfDay}"] + 1
                                    data["total-tv"] = data["total-tv"] + 1

                                if _arr[1] == "redes sociales":
                                    _control[f"social-network-{_nameOfDay}"].append(j)
                                    data[f"total-social-network-{_nameOfDay}"] = data[f"total-social-network-{_nameOfDay}"] + 1
                                    data["total-social-network"] = data["total-social-network"] + 1

                                # Counter ++
                                data["total"] = data["total"] + 1
                        except:
                            pass
        except:
            pass

        # Calculate AVG
        for i in self.tiempo.diasDeLaSemana:
            total = len(_control[i])

            try:
                sum = data[f"total-faptime-{i}"]
                data[f"avg-faptime-{i}"] = round(sum/total, 2)
            except:
                pass

            try:
                sum = data[f"total-tv-{i}"]
                data[f"avg-tv-{i}"] = round(sum/total, 2)
            except:
                pass

            try:
                sum = data[f"total-leisure-{i}"]
                data[f"avg-leisure-{i}"] = round(sum/total, 2)
            except:
                pass

            try:
                sum = data[f"total-social-network-{i}"]
                data[f"avg-social-network-{i}"] = round(sum/total, 2)
            except:
                pass

        return data


    def getSumaryOfDrugs(self, path):
        """
        Enter a path //DRUGS//YYYY return {}
        data[DRUGSQTY] = {drug, qty}
        data[DRUGSDAYS] = {monday: qty, th...}
        data[REASON] = {keyword: qty, ...}
        data[EFFECT] = {keyword: qty, ...}
        """
        data = {}
        data["DRUGSQTY"] = {}
        data["DRUGSDAYS"] = {}
        data["REASON"] = {}
        data["EFFECT"] = {}
        data["METADATA"] = {}

        _regs = self.folderControler.listarTodosLosArchivosdeCarpeta(path, ".txt")

        try:
            for i in _regs:
                _fileTitle = str(i) # drug - YYYY MM DD.txt
                # Count drug
                _iDrug = _fileTitle.split("-")[0].strip()
                if _iDrug not in data["DRUGSQTY"].keys():
                    data["DRUGSQTY"][_iDrug] = 0
                data["DRUGSQTY"][_iDrug] = data["DRUGSQTY"][_iDrug] + 1
                # Count day
                _iDrugDate = _fileTitle.split("-")[1]
                _iDrugDate = _iDrugDate.replace(".txt", "").lstrip().rstrip()
                _iDrugDate = _iDrugDate.split(" ")
                _iDrugDate = self.tiempo.getNameOfDayByDate([int(_iDrugDate[0]),int(_iDrugDate[1]),int(_iDrugDate[2])])
                if _iDrugDate not in data["DRUGSDAYS"].keys():
                    data["DRUGSDAYS"][_iDrugDate] = 0
                data["DRUGSDAYS"][_iDrugDate] = data["DRUGSDAYS"][_iDrugDate] + 1

                #Detonators
                _txt = self.folderControler.getTextInFile(f"{path}\\{i}")
                # Ge reasons
                _counter = 0
                _tempRasons = {}
                _tempEffecs = {}
                for iterTXT in str(_txt).split("\n\n\n"):
                    if iterTXT.strip() != "":
                        if _counter == 0:
                            if _iDrug not in _tempRasons.keys():
                                _tempRasons[_iDrug] = ""

                            _tempRasons[_iDrug] = _tempRasons[_iDrug] + " " + iterTXT
                            

                        if _counter == 1:
                            if _iDrug not in _tempEffecs.keys():
                                _tempEffecs[_iDrug] = ""

                            _tempEffecs[_iDrug] = _tempEffecs[_iDrug] + " " + iterTXT

                        if _counter >= 2:
                            _counter = 0

                        _counter = _counter + 1

                self._getSumaryOfDrugsGetReasonsOrEffects("REASON", _tempRasons, data)
                self._getSumaryOfDrugsGetReasonsOrEffects("EFFECT", _tempEffecs, data)
        except:
            pass

        # Order
        data["DRUGSQTY"] = self._shorterDic(data["DRUGSQTY"])
        data["DRUGSDAYS"] = self._shorterDic(data["DRUGSDAYS"])

        _temp = {}
        for i in data["REASON"]:
            _temp[i] = self._shorterDic(data["REASON"][i])
        data["REASON"] = _temp
        _temp = {}
        for i in data["EFFECT"]:
            _temp[i] = self._shorterDic(data["EFFECT"][i])
        data["EFFECT"] = _temp
        data["METADATA"]["lenght"] = len(_regs)

        return data
    
    def _getSumaryOfDrugsGetReasonsOrEffects(self, key, _temp, data):
        """
        Enter data["REASON"] or data["EFFECT"] and save _temp information
        """
        for _iterDrugTempRasons in _temp:
            _dataGroupByWords = self.stringProcessor.groupTextByWords(_temp[_iterDrugTempRasons])
            if _dataGroupByWords != {}:
                if _iterDrugTempRasons not in data[key].keys():
                    data[key][_iterDrugTempRasons] = {}

                for _iterWorddataGroupByWords in _dataGroupByWords:
                    if _iterWorddataGroupByWords not in data[key][_iterDrugTempRasons].keys():
                        data[key][_iterDrugTempRasons][_iterWorddataGroupByWords] = _dataGroupByWords[_iterWorddataGroupByWords]
                    else:
                        data[key][_iterDrugTempRasons][_iterWorddataGroupByWords] = data[key][_iterDrugTempRasons][_iterWorddataGroupByWords] + _dataGroupByWords[_iterWorddataGroupByWords]


    def getSumaryYYYYAllActivities24HPerDayOfWeek(self, path):
        """
        Enter a PATH DATA\DISTRIBUCIONTIEMPO\YYYY 
        and return {"name of day":{"HOUR":{"activuty":counter..."activuty":counter}}}
        """
        data = {}

        #init data with days
        for i in self.tiempo.diasDeLaSemana:
            data[i] = {}


        for i in self.folderControler.listarTodosLosArchivosdeCarpeta(path, ".txt"):
            try:
                # Get all day summary
                _data = self.folderControler.getTextInFile(path + "\\" + str(i))
                _whatDay = str(i).split(".txt")[0]
                _whatDay = str(_whatDay).split(" ")
                YYYY = int(_whatDay[0])
                MM = int(_whatDay[1])
                DD = int(_whatDay[2])
                # Get name of day in the date YYYY MM DD
                _whatDay = self.tiempo.getNameOfDayByDate([YYYY, MM, DD])
                for j in _data.split("\n"):
                    _temp = str(j).split(":")
                    _hour = _temp[0]
                    _activity = _temp[1]

                    if not str(_hour) in data[_whatDay].keys():
                        data[_whatDay][_hour] = {}

                    if not _activity in data[_whatDay][_hour].keys():
                        data[_whatDay][_hour][_activity] = 0

                    data[_whatDay][_hour][_activity] = data[_whatDay][_hour][_activity] + 1
            except:
                pass

        return data


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
    
    def getFormatedEconomyReportByYear(self, YYYY):
        """
        return d = {"DATA":{"YYYY-MM-DD":{"IN": $, "OUT":$}}, "METADATA":{"maxin":$, maxout:$}}
        """
        data = {}
        data["DATA"] = {}
        maxIN = 0
        maxOUT = 0

        try:
            _path = f"{self.rutaDelProyecto}\\DATA\\ECONOMIA\\{YYYY}"
            _filesNames = self.getAllFilesNamesxTypeInFolderPath(_path, ".xlsx")

            for i in _filesNames:
                txt = self.getTextInFile(f"{_path}\\{i}") # Get Economic Data

                if txt != "": # Group Data By Day
                    try:
                        moneyIn = 0
                        moneyOut = 0
                        for j in txt.split("\n"):
                            if str(j).strip() != "":
                                _info = j.split(";")
                                moneyIn = moneyIn + int(_info[1])
                                moneyOut = moneyOut + int(_info[2])
                    except:
                        continue
                
                # Save day
                id = i.split(".")[0] 
                id = id.split(" ")
                id = f"{YYYY}-{self.tiempo.getMonthNumberByMonthName(id[0])}-{id[1]}"
                if maxIN < moneyIn:
                    maxIN = moneyIn
                if maxOUT < moneyOut:
                    maxOUT = moneyOut
                data["DATA"][id] = {"in":moneyIn, "out":moneyOut}
        except:
            pass

        data["METADATA"] = {"maxin":maxIN,"maxout":maxOUT}
        return data

    def getFormatedTimeDistributionReportByYear(self, YYYY):
        """
        return d = {"DATA":{"YYYY-MM-DD":{"sleep": hrs, "life": hrs}}, "METADATA":{}}
        """
        data = {"DATA":{}, "METADATA":{}}

        try:
            _path = f"{self.rutaDelProyecto}\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\{YYYY}"
            _filesNames = self.getAllFilesNamesxTypeInFolderPath(_path, ".txt")

            for i in _filesNames:
                txt = self.getTextInFile(f"{_path}\\{i}")

                if txt != "":
                    try:
                        _totalHoursDay = 0
                        _hoursSleep = 0
                        for j in txt.split("\n"):
                            if str(j).strip() != "":
                                _info = j.split(":")[1]
                                if _info == "dormir":
                                    _hoursSleep = _hoursSleep + 1
                                _totalHoursDay = _totalHoursDay + 1

                    except:
                        continue

                    
                id = str(i).split(".")[0]
                id = id.split(" ")
                id = f"{id[0]}-{id[1]}-{id[2]}"

                data["DATA"][id] = {"sleep":_hoursSleep, "life":_totalHoursDay-_hoursSleep}

        except:
            pass

        return data

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
    

    def getTAccountsReportByKeyWord(self, keyword):
        """
        Read data in DATA/ECONOMIA
        and return {size=#, data=[(concept, #, #),...(concept, #, #)], in=totalMoneyIn, out=totalMoneyOut}
        """
        _data = {}
        _data["size"] = 0
        _data["data"] = []
        _data["in"] = 0
        _data["out"] = 0
        try:
            path = f"{self.rutaDelProyecto}\\DATA\\ECONOMIA"
            _folders = self.getALLFoldersNamesInFolderPath(path)

            for i in _folders:
                try:
                    # Only info of years
                    YYYY = int(i)
                    _filesNanesPerYYYY = self.getAllFilesNamesxTypeInFolderPath(f"{path}\\{YYYY}", ".xlsx")

                    for j in _filesNanesPerYYYY:
                        _codename = f"{YYYY} {str(j).replace(".xlsx", "")}"
                        _readFileData = self.getTextInFile(f"{path}\\{YYYY}\\{j}")
                        for k in _readFileData.split("\n"):
                            if str(k).strip() != "":
                                try:
                                    _rowTAccount = k.split(";")
                                    
                                    # Save only by keyword
                                    if str(keyword).lower() in str(_rowTAccount[0]).lower():
                                        _data["data"].append((_codename, _rowTAccount[1], _rowTAccount[2]))

                                        _data["in"] = _data["in"] + int(_rowTAccount[1])
                                        _data["out"] = _data["out"] + int(_rowTAccount[2])
                                except:
                                    pass
                except:
                    pass
        except:
            pass

        _data["size"] = len(_data["data"])

        return _data
    

    def getFullReport(self, data):
        """
        retrun a  sumary of {diary:str, dreams:str, people:str, economy:str, time:str, feelings:str, app use:str}
        """
        information = {}
        try:
            self._getDiarySummary(information, data)
            self._getDreamSumary(information, data)
            self._getPeopleSumary(information, data)
            self._getEconomySumary(information, data)

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
            information["Diario"] = txt
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
            information["Sueños"] = txt
        except:
            pass

    def _getPeopleSumary(self, information, data):
        """
        Proccess all people data and append in information
        """
        try:
            txt = ""
            
            txt = self._analizedDataPeople(data)
            
            txt = txt + "\n\n\nConectaste con un total de: "+ str(len(data["people_names"])) + " Personas."

            # Add information
            information["Personas"] = txt
        except:
            pass

    def _analizedDataPeople(self, data):
        """
        Serach in all description of people the points and get a emoji
        """
        txt = ""

        for i in data["people"]:
            # Save a Name:
            txt = txt + "\n *  " + str(i).upper()

            emotional = ""
            count = 0

            for j in data["people"][i]:
                if "alias" in j:
                    txt = txt + "\nAlias: " + data["people"][i][j]

                if "description-" in j:
                    points = data["people"][i][j].split("\n")[-1]
                    emotional = emotional + self._rtnEmotional(str(points))
                    count = count + 1
            
            txt = txt + "\nEfectos en ti: " + emotional
            txt = txt + "\nTotal descripciones: " + str(count) + "\n\n"


        return txt 
    
    def _rtnEmotional(self, emotional):
        """
        Enter a points [0, 100] and return emoji
        """
        emoji = ['😔', '☹️', '🤨', '😐', '🙃', '🙂', '😀', '😄', '😆', '😁']

        try:
            emotional = round(int(emotional)/len(emoji))
            if emotional == 0:
                return emoji[emotional]
            else:
                return emoji[emotional-1]
        except:
            return ""
    

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
    

    def _getEconomySumary(self, information, data):
        try:
            txt = ""

            _counter_mov = 0
            _aku_money_in = 0
            _aku_money_out = 0

            for i in data["economy"]:
                _total_in = 0
                _total_out = 0

                txt = txt +  "\nAño: " + i
                
                for j in data["economy"][i]:
                    e_data = data["economy"][i][j]

                    for k in e_data.split("\n"):
                        if str(k).strip() != "":
                            _counter_mov = _counter_mov + 1
                            try:
                                e_i_info = k.split(";")

                                description = e_i_info[0]

                                e_in = int(e_i_info[1])
                                _aku_money_in = _aku_money_in + e_in # For all time
                                _total_in = _total_in + e_in # Only for the year

                                e_out = int(e_i_info[2])
                                _aku_money_out = _aku_money_out + e_out
                                _total_out = _total_out - e_out
                            except:
                                pass

                txt = txt + "\nEntradas: $" + str(_total_in) + " ,Salidas: $" + str(_total_out) + "\n\n"

            txt = txt + "\nTotal movimientos economicos: " + str(_counter_mov) + ".\n"
            txt = txt + "\nTotal dinero entrante: $" + str(_aku_money_in)  + "."
            txt = txt + "\nTotal dinero saliente: $" + str(_aku_money_out)  + "."


            information["Economia"] = txt
        except:
            pass


    def _shorterDic(self, dic):
        """
        Enter a Dic {key:str, value:int}
        and order via bubbleshort
        return [('X', #),...('Z', #))]
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
