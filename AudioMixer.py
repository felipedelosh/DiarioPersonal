"""
FelipedelosH

AudioMixer v1.0

Aqui se necesita la carpeta RECURSOS/audio/ 
line es el que reproduce sonido  ojo... no le puedes poner .wav

Por ejemplo: si tu le dices



"""
# -⁻- coding: UTF-8 -*-
import winsound
import sys

class AudioMixer:
    def __init__(self):
        self.line = "" # Aqui se pone el sonido ejemplo : DirPath+recuros/audio/hola mundo

    def playSound(self):
        winsound.PlaySound(self.line+".wav", winsound.SND_FILENAME)