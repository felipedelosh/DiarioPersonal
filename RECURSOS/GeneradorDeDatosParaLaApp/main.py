"""
Esto es el genrador de datos para la APP android del diario.

Se procede a actuar de 2 modos: con datos ramdom
                                con los datos de la carpeta Datos

y procede a generar  SQL.txt

100 registros random
todos los registros reales

option 1 : generate ramdon data of time inversion
option 2 : generate ramdon data of time inversion


"""
from tkinter import * # para graficar
import os # Libreria para acceder al disco duro y carpetas
from tiempo import *  # Para el manejo de fechas
import random # Para datos aleatoreos


class Software:
    def __init__(self) -> None:
        self.rutaDelProyecto = str(os.path.dirname(os.path.abspath(__file__))) # En donde estoy padado
        self.tiempo = Tiempo()
        self.pantalla = Tk()
        self.tela = Canvas(self.pantalla, height=480, width=720, bg="snow")
        self.lblPrograma = Label(self.tela, text="Generador de datos para la base de datos de la APP")
        self.lblGenerarDatosDeInversionTiempo = Label(self.tela, text="Generar Datos inversión de tiempo")
        self.btnGenerateDatosInversionTiempoRandom = Button(self.tela, text="Random", command= lambda : self.generateRandomData(1))
        self.btnGenerateDatosInversionTiempoReal = Button(self.tela, text="Real")


        #Mostrar vista
        self.renderizar()


    def renderizar(self):
        self.pantalla.title("LifeRegisterDiary Data generator v1.0")
        self.pantalla.geometry("720x480")

        self.tela.place(x=0, y=0)
        self.lblPrograma.place(x=20, y=20)
        self.lblGenerarDatosDeInversionTiempo.place(x=20, y=80)
        self.btnGenerateDatosInversionTiempoRandom.place(x=90, y=110)
        self.btnGenerateDatosInversionTiempoReal.place(x=100, y=140)


        self.pantalla.mainloop()


    def generateRandomData(self, option):
        if option == 1:
            try:
                path = self.rutaDelProyecto+"\\Datos\\actividades.txt"
                estadosEmocionalesFile = open(path, "r", encoding="UTF-8")
                txtEstadosEmociolaes = estadosEmocionalesFile.read().split("\n")
                timeStampAño = str(self.tiempo.año())
                timeStampMes = str(self.tiempo.mes())
                timeStampDia = str(self.tiempo.diaNumero())
                SQL = ""
                #GenerateSqlOutPut
                for i in range(0, 100):
                    SQLHead = "INSERT INTO t_day_time_distribution (timeStamp, hour, activity) VALUES ("
                    # Generate data all day
                    for h in range(0, 24):
                        try:
                            newTimeStamp = self.tiempo.incrementarFechaXDias(timeStampAño, timeStampMes, timeStampDia, i)
                        except:
                            print("Error en", i, timeStampAño, timeStampMes, timeStampDia)
                        activity = txtEstadosEmociolaes[random.randint(0, len(txtEstadosEmociolaes)-1)]
                        newSQL =  SQLHead + "\'"+newTimeStamp+"\', "+"\'"+self.getHourFormat(h)+"\', "+"\'"+activity+"\');\n" 
                        SQL = SQL + newSQL

                self.saveInTXT(SQL)
            except:
                self.poppup("Error no se puede generar los datos")
            

    def generateRealData(self):
        pass


    def poppup(self, text):
        t = Toplevel()
        t.geometry("300x300")
        lbl = Label(t, text=text)
        lbl.place(x=10, y=10)


    def getHourFormat(self, h):
        ampm = "am"
        hour = 0

        # Put am pm
        if(h>6 and h<19):
            ampm = "pm"

        # put hour
        if(h<=6):
            hour = 6 + h
        elif (h>6 and h<19):
            hour = h - 6
        else:
            hour = h - 18

        return str(hour) + ":" + ampm


    def saveInTXT(self, data):
        try:
            path = self.rutaDelProyecto + "\\SQL.txt" 
            f = open(path, "w")
            f.write(data)
            f.close()
        except:
            pass
        



s = Software()
