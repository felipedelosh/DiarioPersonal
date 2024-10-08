"""
El tiempo a mi gusto
"""
# -⁻- coding: UTF-8 -*-
import datetime
from datetime import date
from os import path
from random import randint
import math
import time

class Tiempo:
    def __init__(self):
        # Obj para extraer la información del tiempo
        self.tiempo = date.today()
        # Para Obtener los dias de la semana
        self.diasDeLaSemana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
        self.meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        # Para saber que mes tiene 31 y 31 dias, feb no le voy a contar el bisciesto
        self.duracionMeses = [31,28,31,30,31,30,31,31,30,31,30,31]

    def getOnlyHour(self):
        """
        Get hour 
        """
        hour = str(time.ctime()).split(" ")
        hour = hour[-2]

        return hour

    def año(self):
        """Retorna en que a+o estamios"""
        return self.tiempo.year

    def mes(self):
        """Retorna en que mes estamos"""
        return self.tiempo.month

    def diaNumero(self):
        """Retorna en que dia estamos el nro de dia"""
        return self.tiempo.day

    def diaDeLaSemana(self):
        """Retorna que dia es lunes o martes..."""
        return self.diasDeLaSemana[self.tiempo.weekday()]

    def nombreMes(self, mes):
        """
        Retorna el nombre del mes 0-> enero 1->febrero
        """
        return self.meses[mes]

    def diasDeMes(self, mes):
        """
        Retorna de los meses del
        mes = integer 
        0 -> Enero 
        11 -> Diciembre
        cuantos dias tienen dicho mes
        """
        if mes == 1:
            return self._countDaysFEB()

        return self.duracionMeses[mes]
    
    def _countDaysFEB(self):
        YYYY = self.tiempo.year
        if YYYY % 4 == 0 and (YYYY % 100 != 0 or YYYY % 400 == 0):
            return 29
        else:
            return 28

    def hora(self):
        """
        Esto retorna la hora string MM + NrDay + HH:MM + YYYY
        """
        hour = str(time.ctime())
        return hour


    def incrementarFechaXDias(self, año, mes, dia, incremento):
        """Retorna la fecha despues del incremento de dias.
        Nota: no es tan exacto... aveces falla por dos o tres dias
        """

        nuevoAño = año
        nuevoMes = mes
        nuevoDia = dia

        # Si no hay que incrementar dias
        if(incremento == 0):
            return str(nuevoAño) +":"+str(self.meses[int(nuevoMes)-1])+":"+str(nuevoDia)

        # calcular si es más de un año
        if(incremento>=365):
            if(incremento == 365):
                return str(int(nuevoAño)+1) +":"+str(self.meses[int(nuevoMes)-1])+":"+str(nuevoDia)
            else:
                #Recalcular año y volver a llamar
                aumentoAños = math.floor(incremento / 365)
                nuevoIncremento = incremento%365
                return self.incrementarFechaXDias(año+aumentoAños, mes, dia, nuevoIncremento)


        # Calcular cuatos dias falta para que termine el año
        diasFaltantes = self.cuantosDiasFaltanParaTerminarElAñoFechaX(int(mes), int(dia))
        if diasFaltantes < incremento:
            # Poner la fecha en 1 ro de enero del siguiente año y recalcular
            return self.incrementarFechaXDias(año+1, 1, 1, incremento-diasFaltantes)

        
        # Comienza a incrementar los dias
        contador = 1
        temporalDiasMesActual = nuevoDia
        while incremento > 0:

            if contador + temporalDiasMesActual > self.duracionMeses[int(nuevoMes)-1]:
                temporalDiasMesActual = 0
                nuevoDia = 1
                contador = 1
                nuevoMes = int(nuevoMes) + 1

            nuevoDia = int(nuevoDia) + 1

            contador = contador + 1
            incremento = incremento - 1
        

        return str(nuevoAño)+":"+str(nuevoMes)+":"+str(nuevoDia)

    def cuantosDiasFaltanParaTerminarElAño(self):
        mesActual = self.mes()
        diaActual = self.diaNumero()

        cuantosDiashanPasado = 0
        #Cuantos Dias han pasado
        for i in range(0, mesActual-1):
            cuantosDiashanPasado = cuantosDiashanPasado + self.duracionMeses[i]

        #Le sumo los dias actuales
        cuantosDiashanPasado = cuantosDiashanPasado + diaActual
           
        return 365 - cuantosDiashanPasado

    def cuantosDiasFaltanParaTerminarElAñoFechaX(self, mes, dia):
        """
        enero = 1
        """
        mesActual = mes
        diaActual = dia

        cuantosDiashanPasado = 0
        #Cuantos Dias han pasado
        for i in range(0, mesActual-1):
            cuantosDiashanPasado = cuantosDiashanPasado + self.duracionMeses[i]

        #Le sumo los dias actuales
        cuantosDiashanPasado = cuantosDiashanPasado + diaActual
           
        return 365 - cuantosDiashanPasado



    def estampaDeTiempo(self):
        """
        Este metodo retorna la firma de mi tiempo:
        Año NumeroMes NumeroDia
        """
        return str(self.año()) + " " + str(self.mes()) + " " + str(self.diaNumero())


    def getMonthNumberByMonthName(self, monthName):
        """
        Enter a name of month
        and return the number of month...
        Example:
        Enero RTRN 1
        Diciembre RTRN 12
        """
        counter = 1
        for i in self.meses:
            if i == monthName:
                return counter
            counter = counter + 1
        
        return -1
    

    def getNameOfDayByDate(self, d):
        """
        Enter a date [YYYY, MM, DD] and return a name of day
        """
        day = ""

        try:
            _d = date(d[0], d[1], d[2])
            _d = _d.weekday()
            day = self.diasDeLaSemana[_d]
        except:
            pass

        return day
    

    def getNextDay(self, YYYY, MM, DD):
        """
        ENTER A DATE: int(YYYY), int(MM), int(DD)
        return the next day [int(YYYY), int(MM), int(DD)]
        NOTE: MM = [1-12]
        """
        _d = [0,0,0]

        try:
            YYYY = int(YYYY)
            MM = int(MM)
            DD = int(DD)

            if DD < self.duracionMeses[MM-1]:
                _d = [YYYY, MM, DD + 1]
            else:
                if DD == self.duracionMeses[MM-1] and MM != 12:
                    _d = [YYYY, MM+1, 1]
                else:
                    _d = [YYYY+1, 1, 1]
        except:
            pass

        return _d


    def getNameOfDayByDateYYYYMMDD(self, strTime):
        """
        Enter a date in format YYYY-MM-DD
        and return a name of these day.
        """
        _date = datetime.datetime.strptime(strTime, "%Y-%m-%d")
        _nr_day = _date.weekday()

        return self.diasDeLaSemana[_nr_day]
