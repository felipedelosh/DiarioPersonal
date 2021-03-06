# -⁻- coding: UTF-8 -*-
"""
Esta es la controladora del diario

controladoraDeCarpetas
controladoraProcesamientoDatos
tiempo

control de archivos de imagenes de fondo, imagenes de botonos y sonidos.
"""
import os # Libreria para acceder al disco duro y carpetas
from tiempo import *
from controladoraCarpetas import *
from controladoraProcesamientoDeDatos import *
from tkMagicColorByLoko import *
from ArbolDeDeciciones import *
from AudioMixer import *
import random

class Controladora:
    def __init__(self):
        self.rutaDelProyecto = str(os.path.dirname(os.path.abspath(__file__))) # En donde estoy padado
        self.audioMixer = AudioMixer() # Reproductor de sonido
        self.tiempo = Tiempo() # Metodos personalizados de tiempo
        self.controladoraCarpetas = ControladoraCarpetas(self.tiempo, self.rutaDelProyecto) # Para crear y aceder a informacion
        self.controladoraProcesamientoDeDatos = ControladoraProcesamientoDeDatos(self.rutaDelProyecto, self.tiempo) # Aca se hace la mineria de datos
        self.estadoDeLasCarpetas = self.crearCarpetasDelSistema()
        self.coloresParaGraficos = MagicColor() # Color
        self.coloresParaGraficoCircular = [] # Color que le va a corresponder al grafico circular
        self.arbolDeDeDecicion = Arbol() # Es un arbol temporal que guarda las deciciones
        self.arbolDeDecicionListo = False # Me dice si se cargo o creo el arbol


        """
        Se procede a saludar al usuario
        """
        self.saludarAlUsuario()

    def crearCarpetasDelSistema(self):
        """
        Se procede a acceder al disco duro y verificar si las carpetas de trabajo existen
        carpeta de trabajo>Es donde se almacena y se saca la informacion
        """
        try:
            self.controladoraCarpetas.crearYVerificarCarpetas()
            return True
        except:
            return False

    def retornarRutaDelProyecto(self):
        return self.rutaDelProyecto

    def retornarRutaImagenDeFondo(self):
        """
        En la carpeta RECURSOS/img/bg hay fotos.gif
        con id [0-9] se retorna por randon
        """
        id = str(random.randint(0, 11))
        return self.rutaDelProyecto+"\\RECURSOS\\img\\bg\\"+id+".gif"

    def guardarPaginaDiario(self, palabraMagica, texto):
        try:
            """Se genera la ruta del disco duro donde va a estar el archivo"""
            rutaDiario = self.rutaDelProyecto + "\\DATA\\DIARIO\\" + str(self.tiempo.año())
            archivo = rutaDiario+"\\"+self.tiempo.estampaDeTiempo() + " - " + palabraMagica + ".txt"
            if(len(palabraMagica.strip()) > 0):
                texto = texto + "\n\n" + self.tiempo.hora() + "\n\n"
                f = open(archivo, "a", encoding="UTF-8")
                f.write(texto)
                f.close()
                return True
            else:
                return False
                
        except:
            return False

    def cargarpaginaDeDiario(self, palabraMagica):
        try:
            rutaDiario = self.rutaDelProyecto + "\\DATA\\DIARIO\\" + str(self.tiempo.año())
            archivo = rutaDiario+"\\"+self.tiempo.estampaDeTiempo() + " - " + palabraMagica + ".txt"

            f = open(archivo, "r", encoding="UTF-8")
            return f.read()
            
        except:
            return None

    def guardarNota(self, palabraMagica, texto):
        """
        las notas son como un diccionario:

        la nota se va a guardar en 

        """
        try:
            archivo = self.rutaDelProyecto + "\\DATA\\NOTAS\\"+ palabraMagica + ".txt"

            if(len(palabraMagica.strip()) > 0):
                texto = texto + "\n\n" + self.tiempo.hora() + "\n\n"
                f = open(archivo, "a", encoding="UTF-8")
                f.write(texto)
                f.close()
                return True
            else:
                return False
        except:
            return False

    def cargarNotas(self, letra):
        """
        Entra un letra y luego se retornan todas las notas que empiecen por esa letra
        """
        try:
            informacion = {}

            ruta = self.rutaDelProyecto+"\\DATA\\NOTAS"
            lista = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(ruta, ".txt")

            if letra == "#":
                print("Epa")
            else:
                for i in lista:
                    if i[0] == letra:
                        f = open(ruta+"\\"+i, "r", encoding="UTF-8")
                        informacion[i] = f.read()
                        f.close()

            return informacion
        except:
            return {}

    def guardarSentimiento(self, sentimiento):
        try:
            if sentimiento != "":
                rutaDiario = self.rutaDelProyecto + "\\DATA\\SENTIMIENTOS\\" + str(self.tiempo.año())
                archivo = rutaDiario+"\\"+self.tiempo.estampaDeTiempo()+".txt"
                f = open(archivo, 'w', encoding="UTF-8")
                f.write(sentimiento)
                f.close()
                return True
            else:
                return False
        except:
            return False

    def procesarDatosSentimientos(self, año):
        """
        Entra un a+o luego se leen todos los sentimientos de ese a+o y se entregan 
        los datos para ser graficados.
        """
        # Se llaman todos los nombre archivos de ese a+o
        ruta = self.rutaDelProyecto+"\\DATA\\SENTIMIENTOS\\"+año
        listadoNombreArchivoSentimientos = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(ruta, ".txt")
        sentimientos = []
        # Se abren los archivos y se guardan en una lista
        for i in listadoNombreArchivoSentimientos:
            try:
                f = open(ruta+"\\"+i ,'r', encoding="UTF-8")
                sentimientos.append(f.read())
                f.close()
            except:
                pass 

        # Todos esos sentimientos se los mando a la procesadora de datos
        dataSentimientos = self.controladoraProcesamientoDeDatos.procesarDatosSentimientos(self.controladoraCarpetas.cargarEstadosEmocionanes(),sentimientos)
        return dataSentimientos

    def guardarDistribucionTiempoDiario(self, reporte):
        """
        reporte : ['Hora:Actividad', 'Hora:Actividad', ...]
        eso se guarda en DATA/DISTRTIEMP/TDIA/A+o/estampadetiempo.txt
        """
        try:
            txt = ""
            for i in reporte:
                txt = txt + i + "\n"
            ruta = self.rutaDelProyecto+"\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\"+str(self.tiempo.año())+"\\"+str(self.tiempo.estampaDeTiempo())+".txt"
            f = open(ruta, 'w', encoding="UTF-8")
            f.write(txt)
            f.close()
            return True
        except:
            return False

    def procesarInformacionSemanal(self, informacion):
        """
        el metodo de horario semanal 
        {actividad : %, actividad : %, ...}
        """
        dataHorario = self.controladoraProcesamientoDeDatos.procesarDatosSemanalHorario(self.controladoraCarpetas.cargarActividades(), informacion)
        # Se acualizan los colores para el grafico circular
        contador = 0
        for i in dataHorario:
            if dataHorario[i] != 0:
                contador = contador + 1
        
        self.coloresParaGraficoCircular = self.retornarColores(contador)
        return dataHorario


    def retornarColores(self, cantidad):
        """
        deacuerdo a la cantidad retorna un vector [color, color, color, ....]
        """
        colores = []

        for i in range(0, cantidad):
            colores.append(self.coloresParaGraficos.colorAleatoreo())

        return colores
    

    def guardarHorario(self, informacion):
        """
        Se guarda el horario y la copia
        """
        try:
            # Se guarda el original
            ruta = self.rutaDelProyecto+"\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\HORARIO\\horario.txt"
            h = open(ruta, 'w', encoding="UTF-8")
            h.write(informacion)
            h.close()

            # Se guarda la copia
            ruta = self.rutaDelProyecto+"\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\HORARIO\\"+str(self.tiempo.año())+"\\"+str(self.tiempo.estampaDeTiempo())+".txt"
            bk = open(ruta, 'w', encoding="UTF-8")
            bk.write(informacion)
            bk.close()
            
            return True
        except:
            return False

    def cargarHorario(self):
        """
        Se abre DATA/DDT/HORARIO/horario.txt
        """
        try:
            informacion = ""
            ruta = self.rutaDelProyecto+"\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\HORARIO\\horario.txt"

            h = open(ruta, 'r', encoding="UTF-8")
            informacion = h.read()
            return informacion

        except:
            return None

    def cargarDatosFechasInformacionEconomica(self):
        valuesComboBox = []
        # Se cargan los a+os disponibles
        añosDisponbibles = self.controladoraCarpetas.listarAñosDeEconomia()
        # Se retornan los meses disponibles.
        mesesDisponibles = self.tiempo.meses[0:self.tiempo.mes()]
        valuesComboBox = valuesComboBox + añosDisponbibles + mesesDisponibles

        return valuesComboBox


    def crearCarpetaArbolDeDeciciones(self, txt):
        # Se reinicia el arbol
        self.arbolDeDeDecicion = Arbol()
        self.arbolDeDeDecicion.nickName = txt
        return self.controladoraCarpetas.crearCarpetaEnDeciociones(txt)

    def agregarNodoAlArbolDeDecion(self, info):
        # la info es un vector[IDpadre, id, titulo, info]
        """
        1 -> los ID son de tipo numerico
        2 -> agregar al arbol
        """

        try:
            idPadre = int(info[0])
            idNodo = int(info[1])
            d = Decicion(idPadre, idNodo, info[2], info[3])
            self.arbolDeDeDecicion.addDato(d)
            
            return self.guardarNodoEnHDD(d)
        except:
            return False

    def guardarNodoEnHDD(self, decicion):
        """
        Una Decion[idPadre, Id, Titulo, Info]
        va a ser guardada en su carpeta correspondiente (Arbol.nickName)
        como id.txt
        con formato
        <IDPadre>ID</IDpadre>
        <ID>ID</ID>
        <HIJOS>ID,ID,ID</HIJOS>
        <TITULO>TituloDeMierda</TITULO>
        <EVENTO>EventoDeMierda</EVENTO>
        """
        idPadre = "<IDPadre>"+str(decicion.idPadre)+"</IDpadre>\n"
        idNodo = "<ID>" + str(decicion.id) + "</ID>\n"
        hijos = "<HIJOS>" + "</HIJOS>\n"
        titulo = "<TITULO>" +str(decicion.titulo)+ "</TITULO>\n"
        evento = "<EVENTO>\n"+str(decicion.quePaso)+"</EVENTO>"

        data = idPadre + idNodo + hijos + titulo + evento

        # Se guarda en HDD 
        try:
            ruta = self.rutaDelProyecto + "\\DATA\\DECICIONES\\" + str(self.arbolDeDeDecicion.nickName)  + "\\" + str(decicion.id) + ".txt"
            f = open(ruta, "w")
            f.write(data)
            f.close()
            return True
        except:
            return False
        

    def arbolDeDecicionEstaListo(self):
        """
        Si el arbol esta listo para trabajar : True or false
        """
        return self.arbolDeDecicionListo


    def retornarInformacionEconomica(self, tipo):
        """
        Cuando se solicite informacion sobre un año, 
        o un mes en especifico se retornara los conceptos de 
        ingresos o egresos de ese periodo.
        """
        tipoDeVista = None
        
        try: # Si es un año
            tipoDeVista = int(tipo)
            # Se retorna toda la informacion del año

            ruta = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\" + str(tipo) # Obtengo la ruta
            arch = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(ruta, ".xlsx") # Obtengo el nombre de todos los archivos


            data = [] # Aqui se empaqueta toda la informacion para procesarla


            for i in arch:
                rutaTemp = ruta + "\\" + i
                
                f = open(rutaTemp, encoding="UTF-8")
                data.append(f.read())
                f.close()

            # La informacion va a ser procesada
            return self.controladoraProcesamientoDeDatos.procesarReporteEconomigo(data)


        except: # Si es un mes
            
            # Se recupera la informacion del año actual
            ruta = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\" + str(self.tiempo.año()) # Obtengo la ruta
            arch = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(ruta, ".xlsx") # Obtengo el nombre de todos los archivos
            data = [] # Aqui se empaqueta toda la informacion para procesarla
            # Solo empaquetos los archivos que contengan informacion de ese mes
            for i in arch:
                if tipo in i:
                    rutaTemp = ruta + "\\" + i
                
                    f = open(rutaTemp, encoding="UTF-8")
                    data.append(f.read())
                    f.close()

            # La informacion va a ser procesada
            return self.controladoraProcesamientoDeDatos.procesarReporteEconomigo(data)

    def guardarEstadoCajaMayor(self, monto):
        """
        Si el monto es un numero se procede a guardar
        Se guarda una copia en el final del txt \\DATA\\ECONOMIA\\CAJA\\cajaMayor(año).txt
        """
        ruta = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\CAJA\\cajaMayor.txt"
        try:
            txtM = int(monto)
            f = open(ruta, "w", encoding="UTF-8")
            f.write(monto)
            f.close()

            try:
                rutaTemp = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\CAJA\\cajaMayor" + str(self.tiempo.año()) + ".txt"
                temp = open(rutaTemp, 'r', encoding="UTF-8")
                k = temp.read() + monto + "\n"
                temp.close()
                temp = open(rutaTemp, 'w', encoding="UTF-8")
                temp.write(k)
                temp.close()

            except:
                rutaTemp = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\CAJA\\cajaMayor" + str(self.tiempo.año()) + ".txt"
                temp = open(rutaTemp, "w", encoding="UTF-8")
                temp.write(monto + "\n")
                temp.close()

            return True
        except:
            return False


    def cargarEstadoCajaMayor(self):
        """
        Se carga el monto contenido en DATA/ECONOMIA/CAJA/cajaMayor.txt

        >Si el txt no existe se crea y se retorna $0
        """
        ruta = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\CAJA\\cajaMayor.txt"
        try:
            f = open(ruta, encoding="UTF-8")
            return f.read()
        except:
            f = open(ruta, "w", encoding="UTF-8")
            f.write("0")
            f.close()
            return 0

    def cargarRecordEstadoCajaMayor(self):
        """
        se cargan los montos contenidos en \\DATA\\ECONOMIA\\CAJA\\cajaMayor(año).txt
        """
        try:
            ruta = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\CAJA\\cajaMayor" + str(self.tiempo.año()) + ".txt"
            f = open(ruta, 'r', encoding="UTF-8")
            valores = []

            for i in f.readlines():
                try:
                    valores.append(int(i))
                except:
                    pass

            return valores
        except:
            return []


    def cargarEstadoCajaMenor(self):
        """
        Se carga el monto contenido en DATA/ECONOMIA/CAJA/cajaMenor.txt

        >Si el txt no existe se crea y se retorna $0
        """
        ruta = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\CAJA\\cajaMenor.txt"
        try:
            f = open(ruta, encoding="UTF-8")
            return f.read()
        except:
            f = open(ruta, "w", encoding="UTF-8")
            f.write("0")
            f.close()
            return 0

    def cargarRecordEstadoCajaMenor(self):
        """
        se cargan los montos contenidos en \\DATA\\ECONOMIA\\CAJA\\cajaMenor(año).txt
        """
        try:
            ruta = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\CAJA\\cajaMenor" + str(self.tiempo.año()) + ".txt"
            f = open(ruta, 'r', encoding="UTF-8")
            valores = []

            for i in f.readlines():
                try:
                    valores.append(int(i))
                except:
                    pass

            return valores
        except:
            return []

    def guardarEstadoCajaMenor(self, monto):
        """
        Si el monto es un numero se procede a guardar
        Se procede a guardar una copia en el final del txt \\DATA\\ECONOMIA\\CAJA\\cajaMenor(año).txt
        """
        ruta = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\CAJA\\cajaMenor.txt"
        try:
            txtM = int(monto)
            f = open(ruta, "w", encoding="UTF-8")
            f.write(monto)
            f.close()

            try:
                rutaTemp = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\CAJA\\cajaMenor" + str(self.tiempo.año()) + ".txt"
                temp = open(rutaTemp, 'r', encoding="UTF-8")
                k = temp.read() + monto + "\n"
                temp.close()
                temp = open(rutaTemp, 'w', encoding="UTF-8")
                temp.write(k)
                temp.close()

            except:
                rutaTemp = self.rutaDelProyecto + "\\DATA\\ECONOMIA\\CAJA\\cajaMenor" + str(self.tiempo.año()) + ".txt"
                temp = open(rutaTemp, "w", encoding="UTF-8")
                temp.write(monto + "\n")
                temp.close()

            return True
        except:
            return False

    def queAñoEs(self):
        """
        Retorna el año en que nos encontramos
        """
        return self.tiempo.año()

    def queMesEs(self):
        """
        Retorna el mes actual
        """
        return self.tiempo.mes()

    def queNumeroDeDiaEs(self):
        """
        Retorna el # dia en que estamos
        """
        return self.tiempo.diaNumero()

    def guardarInformacionPerfil(self, informacion):
        """
        Se guarda la informacion en los txt correspondientes
        """
        try:
            ruta = self.rutaDelProyecto + "\\DATA\\PERFIL\\"
            
            f = open(ruta+"nombreApellido.txt", "w", encoding="UTF-8")
            f.write(informacion[0])
            f.close()

            f = open(ruta+"fechaNacimiento.txt", "w", encoding="UTF-8")
            f.write(informacion[1])
            f.close()

            f = open(ruta+"sexo.txt", "w", encoding="UTF-8")
            f.write(informacion[2])
            f.close()

            f = open(ruta+"edad.txt", "w", encoding="UTF-8")
            f.write(informacion[3])
            f.close()

            f = open(ruta+"username.txt", "w", encoding="UTF-8")
            f.write(informacion[4])
            f.close()

            f = open(ruta+"biografia.txt", "w", encoding="UTF-8")
            f.write(informacion[5])
            f.close()

            return True
        except:
            return False

    def cargarInformacionDelPerfil(self):
        try:
            informacion = []

            ruta = self.rutaDelProyecto + "\\DATA\\PERFIL\\"
            try:
                f = open(ruta+"nombreApellido.txt", "r", encoding="UTF-8")
                informacion.append(f.read())
                f.close()
            except:
                pass


            try:
                f = open(ruta+"fechaNacimiento.txt", "r", encoding="UTF-8")
                informacion.append(f.read())
                f.close()
            except:
                pass

            try:
                f = open(ruta+"sexo.txt", "r", encoding="UTF-8")
                informacion.append(f.read())
                f.close()
            except:
                pass

            try:
                f = open(ruta+"edad.txt", "r", encoding="UTF-8")
                informacion.append(f.read())
                f.close()
            except:
                pass
            
            try:
                f = open(ruta+"username.txt", "r", encoding="UTF-8")
                informacion.append(f.read())
                f.close()
            except:
                pass

            try:
                f = open(ruta+"biografia.txt", "r", encoding="UTF-8")
                informacion.append(f.read())
                f.close()
            except:
                pass


            return informacion
        except:
            return []

    def cargarAñosDeRegistroActividades(self):
        """
        Se cargan los años registrados en "\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\"
        """
        return self.controladoraCarpetas.listarAñosRegistradosDistribucionDeTiempo()

    def cargarActividades(self):
        """
        Se carga toda la informacion contenida RECURSOS/actividades.txt
        """
        try:
            ruta = self.rutaDelProyecto + "\\RECURSOS\\actividades.txt"
            f = open(ruta, "r", encoding="UTF-8")
            return f.read()
        except:
            return "dormir\nalimentacion\nNada"

    def cargarPorcentajesDeActividades(self, año):
        """
        Se carga el % de gasto de cada actividad en el año correspondiente en un dic
        {dormir:0.2, comer:0.1, trabajar:0.5}
        """
        try:
            ruta = self.rutaDelProyecto + "\\DATA\\DISTRIBUCIONTIEMPO\\TIEMPODIARIO\\" + str(año)
            data = self.controladoraCarpetas.listarTodosLosArchivosdeCarpeta(ruta, "txt")


            informacion = {}
            totalHoras = 0  

            # Se lee cada archivo de horario
            for i in data:
                try:
                    f = open(ruta+"\\"+i, "r", encoding="UTF-8")
                    txt = f.read().split("\n")
                    
                    # Se analiza actividad hora por hora
                    for j in txt:
                        if j.strip() != "":
                            key = j.split(":")[1]
                            if key in informacion:
                                temp = informacion[key] + 1
                                informacion[key] = temp
                            else:
                                informacion[key] = 1
                            totalHoras = totalHoras + 1

                except:
                    pass

            # Se pone la informacion en terminos de porcentaje
            for i in informacion:
                informacion[i] = informacion[i]/totalHoras    

            return informacion
        except:
            return {"No data":0.5, "No Data":0.5}


    """
    AUDIO
    AUDIO
    AUDIO
    """
    def saludarAlUsuario(self):
        """
        Dependiendo de la hora da un saludo
        """
        hora = str(self.tiempo.hora()).split(":")[0]
        hora = hora.split(" ")
        hora = int(hora[len(hora)-1])

        if hora >= 20:
            self.audioMixer.line = self.rutaDelProyecto + "\\recursos\\audio\\buenas noches"
            self.audioMixer.playSound()
        else:
            if hora > 12:
                self.audioMixer.line = self.rutaDelProyecto + "\\recursos\\audio\\buenas tardes"
                self.audioMixer.playSound()
            else:
                self.audioMixer.line = self.rutaDelProyecto + "\\recursos\\audio\\buenos dias"
                self.audioMixer.playSound()

    def decir(self, palabra):
        """
        Sera dicha una palabra
        """
        self.audioMixer.line = self.rutaDelProyecto + "\\recursos\\audio\\" + palabra
        self.audioMixer.playSound()


    """AYUDA"""
    """AYUDA"""
    """AYUDA"""
    def retornarMensajePrincipalAyuda(self):
        try:
            ruta = self.rutaDelProyecto + "\\RECURSOS\\manual\\MensajePrincipal.txt"
            f = open(ruta, 'r', encoding="UTF-8")
            return f.read()
        except:
            return "No se pudo abrir ni mierda"

    def retornarListadoDePosibilidades(self):
        try:
            ruta = self.rutaDelProyecto + "\\RECURSOS\\manual\\ListadoDePosibilidades.txt"
            f = open(ruta, 'r', encoding="UTF-8")
            return f.read()
        except:
            return "Error acediendo a HDD"


            