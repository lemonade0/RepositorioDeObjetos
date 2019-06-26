
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
    pass
class Dedo(object):
    longitud = ""
    forma = ""
    color = ""
class Pie(object):
    forma = ""
    color = ""
    dedos = Dedo()
# NuevoObjeto sí hereda de otra clase: Objeto
class NuevoObjeto(Objeto):
    pie = Pie()
def saltar(self):
    pass