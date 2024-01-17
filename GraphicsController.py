"""
FelipedelosH
2023

User tikinter Draw Canvas

"""
from tkinter import *
import random

class GraphicsController:
    

    def showFeelingsYearGraphic(self, data):
        """
        Enter a processor of DATA\SENTIMIENTOS
        {"feeling":frecuency, "feeling":frecuency, "feeling":frecuency ...}
        and draw
        """
        pantalla = Toplevel()
        pantalla.title("Histograma sentimientos ")
        pantalla.geometry("800x600")
        tela = Canvas(pantalla, width=800, height=600, bg="snow")
        tela.place(x=0, y=0)
        # Screem values
        _x = int(tela['width'])
        _y = int(tela['height'])
        _maxGrapichFrecuencyValueX = _x - _x*0.35 # This is a width of 100% line 0.2 + 0.15
        _maxGrapichFrecuencyValueY = _y - _y*0.1  # This is a total heigth
        _totalFeelingsSpace = _maxGrapichFrecuencyValueY / len(data)
        _totalFeelingsSpace = _totalFeelingsSpace * 0.8
        _xKons = _x*0.2 # The bit scale

        # Search a max value in data
        _maxYValue = 0
        for i in data:
            if _maxYValue < data[i]:
                _maxYValue = data[i]

        # Paint Axis XY
        tela.create_line(_xKons, _y*0.1, _xKons + _maxGrapichFrecuencyValueX, _y*0.1, arrow=LAST) # X


        # Paint scale lines:
        _scaleX = (_maxGrapichFrecuencyValueX) / 10
        for i in range(1, 10):
            tela.create_line((_xKons+(_scaleX*i)),((_y*0.1)-5),(_xKons+(_scaleX*i)),((_y*0.1)+5))
        # Paint medium and max values
        tela.create_text(_xKons+(_scaleX*5), _y*0.075, text=str(round((_maxYValue/2), 2)))
        tela.create_text(_xKons+(_scaleX*10), _y*0.075, text=str(_maxYValue))


        tela.create_line(_xKons, _y*0.1, _xKons, _maxGrapichFrecuencyValueY, arrow=LAST) # Y

        # Paint Labels
        counter = 1
        for i in data:
            # Paint feeling Label
            yPos = (_totalFeelingsSpace*counter)+_y*0.1
            tela.create_text(_x * 0.07, yPos, text=i)

            _percentValueFrecuency = data[i]/_maxYValue
            # Paint frecuency 
            x0 = _xKons
            y0 = yPos - 5
            x1 = _xKons + (_maxGrapichFrecuencyValueX * _percentValueFrecuency)
            y1 = yPos + 5
            tela.create_rectangle(x0, y0, x1, y1, fill="blue")

            counter = counter + 1


    def graphEconomyBoxStates(self, canvas, dataLitleBox, dataBigBox):
        """
        Enter a tkinter canvas and [#, #, #]
        """
        h = int(canvas['height'])
        w = int(canvas['width'])
        data = dataLitleBox

        if len(data) > 0:
            # get the top value of data
            maxY = 0
            for i in data:
                if i > maxY:
                    maxY = i

            canvas.create_text(w*0.04, h*0.95, fill="blue", text="$0.0", tags="estadocajas")
            canvas.create_text(w*0.04, h*0.48, fill="blue", text="$"+str(maxY/2), tags="estadocajas")
            canvas.create_text(w*0.04, h*0.05, fill="blue", text="$"+str(maxY), tags="estadocajas")


            _dxPivot = w / len(data)
            _ink = w*0.04
            # Graph the points x,y 
            for i in range(0, len(data)-1):
                x0 = _dxPivot*i + _ink
                y0 = h * (1-(data[i]/maxY)) 
                x1 = _dxPivot*(i+1) + _ink
                y1 = h * (1-(data[i+1]/maxY))
                canvas.create_line(x0, y0, x1, y1, fill="blue", tags="estadocajas")

        
        data = dataBigBox
        if len(data) > 0:  
            # get the top value of data
            maxY = 0
            for i in data:
                if i > maxY:
                    maxY = i


            # Se grafican 3 labes cero, montoMedio, MaximoMonto
            canvas.create_text(w*0.9, h*0.95, fill="green", text="$0.0", tags="estadocajas")
            canvas.create_text(w*0.9, h*0.48, fill="green", text="$"+str(maxY/2), tags="estadocajas")
            canvas.create_text(w*0.9, h*0.05, fill="green", text="$"+str(maxY), tags="estadocajas")



            # Se procede a graficar los puntos
            _dxPivot = w / len(data)
            _ink = w*0.04
            for i in range(0, len(data)-1):
                x0 = _dxPivot*i + _ink
                y0 = h * (1-(data[i]/maxY))
                x1 = _dxPivot*(i+1) + _ink
                y1 = h * (1-(data[i+1]/maxY))
                canvas.create_line(x0, y0, x1, y1, fill="green", tags="estadocajas")
    

    def getBackgroundImage(self, projectPath):
        """
        Read Folder RECURSOS/img/bg return photoimage
        """
        _simbolikSep = self.getSimbolikPathSeparator(projectPath)

        id = str(random.randint(0, 38))
        _pathIMG = f"{projectPath}{_simbolikSep}RECURSOS{_simbolikSep}img{_simbolikSep}bg{_simbolikSep}{id}.gif"

        return PhotoImage(file=_pathIMG)
    

    def returnIMGRnBtnRousourceX(self, projectPath, resource):
        """
        Read Folder RECURSOS/img/bnts return photoimage
        """
        _simbolikSep = self.getSimbolikPathSeparator(projectPath)

        id = str(random.randint(0, 9))
        _pathIMG = f"{projectPath}{_simbolikSep}RECURSOS{_simbolikSep}img{_simbolikSep}btns{_simbolikSep}{resource}{_simbolikSep}{resource}"+id+".gif"

        return PhotoImage(file=_pathIMG)
    

    def getIMGPeople(self, projectPath, qty_people):
        """
        Get IMG of folder RECURSOS/img/btns/people
        """
        _simbolikSep = self.getSimbolikPathSeparator(projectPath)

        if not 0 <= qty_people < 10:
            qty_people = 0
            
        _pathIMG = f"{projectPath}{_simbolikSep}RECURSOS{_simbolikSep}img{_simbolikSep}btns{_simbolikSep}people{_simbolikSep}people{qty_people}.gif"

        return PhotoImage(file=_pathIMG)
    

    def getSimbolikPathSeparator(self, projectPath):
        """
        In Some SO usages / or \ to separates folder PATH
        """
        _simbolikSep = "\\"

        if _simbolikSep not in projectPath:
            _simbolikSep = "/"

        
        return _simbolikSep
    