from estudiante import Estudiante
class Resumen:
    def __init__(self, est : list[Estudiante]):
        ''' completar docstring '''
        self.cantidad : int = len(est)
        self.promedio_matematica : float = 0
        self.promedio_lengua : float = 0
        self.promedio_NSE : float = 0
        for es in est:
            self.promedio_matematica += es.puntaje_matematica
            self.promedio_lengua += es.puntaje_lengua
            self.promedio_NSE += es.puntaje_NSE
            if es.ambito == "Urbano":
                self.proporcion_ambito_rural += self.proporcion_ambito_rural
            if es.sector == "Estatal":
                self.proporcion_sector_estatal += self.proporcion_sector_estatal
        self.promedio_matematica = self.promedio_matematica / self.cantidad
        self.promedio_lengua  = self.promedio_lengua / self.cantidad
        self.promedio_NSE  = self.promedio_NSE/ self.cantidad
        self.proporcion_ambito_rural : float = self.proporcion_ambito_rural / self.cantidad
        self.proporcion_sector_estatal : float = self.proporcion_sector_estatal / self.cantidad
    def __repr__(self) -> str:
        ''' completar docstring '''
        return "Mat : " + round (self.promedio_matematica, 2) + " Leng : " + round(self.promedio_lengua, 2) + " NSE : " + round(self.promedio_NSE, 2) + " Rural : " + round(self.proporcion_ambito_rural, 2) + " Estado : " + round(self.proporcion_sector_estatal, 2) + " N : " + self.cantidad
 

    def __eq__(self, ...) -> ...:
        ''' completar docstring '''
        pass

