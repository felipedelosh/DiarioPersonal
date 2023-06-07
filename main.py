"""
https://github.com/felipedelosh
a los 29 dias de sept de 2020

Diario del loko v2.0

Más que un software me propongo a proporcionar, organizar y gestionar mi información más personal.

Sientase libre de copiar, modificar y usar a su antojo.

"""
# -⁻- coding: UTF-8 -*-
from tkinter import * # Libreria para graficos> ventanas, botones, imagenes
from Controladora import * # Conexion entre interfaz y archivos
from tkinter import ttk # Para poder hacer el combo box
import math

class TimeHackingLoko():
    def __init__(self):
        self.controladora = Controladora()
        self.pantalla = Tk() # Esta es la pantalla principal. 
        self.tela = Canvas(self.pantalla, width=640, height=480) # Aqui se van a pintar los elementos en pantalla
        """Se invocan las imagenes"""
        self.imgFondo = PhotoImage(file=self.controladora.retornarRutaImagenDeFondo())
        self.imgBtnDiario = PhotoImage(file=self.controladora.returnIMGRnBtnRousourceX("diary"))
        self.imgPersonalDiary = PhotoImage(file=self.controladora.returnIMGRnBtnRousourceX("diary"))
        self.imgDreamDiary = PhotoImage(file=self.controladora.returnIMGRnBtnRousourceX("dreams"))
        self.imgPeople = PhotoImage(file=self.controladora.retornarRutaDelProyecto()+'/RECURSOS/img/people.gif')
        self.imgBtnAgenda = PhotoImage(file=self.controladora.returnIMGRnBtnRousourceX("calendary"))
        self.imgBtnNotas = PhotoImage(file=self.controladora.returnIMGRnBtnRousourceX("notes"))
        self.imgBtnEconimia = PhotoImage(file=self.controladora.retornarRutaDelProyecto()+'/RECURSOS/img/contabilidad.gif')
        self.imgBtnResultadoAnual = PhotoImage(file=self.controladora.retornarRutaDelProyecto()+'/RECURSOS/img/resultadoAnual.gif')
        self.imgFemputadora = PhotoImage(file=self.controladora.retornarRutaDelProyecto()+'/RECURSOS/img/femputadora.gif')
        self.imgBtnRegistoEmociones = PhotoImage(file=self.controladora.retornarRutaDelProyecto()+'/RECURSOS/img/emociones.gif')
        self.imgSaveFeeling = PhotoImage(file=self.controladora.retornarRutaDelProyecto()+'/RECURSOS/img/saveFeeling.gif')
        self.imgFeelingReport = PhotoImage(file=self.controladora.retornarRutaDelProyecto()+'/RECURSOS/img/feelingReport.gif')
        self.imgSaveTimeDistribution = PhotoImage(file=self.controladora.retornarRutaDelProyecto()+'/RECURSOS/img/saveTimeDistribution.gif')
        self.imgViewTimeDistribution = PhotoImage(file=self.controladora.retornarRutaDelProyecto()+'/RECURSOS/img/timeDistribution.gif')
        self.imgSchedule = PhotoImage(file=self.controladora.retornarRutaDelProyecto()+'/RECURSOS/img/schedule.gif')
        self.imgBtnDecicionesDeMierda = PhotoImage(file=self.controladora.retornarRutaDelProyecto()+'/RECURSOS/img/decicionesDeMierda.gif')
        self.imgTAccount = PhotoImage(file=self.controladora.retornarRutaDelProyecto()+'/RECURSOS/img/taccount.gif')
        self.imgEconomyReport = PhotoImage(file=self.controladora.retornarRutaDelProyecto()+'/RECURSOS/img/economyReport.gif')
        self.imgBox = PhotoImage(file=self.controladora.retornarRutaDelProyecto()+'/RECURSOS/img/box.gif')
        self.imgBtnConfiguracion = PhotoImage(file=self.controladora.retornarRutaDelProyecto()+'/RECURSOS/img/configuracion.gif')
        self.imgBtnAyuda = PhotoImage(file=self.controladora.retornarRutaDelProyecto()+'/RECURSOS/img/ayuda.gif')
        self.imageIcoPersona = PhotoImage(file=self.controladora.retornarRutaDelProyecto()+'/RECURSOS/img/ico/persona.png')
        """Imagenes de la pantalla principal"""
        self.btnDiario = Button(self.tela, image=self.imgBtnDiario, command=self.launchMenuDiary)
        self.btnAgenda = Button(self.tela, image=self.imgBtnAgenda, command=self.launchCalendary)
        self.btnNotas = Button(self.tela, image=self.imgBtnNotas, command=self.lanzarInterfaceNotas)
        self.btnEconomia = Button(self.tela, image=self.imgBtnEconimia, command=self.launchEconomyMenu)
        #self.btnResultadoAnual = Button(self.tela, image=self.imgBtnResultadoAnual, command=self.lanzarInterfaceResultadoAnual)
        self.btnFemputadora = Button(self.tela, image=self.imgFemputadora, command=self.launchFemputadoraInterface)
        self.btnRegistroEmociones = Button(self.tela, image=self.imgBtnRegistoEmociones, command=self.launchInterfaceFeeling)
        self.btnDedcicionesDeMierda = Button(self.tela, image=self.imgBtnDecicionesDeMierda, command=self.lanzarInterfaceDecicionesDeMierda)
        self.btnConfiguracion = Button(self.tela, image=self.imgBtnConfiguracion, command=self.lanzarInterfaceConfiguracion)
        self.btnAyuda = Button(self.tela, image=self.imgBtnAyuda, command=self.lanzarInterfaceAyuda)
        """Vars"""
        """vars to read a diary"""
        self.allInfoDiaryPages = [] # Save title, text to diary pages... It´s only to read.
        self.diaryPaginatorController = 0
        """Variables registro de sentimientos"""
        self.comboBoxSentimientosValor = StringVar()
        self.sentimientos = self.controladora.controladoraCarpetas.cargarEstadosEmocionanes()
        """Variables de rendicion de cuentas"""
        self.comboBoxAño = StringVar() # Guarda el Año que se necesita
        self.comboBoxEconomiaDia = StringVar() # Guarda en que dia estamos o que dia se necesita
        self.comboBoxEconomiaMes = StringVar() # Guarda en que mes estamos o cual se necesita
        self.comboBoxVistaEconomica = StringVar() # Guarda el periodo de tiempo que se va a graficar
        self._comboBoxYear = StringVar() # Save a year to wacth in calendar
        self._comboBoxMonth = StringVar() # Save a month to wacth in calendar
        self._dayToCalendaryFilter = 0 # To filter in calendary

        self.pintarYConfigurar() # se muestra la pantalla

    
    def pintarYConfigurar(self):
        self.pantalla.geometry("640x480")
        self.pantalla.title("Hackeo del Tiempo By LOko")
        self.tela.place(x=0, y=0)
        self.tela.create_image(0,0,image=self.imgFondo, anchor=NW)
        self.btnDiario.place(x=30, y=30)
        self.btnAgenda.place(x=250, y=30)
        self.btnNotas.place(x=460, y=30)
        self.btnEconomia.place(x=30, y=180)
        #self.btnResultadoAnual.place(x=250, y=180)
        self.btnFemputadora.place(x=250, y=180)
        self.btnRegistroEmociones.place(x=460, y=180)
        self.btnDedcicionesDeMierda.place(x=30, y=330)
        self.btnConfiguracion.place(x=250, y=330)
        self.btnAyuda.place(x=460, y=330)
        self.pantalla.mainloop()

    def ventanaEnmergenteDeAlerta(self, titulo, mensaje):
        top = Toplevel()
        top.geometry("500x300")
        top.title(titulo)
        msg = Text(top, width=55, height=13)
        msg.insert(END, mensaje)
        msg.place(x=25, y=20)
        button = Button(top, text="Aceptar", command=top.destroy)
        button.place(x=222, y=260)


    """Se declaran las interfaces TopLevel"""
    """Se declaran las interfaces TopLevel"""
    """Se declaran las interfaces TopLevel"""
    def launchMenuDiary(self):
        t = Toplevel()
        t.title("Diary Main MEnú...")
        t.geometry("250x400")
        canvas = Canvas(t, width=250, height=400)
        canvas.place(x=0, y=0)
        btnPersonalDiary = Button(canvas, image=self.imgPersonalDiary, command=self.lanzarPantallaDiario)
        btnPersonalDiary.place(x=70, y=20)
        btnDreams = Button(canvas, image=self.imgDreamDiary, command=self.launchInterfaceDreams)
        btnDreams.place(x=70, y=140)
        btnPeople = Button(canvas, image=self.imgPeople, command=self.launchInterfacePeople)
        btnPeople.place(x=70, y=260)

    def launchCalendary(self):
        t = Toplevel()
        t.title("Agenda")
        t.geometry("600x400")
        canvas = Canvas(t, height=400, width=600)
        canvas.place(x=0, y=0)
        # Get all years to user write
        lblYear = Label(canvas, text="Año: ")
        lblYear.place(x=20, y=20)
        comboBoxYear = ttk.Combobox(canvas, state='readonly', textvariable=self._comboBoxYear)
        yearsToUseAPP = self.controladora.getYearsToAPPUse()
        comboBoxYear['values'] = ["all"]+yearsToUseAPP
        comboBoxYear.current(0)
        comboBoxYear.place(x=20, y=50)
        # Get The Month
        lblMonth = Label(canvas, text="Mes: ")
        lblMonth.place(x=180, y=20)
        getCurrentMonth = self.controladora.tiempo.mes()
        comboBoxMonth = ttk.Combobox(canvas, state='readonly', textvariable=self._comboBoxMonth)
        comboBoxMonth['values'] = ["all"]+self.controladora.tiempo.meses
        comboBoxMonth.current(getCurrentMonth)
        comboBoxMonth.bind('<<ComboboxSelected>>', lambda k : self._refreshAdaysInCalendary(comboBoxMonth.current(), canvas))
        comboBoxMonth.place(x=180, y=50)
        # USE
        """
        Filter By Diary, Dream, Economy ...
        """

        # Paint month days
        self._refreshAdaysInCalendary(comboBoxMonth.current(), canvas)

        btnGetView = Button(canvas, text="Vizualizar", command=self._vizualizeDateCalendary)
        btnGetView.place(x=250, y=350)

    def _refreshAdaysInCalendary(self, month_number, canvas):
        """
        Enter a month and paints the days in canvas
        """
        if month_number != "all":
            days = self.controladora.tiempo.diasDeMes(month_number-1)
            btnsDays = []
            
            counter = 0
            _x = 60
            _y = 120
            for i in range(0, days):
                if counter == 9:
                    _x = 60
                    _y = _y + 50
                    counter = 0

                btnsDays.append(Button(canvas, text=str(i+1)))
                btnsDays[i].place(x=_x+(50*counter), y=_y)
                btnsDays[i].bind("<Button-1>", lambda b: self._markADayInCalendary(b.widget.cget('text')))

                counter = counter + 1

    def _markADayInCalendary(self, day):
        """
        If you prees a day button in calendary save it to filter then
        """
        self._dayToCalendaryFilter = day


    def _vizualizeDateCalendary(self):
        """
        If you mark a date in calendary get the report
        """
        data = self.controladora.loadCalendaryReport(self._comboBoxYear.get(), self._comboBoxMonth.get(), self._dayToCalendaryFilter)
        t = Toplevel()
        t.title("Resumen...")
        t.geometry("640x480")
        canvas = Canvas(t, height=480, width=640)
        canvas.place(x=0, y=0)
        txt = Text(canvas, width=76, height=28)
        txt.place(x=10, y=10)

        _txt = ""
        for i in data:
            _txt = _txt + str(i).upper() + "\n__________________________\n"
            _txt = _txt + data[i] + "\n\n\n\n\n\n"

        txt.insert(END, _txt)


    def launchEconomyMenu(self):
        t = Toplevel()
        t.title("Menú Economia...")
        t.geometry("400x500")
        canvas = Canvas(t, height=500, width=400)
        canvas.place(x=0, y=0)
        btnTAccount = Button(canvas, image=self.imgTAccount, command=self.lanzarInterfaceEconomia)
        btnTAccount.place(x=140, y=20)
        btnEconomyReport = Button(canvas, image=self.imgEconomyReport, command=self.subInterfaceReporteEconomico)
        btnEconomyReport.place(x=140, y=140)
        btnBox = Button(canvas, image=self.imgBox, command=self.subInterfacebalaceDeCajas)
        btnBox.place(x=140, y=260)
        

            

    def lanzarPantallaDiario(self):
        interfaceDiario = Toplevel()
        interfaceDiario.title("Diario by loko")
        interfaceDiario.geometry("500x500")
        lblPalabraMagica = Label(interfaceDiario, text="Palabra Magica: ")
        lblPalabraMagica.place(x=20, y=20)
        txtpalabraMagica = Entry(interfaceDiario)
        txtpalabraMagica.place(x=130, y=20)
        txtTexto = Text(interfaceDiario, height = 22, width = 58)
        txtTexto.place(x=10, y=80)
        scrollTxtTexto = Scrollbar(interfaceDiario, orient=VERTICAL, command=txtTexto.yview)
        scrollTxtTexto.place(x=470, y=20)
        btnLoad = Button(interfaceDiario, text="Cargar", command=lambda : self.cargarpaginaDeDiario(txtpalabraMagica.get(), txtTexto))
        btnLoad.place(x=270, y=20)
        btnReader = Button(interfaceDiario, text="Lector", command=lambda :self.loadFullReader("diary"))
        btnReader.place(x=340, y=20)
        btnSave = Button(interfaceDiario, text="Guardar", command=lambda : self.guardarPaginaEnDiario(txtpalabraMagica.get(), txtTexto.get("1.0", END)))
        btnSave.place(x=400,y=20)

    def launchInterfaceDreams(self):
        t = Toplevel()
        t.title("Diario de sueños")
        t.geometry("500x500")
        lblKeyword = Label(t, text="Palabra Magica: ")
        lblKeyword.place(x=20, y=20)
        txtKeyword = Entry(t)
        txtKeyword.place(x=130, y=20)
        txtText = Text(t, height = 22, width = 58)
        txtText.place(x=10, y=80)
        scrollTxtText = Scrollbar(t, orient=VERTICAL, command=txtText.yview)
        scrollTxtText.place(x=470, y=20)
        btnLoad = Button(t, text="Cargar", command=lambda : self.loadDreamPageDiary(txtKeyword.get(), txtText))
        btnLoad.place(x=270, y=20)
        btnReader = Button(t, text="Lector", command=lambda :self.loadFullReader("dreams"))
        btnReader.place(x=340, y=20)
        btnSave = Button(t, text="Guardar", command=lambda : self.saveDreamDiaryPage(txtKeyword.get(), txtText.get("1.0", END)))
        btnSave.place(x=400,y=20)

    def launchInterfacePeople(self):
        t = Toplevel()
        t.title("Personas...")
        t.geometry("400x500")
        canvas = Canvas(t, height=500, width=400)
        canvas.place(x=0, y=0)
        lblNamePerson = Label(canvas, text="Nombre Persona: ")
        lblNamePerson.place(x=10, y=20)
        txtNamePerson = Entry(canvas, width=36)
        txtNamePerson.place(x=120, y=20)
        btnShowAllPeople = Button(canvas, text="?", command=self._showAllPeopleNames)
        btnShowAllPeople.place(x=350, y=18)
        lblAlias = Label(canvas, text="Apodo (Alias): ")
        lblAlias.place(x=10, y=48)
        txtAlias = Entry(canvas, width=36)
        txtAlias.place(x=120, y=48)
        btnShowAllAlias = Button(canvas, text="?", command=self._showAllPeopleAlias)
        btnShowAllAlias.place(x=350, y=46)
        lblDescription = Label(canvas, text="Descripción y/o anecdota:")
        lblDescription.place(x=10, y=100)
        txtDescription = Text(t, height = 12, width = 44)
        txtDescription.place(x=10, y=120)
        lblQualification = Label(canvas, text="Calificación de la experiencia:")
        lblQualification.place(x=10, y=350)
        _scale = Scale(canvas, from_=0, length=360, to=100, orient=HORIZONTAL)
        _scale.place(x=10, y=370)
        btnSave = Button(canvas, text="GUARDAR", command=lambda : self.savePeopleDescription(txtNamePerson.get(), txtAlias.get(), txtDescription.get("1.0", END), _scale.get()))
        btnSave.place(x=160, y=460)

    def _showAllPeopleNames(self):
        data = self.controladora.controladoraCarpetas.listOfAllPeople()
        _title = "Todos los Nombres"
        _names = ""
        if data == []:
            self.ventanaEnmergenteDeAlerta(_title, "HP no hay Nadie... 4everAlone .l..")
        else:
            for i in data:
                _names = _names + i + "\n"
            self.ventanaEnmergenteDeAlerta(_title, _names)

    def _showAllPeopleAlias(self):
        data = self.controladora.controladoraCarpetas.listOfNamePeopleAndAlias()
        _title = "Todos los Alias"
        _names = ""
        if data == []:
            self.ventanaEnmergenteDeAlerta(_title, "HP no hay Nadie... Nadie MRK!!!!")
        else:
            for i in data:
                _names = _names + i + "\n"
            self.ventanaEnmergenteDeAlerta(_title, _names)
    


    def lanzarInterfaceNotas(self):
        interfaceNotas = Toplevel()
        interfaceNotas.title("Notas del Loko")
        interfaceNotas.geometry("500x500")
        lblPalabraMagica = Label(interfaceNotas, text="Palabra Magica: ")
        lblPalabraMagica.place(x=30, y=22)
        txtpalabraMagica = Entry(interfaceNotas)
        txtpalabraMagica.place(x=150, y=22)
        txtTexto = Text(interfaceNotas, height = 22, width = 58)
        txtTexto.place(x=10, y=80)
        btnLector = Button(interfaceNotas, text="Lector", command=lambda :self.loadFullReader("notes"))
        btnLector.place(x=320, y=20)
        btnSave = Button(interfaceNotas, text="Guardar", command=lambda : self.guardarNota(txtpalabraMagica.get(), txtTexto.get("1.0", END)))
        btnSave.place(x=400,y=20)

    def lanzarInterfaceEconomia(self):
        interfaceEconomia = Toplevel()
        interfaceEconomia.title("Economia by Loko ")
        interfaceEconomia.geometry("640x500")
        enQueDiaEstamos = self.controladora.tiempo.diaNumero()
        enQueMesEstamos = self.controladora.tiempo.mes()
        lblDia = Label(interfaceEconomia, text="Dia: ")
        lblDia.place(x=20, y=20)
        comboBoxDia = ttk.Combobox(interfaceEconomia, state='readonly', textvariable=self.comboBoxEconomiaDia)
        comboBoxDia['values'] = self.refrescarDias(enQueMesEstamos) # Se ponen los valores del mes en que estamos
        comboBoxDia.current(enQueDiaEstamos-1) # Se le pone el dia en que estamos por defecto
        comboBoxDia.place(x=20, y=40)
        lblMes = Label(interfaceEconomia, text="Mes: ")
        lblMes.place(x=200, y=20)
        comboBoxMes = ttk.Combobox(interfaceEconomia, state="readonly", textvariable=self.comboBoxEconomiaMes)
        comboBoxMes['values'] = self.controladora.tiempo.meses
        comboBoxMes.current(enQueMesEstamos-1)
        comboBoxMes.bind('<<ComboboxSelected>>', lambda temporal : self._refrescarDias(comboBoxMes.current(), comboBoxDia))
        comboBoxMes.place(x=200, y=40)
        lblConcepto = Label(interfaceEconomia, text="Concepto")
        lblConcepto.place(x=40, y=90)
        lblDebe = Label(interfaceEconomia, text="+Debe")
        lblDebe.place(x=300, y=90)
        lblHaber = Label(interfaceEconomia, text="-Haber")
        lblHaber.place(x=450, y=90)
        """Se pinta las leyendas 1,2,3...osea nro de renglon"""
        leyendas = []
        txtConcepto = []
        txtDebe = []
        txtHaber = []
        for i in range(0, 12):
            leyendas.append(Label(interfaceEconomia, text=str(i+1)+":"))
            leyendas[i].place(x=10, y=(130+(25*i)))
            """Se pintan los entry del concepto"""
            txtConcepto.append(Entry(interfaceEconomia, width=38))
            txtConcepto[i].place(x=40, y=(132+(25*i)))
            """Se pintan los entry de debe"""
            txtDebe.append(Entry(interfaceEconomia, width=20))
            txtDebe[i].place(x=300, y=(132+(25*i)))
            """Se pintan los entry de haber"""
            txtHaber.append(Entry(interfaceEconomia, width=20))
            txtHaber[i].place(x=450, y=(132+(25*i)))

        btnCargar = Button(interfaceEconomia, text="Cargar", command= lambda : self.cargarEconomia(txtConcepto, txtDebe, txtHaber))
        btnCargar.place(x=400, y=32)
        btnGuardar = Button(interfaceEconomia, text="Guardar", command=lambda : self.guardarEconomia(txtConcepto, txtDebe, txtHaber))
        btnGuardar.place(x=500, y=32)

    def launchFemputadoraInterface(self):
        t = Toplevel()
        t.title("Femputadora")
        t.geometry("640x480")
        canvas = Canvas(t, height=4480, width=640, bg="gray12")
        canvas.place(x=0, y=0)
        lblEnterText = Label(canvas, text="Ingrese el texto: ", bg="gray10", fg="white")
        lblEnterText.place(x=20, y=20)
        txtUserEntry = Entry(canvas ,width=80, fg="white", bg="gray20")
        txtUserEntry.place(x=120, y=20)
        txtMachineOutput = Text(canvas, fg="white", bg="gray8", height=22, width=70)
        txtMachineOutput.place(x=30, y=60)
        self.controladora.saveUseWrite("femputadora")
        txtUserEntry.bind('<Key>', lambda event : self._enterTXTinFemputadora(event, txtUserEntry, txtMachineOutput))



    def lanzarInterfaceResultadoAnual(self):
        interfaceResultadoAnual = Toplevel()
        interfaceResultadoAnual.title("Rendicion de cuentas By Loko")
        interfaceResultadoAnual.geometry("500x500")
        btnRegistrarLogroDeMiVida = Button(interfaceResultadoAnual, text="Registrar Logro", command=self.subInterfazRegistrarLogroDeMiVida)
        btnRegistrarLogroDeMiVida.place(x=20, y=20)
        btnRegistrarActividad = Button(interfaceResultadoAnual, text="Registrar Actividad", command=self.subInterfaceRegistrarActividad)
        btnRegistrarActividad.place(x=20, y=60)
        btnInversionDeTiempo = Button(interfaceResultadoAnual, text="Inversion de tiempo", command=self.subInterfaceInversionTiempoDiario)
        btnInversionDeTiempo.place(x=20, y=100) 
        btnHorario = Button(interfaceResultadoAnual, text="HORARIO", command=self.subInterfaceHorario)
        btnHorario.place(x=20, y=140)
        btnReporteEconomico = Button(interfaceResultadoAnual, text="Reporte economico", command=self.subInterfaceReporteEconomico)
        btnReporteEconomico.place(x=20, y=180)
        btnBalanceDeCaja = Button(interfaceResultadoAnual, text="Estado de la caja", command=self.subInterfacebalaceDeCajas)
        btnBalanceDeCaja.place(x=20, y=220)
        btnReporteDeSentimientos = Button(interfaceResultadoAnual, text="Reporte de sentimientos", command=self.subInterfaceReporteDeSentimientos)
        btnReporteDeSentimientos.place(x=20, y=260)
        btnGastoDeVida = Button(interfaceResultadoAnual, text="Gasto de vida", command=self.subInterfaceGastoDeVida)
        btnGastoDeVida.place(x=20, y=300)
        btnPilaresDeLaFelicidad = Button(interfaceResultadoAnual, text="pilares de la felicidad", command=self.subInterfacePilaresDeLaFelicidad)
        btnPilaresDeLaFelicidad.place(x=20, y=340)



    def lanzarInterfaceDecicionesDeMierda(self):
        interfaceDecicionesDeMierda = Toplevel()
        interfaceDecicionesDeMierda.title("Deciciones De Mierda")
        interfaceDecicionesDeMierda.geometry("1280x720")
        tela = Canvas(interfaceDecicionesDeMierda, width=1280, height=720, bg='snow')
        tela.place(x=0, y=0)
        lblDecicion = Label(tela, text="Arbol: ")
        lblDecicion.place(x=20, y=20)
        txtDecicion= Entry(tela, width=50)
        txtDecicion.place(x=100, y=20)
        btnCrear = Button(tela, text="Crear", command= lambda : self.crearCarpetaDeDeciciones(txtDecicion.get()))
        btnCrear.place(x=440, y=18)
        btnCargar = Button(tela, text="Cargar")
        btnCargar.place(x=500, y=18)
        btnDecicion = Button(tela, text="Agregar Estado", command=self.lanzarInterfaceDecicionesDeMierdaAgregarEstado)
        btnDecicion.place(x=700, y=18)

        """
        Se genera el tablero en donde se van a pintar las deciciones
        """
        for i in range(0, 10):
            tela.create_line(0,120+(i*60),1280,120+(i*60), fill='blue')
            tela.create_line(100+(i*120), 120, 100+(i*120), 660, fill='blue')

    def launchInterfaceFeeling(self):
        t = Toplevel()
        t.title("Menú Sentimientos...")
        t.geometry("400x500")
        canvas = Canvas(t, height=500, width=400)
        canvas.place(x=0, y=0)
        btnSaveFeeling = Button(canvas, image=self.imgSaveFeeling, command=self.lanzarPantallaRegistroSentimientos)
        btnSaveFeeling.place(x=60, y=20)
        btnFeelingReport = Button(canvas, image=self.imgFeelingReport, command=self.subInterfaceReporteDeSentimientos)
        btnFeelingReport.place(x=220, y=20)
        btnSaveTimeDistribution = Button(canvas, image=self.imgSaveTimeDistribution, command=self.subInterfaceInversionTiempoDiario)
        btnSaveTimeDistribution.place(x=60, y=140)
        btnViewTimeDistribution = Button(canvas, image=self.imgViewTimeDistribution, command=self.subInterfacePilaresDeLaFelicidad)
        btnViewTimeDistribution.place(x=220, y=140)
        btnSchedule = Button(canvas, image=self.imgSchedule, command=self.subInterfaceHorario)
        btnSchedule.place(x=60, y=260)

    def lanzarPantallaRegistroSentimientos(self):
        interfaceSentimientos = Toplevel()
        interfaceSentimientos.title("Registro de sentimientos...")
        interfaceSentimientos.geometry("500x150")
        lblComoTeSientesHoy = Label(interfaceSentimientos, text="Como te sientiste hoy: ")
        lblComoTeSientesHoy.place(x=20, y=50)
        comboBoxSentimientos = ttk.Combobox(interfaceSentimientos, state='readonly', textvariable=self.comboBoxSentimientosValor)
        comboBoxSentimientos['values'] = self.sentimientos
        comboBoxSentimientos.place(x=180, y=50)
        btnGuardarSentimiento = Button(interfaceSentimientos, text="Guardar", command=self.guardarSentimiento)
        btnGuardarSentimiento.place(x=400, y=50)

    #Ojo: esto esta mal ubicado... declararlo en el futuro como subinterface
    def lanzarInterfaceDecicionesDeMierdaAgregarEstado(self):
        if self.controladora.arbolDeDecicionEstaListo():
            interfaceAgregarEstado = Toplevel()
            interfaceAgregarEstado.title("Agregar decicion de mierda")
            interfaceAgregarEstado.geometry("500x500")
            lblIDPadre = Label(interfaceAgregarEstado, text="ID Padre: ")
            lblIDPadre.place(x=20, y=20)
            txtIDPadre = Entry(interfaceAgregarEstado)
            txtIDPadre.place(x=100, y=20)
            lblID = Label(interfaceAgregarEstado, text="ID nodo: ")
            lblID.place(x=20, y=60)
            txtID = Entry(interfaceAgregarEstado)
            txtID.place(x=100, y=60)
            lblTitulo = Label(interfaceAgregarEstado, text="Titulo: ")
            lblTitulo.place(x=20, y=120)
            txtTitulo = Entry(interfaceAgregarEstado)
            txtTitulo.place(x=100, y=120)
            lblDescripcionEvento = Label(interfaceAgregarEstado, text="Descripcion del evento: ")
            lblDescripcionEvento.place(x=20, y=160)
            txtDescripcionEvento = Text(interfaceAgregarEstado, height = 16, width = 58)
            txtDescripcionEvento.place(x=20, y=180)
            btnGuardar = Button(interfaceAgregarEstado, text="Guardar", command=lambda:self.guardarEstadoEnCarpetaDeDeciciones([txtIDPadre.get(), txtID.get(), txtTitulo.get(), txtDescripcionEvento.get("1.0", END)]))
            btnGuardar.place(x=230, y=460)

        else:
            self.ventanaEnmergenteDeAlerta("Error", "Primero crea o carga un arbol")

    def lanzarInterfaceConfiguracion(self):
        interfaceConfiguracion = Toplevel()
        interfaceConfiguracion.title("Configuración")
        interfaceConfiguracion.geometry("200x300")
        btnProfile = Button(interfaceConfiguracion, text="Perfil", command=self.subInterfacePerfil)
        btnProfile.place(x=70, y=20)


    def lanzarInterfaceAyuda(self):
        interfaceayuda = Toplevel()
        interfaceayuda.title("Manual")
        interfaceayuda.geometry("640x480")
        btnManualDelUsuario = Button(interfaceayuda, text="Manual del Usuario", command=self.linkManualDelUsuario)
        btnManualDelUsuario.place(x=20, y=20)
        btnListadoPosible = Button(interfaceayuda, text="Listado de Posibilidades", command=self.verLasPisibilidades) 
        btnListadoPosible.place(x=200, y=20)
        btnProgramacion = Button(interfaceayuda, text="Como estoy programado")
        btnProgramacion.place(x=400, y=20)
        k = self.controladora.retornarMensajePrincipalAyuda()
        txtMensajePrincipal = Text(interfaceayuda, height = 22, width = 75)
        txtMensajePrincipal.insert(END, k)
        txtMensajePrincipal.place(x=20, y=100)



    """Se declaran las interfaces TopLevel"""
    """Se declaran las interfaces TopLevel"""
    """Se declaran las interfaces TopLevel"""
    #------------------------------------------
    """Se declaran las subinterfaces TopLevel"""
    """Se declaran las subinterfaces TopLevel"""
    """Se declaran las subinterfaces TopLevel"""
    """Subinterfaces de registros anuales y rendicion de cuentas"""
    def subInterfazRegistrarLogroDeMiVida(self):
        interfazRegistrarLogro = Toplevel()
        interfazRegistrarLogro.title("Registrar Logro en mi vida")
        interfazRegistrarLogro.geometry("500x150")
        lblAyuda = Label(interfazRegistrarLogro, text="Ingresa el año y el logro: ")
        lblAyuda.place(x=20, y=20)
        """se configura el combox del año"""
        misAñosDeVida = []
        for i in range(1991, 2066):
            misAñosDeVida.append(i)

        comboAño = ttk.Combobox(interfazRegistrarLogro, state='readonly', textvariable=self.comboBoxAño)
        comboAño['values'] = misAñosDeVida
        comboAño.place(x=20, y=80)

        txtLogro = Entry(interfazRegistrarLogro)
        txtLogro.place(x=200, y=80)

        btnRegistrarLogro = Button(interfazRegistrarLogro, text="Registrar", command= lambda: self.registrarLogro(txtLogro.get()))
        btnRegistrarLogro.place(x=350, y=80)

    def subInterfaceRegistrarActividad(self):
        interfaceRegistrarActividad = Toplevel()
        interfaceRegistrarActividad.title("Registrar Actividad by loko")
        interfaceRegistrarActividad.geometry("500x150")
        lblQueHisisteHoy = Label(interfaceRegistrarActividad, text="Que hisiste hoy?")
        lblQueHisisteHoy.place(x=20, y=20)
        txtActividad = Entry(interfaceRegistrarActividad, width=50)
        txtActividad.place(x=20, y=80)
        btnRegistrar = Button(interfaceRegistrarActividad, text="Registrar", command=lambda : self.registrarActividad(txtActividad.get()))
        btnRegistrar.place(x=390, y=76)


    def subInterfaceReporteDeSentimientos(self):
        self.comboBoxAño.set("") # Se reinicia el valor del combo box
        interfaceReporteSentimientos = Toplevel()
        interfaceReporteSentimientos.title("Reporte de Sentimientos")
        interfaceReporteSentimientos.geometry("300x200")
        lblElijeAño = Label(interfaceReporteSentimientos, text="Elije el año y grafica: ")
        lblElijeAño.place(x=20, y=20)
        comboAñosDeRegistroSentimientos = ttk.Combobox(interfaceReporteSentimientos, state='readonly', textvariable=self.comboBoxAño)
        comboAñosDeRegistroSentimientos['values'] = self.controladora.controladoraCarpetas.listarAñosDeRegistroSentimientos()
        comboAñosDeRegistroSentimientos.place(x=20 , y=80)
        btnGraficasentimientos = Button(interfaceReporteSentimientos, text="Graficar", command=self.graficarAñoSentimiento)
        btnGraficasentimientos.place(x=140, y=160)


    def subInterfaceInversionTiempoDiario(self):
        interfaceTiempoDia = Toplevel()
        interfaceTiempoDia.title("Inversión tiempo día")
        interfaceTiempoDia.geometry("300x700")
        lblHora = Label(interfaceTiempoDia, text="Hora: ")
        lblHora.place(x=20, y=20)
        lblActividad = Label(interfaceTiempoDia, text="Actividad: ")
        lblActividad.place(x=100, y=20)

        # Se ponen todas las horas empezando desde las 6 de la ma+ana
        formato12h = 6
        controlAMPM = 0 # Controla si se asigna AM o PM
        AMPM = ""
        lblHr = [] # Aqui se van a guardar los labels que informan la hora
        actividades = [] # Aqui se van a guardas los combobox con actidades posibles 
        actividadesPosibles = self.controladora.controladoraCarpetas.cargarActividades() # lista de actividades
        strActividades = [] # Aqui se guardan los string var que van a gardar las actividades

        for i in range(0, 24):
            
            if formato12h == 13:
                formato12h = 1

                if controlAMPM == 0:
                    controlAMPM = 1
                else:
                    controlAMPM = 0
         
            if controlAMPM == 0:
                AMPM = "am"
            else:
                AMPM = "pm"

            # Se poenen las horas
            lblHr.append(Label(interfaceTiempoDia, text=str(formato12h)+AMPM))
            lblHr[i].place(x=20, y=60+(25*i))
            # Aqui se almacena esta actividad
            strActividades.append(StringVar())
            # Se ponen los comboBox de actividades
            actividades.append(ttk.Combobox(interfaceTiempoDia, state='readonly', textvariable=strActividades[i], values=actividadesPosibles))
            actividades[i].place(x=100, y=60+(25*i))

            formato12h = formato12h + 1

        # Se crea el boton para guardar
        btnGuardar = Button(interfaceTiempoDia, text="GUARDAR", command = lambda : self.guardarInversionTiempoDiaria(lblHr, strActividades))
        btnGuardar.place(x=180, y=20)

    def subInterfaceGastoDeVida(self):
        nacimientoUsuario = 1991

        interfaceGastoDeVida = Toplevel()
        interfaceGastoDeVida.geometry("640x500")
        interfaceGastoDeVida.title("Gasto de Vida " + str(nacimientoUsuario))
        lienzo = Canvas(interfaceGastoDeVida, height=500, width=640, bg="snow")
        lienzo.place(x=0, y=0)
        btnAnterio = Button(interfaceGastoDeVida, text="<<")
        btnAnterio.place(x=500, y=20)
        btnSiguiente = Button(interfaceGastoDeVida, text=">>")
        btnSiguiente.place(x=550, y=20)
        btnVertotal = Button(interfaceGastoDeVida, text="Ver Total", command=lambda : self.graficarTiempoDeVida(lienzo, nacimientoUsuario))
        btnVertotal.place(x=20, y=20)

        # Se pintan 100 años mas desde la fecha de tu nacimiento
        for i in range(0, 20):
            lienzo.create_text(20, (20*i)+60, text=str(nacimientoUsuario+i), tags="life")
            # Cada a+o tiene 54 semanas
            for j in range(0, 54):
                x0 = 50 + (j*10)
                y0 = 55 + (20*i)
                x1 = x0 + 8
                y1 = y0 + 8

                lienzo.create_rectangle((x0), (y0), (x1),(y1), fill="red", tags="life")


    def subInterfaceHorario(self):
        interfaceHorario = Toplevel()
        interfaceHorario.title("Horario")
        interfaceHorario.geometry("1280x700")
        tela = Canvas(interfaceHorario, width=1280, height=700, bg="snow")
        tela.place(x=0, y=0)
        lblHora = [] # Aqui se pintan las horas militares
        lblDias = [] # Aqui estaran los labels que indican el dia de la semana
        controlHoraMilitar = 7 # La hora empezara desde las 7:00
        lunes = []
        opcionesLunes = []
        martes = []
        opcionesMartes = []
        miercoles = []
        opcionesMiercoles = []
        jueves = []
        opcionesJueves = []
        viernes = []
        opcionesViernes = []
        sabado = []
        opcionesSabado = []
        domingo = []
        opcionesDomingo = []
        opcionesComboBox = self.controladora.controladoraCarpetas.cargarActividades()
        # Se pintan los elementos semanal
        for i in range(0, 7):
            lblDias.append(Label(tela, text=self.controladora.tiempo.diasDeLaSemana[i]))
            lblDias[i].place(x=60+(110*i), y=10)

        #Se pintan los elementos por hora
        for j in range(0, 24):
            if controlHoraMilitar == 24:
                controlHoraMilitar = 0
            lblHora.append(Label(tela, text=str(controlHoraMilitar)+":00"))
            controlHoraMilitar = controlHoraMilitar + 1
            lblHora[j].place(x=10, y=60+(26*j))

            # Se pintan los combo box dia
            opcionesLunes.append(StringVar())
            lunes.append(ttk.Combobox(interfaceHorario, state='readonly', values=opcionesComboBox, width=12, textvariable=opcionesLunes[j]))
            lunes[j].bind('<<ComboboxSelected>>', lambda temporal: self.graficaCircularDelHorario(tela, opcionesLunes, opcionesMartes, opcionesMiercoles, opcionesJueves, opcionesViernes, opcionesSabado, opcionesDomingo))
            lunes[j].place(x=60, y=60+(26*j))
            opcionesMartes.append(StringVar())
            martes.append(ttk.Combobox(interfaceHorario, state='readonly', values=opcionesComboBox, width=12, textvariable=opcionesMartes[j]))
            martes[j].bind('<<ComboboxSelected>>', lambda temporal: self.graficaCircularDelHorario(tela, opcionesLunes, opcionesMartes, opcionesMiercoles, opcionesJueves, opcionesViernes, opcionesSabado, opcionesDomingo))
            martes[j].place(x=170, y=60+(26*j))
            opcionesMiercoles.append(StringVar())
            miercoles.append(ttk.Combobox(interfaceHorario, state='readonly', values=opcionesComboBox, width=12, textvariable=opcionesMiercoles[j]))
            miercoles[j].bind('<<ComboboxSelected>>', lambda temporal: self.graficaCircularDelHorario(tela, opcionesLunes, opcionesMartes, opcionesMiercoles, opcionesJueves, opcionesViernes, opcionesSabado, opcionesDomingo))
            miercoles[j].place(x=280, y=60+(26*j))
            opcionesJueves.append(StringVar())
            jueves.append(ttk.Combobox(interfaceHorario, state='readonly', values=opcionesComboBox, width=12, textvariable=opcionesJueves[j]))
            jueves[j].bind('<<ComboboxSelected>>', lambda temporal: self.graficaCircularDelHorario(tela, opcionesLunes, opcionesMartes, opcionesMiercoles, opcionesJueves, opcionesViernes, opcionesSabado, opcionesDomingo))
            jueves[j].place(x=390, y=60+(26*j))
            opcionesViernes.append(StringVar())
            viernes.append(ttk.Combobox(interfaceHorario, state='readonly', values=opcionesComboBox, width=12, textvariable=opcionesViernes[j]))
            viernes[j].bind('<<ComboboxSelected>>', lambda temporal: self.graficaCircularDelHorario(tela, opcionesLunes, opcionesMartes, opcionesMiercoles, opcionesJueves, opcionesViernes, opcionesSabado, opcionesDomingo))
            viernes[j].place(x=500, y=60+(26*j))
            opcionesSabado.append(StringVar())
            sabado.append(ttk.Combobox(interfaceHorario, state='readonly', values=opcionesComboBox, width=12, textvariable=opcionesSabado[j]))
            sabado[j].bind('<<ComboboxSelected>>', lambda temporal: self.graficaCircularDelHorario(tela, opcionesLunes, opcionesMartes, opcionesMiercoles, opcionesJueves, opcionesViernes, opcionesSabado, opcionesDomingo))
            sabado[j].place(x=610, y=60+(26*j))
            opcionesDomingo.append(StringVar())
            domingo.append(ttk.Combobox(interfaceHorario, state='readonly', values=opcionesComboBox, width=12, textvariable=opcionesDomingo[j]))
            domingo[j].bind('<<ComboboxSelected>>', lambda temporal: self.graficaCircularDelHorario(tela, opcionesLunes, opcionesMartes, opcionesMiercoles, opcionesJueves, opcionesViernes, opcionesSabado, opcionesDomingo))
            domingo[j].place(x=720, y=60+(26*j))

        btnLimpiarHorario = Button(interfaceHorario, text="Limpiar", command=lambda : self.limpiarHorario(lunes, martes, miercoles, jueves, viernes, sabado, domingo))
        btnLimpiarHorario.place(x=900, y=10)
        btnCargarHorario = Button(interfaceHorario, text="Cargar", command=lambda : self.cargarHorario(lunes, martes, miercoles, jueves, viernes, sabado, domingo))
        btnCargarHorario.place(x=1000, y=10)
        btnGuardarHorario = Button(interfaceHorario, text="Guardar", command=lambda : self.guardarHorario(opcionesLunes, opcionesMartes, opcionesMiercoles, opcionesJueves, opcionesViernes, opcionesSabado, opcionesDomingo))
        btnGuardarHorario.place(x=1100, y=10)


    def subInterfaceReporteEconomico(self):
        """
        para ver ingresos y egresos atravez del tiempo
        """
        reporteEconomico = Toplevel()
        reporteEconomico.title("Reporte Economico")
        reporteEconomico.geometry("720x480")
        lblTipoDeVistaReporte = Label(reporteEconomico, text="Tipo de vista:")
        lblTipoDeVistaReporte.place(x=20, y=20)
        valuesComboBox = self.controladora.cargarDatosFechasInformacionEconomica()
        
        tela = Canvas(reporteEconomico, height=400, width=650, bg="snow")
        tela.place(x=30, y=60)
        cmbxVistasReporteEconomico = ttk.Combobox(reporteEconomico, state='readonly', values=valuesComboBox, textvariable=self.comboBoxVistaEconomica)
        cmbxVistasReporteEconomico.place(x=100, y=20)

        btnMostrarInformacion = Button(reporteEconomico, text="Ver", command= lambda : self.graficaPeridoEconomica(tela))
        btnMostrarInformacion.place(x=280, y=18)

    def subInterfacebalaceDeCajas(self):
        """
        Existen 2 tipos de cajas:
        ->Caja mayor: Contiene los ahorros y solo se gasta en caso de emergencia
        ->Caja menor es el monto que se puede gastar cada dia.

        Ambas cajas estan contenidas en DATA/ECONOMIA/CAJAS/cajaMayor.txt y cajaMenor.txt

        Aqui se puede guardar manualmente el monto de ambas cajas 
        ademas de decirme cuanto dinero me puedo gastar en 1 dia deacuerdo a los ingresos.
        """
        interfaceCaja = Toplevel()
        interfaceCaja.geometry("500x500")
        lienzo = Canvas(interfaceCaja, height=300, width=480, bg="snow")
        lienzo.place(x=10, y=120)
        # Se pintan las graficas
        self.graficaEstadoDeCajas(lienzo)
        # Se ponen los labels
        lblEstadoCajaMayor = Label(interfaceCaja, text="Estado Caja Mayor: $")
        lblEstadoCajaMayor.place(x=20, y=50)
        txtEstadoCajaMayor = Entry(interfaceCaja, width=40)
        k = self.controladora.cargarEstadoCajaMayor() # Se retorna la informacion de la caja mayor
        txtEstadoCajaMayor.insert(0, k)
        txtEstadoCajaMayor.place(x=140, y=52)
        btnGuardarEstadoCajaMayor = Button(interfaceCaja, text="Actualizar", command=lambda : self.guardarMontoCajaMayor(txtEstadoCajaMayor.get(), lienzo))
        btnGuardarEstadoCajaMayor.place(x=400, y=48)
        lblEstadoCajaMenor = Label(interfaceCaja, text="Estado Caja Menor: $")
        lblEstadoCajaMenor.place(x=20, y=80)
        txtEstadoCajaMenor = Entry(interfaceCaja, width=40)
        k = self.controladora.cargarEstadoCajaMenor() # Se retorna la informacion de la caja mayor
        txtEstadoCajaMenor.insert(0, k)
        txtEstadoCajaMenor.place(x=140, y=82)
        btnGuardarEstadoCajaMenor = Button(interfaceCaja, text="Actualizar", command=lambda : self.guardarMontoCajaMenor(txtEstadoCajaMenor.get(), lienzo))
        btnGuardarEstadoCajaMenor.place(x=400, y=78)



        # Se procede a calcular el dinero que puedes gastar hoy
        # Se supone que el dinero de la caja menor tiene que durar 1 mes
        d = self.controladora.queNumeroDeDiaEs() # Información del dia actual
        d = abs(30 - d) # Que tan lejos estoy a fin de mes
        dineroQuePuedesGastarHoy = round((int(k) / d), 2)
        lblDineroQuePuedesGastarHoy = Label(interfaceCaja, text="Hoy puedes gastar > $ "+str(dineroQuePuedesGastarHoy))
        lblDineroQuePuedesGastarHoy.place(x=100, y=460)

    def subInterfacePerfil(self):
        interfacePerfil = Toplevel()
        interfacePerfil.title("Perfil: ")
        interfacePerfil.geometry("640x480")
        lienzo = Canvas(interfacePerfil, width=640, height=480)
        lienzo.place(x=0, y=0)
        lienzo.create_rectangle(20, 20, 220, 220, fill="blue")

        lblNombreYApellido = Label(lienzo, text="Nombre y apellido: ")
        lblNombreYApellido.place(x=240, y=18)
        txtNombreYApellido = Entry(lienzo, width=35)
        txtNombreYApellido.place(x=360, y=20)
        lblFechaDeNacimiento = Label(lienzo, text="Fecha de Nacimiento: ")
        lblFechaDeNacimiento.place(x=240, y=50)
        txtFechaDeNacimiento = Entry(lienzo, width=35)
        txtFechaDeNacimiento.place(x=360, y=52)
        lblGenero = Label(lienzo, text="Genero: ")
        lblGenero.place(x=240, y=80)
        comboBoxGenero = ttk.Combobox(lienzo, values=['Masculino', 'Femenino'])
        comboBoxGenero.place(x=300, y=80)
        lblEdad = Label(lienzo, text="Edad: ")
        lblEdad.place(x=460, y=80)
        txtEdad = Entry(lienzo, width=10)
        txtEdad.place(x=510, y=80)
        lblUsername = Label(lienzo, text="Username:  ")
        lblUsername.place(x=20, y=230)
        txtUsername = Entry(lienzo, width=20)
        txtUsername.place(x=100, y=230)
        lblBiografia = Label(lienzo, text="Biografia: ")
        lblBiografia.place(x=240, y=110)
        txtBiografia = Text(lienzo, width=42, height=7)
        txtBiografia.place(x=240, y=132)
        # Neurotransmisores
        




        # Se cargan los datos si existen
        info = self.controladora.cargarInformacionDelPerfil()
        if info != []:
            txtNombreYApellido.insert(0, info[0])
            txtFechaDeNacimiento.insert(0, info[1])
            comboBoxGenero.set(info[2])
            txtEdad.insert(0, info[3])
            txtUsername.insert(0, info[4])
            txtBiografia.insert("1.0", info[5])

        # Se guarda la información para poder editarla mas tarde
        informacion = [txtNombreYApellido, txtFechaDeNacimiento, comboBoxGenero, txtEdad, txtUsername, txtBiografia]


        btnGuardar = Button(lienzo, text="Guardar", command= lambda : self.guardarInformacionPerfil(informacion))
        btnGuardar.place(x=300, y=450)



    def subInterfacePilaresDeLaFelicidad(self):
        """
        Se graficaran : Un grafico circular de la inversion de tu tiempo
        """
        graficarPilares = Toplevel()
        graficarPilares.geometry("800x600")
        graficarPilares.title("Asi estas gastando tu tiempo")
        lienzo = Canvas(graficarPilares, width=800, height=600)
        lienzo.place(x=0, y=0)
        lienzo.create_image(400, 300, image=self.imageIcoPersona)
        comboxAñosActividades = ttk.Combobox(lienzo, state="readonly", values=self.controladora.cargarAñosDeRegistroActividades())
        comboxAñosActividades.place(x=20, y=20)
        btnVer = Button(lienzo, text="Graficar", command=lambda: self.graficarPilaresDeLaFelicidad(lienzo, comboxAñosActividades.get()))
        btnVer.place(x=200, y=20)

        
    
        
    """Se declaran las subinterfaces TopLevel"""
    """Se declaran las subinterfaces TopLevel"""
    """Se declaran las subinterfaces TopLevel"""
    def guardarPaginaEnDiario(self, palabraMagica, texto):
        """
        La pagina del diario va a ser guardada  al final de en DIARIO/AÑO/estampa+palabraMagica.txt
        """
        if self.controladora.guardarPaginaDiario(palabraMagica, texto):
            self.ventanaEnmergenteDeAlerta('Aceptado.', 'Guardado con exito.')
        else:
            self.ventanaEnmergenteDeAlerta('Error Fatal', 'No puedo guardar esa mierda.')

    def cargarpaginaDeDiario(self, palabraMagica, cajaDeTexto):
        temp = self.controladora.cargarpaginaDeDiario(palabraMagica)
        if temp != None:
            if(len(temp.strip())>0):
                cajaDeTexto.delete("1.0", END)
                cajaDeTexto.insert("1.0", temp)
        else:
            self.ventanaEnmergenteDeAlerta('Error', 'No encontre ni mierda')


    def saveDreamDiaryPage(self, keyword, text):
        """
        Save a dream diary page in folder : DREAMS/YEAR/timestamp + keyword .txt
        """
        if self.controladora.saveDreamDiaryPage(keyword, text):
            self.ventanaEnmergenteDeAlerta('Aceptado.', 'Sueño guardado con exito.')
        else:
            self.ventanaEnmergenteDeAlerta('Error Fatal', 'No se hizo ni una puta mierda')

    def loadDreamPageDiary(self, keyword, textArea):
        temp = self.controladora.loadDreamDiarypage(keyword)

        if temp != None and temp != "":
            textArea.delete("1.0", END)
            textArea.insert("1.0", temp)
        else:
            self.ventanaEnmergenteDeAlerta('Error', 'No encontre ni mierda')


    def loadFullReader(self, _type=""):
        """
        Show a interactive window to serach all text write in a diary
        """
        t = Toplevel()
        t.title("Enciclopedia: "+_type)
        t.geometry("800x600")

        canvas = Canvas(t, width=800, height=600)
        canvas.place(x=0, y=0)


        # paint a mini pages
        lblTitles = [] # Save all titles 
        txtNotes = [] # Save all information
        
        miniPagesCounter = 0
        miniPagesAux_x = 0
        miniPagesAux_y = 0
        for _ in range(0, 6):
            if miniPagesAux_y > 2:
                miniPagesAux_y = 0
            
            if miniPagesCounter > 2:
                miniPagesAux_x = 1

            lblTitles.append(Label(canvas, text="txt"))
            lblTitles[miniPagesCounter].place(x=80+(miniPagesAux_x*350), y=50+(miniPagesAux_y*180))
            txtNotes.append(Text(canvas, width=36, height=8))
            txtNotes[miniPagesCounter].place(x=80+(miniPagesAux_x*350), y=80+(miniPagesAux_y*180))

            miniPagesAux_y = miniPagesAux_y + 1
            miniPagesCounter = miniPagesCounter + 1


        # Paint a line to separate
        canvas.create_line(0, 30, 800, 30)
        canvas.create_line(400, 30, 400, 600)

        # paint indicator
        lblPageIndicator = Label(canvas, text="Pages: 0/0")
        lblPageIndicator.place(x=720, y=6)

        # Control Btns
        btns = []
        btnsCounter = 0
        btnsText = [".", "#", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        
        if _type == "diary":
            # Paint letters to filter
            for i in btnsText:
                btns.append(Button(canvas, text=i))
                btns[btnsCounter].bind("<Button-1>", lambda key: self._filterDiaryFullReader(key.widget.cget('text'), lblTitles, txtNotes, lblPageIndicator))
                btns[btnsCounter].place(x=(22*btnsCounter)+4, y=2)
                btnsCounter = btnsCounter + 1
        

        if _type == "dreams":
            # Paint letters to filter
            for i in btnsText:
                btns.append(Button(canvas, text=i))
                btns[btnsCounter].bind("<Button-1>", lambda key: self._filterDreamsFullReader(key.widget.cget('text'), lblTitles, txtNotes, lblPageIndicator))
                btns[btnsCounter].place(x=(22*btnsCounter)+4, y=2)
                btnsCounter = btnsCounter + 1


        if _type == "notes":
            # Paint letters to filter
            for i in btnsText:
                btns.append(Button(canvas, text=i))
                btns[btnsCounter].bind("<Button-1>", lambda key: self._filterNotesFullReader(key.widget.cget('text'), lblTitles, txtNotes, lblPageIndicator))
                btns[btnsCounter].place(x=(22*btnsCounter)+4, y=2)
                btnsCounter = btnsCounter + 1

        btnNextInformacion = Button(canvas, text=">>", command=lambda : self._nextPagesInDiaryFullReader(lblTitles, txtNotes, lblPageIndicator))
        btnNextInformacion.place(x=760, y=300)
        btnPrevInformacion = Button(canvas, text="<<", command=lambda : self._PreviuosPagesInDiaryFullReader(lblTitles, txtNotes, lblPageIndicator))
        btnPrevInformacion.place(x=10, y=300)


        
    def _filterDiaryFullReader(self, filter, lblTitles, txtNotes, lblPageIndicator):
        self.allInfoDiaryPages = self.controladora.loadDiaryDataFilterByLetter(filter)
        self._refreshSixDiaryPages(lblTitles, txtNotes, lblPageIndicator)


    def _nextPagesInDiaryFullReader(self, lblTitles, txtNotes, lblPageIndicator):
        if self.diaryPaginatorController + 6 < len(self.allInfoDiaryPages):
            self.diaryPaginatorController = self.diaryPaginatorController + 6

            self._refreshSixDiaryPages(lblTitles, txtNotes, lblPageIndicator)


    def _PreviuosPagesInDiaryFullReader(self, lblTitles, txtNotes, lblPageIndicator):
        if self.diaryPaginatorController - 6 >= 0:
            self.diaryPaginatorController = self.diaryPaginatorController - 6

            self._refreshSixDiaryPages(lblTitles, txtNotes, lblPageIndicator)


    def _refreshSixDiaryPages(self, lblTitles, txtNotes, lblPageIndicator):
        if len(self.allInfoDiaryPages) > 0:
            # Show 6 pages
            for i in range(0, 6):
                try:
                    _title = self.allInfoDiaryPages[self.diaryPaginatorController+i]["title"]
                    _text = self.allInfoDiaryPages[self.diaryPaginatorController+i]["text"]
                    lblTitles[i]['text'] = _title
                    txtNotes[i].delete('1.0', END)
                    txtNotes[i].insert(END, _text)
                except:
                    lblTitles[i]['text'] = ""
                    txtNotes[i].delete('1.0', END)



        # Update indicator
        current_page = self.diaryPaginatorController/6
        current_page = round(current_page)
        total_pages = len(self.allInfoDiaryPages)/6
        total_pages = round(total_pages)
        lblPageIndicator['text'] = "Pages: " + str(current_page) + ":" + str(total_pages)


    def _filterDreamsFullReader(self, filter, lblTitles, txtNotes, lblPageIndicator):
        self.allInfoDiaryPages = self.controladora.loadDreamsDataFilterByLetter(filter)
        self._refreshSixDiaryPages(lblTitles, txtNotes, lblPageIndicator)


    def guardarNota(self, palabraMagica, texto):
        """
        las notas son como un diccionario:

        la nota se va a guardar en DATA/NOTAS/PalabraMagica.txt

        """
        if self.controladora.guardarNota(palabraMagica, texto):
            self.ventanaEnmergenteDeAlerta('Aceptado.', 'Guardado con exito.')
        else:
            self.ventanaEnmergenteDeAlerta('Error Fatal', 'No puedo guardar.')

    def _filterNotesFullReader(self, filter, lblTitles, txtNotes, lblPageIndicator):
        self.allInfoDiaryPages = self.controladora.loadNotesDataFilterByLetter(filter)
        self._refreshSixDiaryPages(lblTitles, txtNotes, lblPageIndicator)


    def guardarSentimiento(self):
        if self.controladora.guardarSentimiento(self.comboBoxSentimientosValor.get()):
            self.ventanaEnmergenteDeAlerta('Aceptado.', 'Guardado con exito.')
        else:
            self.ventanaEnmergenteDeAlerta('Error Fatal', 'No puedo guardar.')

    def registrarLogro(self, txtlogro):
        if len(txtlogro.strip()) > 0:
            if len(self.comboBoxAño.get()) > 0:
                if self.controladora.controladoraProcesamientoDeDatos.registrarLogroDeMiVida(self.comboBoxAño.get(), txtlogro):
                    self.ventanaEnmergenteDeAlerta('Enviado...', 'enviando a base de datos.')
                else:
                    self.ventanaEnmergenteDeAlerta('Error Faltal', 'No registre ni mierda')
            else:
                self.ventanaEnmergenteDeAlerta('Que Bestia!', 'Tienes que indicar un año')
        else:
            self.ventanaEnmergenteDeAlerta('Que Bestia!', 'Tienes que Escribir un logro')

    def registrarActividad(self, actividad):
        if len(actividad.strip()) > 0:
            if self.controladora.controladoraProcesamientoDeDatos.registrarActividad(actividad):
                self.ventanaEnmergenteDeAlerta('Epa', 'Esa vaina fue registrada')
            else:
                self.ventanaEnmergenteDeAlerta('Error', 'Alguna mierda paso.')
        else:
            self.ventanaEnmergenteDeAlerta('Error', 'Introduce una actividad')

    def savePeopleDescription(self, name, alias, description, qualification):
        if not self.validatesTxt(name):
            self.ventanaEnmergenteDeAlerta("Error Fatal", "Tiene que indicar el puto nombre")
        elif not self.validatesTxt(description):
            self.ventanaEnmergenteDeAlerta("Error Fatal", "Tiene que indicar una descripción")
        else:
            if self.controladora.savePeopleDescription(name, alias, description, qualification):
                self.ventanaEnmergenteDeAlerta("Exito", "Referencia guardada")
            else:
                self.ventanaEnmergenteDeAlerta("Error FAtal", "No pude guardar ni mierda")


    def guardarEconomia(self, conceptos, debe, haber):
        """
        Esto le entran 3 vectores de tipo tkinter.Entry[12]
        >Si debeHaber no tiene concepto no se guarda
        >Si el informe esta correcto es xq no hay errores
        """
        errorDeReporte = 0
        txtReporte = ""
        for i in range(0, 12):
            txtConcepto =  conceptos[i].get() + ";"
            txtDebe = str(debe[i].get()).strip() + ";"
            txtHaber = str(haber[i].get()).strip() + ";\n"

            if txtConcepto.strip() == ";":
                if txtDebe != ";" or txtHaber != ";\n":
                        errorDeReporte = errorDeReporte + 1
                        break
            else:
                # Se agrega el conepto al reporte
                txtReporte = txtReporte + txtConcepto

                # Si debe esta vacio se pone 0
                if txtDebe == ";":
                    txtDebe = "0;"

                # Si el haber esta vacio
                if txtHaber == ";\n":
                    txtHaber = "0;\n"
                try:
                    # se comprueba que el debe y el haber no esten vacios al mismo tiempo
                    if txtDebe == "0;" and txtHaber == "0;\n":
                        errorDeReporte = errorDeReporte + 1
                        break    
                    else:
                        # Se comprieba de que debe y haber sean enteros positivos
                        if not int(txtDebe.replace(";", '')) >= 0 and int(txtHaber.replace(";\n", ''))>=0:
                            errorDeReporte = errorDeReporte + 1
                            
                        # Todo esta bien se anexa al reporte
                        txtReporte = txtReporte + txtDebe + txtHaber
                except:
                    errorDeReporte = errorDeReporte + 1
                    break

        if errorDeReporte == 0:
            if self.controladora.controladoraProcesamientoDeDatos.guardarReporteEconomicoDebeHaber(txtReporte, self.comboBoxEconomiaDia.get(), self.comboBoxEconomiaMes.get()):
                self.controladora.saveUseWrite("economy")
                self.ventanaEnmergenteDeAlerta('$Acept', 'Reporte Guardado Con exito')
            else:
                self.ventanaEnmergenteDeAlerta('error', 'Esa Mierda no se pudo guardar')
        else:
            self.ventanaEnmergenteDeAlerta('Error', 'El reporte contiene errores')

    def cargarEconomia(self, concepto, debe, haber):
        """
        Este metodo depende de la controladora de datos
        Dependiendo del mes y dia se carga el reporte: No le veo senido a cargar reporte de años anteriores
        Si el repote existe se retorna el reporte en texto plano, si no existe se reporta nada
        cada renglon se corta y se guarda cada renglon en temp
        """
        reporte = self.controladora.controladoraProcesamientoDeDatos.cargarReporteEconomicoDebeHaber(self.comboBoxEconomiaDia.get(), self.comboBoxEconomiaMes.get())

        if reporte != None:
            """Se borra el reporte"""
            for i in range(0, 12):
                concepto[i].delete(0, END)
                debe[i].delete(0, END)
                haber[i].delete(0, END)

            """Se rellenan los resultados"""
            contador = 0
            for i in reporte.split("\n"):
                if str(i).strip() != "":
                    temp = i.split(";")
                    concepto[contador].insert(0, str(temp[0]))
                    debe[contador].insert(0, str(temp[1]))
                    haber[contador].insert(0, str(temp[2]))
                    contador = contador + 1
        else:
            self.ventanaEnmergenteDeAlerta('Error', 'Yo no encontre ni mierda')


    def guardarInversionTiempoDiaria(self, hr, informacion):
        """
        Entran: hr=[6am, 7am, 8pm...]
                informacion = [actividad.get(), actividad.get(), actividad.get()...]

        Se procesa informacion solo se guarda si todas las horas estan registradas//no hay errores
        """
        errores = 0
        reporte = []
        for i in range(0, 24):
            if informacion[i].get() != "":
                reporte.append(hr[i]['text']+":"+informacion[i].get())
            else:
                errores = errores + 1
            
        if errores == 0:
            if self.controladora.guardarDistribucionTiempoDiario(reporte):
                self.ventanaEnmergenteDeAlerta('Aceptado', 'Guardado con exito')
            else:
                self.ventanaEnmergenteDeAlerta('Error', 'No se pudo guardar esa mierda')
        else:
            self.ventanaEnmergenteDeAlerta('Error', 'Faltan valores por asignar')

    def guardarHorario(self, lunes, martes, miercoles, jueves, viernes, sabado, domingo):
        txt = self.informacionSemanalHorario(lunes, martes, miercoles, jueves, viernes, sabado, domingo)

        if self.controladora.guardarHorario(txt):
            self.ventanaEnmergenteDeAlerta('Acept!', 'Guardado con exito')
        else:
            self.ventanaEnmergenteDeAlerta('Error', 'Paso alguna mierda')

    def cargarHorario(self, lunes, martes, miercoles, jueves, viernes, sabado, domingo):
        """
        Se carga la informacion desde la controladora.
        LMMJVSD
        LMMJVSD
        LMMJVSD
        ...
        Luego se trata la matrix de actividades y se asigna en cargarHorarioAsignarActividad
        """
        actividadesDeHorario = self.controladora.controladoraCarpetas.cargarActividades() # Controlar el indice del combo box y que no enten piratas
        informacion = self.controladora.cargarHorario() # Se carga la informacion del horario


        contadorHora = 0 # 
        if informacion != None:
            # Se rellena el horario
            for i in informacion.split("\n"):
                
                actividad = i.split(";")
                
                if len(actividad) == 7:
                    self._cargarActividadHorario(actividad[0], lunes, contadorHora, actividadesDeHorario)
                    self._cargarActividadHorario(actividad[1], martes, contadorHora, actividadesDeHorario)
                    self._cargarActividadHorario(actividad[2], miercoles, contadorHora, actividadesDeHorario)
                    self._cargarActividadHorario(actividad[3], jueves, contadorHora, actividadesDeHorario)
                    self._cargarActividadHorario(actividad[4], viernes, contadorHora, actividadesDeHorario)
                    self._cargarActividadHorario(actividad[5], sabado, contadorHora, actividadesDeHorario)
                    self._cargarActividadHorario(actividad[6], domingo, contadorHora, actividadesDeHorario)

                contadorHora = contadorHora + 1
        else:
            self.ventanaEnmergenteDeAlerta('Error', 'Yo No encontre ni mierda')

    def _cargarActividadHorario(self, actividad, dia, hora, controlActividades):
        """
        Actividad : dormer, comer, trabajar .... tiene que estar en control actividades
        dia = Combolunes[], Combomartes[] ...
        hora = 1pm, 2pm, 3pm, 4pm,  ...  Ojo: las 0 son las 7 am
        controlactividades => Es el registro de todas las actividades para que no entren valores piratas

        Si la actividad esta vacia se limpia el comboBox
        Si hay una actividad se verifica que este registrada
        Si la actividad no esta registrada se limpia todo
        """
        if actividad != "":
            if actividad in controlActividades:
                dia[hora].set(actividad)
            else:
                dia[hora].set('')
        else:
            dia[hora].set('')


    def limpiarHorario(self, lunes, martes, miercoles, jueves, viernes, sabado, domingo):
        for i in range(0, 24):
            lunes[i].set('')
            martes[i].set('')
            miercoles[i].set('')
            jueves[i].set('')
            viernes[i].set('')
            sabado[i].set('')
            domingo[i].set('')
        

    """GRAFICAS"""
    """GRAFICAS"""
    """GRAFICAS"""
    def graficarAñoSentimiento(self):
        if self.comboBoxAño.get() != "":
            dataSentimientos = self.controladora.procesarDatosSentimientos(self.comboBoxAño.get())
            self.mostrarGraficaSentimientos(dataSentimientos)
        else:
            self.ventanaEnmergenteDeAlerta('Error', 'Pedazo de bestia ingresa el año')

    def mostrarGraficaSentimientos(self, dataSentimientos):
        self.controladora.vizualizeFeelingsData(dataSentimientos)


    def graficaCircularDelHorario(self, tela, lunes, martes, miercoles, jueves, viernes, sabado, domingo):
        """Se recolecta la informacion"""
        informacion = self.informacionSemanal(lunes, martes, miercoles, jueves, viernes, sabado, domingo)
        # Se procesa la informacion para sacar los porcentajes
        dataSemanal = self.controladora.procesarInformacionSemanal(informacion)

        
        # Se borran los valores anteriores
        tela.delete("graficoCircular")

        # Se pinta el circulo mayor
        tela.create_oval(900, 40, 1200, 330, tags="graficoCircular", width=1)

        anguloInicio = 0
        anguloFin = 0

        # Solo se pintan los valores que tengan algun porcentajes
        """
        Un circulo tienen 360 grados:
        si duermo el 20% del tiempo pues inicio = 0 y fin = 72
        si como el 10% del tiempo pues inicio = 72 y fin = 36
        El color que lleva lo escogio la controladora
        controladora.coloresParaGraficoCircular
        """
        contador = 0
        for i in dataSemanal:
            if dataSemanal[i] != 0:
                anguloFin = 360*(dataSemanal[i]/100)

                # Se pinta el arco
                tela.create_arc(900, 40, 1200, 330, width=1, tags="graficoCircular", fill=self.controladora.coloresParaGraficoCircular[contador], start=anguloInicio, extent=anguloFin)
        
                # Se actualiza el nuevo inicio
                anguloInicio = anguloFin
                contador = contador + 1


    def graficaPeridoEconomica(self, tela):
        if self.comboBoxVistaEconomica.get() != "":
            """
            Deacuerdo año tipo de vista : Año o un mes en particular se pide esa informacion para graficar
            
            1 -> Se divide h entre Ingresos, egresos
            2 -> El 100% sera w
            3 -> La controladora.procesadoraDeDatos 
            4 -> se muestra la informacion con labels
            
            """
            data = self.controladora.retornarInformacionEconomica(self.comboBoxVistaEconomica.get())

            tela.delete("economia") # Se limpia la tela

            h = int(tela['height'])
            w = int(tela['width'])

            total = 0 # Guardata ingresos+abs(egresos)
            totalIngresos = 0 # Saldos positivos
            totalEgresos = 0 # Saldos negativos

             # Se calculan los ingresos y egresos mas importantes
            topIngresos = ['', 0]
            topEgresos = ['', 0]

            for i in data:
                if data[i] >= 0 and topIngresos[1] < data[i]: # Se calculan ingresos mas importantes
                    topIngresos = [i, data[i]]

                if data[i] < 0 and -1*topEgresos[1] < -1*(data[i]): # Se calculan Egresos mas importantes
                    topEgresos = [i, data[i]]

                if data[i] >0: # Se calculan totales
                    totalIngresos = totalIngresos + data[i]
                else:
                    totalEgresos = totalEgresos + data[i]


            # Se calcula el total
            total = totalIngresos + ((totalEgresos)*-1)
            # Se calculan los porcentajes de ingresos y egresos
            if total != 0:
                porcentajeIngresos = totalIngresos/total
                porcentajeEgresos = ((totalEgresos)*-1)/total
            else:
                porcentajeIngresos = 0
                porcentajeEgresos = 0
            
            # Se pone la graficas de barra principales ingresos, egresos
        
            #Se calculan las medidas de la grafica de ingresos
            x0 = 0 + 2
            y0 = 0 + 2
            x1 = w*porcentajeIngresos + 2
            y1 = h/10

            tela.create_rectangle(x0, y0, x1, y1, fill="green", tags="economia")
            # Se calculan las medidas de la grafica de egresos
            x0 = 0 + 2
            y0 = (h/2) + 2
            x1 = w*porcentajeEgresos + 2
            y1 = (h/2) + (h/10)
            tela.create_rectangle(x0, y0, x1, y1, fill="red", tags="economia")

            # Se pone la linea divisoria e ingresos, ingresos
            tela.create_text(w/7, 20, text="Ingresos: $" + str(totalIngresos), tags="economia")
            tela.create_text(w/7, (h/2)+20, text="Egresos: $" + str(totalEgresos), tags="economia")
            tela.create_line(0, h/2, w, h/2)

            # Se ponen los labels de ingresos y egresos mas impotantes
            tela.create_text(w/7, (h/10)+20, text=str(topIngresos), tags="economia")
            tela.create_text(w/7, (h/2)+(h/10)+20, text=str(topEgresos), tags="economia")
            # Se pone una linea divisoria de los top
            tela.create_line(0, (h/10)+35, w, (h/10)+35, tags="economia") 
            tela.create_line(0, (h/2)+(h/10)+35, w, (h/2)+(h/10)+35, tags="economia")
            # Se procede a mostrar una matrix de 3x3 con algunos de los ingresos y egresos
            contadorIngresos = 0 # Solo se mostraran 9 ingresos
            contaSaltoLineaIngresos = 0 # Cada 3 ingresos hay que hacer un salto de linea 
            posxI = w/7 # x donde se pinta un ingreso
            posyI = h/4 # y donde se pinta un igreso
            contadorEgresos = 0 # Solo se mostraran 9 egresos
            contaSaltoLineaEgresos = 0 # Cada 3 Egresos hay que poner un salto de linea
            posxE = w/7 # x donde se pinta un egreso
            posyE = h/1.35 # y donde se pinta un egreso 
            # Se va a pintar una matrix por ello se debe de dividir la pantalla
            kx = w/3
            ky = h/3

            for i in data:
                if int(data[i]) >= 0:
                    # Si hay menos de 9 ingresos pintelos
                    if contadorIngresos < 9:
                        tela.create_text((posxI), (posyI), text=str(i)+":"+str(data[i]), tags="economia")
                        posxI = posxI + kx

                        if contaSaltoLineaIngresos < 2:
                            contaSaltoLineaIngresos = contaSaltoLineaIngresos + 1
                        else:
                            contaSaltoLineaIngresos = 0
                            posxI = w/7 # Se reinicia el controlador ponedor x
                            posyI = posyI + 30 # Se aunmenta un poquito en y

                        contadorIngresos = contadorIngresos + 1
                else:
                    if contadorEgresos <= 11:
                        tela.create_text((posxE), (posyE), text=str(i)+":"+str(data[i]), tags="economia")
                        posxE = posxE + kx

                        if contaSaltoLineaEgresos < 2:
                            contaSaltoLineaEgresos = contaSaltoLineaEgresos + 1
                        else:
                            contaSaltoLineaEgresos = 0
                            posxE = w/7 # Se reinicia el controlador ponedor x
                            posyE = posyE + 30 # Se aunmenta un poquito en y

                        contadorEgresos = contadorEgresos + 1
                    
            

    def graficaEstadoDeCajas(self, tela):
        """
        1 -> Se pide la informacion de la caja menor.
        2 -> Se divide la tela entre el numero de datos
        3 -> Se grafican los puntos en azul
        4 -> Se pide la informacion de la caja mayor
        5 -> Se divide la tela entre el numero de datos
        6 -> Se grafican los puntos en verde
        """
        tela.delete("estadocajas")
        # Se toman la informacion de largo y ancho del tablero
        h = int(tela['height'])
        w = int(tela['width'])

        # Se pide la informacion a graficar de la caja menor
        info = self.controladora.cargarRecordEstadoCajaMenor()
        # Si hay informacion de la caja menor grafiquela
        if len(info) > 0:
            # Se busca el valor mayor
            maxY = 0
            for i in info:
                if i > maxY:
                    maxY = i

            # Se grafican 3 labes cero, montoMedio, MaximoMonto
            tela.create_text(20, h-10, fill="blue", text="$0.0", tags="estadocajas")
            tela.create_text(20, h/2, fill="blue", text="$"+str(maxY/2), tags="estadocajas")
            tela.create_text(20, 20, fill="blue", text="$"+str(maxY), tags="estadocajas")


            # Distancia de los puntos
            d = w / len(info)

            # Se procede a graficar los puntos
            for i in range(0, len(info)-1):
                x0 = d*i
                y0 = h * (1-(info[i]/maxY))
                x1 = d*(i+1)
                y1 = h * (1-(info[i+1]/maxY))
                tela.create_line(x0, y0, x1, y1, fill="blue", tags="estadocajas")


        # Se pide la informacion a graficar >> Caja Mayor
        info = self.controladora.cargarRecordEstadoCajaMayor()
        if len(info) > 0:
            # Se busca el valor mayor
            maxY = 0
            for i in info:
                if i > maxY:
                    maxY = i

            # Se grafican 3 labes cero, montoMedio, MaximoMonto
            tela.create_text(w*0.9, h-10, fill="green", text="$0.0", tags="estadocajas")
            tela.create_text(w*0.9, h/2, fill="green", text="$"+str(maxY/2), tags="estadocajas")
            tela.create_text(w*0.9, 20, fill="green", text="$"+str(maxY), tags="estadocajas")

            # Se procede a graficar los puntos
            for i in range(0, len(info)-1):
                x0 = d*i
                y0 = h * (1-(info[i]/maxY))
                x1 = d*(i+1)
                y1 = h * (1-(info[i+1]/maxY))
                tela.create_line(x0, y0, x1, y1, fill="green", tags="estadocajas")


    def graficarTiempoDeVida(self, tela, añoNacimiento):
        """
        Aqui se grafica el tiempo transcurrido de vida contrastado con el tiempo que podrias vivir.
        """
        tela.delete("life")
        y = añoNacimiento

        w = int(tela['width'])
        h = int(tela['height'])

        # Se pinta el rectangulo principal
        tela.create_rectangle((w*0.1), (h*0.15), (w-10), (h-10), fill="white", tags="life")

        # Se pintan los años
        for i in range(0, 20):
            tela.create_text(30, (h*0.15+(i*20))+2, text=str(y), tags="life")
            y = y + 5

        # Segun el año cursado se calcula el %
        """
        el tiempo de vida del humano del futuro promedio sera 100 años
        tiempo vida = 100 - (añoActual - añoNacimiento)
        """
        t = 100 - (self.controladora.queAñoEs() - añoNacimiento)

        # Necesito saber cual es el grosor del rectangulo
        dy = (h-10) - (h*0.15)
        l = dy/100

        # Se pinta en rojo el tiempo trascurrido
        for i in range(0, (100-t)-1):
            x0 = w*0.1
            y0 = (h*0.15)+(i*l)
            x1 = w-10
            y1 = y0+2
            tela.create_rectangle((x0), (y0), (x1), (y1), fill="red", tags="life")

        # Se pinta en rojo el trozo del a+o actual transcurrido
        m = self.controladora.queMesEs()/12
        tela.create_rectangle((x0), (h*0.15)+((i+1)*l), x0+(x1*m), ((h*0.15)+((i+1)*l))+2, fill="red", tags="life")
        # Se pinta un rectangulo amarillo para saber el punto en que estamos
        tela.create_rectangle(x0+(x1*m), (h*0.15)+((i+1)*l), x0+(x1*m)+5, ((h*0.15)+((i+1)*l))+5, fill="yellow", tags="life")
        # Se continua con una linea verde
        tela.create_rectangle(x0+(x1*m)+5, (h*0.15)+((i+1)*l), w-10, ((h*0.15)+((i+1)*l))+2, fill="green", tags="life")

       
        # Se pintan los años venideros
        for i in range((100-t), 100 ):
            x0 = w*0.1
            y0 = (h*0.15)+(i*l)
            x1 = w-10
            y1 = y0+2
            tela.create_rectangle((x0), (y0), (x1), (y1), fill="green", tags="life")

    def graficarPilaresDeLaFelicidad(self, lienzo, año):
        """
        Se grafican los datos de manera porcentual circular
        """
        if año != "":
            lienzo.delete("inversionTiempo")
            # Se grafican los textos de los pilares
            data = self.controladora.cargarPorcentajesDeActividades(año)

            maxX = int(lienzo['width'])
            maxY = int(lienzo['height'])
            centroPantalla = [maxX/2, maxY/2]
            radio = maxY*0.45
            posx = 0
            posy = 0

            if len(data) != 0: 
                separacion = (2 * 3.1416)/len(data)
            else:
                separacion = 0

            contador = 0 # Para saber en que angulo pintar
            
            for i in data:
                # Para el texto y porcentajes
                x = centroPantalla[0] + (radio * math.cos(contador*separacion)) # Texto
                x0 = centroPantalla[0] + ((radio*0.7) * math.cos(contador*separacion)) # % Texto
                y = centroPantalla[1] - (radio * math.sin(contador*separacion)) # Texto
                y0 = centroPantalla[1] - ((radio*0.7) * math.sin(contador*separacion)) # % Texto

                # Para Graficos de barras base roja
                xa = centroPantalla[0] + ((radio*0.15) * math.cos(contador*separacion))
                ya = centroPantalla[1] - ((radio*0.15) * math.sin(contador*separacion))
                xb = centroPantalla[0] + ((radio*0.6) * math.cos(contador*separacion))
                yb = centroPantalla[1] - ((radio*0.6) * math.sin(contador*separacion))
                # Para Graficos de barras base verde
                xc = centroPantalla[0] + ((radio*0.6*(0.25+data[i])) * math.cos(contador*separacion))
                yc = centroPantalla[1] - ((radio*0.6*(0.25+data[i])) * math.sin(contador*separacion))

                lienzo.create_text(x, y, text=i, tags="inversionTiempo") # Texto informativo
                porcentaje = round((data[i] * 100), 3) 
                lienzo.create_text(x0, y0, text=str(porcentaje)+"%", tags="inversionTiempo") # Texto porcentaje
                lienzo.create_line(xa, ya, xb, yb, width=3, fill="red", tags="inversionTiempo") # Barra roja
                lienzo.create_line(xc, yc, xa, ya, width=4, fill="green", tags="inversionTiempo") # Barra verde
                contador = contador + 1
                

    """GRAFICAS"""
    """GRAFICAS"""
    """GRAFICAS"""


    """Metodos de refresco de comboBox"""
    def refrescarDias(self, mes):
        dias = []
        for i in range(1, self.controladora.tiempo.diasDeMes(mes-1)+1):
            dias.append(i)
        return dias
    def _refrescarDias(self, mes, comboBoxDia):
        comboBoxDia['values'] = self.refrescarDias(mes+1)

    def informacionSemanal(self, lunes, martes, miercoles, jueves, viernes, sabado, domingo):
        """
        Dada la informacion del horario se almacena la informacion semanal en informacion
        Esto es para graficas y estadisticas
        """

        informacion = []
        informacion = self.informacionDaria(lunes) + self.informacionDaria(martes) + self.informacionDaria(miercoles) + self.informacionDaria(jueves) + self.informacionDaria(viernes) + self.informacionDaria(sabado) + self.informacionDaria(domingo)
        return informacion


    def informacionDaria(self, dia):
        """
        Se almacena lo que hace cada hora en informacion
        para graficas y estadisticas
        """
        informacion = []

        for i in range(0 , 24):
            if dia[i].get() != "":
                informacion.append(dia[i].get())

        return informacion

    def informacionSemanalHorario(self, lunes, martes, miercoles, jueves, viernes, sabado, domingo):
        """
        Entran  todos los dias de la semana y se garda en informacion
        Esto es para guardar el horario en DATA/DT/HORARIO [backup y save]
        """
        horario = ""

        for i in range(0, 24):
            horario = horario + lunes[i].get() + ";" + martes[i].get() + ";" + miercoles[i].get() + ";" + jueves[i].get() + ";" + viernes[i].get() + ";" + sabado[i].get() + ";" + domingo[i].get() + "\n"

        return horario

    def crearCarpetaDeDeciciones(self, txt):
        if str(txt).strip() != "":
            if self.controladora.crearCarpetaArbolDeDeciciones(txt):
                self.ventanaEnmergenteDeAlerta('Aceptado', 'Creado')
                # Se procede a generarElArbol
                self.controladora.arbolDeDecicionListo = True # Se indica que el arbol esta listo para trabajar

            else:
                self.ventanaEnmergenteDeAlerta('Error', 'Ya existe?')
        else:
            self.ventanaEnmergenteDeAlerta('Error', 'Para crear un árbol de decición introduzca nombre')

    def guardarEstadoEnCarpetaDeDeciciones(self, info):
        """
        info es un vector
        0 -> ID padre
        1 -> ID nodo
        3 -> Titulo
        4 -> Descripcion
        """
        if self.controladora.arbolDeDecicionEstaListo():
            self.controladora.agregarNodoAlArbolDeDecion(info)
            self.ventanaEnmergenteDeAlerta("Exito", "Guardado con exito")
        else:
            self.ventanaEnmergenteDeAlerta("Error Fatal", "esa puta madre se chingo")

    def guardarMontoCajaMayor(self, monto, lienzo):
        if self.controladora.guardarEstadoCajaMayor(monto):
            self.graficaEstadoDeCajas(lienzo)
            self.ventanaEnmergenteDeAlerta("Exito", "Monto Actualizado")
        else:
            self.ventanaEnmergenteDeAlerta("Error", "Error Fatal Alguna Mierda Esta Mal")

    def guardarMontoCajaMenor(self, monto, lienzo):
        if self.controladora.guardarEstadoCajaMenor(monto):
            self.graficaEstadoDeCajas(lienzo)
            self.ventanaEnmergenteDeAlerta("Exito", "Monto Actualizado")
        else:
            self.ventanaEnmergenteDeAlerta("Error", "Error Fatal Alguna Mierda Esta Mal")

    def guardarInformacionPerfil(self, informacion):
        """
        Se guardaran los datos ingresados en PERFIL
        info = [txtNombreYApellido, txtFechaDeNacimiento, comboBoxGenero, txtEdad, txtUsername, txtBiografia]
        """
        nomApe = informacion[0].get()
        naci = informacion[1].get()
        sexo = informacion[2].get()
        edad = informacion[3].get()
        username = informacion[4].get()
        txtBiografia = informacion[5].get("1.0", END)
        
        informacion=[nomApe, naci, sexo, edad, username, txtBiografia]

        if self.controladora.guardarInformacionPerfil(informacion):
            self.ventanaEnmergenteDeAlerta("Exito", "Información almacenada.")
        else:
            self.ventanaEnmergenteDeAlerta("Error", "Algo malo ha pasado y no se pudo guardar la info")

    """
    AYUDA
    AYUDA
    AYUDA
    """
    def linkManualDelUsuario(self):
        """
        Se in voca la ventana de emergencia con el link del pdf del manual
        """
        link = "https://github.com/felipedelosh/DiarioPersonal/blob/master/RECURSOS/manual/Manual%20del%20Usuario.pdf"
        self.ventanaEnmergenteDeAlerta("Manual del usuario", link)

    def verLasPisibilidades(self):
        """
        Se muestran las posibilidades
        """
        data = self.controladora.retornarListadoDePosibilidades()
        self.ventanaEnmergenteDeAlerta("Listado de posibilidades", data)

    """
    END AYUDA
    END AYUDA
    END AYUDA
    """

    """FEMPUTADORA"""
    """FEMPUTADORA"""
    """FEMPUTADORA"""

    def _enterTXTinFemputadora(self, event, textArea, txtMachineOutput):
        txt = textArea.get()

        if txt.strip() != "":
            if event.keysym == "Return":
                self.controladora.userInputTXT(txt)
                self._clearTXTinFemputadora(textArea)
                self.updateChatHistorial(txtMachineOutput)


    def _clearTXTinFemputadora(self, textArea):
        textArea.delete(0, END)


    def updateChatHistorial(self, txtMachineOutput):
        txtMachineOutput.delete("1.0", "end")
        txtMachineOutput.insert(END, self.controladora.getFemputadoraChatHistorial())
        txtMachineOutput.see(END)

        
    """END FEMPUTADORA"""
    """END FEMPUTADORA"""
    """END FEMPUTADORA"""

    def validatesTxt(self, txt):
        """
        Enter a str and return is valid
        """
        return txt.strip() != "" and "\"" not in txt

    
thl = TimeHackingLoko()
