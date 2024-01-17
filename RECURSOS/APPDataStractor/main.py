"""
FelipedelosH
2023

Para extrer la info de la APP hacia la versión desktop
"""

from tkinter import *
from tkinter import ttk
from Controller import *

class Software:
    def __init__(self) -> None:
        self.controller = Controller()
        self.screem = Tk()
        self.canvas = Canvas(self.screem, height=300, width=640, bg="snow")
        """Vars"""
        self._comboBoxYear = StringVar()
        self._comboBoxTypeSelector = StringVar()

        self.lblYearSelector = Label(self.canvas, text="Año: ")
        self.comboBoxYear = ttk.Combobox(self.canvas, state='readonly', textvariable=self._comboBoxYear)
        self.comboBoxYear['values'] = ['all','2020', '2021', '2022', '2023', '2024']
        self.comboBoxYear.current(0)
        self.lblTypeSelector = Label(self.canvas, text="Tipo de recurso: ")
        self.comboBoxTypeSelector = ttk.Combobox(self.canvas, state='readonly', textvariable=self._comboBoxTypeSelector)
        self.comboBoxTypeSelector['values'] = ['all', 'diary', 'dreams', 'time', 'feelings', 'economy']
        self.comboBoxTypeSelector.current(0)
        self.txtConsole = Text(self.canvas, width=77, height=10)
        self.btnCreateInfo = Button(self.canvas, text="Crear INFO", command= lambda : self.generateInfo(self._comboBoxYear.get(), self._comboBoxTypeSelector.get()))

        self.vizualizedAndRun()

    def vizualizedAndRun(self):
        self.screem.title("SQL APP data stractor")
        self.screem.geometry("640x300")
        self.canvas.place(x=0, y=0)
        self.lblYearSelector.place(x=20, y=20)
        self.comboBoxYear.place(x=80, y=20)
        self.lblTypeSelector.place(x=280, y=20)
        self.comboBoxTypeSelector.place(x=380, y=20)
        self.txtConsole.place(x=10, y=60)
        self.btnCreateInfo.place(x=280, y=260)


        self.screem.mainloop()

    def generateInfo(self, year, _type):
        self.controller.generateInfo(year, _type)
        self.txtConsole.delete('1.0', END)
        self.txtConsole.insert(END, self.controller.consoleText)
        



s = Software()
