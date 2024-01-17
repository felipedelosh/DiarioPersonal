"""
a los 31 dias de oct de 2020

Procedo a crear la controladora de deciciones:
Contiene 
"""

class Decicion(object):
    def __init__(self, id, idpadre, hijos, titulo, quePaso):
        self.id = id
        self.idpadre = idpadre
        self.hijos = hijos
        self.titulo = titulo
        self.quePaso = quePaso

    def formatoParaGuardar(self):
        """
        Se retorna en el formato correspondiente para ser guardado
        ID,PADRE\n
        HIJOS\n
        titulo 
        QuePaso => Es una descripcion Breve
        """
        txt=""
        txt=str(self.id)+","+str(self.idpadre)+"\n"
        txt=txt+str(self.hijos)+"\n"
        txt=txt+self.titulo+"\n"+self.quePaso

        return txt

