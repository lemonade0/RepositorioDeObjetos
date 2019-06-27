"""
Crea una clase que se llame Persona, tendrá edad y nombre y podrá correr, saltar y
caminar. Crea a Esteban como objeto de la clase Persona y añadele las propiedades
correspondientes y los cuando llame a los métodos estos indicarán en una frase que puede hacer
(correr, saltar...).
"""
class Persona(object):
    edad = "20"
    nombre = "La Pepi"

    def correr(self):
        return ("Vamos a correr.")

    def saltar(self):
        return ("Saltar de una linea a otra.")

    def caminar(self):
        return("En el camino vamos todos.")


