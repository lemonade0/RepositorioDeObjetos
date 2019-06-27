# -*- coding: utf-8 -*-
from PruebaClase import *
from Empleado import *
from Factura import *
from Persona import *
from Reloj import *

et = Objeto()
print(et.color)
print(et.tamanio)
print (et.aspecto)
et.color = "rosa"
print (et.color)

#objeto = MiClase()
#print(objeto.propiedad)
#objeto.otra_propiedad = "Nuevo valor"
#variable = objeto.metodo()
#print(variable)
#print(objeto.otro_metodo())

objeto = NuevoObjeto()
print(objeto.color)
objeto.color = "Blue"

variable = objeto.pie.amputar()
print(variable)

#Llamada a clase ejercicio 1

# Llame del archivo Empleado

empleado1 = Empleado("Francisco", 30000)
print(empleado1.getnombre())
empleado1.setnombre("Francisco José")
print(empleado1.getnombre(), ",", empleado1.getsalario())

#llame del archivo Factura
compra1 = Factura(12, 110)
print(compra1.unidad)
print(compra1.unidad)
print(compra1.a_pagar(),"euros")
#print(Factura.__tasa) #Error:



esteban = Persona()

print(esteban.saltar())


#print(Reloj.hora,Reloj.minuto,Reloj.segundo)

hora = int(input("dame la hora :" ))
if hora < 0 or hora > 24:
    print("Parametro de error en la hora")
minuto = int(input("dame los minutos :"))
if minuto < 0 or minuto > 59:
    print("Parametro de error en la minutos")
segundos = int(input("dame los segundos :"))
if segundos < 0 or segundos > 59:
    print("Parametro de error en la segundos")

print( "Son las ",hora,"horas",minuto,"minutos y", segundos,"segundos")
