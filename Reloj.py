"""Escribir una clase que represente un Reloj que señale la hora, el minuto y el segundo.
Podemos poner por defecto los parámetros a 0:0:0 o pasarle la hora, los minutos y los
segundos.
○ Los atributos serán tres enteros: para la hora, los minutos y los segundos.
○ Existirá un método que da la hora, que se llamará dame_hora() y la devolverá como
un objeto string.
○ La hora, los minutos y los segundos serán representados en todos los casos con
valores del tipo int. No obstante, se comprobarán los rangos adecuados (p.e. no
poner hora 35 horas)."""

class Reloj(object):
    hora = 0
    minuto = 0
    segundo = 0

def set__hora(self, hora=0, minuto=0, segundo=0):
    self.hora = hora
    self.minuto = minuto
    self.segundo = segundo

def comprobar(self, hora, minuto, segundo):
    comprobar = False

while comprobar == False:
    hora = int(input("dame la hora"))
    minuto = int(input("dame la minuto"))
    segundo = int(input("dame la segundo"))

if 0< hora < 25 and 0<minuto<60 and 0<segundo<60:
        return False
    else:
        return True

def set_hora(self, hora, minutos, segundos):
    self.hora = hora
    self.minutos = minutos
    self.segundos = segundos