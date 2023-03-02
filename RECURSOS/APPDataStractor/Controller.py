import os


class Controller:
    def __init__(self) -> None:
        self.path = str(os.path.dirname(os.path.abspath(__file__)))
        self._outputDataDiary = {}
        self.consoleText = "Test"
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

    def generateInfo(self, year, type_info):
        t_personal_page_diary = False
        t_personal_dream_diary = False
        t_day_time_distribution = False
        t_personal_feeling_counter = False
        t_economy_t_account = False

        if type_info == "all" or type_info == "diary":
            t_personal_page_diary = True

        if type_info == "all" or type_info == "dreams":
            t_personal_dream_diary = True

        if type_info == "all" or type_info == "time":
            t_day_time_distribution = True

        if type_info == "all" or type_info == "feelings":
            t_personal_feeling_counter = True

        if type_info == "all" or type_info == "economy":
            t_economy_t_account = True

        for i in self.dataSQL.split("\n"):
            if str(i).strip() != "":
                if t_personal_page_diary:
                    if "t_personal_page_diary" in i:
                        data = str(i).split("INSERT INTO t_personal_page_diary (ID, pageName, year, timeStamp, history) VALUES ")[1]
                        data = data.split(", ")
                        
                        title_counter = data[0]
                        title_counter = title_counter.replace('(', '')

                        title = data[1]
                        title = title.replace("\'", '')

                        date = self._translateDate(data[3])
                        
                        date = date.replace(":", ' ')

                        file_name = date + " - " + title+title_counter + ".txt"

                        print(file_name)


    

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

