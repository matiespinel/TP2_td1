import unittest
# Importamos el codigo a testear.
from pais import Pais
from resumen import Resumen

class TestPais(unittest.TestCase):
    def setUp(self):
        """Se ejecuta antes de cada test."""
        self.pais = Pais("Libro1.csv")

    def test_tamano_total(self):
        """Testea que tamano() devuelva la cantidad esperada."""
        '''logitud del archivo'''
        with open("Libro1.csv", "r") as f:
            lineas = f.readlines()
        lineas = len(lineas) - 1
        self.assertEqual(self.pais.tamano(), lineas) 
        self.assertEqual(self.pais.tamano(), 199)

    def test_provincias_presentes(self):
        """Testea que se detecten todas las provincias correctamente"""
        esperado = {"MZA", "MIS", "SFE", "TUC", "SDE"}
        self.assertEqual(self.pais.provincias, esperado)

    def test_resumen_provincia_mza(self):
        """Testea el resumen de MZA con valores conocidos."""
        resumen = self.pais.resumen_provincia("MZA")
        self.assertEqual(resumen.cantidad, 34)
        self.assertAlmostEqual(resumen.promedio_matematica, 469.95, places=2)
        self.assertAlmostEqual(resumen.promedio_lengua, 450.19, places=2)

    def test_resumenes_pais(self):
        """Testea que se devuelvan resúmenes para todas las provincias."""
        resumenes = self.pais.resumenes_pais()
        self.assertEqual(set(resumenes.keys()), self.pais.provincias)
        for r in resumenes.values():
            self.assertIsInstance(r.cantidad, int)
            self.assertIsInstance(r, Resumen)

    def test_estudiantes_en_intervalo(self):
        """Testea cantidad de estudiantes con NSE entre 0.0 y 0.5 en MZA y TUC."""
        provincias = {"MZA", "TUC"}
        cantidad = self.pais.estudiantes_en_intervalo("nse", -1.0, 0.5, provincias)
        cantidad2 = self.pais.estudiantes_en_intervalo("mat", 0.0, 200, provincias)
        self.assertEqual(cantidad, 65)
        self.assertEqual(cantidad2, 0)
        provincias = {"SFE"}
        cantidad3= self.pais.estudiantes_en_intervalo("len", 450, 550, provincias)
        self.assertEqual(cantidad3, 29)
        
    def test_exportar_por_provincias_crea_archivo(self):
        """Testea que el archivo de resumen por provincias se genera correctamente."""
        self.pais.exportar_por_provincias("test_salida.csv", {"SFE", "MZA"})
        with open("test_salida.csv", "r") as f:
            lineas = f.readlines()
        self.assertEqual(len(lineas), 3)
        self.assertEqual(lineas[0], "provincia,cantidad,promedio_matematica,promedio_lengua,promedio_nse,proporcion_ambito_rural,proporcion_sector_estatal\n")
    def test_mejor_materia_por_provincia(self):
        """Testea conteo de alumnos con puntajes mayores al umbral por provincia (primeros 40 en este caso (primeros 40 del documento completo asignado para este trabajo))."""
        esperado = {'MZA': {'mat': 11, 'len': 3}, 'MIS': {'mat': 1, 'len': 0}}
        self.assertEqual(self.pais.mejor_materia_por_provincia(500, cantidad=40), esperado)


unittest.main()
