
# -*- coding: utf-8 -*-

class Antena():
    color = ""
    longitud = ""
class Pelo():
    color = ""
    textura = ""
class Ojo():
    forma = ""
    color = ""
    tamanio = ""
class Objeto():
    color = ""
    tamanio = ""
    aspecto = ""
    antenas = Antena() # propiedad compuesta por el objeto objeto Antena
    ojos = Ojo() # propiedad compuesta por el objeto objeto Ojo
    pelos = Pelo() # propiedad compuesta por el objeto objeto Pelo

class Objeto():
    color = "verde"
    tamanio = "grande"
    aspecto = "feo"
    antenas = Antena()
    ojos = Ojo()
    pelos = Pelo()
def flotar(self):
    print("12")

    #----------------------------------

class Antena(object):
    color = ""
    longitud = ""
class Pelo(object):
    color = ""
    textura = ""
class Ojo(object):
    forma = ""
    color = ""
    tamanio = ""
class Objeto(object):
    color = ""
    tamanio = ""
    aspecto = ""
    antenas = Antena()
    ojos = Ojo()
    pelos = Pelo()
def flotar(self):
    return (12)

class Dedo(object):
    longitud = "12"
    forma = "15"
    color = "11"

class Pie(object):
    forma = "144"
    color = "99"
    dedos = Dedo()
    def amputar(self_):
        return ("te ha cortado un pie")

# NuevoObjeto sí hereda de otra clase: Objeto
class NuevoObjeto(Objeto):
    pie = Pie()
def saltar(self):
    pass