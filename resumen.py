from estudiante import Estudiante
class Resumen:
    def __init__(self, est : list[Estudiante]):
        '''  '''
        self.est : list[Estudiante] = est 
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
        '''devuelve una representación como string del resumen r, con el siguiente formato:
<Mat:FLOAT, Len:FLOAT, NSE:FLOAT, Rural:FLOAT, Estado:FLOAT, N:INT '''
        return "Mat : " + str(round (self.promedio_matematica, 2)) + " Leng : " + str(round(self.promedio_lengua, 2)) + " NSE : " + str(round(self.promedio_NSE, 2)) + " Rural : " + str(round(self.proporcion_ambito_rural, 2)) + " Estado : " + str(round(self.proporcion_sector_estatal, 2)) + " N : " + str(self.cantidad)
 

    def __eq__(self, otro: "Resumen") -> bool:
        ''' devuelve True si r1 y r2 tienen cantidad, promedios y proporciones iguales; y
False en caso contrario. En este contexto, cnsiderar que dos valores float son iguales si la
diferencia absoluta entre ellos es menor que 0.001. '''
        cant_ig : bool = self.cantidad == otro.cantidad
        leng_ig : bool = False
        nse_ig : bool = False
        mat_ig : bool = False
        propor_amb_r : bool = False
        amb_rur : float = self.proporcion_ambito_rural - otro.proporcion_ambito_rural 
        propor_sec_est : bool = False
        sec_ests: float = self.proporcion_sector_estatal - otro.proporcion_sector_estatal 
        propor_amb_r = -0.001 < amb_rur < 0.001
        propor_sec_est = -0.001 < sec_ests < 0.001
        mat_diff = self.promedio_matematica - otro.promedio_matematica
        leng_diff = self.promedio_lengua - otro.promedio_lengua
        nse_diff = self.promedio_NSE - otro.promedio_NSE
        mat_ig = -0.001 < mat_diff < 0.001
        leng_ig = -0.001 < leng_diff < 0.001
        nse_ig = -0.001 < nse_diff < 0.001

        
        return mat_ig and leng_ig and nse_ig and cant_ig and propor_amb_r and propor_sec_est
    def mejor_materia(self, bara : int) -> str:
        """ Devuelve un string con el conteo total de alumnos que tengan como mejor puntaje matematica y lengua, 
        con el siguiente formato: Matemaica: INT,  Lengua: INT (se puede aplicar una bara que permita dejar sin contar los puntajes debajo de ella)
        """
        conteo_mate : int = 0
        conteo_leng : int = 0
        for e in self.est: 
            if e.puntaje_matematica >= bara and e.puntaje_lengua <= e.puntaje_matematica:
                conteo_mate += 1
            if e.puntaje_lengua >= bara and e.puntaje_lengua >= e.puntaje_matematica:
                conteo_leng += 1
        return "Matemaica: " + str(conteo_mate) + ", Lengua: " + str(conteo_leng)
            



