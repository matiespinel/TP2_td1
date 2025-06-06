class Estudiante:
    def __init__(self, pr: str, p_m: float, p_L: float, p_NSE: float, amb : str, sec: str):
        ''' completar docstring/ cambiar custiomes de como se representan las provincias y el ambito??? '''
        self.provincia : str = pr
        self.puntaje_matematica : float = p_m
        self.puntaje_lengua: float = p_L
        self.puntaje_NSE: float = p_NSE
        self.ambito : str = amb
        self.sector : str = sec
        provincias : dict = {
            # for unique values in columna del dataset, appendearlas al dic y darles su valor correspondiente de str
        }


    def __repr__(self) -> str:
        ''' completar docstring '''
        return "Mat " + self.puntaje_matematica + " Leng " + self.puntaje_lengua + " NSE " + self.puntaje_NSE + self.ambito + self.sector + self.provincia



    def __eq__(self, otro: "Estudiante") -> bool:
        ''' completar docstring '''
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

