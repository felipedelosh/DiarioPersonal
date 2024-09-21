"""
FelipedelosH
2023

User tikinter Draw Canvas

"""
from tkinter import *
from tiempo import *
import random

class GraphicsController:
    
    def showHistogramGraphic(self, data, title):
        """
        {"data":frecuency, "data":frecuency, "data":frecuency ...}
        and draw
        """
        if len(data) > 0:
            pantalla = Toplevel()
            pantalla.title(title)
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


    def drawTimeLife(self, data):
        """
        data = {
        YYYY >> All years registred
        METADATA >> {
            maxIN:0
            maxOUT:0
        }
        DATA >> {
            "ARGS":to paint
        }
        }
        """
        if data["YYYY"] and data["DATA"] and data["METADATA"]:
            _timeLIB = Tiempo()
            _h = 480
            _w = 800
            t = Toplevel()
            t.title("TIME LIFE")
            t.geometry(f"{_w}x{_h}")
            canvas = Canvas(t, height=_h, width=_w)
            canvas.place(x=0, y=0)

            _x0 = _w * 0.1
            _totalAixisXInYYYY = _w * 0.8 # MAX X Aixis
            _y0 = _h * 0.1
            _totalAixisY = _h * 0.8 # MAX Y Aixis 

            print("Total YYYY:",len(data["YYYY"]))
            print(data["YYYY"])
            _deltaX = _totalAixisXInYYYY / len(data["YYYY"]) # Space of year in aixis x
            _deltaXDAY = _deltaX / 365 # Space of one day in aixis x
            _delta24HAixisY = _totalAixisY / 24

            _totalDays = 365 * len(data["YYYY"])

            canvas.create_line(_x0, _y0, _x0, _y0+_totalAixisY) # Y Aixis

            if data["METADATA"]["maxin"] > 0:
                canvas.create_text(_x0*0.5, _y0*1.05, fill="green",text=f"${round(data['METADATA']['maxin'],2)}")
                canvas.create_text(_x0*0.5, (_y0+_totalAixisY)/2, fill="green",text=f"${round(data['METADATA']['maxin']/2,2)}")
                canvas.create_text(_x0*0.5, (_y0+_totalAixisY)*0.8, fill="green",text=f"${round(data['METADATA']['maxin']*0.4,2)}")

            canvas.create_line(_x0, _y0+_totalAixisY, _x0+_totalAixisXInYYYY, _y0+_totalAixisY) # X Aixis

            # Create separator lines in X Aixis
            counter = 1
            for i in data["YYYY"]:
                x0 = _x0 + (_deltaX * counter)
                y0 = (_y0+_totalAixisY) * 0.99
                x1 = x0
                y1 = (_y0+_totalAixisY) * 1.01
                x2 = x0 - (_deltaX/2)
                canvas.create_line(x0, y0, x1, y1)
                canvas.create_text(x2, y0*1.05, text=f"{i}")
                counter = counter + 1

            # Create a Hours Aixis Y Separator
            counter = 0
            for _ in range(0, 24):
                x0 = _x0
                y0 = (_totalAixisY + _y0) - (_delta24HAixisY*counter)
                x1 = _x0 * 1.15
                y1 = y0
                canvas.create_line(x0, y0, x1, y1)
                canvas.create_text(x0*1.1, y0-8, text=f"{counter}")
                counter = counter + 1

            # Paint data
            _datePivotYYYY = int(data["YYYY"][0])
            _datePivotMM = 1
            _datePivotDD = 1 
            _dayCounter = 0
            for i in range(0, _totalDays):
                _keyDate = f"{_datePivotYYYY}-{_datePivotMM}-{_datePivotDD}" # Update some lines below
                # PAINT MONEY IN
                try:
                    if _keyDate in data["DATA"].keys():
                        if "in" in data["DATA"][_keyDate].keys():
                            _pivotY = data["DATA"][_keyDate]["in"]/data["METADATA"]["maxin"]

                            if str(_datePivotYYYY).strip() == "2020":
                                d = _timeLIB.getNextDay(_datePivotYYYY, _datePivotMM, _datePivotDD)
                                _datePivotYYYY = d[0]
                                _datePivotMM = d[1]
                                _datePivotDD = d[2]
                                print("epaaa")

                            if _pivotY != 0 and _pivotY > 0.05:
                                print(f"YYYY:{_datePivotYYYY}", _pivotY)
                                x0 = _deltaXDAY * _dayCounter - 3
                                y0 = (_h * (_pivotY))
                                y0 = (_totalAixisY + _y0) - y0
                                x1 = _deltaXDAY * (_dayCounter + 1) + 3
                                y1 = y0 * 0.98
                                print(x0,y0,x1,y1)
                                canvas.create_oval(x0, y0, x1, y1, fill="green")


                        


                except Exception as e:
                    pass
                
                # Paint Sleep VS LIfe
                try:
                    if _keyDate in data["DATA"].keys():
                        #_percentTimeLife = 1 - data["DATA"][_keyDate]["sleep"] / 24
                        _percentTimeSleep = 1 - data["DATA"][_keyDate]["life"] / 24 
                        x0 = _x0 + (_dayCounter*_deltaXDAY)
                        y0 = (_w - (_totalAixisY - (_y0*0.3))) 
                        x1 = x0 + _deltaXDAY
                        y1 = y0 - (_totalAixisY*_percentTimeSleep)
                        canvas.create_rectangle(x0, y0, x1, y1, fill="black")
                        #canvas.create_rectangle(x0, y1, x1, _y0, fill="yellow") # The borders some big
                except:
                    pass

                _dayCounter = _dayCounter + 1

                d = _timeLIB.getNextDay(_datePivotYYYY, _datePivotMM, _datePivotDD)
                _datePivotYYYY = d[0]
                _datePivotMM = d[1]
                _datePivotDD = d[2]

        
    def getBackgroundImage(self, projectPath):
        """
        Read Folder RECURSOS/img/bg return photoimage
        """
        _simbolikSep = self.getSimbolikPathSeparator(projectPath)

        id = str(random.randint(0, 52))
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
    
    def getPhotoImageFromRouteX(self, routeIMGX):
         """
         Enter a path and return photoimage
         """
         return PhotoImage(file=routeIMGX)
    

    def getSimbolikPathSeparator(self, projectPath):
        """
        In Some SO usages / or \ to separates folder PATH
        """
        _simbolikSep = "\\"

        if _simbolikSep not in projectPath:
            _simbolikSep = "/"

        
        return _simbolikSep
 