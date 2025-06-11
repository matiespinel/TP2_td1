from resumen import Resumen
from estudiante import Estudiante
import csv

class Pais:
    def __init__(self, archivo_csv:str):
        """ Inicializa un objeto Pais a partir de un archivo CSV con datos de estudiantes.
              Parámetro:
             - archivo_csv con las columnas:
             'provincia', 'puntaje_matematica', 'puntaje_lengua',
             'puntaje_nse', 'ambito', 'sector'
        """
        self.estudiantes: list[Estudiante] = []

        f = open(archivo_csv)
        for linea in csv.DictReader(f):
            prov: str = linea["provincia"]
            mat: float = float(linea["puntaje_matematica"])
            leng: float = float(linea["puntaje_lengua"])
            nse: float = float(linea["puntaje_nse"])
            amb: str = linea["ambito"]
            sec: str = linea["sector"]

            est: Estudiante = Estudiante(prov, mat, leng, nse, amb, sec)
            self.estudiantes.append(est)
        f.close()
        self.provincias: set[str] = set(e.provincia for e in self.estudiantes)

    def tamano(self) -> int:
        """ Devuelve la cantidad de estudiantes en el dataset.
            Complejidad: O(1).
        """
        return len(self.estudiantes)


    def resumen_provincia(self, provincia:str) -> Resumen:
        """ Devuelve un resumen con estadísticas de estudiantes de una provincia. 
             Parámetros:
             Provincia: código de la provincia (ej: 'BA', 'MZA', 'SFE').
             Complejidad: O(N), siendo N la cantidad de estudiantes.
        """
        estudiantes: list[Estudiante] = [e for e in self.estudiantes if e.provincia == provincia]
        return Resumen(estudiantes)


    def resumenes_pais(self) -> dict[str, Resumen]:
        """ Devuelve un diccionario con un resumen por cada provincia presente en el dataset.
            Claves: códigos de provincia.
            Valores: objetos de la clase Resumen.
            Complejidad: O(N*P), donde N es la cantidad de estudiantes y P la cantidad de provincias.
        """
        res: dict[str, Resumen] = {}
        for prov in self.provincias:
            res[prov] = self.resumen_provincia(prov)
        return res

    def estudiantes_en_intervalo(self, categoria: str, x: float, y: float, provincias: set[str]) -> int:
        """ Devuelve la cantidad de estudiantes en el intervalo [x, y) para cierta categoría,
            dentro de las provincias indicadas.
            Parámetros:
            categoria: puede ser 'mat', 'len' o 'nse'
            x, y: valores límite del intervalo
            provincias: conjunto de códigos de provincia
            Complejidad: O(N*P), donde N es la cantidad total de estudiantes.
        """
        contador: int = 0
        for e in self.estudiantes:
            if e.provincia in provincias:
                valor: float = 0.0
                if categoria == "mat":
                    valor = e.puntaje_matematica
                elif categoria == "len":
                    valor = e.puntaje_lengua
                elif categoria == "nse":
                    valor = e.puntaje_nse
                if x <= valor < y:
                    contador = contador + 1
        return contador

    def exportar_por_provincias(self, archivo_csv: str, provincias: set[str]) -> None:
        """Genera un archivo CSV con un resumen por cada provincia del conjunto dado.
           Columnas:
          provincia, cantidad, promedio_matematica, promedio_lengua,
          promedio_nse, proporcion_ambito_rural, proporcion_sector_estatal
        Complejidad: O(N*P).
        """
        with open(archivo_csv, "w") as archivo:
            encabezado = "provincia,cantidad,promedio_matematica,promedio_lengua,promedio_nse,proporcion_ambito_rural,proporcion_sector_estatal\n"
            archivo.write(encabezado)
            for prov in provincias:
                resumen = self.resumen_provincia(prov)        
                linea = (
                    prov + "," +
                    str(round(resumen.cantidad, 2)) + "," +
                    str(round(resumen.promedio_matematica, 2)) + "," +
                    str(round(resumen.promedio_lengua, 2)) + "," +
                    str(round(resumen.promedio_NSE, 2)) + "," +
                    str(round(resumen.proporcion_ambito_rural, 2)) + "," +
                    str(round(resumen.proporcion_sector_estatal, 2)) + "\n")
            archivo.write(linea)
