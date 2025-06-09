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
        self.puntaje_matematica : float = round (p_m, 2)
        self.puntaje_lengua: float = round(p_L, 2)
        self.puntaje_NSE: float = round(p_NSE, 2)
        self.ambito : str = amb
        self.sector : str = sec
       


    def __repr__(self) -> str:
        ''' devuelve una representación como string del estudiante e, con el siguiente formato: <Mat:FLOAT, Len:FLOAT, NSE:FLOAT,
AMBITO, SECTOR, PROVINCIA>, AMBITO es un string ('Rural' o 'Urbano'), SECTOR es un string ('Estatal' o
'Privado'), y PROVINCIA es un string ('MZA', 'SFE', 'CHU', etc.) '''
        return "Mat " + self.puntaje_matematica + " Leng " + self.puntaje_lengua + " NSE " + self.puntaje_NSE + self.ambito + self.sector + self.provincia



    def __eq__(self, otro: "Estudiante") -> bool:
        ''' devuelve True si e1 y e2 tienen provincia, puntajes, ámbito y sector iguales; y
False en caso contrario '''
        leng_ig : bool = False
        nse_ig : bool = False
        mat_ig : bool = False
        if self.puntaje_matematica - otro.puntaje_matematica < 0.001:
            mat_ig = True
        if self.puntaje_lengua - otro.puntaje_lengua < 0.001:
            leng_ig = True
        if self.puntaje_NSE - otro.puntaje_NSE < 0.001:
            nse_ig = True
        amb_ig = self.ambito == otro.ambito
        sec_ig = self.sector == otro.sector
        prov_ig = self.provincia == otro.provincia
        return mat_ig and leng_ig and nse_ig and amb_ig and sec_ig and prov_ig

