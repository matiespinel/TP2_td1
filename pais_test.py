import unittest
# Importamos el codigo a testear.
from pais import Pais
class TestPais(unittest.TestCase):
    def setUp(self):
        """Se ejecuta antes de cada test."""
        self.pais = Pais("Aprender2023_curado.csv")

    def test_tamano_total(self):
        """Testea que tamano() devuelva la cantidad esperada."""
        '''logitud del archivo'''
        with open("Aprender2023_curado.csv", "r") as f:
            lineas = f.readlines()
        lineas = len(lineas) - 1
        self.assertEqual(self.pais.tamano(), lineas) 

    def test_provincias_presentes(self):
        """Testea que se detecten todas las provincias correctamente, para este caso se espera que el documento contenga todas las provincias"""
        esperado = {
    "MZA", "MIS", "SFE", "SDE", "TUC", "CAT", "CAB", "CRR", "CHA", "ETR", "JJY",
    "PBA", "RNE", "STA", "SJU", "SCZ", "CBA", "CHU", "FOR", "LPA", "LRI", "SLU",
    "NEU", "TDF"}
        self.assertEqual(self.pais.provincias, esperado)

    def test_resumen_provincia_mza(self):
        """Testea el resumen de MZA con valores conocidos."""
        resumen = self.pais.resumen_provincia("MZA")
        self.assertEqual(resumen.cantidad, 27055)
        self.assertAlmostEqual(resumen.promedio_matematica, 472.57, places=2)
        self.assertAlmostEqual(resumen.promedio_lengua, 496.75, places=2)

    def test_resumenes_pais(self):
        """Testea que se devuelvan resúmenes para todas las provincias."""
        resumenes = self.pais.resumenes_pais()
        self.assertEqual(set(resumenes.keys()), self.pais.provincias)
        for r in resumenes.values():
            self.assertIsInstance(r.cantidad, int)

    def test_estudiantes_en_intervalo_nse(self):
        """Testea cantidad de estudiantes con NSE entre 0.0 y 0.5 en MZA y BA."""
        provincias = {"MZA", "BA"}
        cantidad = self.pais.estudiantes_en_intervalo("nse", 0.0, 0.5, provincias)
        self.assertTrue(cantidad, 1)

    def test_estudiantes_en_intervalo_len(self):
        """Testea estudiantes con puntaje de lengua en cierto rango."""
        provincias = {"SFE"}
        cantidad = self.pais.estudiantes_en_intervalo("len", 450, 550, provincias)
        self.assertTrue(cantidad, 0)
        
    def test_exportar_por_provincias_crea_archivo(self):
        """Testea que el archivo de resumen por provincias se genera correctamente."""
        self.pais.exportar_por_provincias("test_salida.csv", {"CRR", "MZA"})
        with open("test_salida.csv", "r") as f:
            lineas = f.readlines()
        self.assertGreaterEqual(len(lineas), 2)
    def test_mejor_materia_por_provincia(self):
        """Testea conteo de alumnos con puntajes mayores al umbral por provincia (primeros 40 en este caso)."""
        esperado = {'MZA': {'mat': 11, 'len': 3}, 'MIS': {'mat': 1, 'len': 0}}
        self.assertEqual(self.pais.mejor_materia_por_provincia(500, cantidad=40), esperado)


unittest.main()
