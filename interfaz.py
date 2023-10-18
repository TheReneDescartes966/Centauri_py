from tkinter import *
from tkinter import ttk

def hacer_click():
 try:
  _valorX = int(entrada_textoX.get())
  printerx.config(text=_valorX)
  _valorY = int(entrada_textoY.get())
  printery.config(text=_valorY)
  _valorZ = int(entrada_textoZ.get())
  printerz.config(text=_valorZ)
  etiqueta.config(text=" ")

 except ValueError:
  etiqueta.config(text="Introduce un numero!")


#TITULO DE LA VENTANA
app = Tk()
app.title("CENTAURI")

#Ventana Principal
vp = Frame(app)
vp.grid(column=0, row=0, padx=(10,10), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)

etiquetaX = Label(vp, text="X")
etiquetaX.grid(column=3, row=2, sticky=(W,E))

etiquetaY = Label(vp, text="Y")
etiquetaY.grid(column=4, row=2, sticky=(W,E))

etiquetaZ = Label(vp, text="Z")
etiquetaZ.grid(column=5, row=2, sticky=(W,E))

etiqueta = Label(vp, text="")
etiqueta.grid(column=4, row=3, sticky=(W,E))


boton = Button(vp, text="OK!", command=hacer_click)
boton.grid(column=1, row=1)

valorX = ""
entrada_textoX = Entry(vp, width=5, textvariable=valorX)
entrada_textoX.grid(column=3, row=1)

valorY = ""
entrada_textoY = Entry(vp, width=5, textvariable=valorY)
entrada_textoY.grid(column=4, row=1)

valorZ = ""
entrada_textoZ = Entry(vp, width=5, textvariable=valorZ)
entrada_textoZ.grid(column=5, row=1)

printerx = Label(vp, text=valorX)
printerx.grid(column=3, row=5, sticky=(W,E))

printery = Label(vp, text=valorY)
printery.grid(column=4, row=5, sticky=(W,E))

printerz = Label(vp, text=valorZ)
printerz.grid(column=5, row=5, sticky=(W,E))


#orientacion
def clicks():
 try:
  _valorR = int(entrada_textoR.get())
  printerR.config(text=_valorR)
  _valorP = int(entrada_textoP.get())
  printerP.config(text=_valorP)
  _valorYW = int(entrada_textoYW.get())
  printerYW.config(text=_valorYW)
  etiqueta2.config(text=" ")

 except ValueError:
  etiqueta2.config(text="Introduce un numero!")


etiquetaR = Label(vp, text="R")
etiquetaR.grid(column=9, row=2, sticky=(W,E))

etiquetaP = Label(vp, text="P")
etiquetaP.grid(column=10, row=2, sticky=(W,E))

etiquetaYW = Label(vp, text="YW")
etiquetaYW.grid(column=11, row=2, sticky=(W,E))

etiqueta2 = Label(vp, text="")
etiqueta2.grid(column=10, row=3, sticky=(W,E))


boton2 = Button(vp, text="OK!", command=clicks)
boton2.grid(column=6, row=1)

valorR= ""
entrada_textoR = Entry(vp, width=5, textvariable=valorR)
entrada_textoR.grid(column=9, row=1)

valorP = ""
entrada_textoP = Entry(vp, width=5, textvariable=valorP)
entrada_textoP.grid(column=10, row=1)

valorYW = ""
entrada_textoYW = Entry(vp, width=5, textvariable=valorYW)
entrada_textoYW.grid(column=11, row=1)

printerR = Label(vp, text=valorR)
printerR.grid(column=9, row=5, sticky=(W,E))

printerP = Label(vp, text=valorP)
printerP.grid(column=10, row=5, sticky=(W,E))

printerYW = Label(vp, text=valorYW)
printerYW.grid(column=11, row=5, sticky=(W,E))


app.mainloop() 