from estudiante import Estudiante
class Resumen:
    def __init__(self, est : list[Estudiante]):
        '''  '''
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
        return "Mat : " + round (self.promedio_matematica, 2) + " Leng : " + round(self.promedio_lengua, 2) + " NSE : " + round(self.promedio_NSE, 2) + " Rural : " + round(self.proporcion_ambito_rural, 2) + " Estado : " + round(self.proporcion_sector_estatal, 2) + " N : " + self.cantidad
 

    def __eq__(self, otro: "Resumen") -> bool:
        ''' devuelve True si r1 y r2 tienen cantidad, promedios y proporciones iguales; y
False en caso contrario. En este contexto, cnsiderar que dos valores float son iguales si la
diferencia absoluta entre ellos es menor que 0.001. '''
        cant_ig : bool = self.cantidad == otro.cantidad
        leng_ig : bool = False
        nse_ig : bool = False
        mat_ig : bool = False
        propor_amb_r : bool = self.proporcion_ambito_rural == otro.proporcion_ambito_rural #arreglar
        propor_sec_est : bool = self.proporcion_sector_estatal == otro.proporcion_sector_estatal #arreglar
        if self.promedio_matematica - otro.promedio_matematica < 0.001:
            mat_ig = True
        if self.promedio_lengua - otro.promedio_lengua < 0.001:
            leng_ig = True
        if self.promedio_NSE - otro.promedio_NSE < 0.001:
            nse_ig = True
        
        return mat_ig and leng_ig and nse_ig and cant_ig and propor_amb_r and propor_sec_est



