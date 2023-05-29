import os
from datetime import datetime


class Controller:
    def __init__(self) -> None:
        self.path = str(os.path.dirname(os.path.abspath(__file__)))
        self._outputDataDiary = {}
        self._counterOutputDataDiary = 0
        self._outputDataFeelings = {}
        self._counterOutputDataFeelings = 0
        self._outputDAtaEconomy = {}
        self._counterOutputDataEconomy = 0
        self.consoleText = ""
        self._loadStatus = False
        self.dataSQL = ""
        self.loadSQL()

    def loadSQL(self):
        try:
            path = self.path + "\\SQL\\BACKUP.sql"
            with open(path, encoding="UTF-8") as f:
                self.dataSQL = f.read()
            self._loadStatus = True
        except:
            self._loadStatus = False

    def createFolder(self, path):
        """IF not extist create"""
        if not os.path.isdir(path):
            os.mkdir(path)

    def generateInfo(self, year, type_info):
        t_personal_page_diary = False
        t_personal_dream_diary = False
        t_day_time_distribution = False
        t_personal_feeling_counter = False
        t_economy_t_account = False

        if type_info == "all" or type_info == "diary":
            self.consoleText = self.consoleText = "Analizando data de diario...\n"
            self._outputDataDiary = {}
            self._counterOutputDataDiary = 0
            t_personal_page_diary = True

        if type_info == "all" or type_info == "dreams":
            t_personal_dream_diary = True

        if type_info == "all" or type_info == "time":
            t_day_time_distribution = True

        if type_info == "all" or type_info == "feelings":
            t_personal_feeling_counter = True


        if type_info == "all" or type_info == "economy":
            self._outputDAtaEconomy = {}
            self._counterOutputDataEconomy = 0
            t_economy_t_account = True

        for i in self.dataSQL.split("\n"):
            self.consoleText = ""

            if str(i).strip() != "":
                if t_personal_page_diary:
                    if "t_personal_page_diary" in i:
                        data = str(i).split("INSERT INTO t_personal_page_diary (ID, pageName, year, timeStamp, history) VALUES ")[1]
                        data = data.split(", ")
                        
                        title_counter = data[0]
                        title_counter = title_counter.replace('(', '')

                        title = data[1]
                        title = title.replace("\'", '')

                        # Day Month #Day Month Hour Year
                        _timeStamp = "\n\n" + self._getANameOfWeekDayByDate(data[3]) + " " + self._translateMonth(data[3]) + " " + self._translateDate(data[3]).split(" ")[2] + " 10:10:10 " +  self._translateDate(data[3]).split(" ")[0] + "\n\n"

                        date = self._translateDate(data[3])
                        
                        date = date.replace(":", ' ')

                        # File name
                        file_name = date + " - " + title+title_counter + ".txt"

                        # Text
                        text = data[-1]
                        # Erases '\n ');
                        text = text[3:-3]
                        text = str(text).replace('\\n', "\n")
                        # Add time stamp
                        text = text + _timeStamp

                        data_year = data[2]
                        data_year = data_year.replace("'", '')




                        if year == "all":
                            # Add to diary info
                            if data_year not in self._outputDataDiary:
                                self._outputDataDiary[data_year] = {}

                            self._outputDataDiary[data_year][file_name] = text 
                            self._counterOutputDataDiary = self._counterOutputDataDiary + 1      
                        else:
                            if data_year == year:
                                if data_year not in self._outputDataDiary:
                                    self._outputDataDiary[data_year] = {}

                                self._outputDataDiary[data_year][file_name] = text 
                                self._counterOutputDataDiary = self._counterOutputDataDiary  + 1


                if t_personal_feeling_counter:
                    if "t_personal_feeling_counter" in i:
                        data = str(i).split("INSERT INTO t_personal_feeling_counter (timeStamp, feelingName) VALUES ")[1]
                        data = data.split(", ")
                        
                        date = data[0]
                        date = date.replace("'", '')
                        date = date.replace("(", '')
                        date = date.split(":")
                        YYYY = date[0]
                        MM = date[1]
                        MM = self._getNumberOfMonthByFullNameMonth(MM)
                        DD = date[2]

                        # Name of file YYYY MM DD
                        fileName = f"{YYYY} {MM} {DD}.txt"


                        # Need Create Year in info?
                        if YYYY not in self._outputDataFeelings.keys():
                            self._outputDataFeelings[YYYY] = {}


                        if fileName not in self._outputDataFeelings[YYYY].keys():
                            self._outputDataFeelings[YYYY][fileName] = ""

                        

                        # Save a feeling
                        concept = data[1]
                        concept = concept.replace("'", "")
                        concept = concept.replace(");", "")
                        self._outputDataFeelings[YYYY][fileName] = concept
                        self._counterOutputDataFeelings = self._counterOutputDataFeelings + 1

                if t_economy_t_account:
                    if "t_economy_t_account" in i:
                        data = str(i).split("INSERT INTO t_economy_t_account (timeStamp, id, concept, debit, credit) VALUES ")[1]
                        data = data.split(", ")

                        

                        date = data[0]
                        # Erase (' '
                        date = date[2:-1]

                        year = date.split(":")[0]
            
                        if year not in self._outputDAtaEconomy:
                            self._outputDAtaEconomy[year] = {}

                        file_name = self._getEconomyFilename(date)

                        if file_name not in self._outputDAtaEconomy[year]:
                            self._outputDAtaEconomy[year][file_name] = ""

                        concept = data[2]
                        concept = concept.replace("\'", '')
                        concept = concept.lstrip()
                        concept = concept.rstrip()

                        money_in = data[3]
                        money_out = data[4]
                        money_out = money_out.replace(");", "")

                        # Save
                        self._outputDAtaEconomy[year][file_name] = self._outputDAtaEconomy[year][file_name] + concept + ";" + money_in + ";" + money_out + ";\n"
                        self._counterOutputDataEconomy = self._counterOutputDataEconomy + 1




        
        # Save LOGS
        if t_personal_page_diary:
            path = self.path + "\\OUTPUT\\DIARIO\\"
            self.saveFiles(path ,self._outputDataDiary)
            self.consoleText = self.consoleText + "Total info encontrada Diario = " + str(self._counterOutputDataDiary) + "\n"


        if t_personal_feeling_counter:
            path = self.path + "\\OUTPUT\\SENTIMIENTOS\\"
            self.saveFiles(path ,self._outputDataFeelings)
            self.consoleText = self.consoleText + "Total info encontrada Sentimientos = " + str(self._counterOutputDataFeelings) + "\n"
            
            

        if t_economy_t_account:
            path = self.path + "\\OUTPUT\\ECONOMIA\\"
            self.saveFiles(path ,self._outputDAtaEconomy)
            self.consoleText = self.consoleText + "Total info encontrada Economia = " + str(self._counterOutputDataEconomy) + "\n"

    def saveFiles(self, path, data):
        try:
            # create sup folder
            self.createFolder(path)
            for i in data:
                # Create a year folder
                self.createFolder(path+i)
                # Save files
                for j in data[i]:
                    with open(path+i+"\\"+j, 'w', encoding="UTF-8") as f:
                        f.write(data[i][j])
                        f.close()

        except:
            print("Error Generando los datos")


    

    def _translateDate(self, date):
        """
        enter date > '2022:Mayo:8'
        output = 2022 5 8
        """
        month = {'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4, 'mayo': 5, 'junio': 6, 'julio': 7, 'agosto': 8, 'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12}
        date = date.replace("\'", '')
        date = date.split(":")

        YYYY = date[0]
        MM = month[str(date[1]).lower()]
        DD = date[2]

        return str(YYYY) + " " + str(MM) + " " + str(DD)
    
    def _translateMonth(self, _date):
        """
        Enter a date '2022:Mayo:8' and return name of month
        """
        _date = self._translateDate(_date)
        month = int(_date.split(" ")[1])
        month = self._getNameOfMonthById(month)
        return month

    

    def _getANameOfWeekDayByDate(self, _date):
        """
        Enter a date YYYY:MM:DD and return a name of day
        """
        _date = self._translateDate(_date)
        _date = _date.split(" ")
        new_date = datetime(int(_date[0]), int(_date[1]), int(_date[2]), 10, 10, 10, 00000)
        day = new_date.weekday()
        day = self._getNameOfDayByID(day)
        return day
    

    def _getNameOfDayByID(self, nroDay):
        days = {0:"Mon", 1:"Tue",2:"Wed",3:"Thu",4:"Fri",5:"Sat",6:"Sun"}
        return days[nroDay]
    
    def _getNumberOfMonthByFullNameMonth(self, nameMonth):
        months = {"Enero": 1,"Febrero": 2,"Marzo": 3,"Abril": 4,"Mayo": 5,"Junio": 6,"Julio": 7,"Agosto": 8,"Septiembre": 9,"Octubre": 10,"Noviembre": 11, "Diciembre": 12}
        return months[nameMonth]
    
    def _getNameOfMonthById(self, nroMonth):
        months = {1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
        return months[nroMonth]
    
    def _getEconomyFilename(self, date):
        """
        Enter a date 2022:Agosto:14 and return Agosto 14.xlsx
        """
        date = date.split(":")

        return date[1] + " " + date[2] + ".xlsx"
