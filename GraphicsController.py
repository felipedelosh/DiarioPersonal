"""
FelipedelosH
2023

User tikinter Draw Canvas

"""
from tkinter import *

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
