"""
El tiempo a mi gusto
"""
# -⁻- coding: UTF-8 -*-
from datetime import date
import time

class Tiempo:
    def __init__(self):
        # Obj para extraer la información del tiempo
        self.tiempo = date.today()
        # Para Obtener los dias de la semana
        self.diasDeLaSemana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado', 'Domingo']
        self.meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        # Para saber que mes tiene 31 y 31 dias, feb no le voy a contar el bisciesto
        self.duracionMeses = [31,28,31,30,31,30,31,31,30,31,0,31]

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
        Retorna de los meses del 0 -> Enero 11 -> Diciembre
        cuantos dias tienen dicho mes
        """
        return self.duracionMeses[mes]

    def hora(self):
        """
        Esto retorna la hora
        """
        return str(time.ctime())

    def estampaDeTiempo(self):
        """
        Este metodo retorna la firma de mi tiempo:
        Año NumeroMes NumeroDia
        """
        return str(self.año()) + " " + str(self.mes()) + " " + str(self.diaNumero())