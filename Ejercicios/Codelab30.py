from abc import ABC, abstractmethod


class Sucesion (ABC):
    def __init__ (self , primero, num_elementos):
        self ._primero = primero
        self ._num_elementos = num_elementos

    @property
    def num_elementos (self ):
        return self ._num_elementos

    @property
    def primero (self ):
        return self ._primero

    @abstractmethod
    def get_elemento (self , num_elemento):
        pass

    @abstractmethod
    def calcula_suma (self ):
        pass

    def __str__ (self ):
        return str([self .get_elemento(i) for i in range (1, self .num_elementos + 1)])

    class ProgresionGeometrica (Sucesion):

        def __init__ (self , primero, num_elementos, razon):
            super ().__init__ (primero, num_elementos)
            self ._razon = razon

    @property
    def razon (self ):
        return self ._razon

    def get_elemento (self , num_elemento):
        if self .num_elementos < num_elemento:
            num_elemento = self .num_elementos
        return self .primero * pow(self .razon, num_elemento - 1)

    def calcula_suma (self ):
        return (self .primero * ( pow(self .razon, self .num_elementos) - 1)) / ( self .razon - 1)

class ProgresionAritmetica (Sucesion):
    def __init__ (self , primero, num_elementos, diferencia):
        super ().__init__ (primero, num_elementos)
        self ._diferencia = diferencia

    @property
    def diferencia (self ):
        return self ._diferencia

    def get_elemento (self , num_elemento):
        if self .num_elementos < num_elemento:
            num_elemento = self .num_elementos
        return self .primero + (num_elemento - 1) * self .diferencia

    def calcula_suma (self ):
        return ((self .primero + self .get_elemento( self .num_elementos)) / 2.0) * self .num_elementos

if __name__ == "__main__":
    progresiones = [ProgresionGeometrica( 4, 5, 3), ProgresionAritmetica( 4, 5, 3), ProgresionAritmetica( 1, 6, 7),
    ProgresionAritmetica( 1, 6, 7)]
    for prog in progresiones:
        print (f"Progresión: {prog }. Suma: {prog.calcula_suma() }")