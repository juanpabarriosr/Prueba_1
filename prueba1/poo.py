'''
Created on 3 oct. 2017

@author: Juan
'''
class Humano:
    def __init__(self,edad):
        self.edad = edad
       # print "soy un nuevo objeto"
        
    def hablar(self,mensaje):
        print mensaje
        
class IngSistemas(Humano):
    def __init__(self):
        print 'Hola init sist'
    
    def programar(self,lenguaje):  
        print 'Voy a programar en ', lenguaje
        
class LicDerecho(Humano):
    def estuadiarCaso(self,de):
        print 'Debo estudiar el caso de ', de


pedro = IngSistemas(26)
print(pedro.edad)
raul = LicDerecho(27)

pedro.programar('Python')
raul.estuadiarCaso('Pedro')

pedro.hablar('Hola')
raul.hablar('Hola Pedro')



 #   
    