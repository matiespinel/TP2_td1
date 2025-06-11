class Estudiante:
    def __init__(self, pr: str, p_m: float, p_L: float, p_NSE: float, amb : str, sec: str):
        ''' La clases estudiante contiene: 
              - proviencia: la proviencia del estudiante
              - puntaje_matematica: puntaje del estudiante en matematica
              - puntaje_lengua: puntaje del estudiante en lengua
              - puntaje_NSE: puntaje del nivel socioeconomico
              - Ambito: ambito de la escuela
              - Sector: sector de la escuela 
              '''
        self.provincia : str = pr
        self.puntaje_matematica : float = p_m
        self.puntaje_lengua: float = p_L
        self.puntaje_NSE: float = p_NSE
        self.ambito : str = amb
        self.sector : str = sec
       


    def __repr__(self) -> str:
        ''' devuelve una representación como string del estudiante e, con el siguiente formato: <Mat:FLOAT, Len:FLOAT, NSE:FLOAT,
AMBITO, SECTOR, PROVINCIA>, AMBITO es un string ('Rural' o 'Urbano'), SECTOR es un string ('Estatal' o
'Privado'), y PROVINCIA es un string ('MZA', 'SFE', 'CHU', etc.) '''
        return "Mat " + str(round(self.puntaje_matematica,2)) + " Leng " + str(round(self.puntaje_lengua,2)) + " NSE " + str(round(self.puntaje_NSE, 2)) + " " + self.ambito + " " + self.sector + " " + self.provincia



    def __eq__(self, otro: "Estudiante") -> bool:
        ''' Devuelve True si e1 y e2 tienen provincia, puntajes, ámbito y sector iguales;
    y False en caso contrario '''
    
        mat_diff = self.puntaje_matematica - otro.puntaje_matematica
        leng_diff = self.puntaje_lengua - otro.puntaje_lengua
        nse_diff = self.puntaje_NSE - otro.puntaje_NSE

        mat_ig = -0.001 < mat_diff < 0.001
        leng_ig = -0.001 < leng_diff < 0.001
        nse_ig = -0.001 < nse_diff < 0.001

        amb_ig = self.ambito == otro.ambito
        sec_ig = self.sector == otro.sector
        prov_ig = self.provincia == otro.provincia
        return mat_ig and leng_ig and nse_ig and amb_ig and sec_ig and prov_ig
