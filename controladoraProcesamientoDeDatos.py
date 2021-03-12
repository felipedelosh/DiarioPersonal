"""
Esta parte se encargara de la mineria:

Procesamiento de datos en json

1 - Registro de Logros de mi vida
2 - Cosas que hago




"""
# -⁻- coding: UTF-8 -*-
import json


class ControladoraProcesamientoDeDatos(object):
    def __init__(self, rutaDelProyecto, tiempo):
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
        

        return self.dataSentimientos

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