import unittest

class TestPais(unittest.TestCase):

    def setup(self):
        """Se ejecuta antes de cada test."""
        self.pais = Pais("data/Aprender2023_curado.csv")

    def test_tamano_total(self):
        """Testea que tamano() devuelva la cantidad esperada."""
        self.assertEqual(self.pais.tamano(), 10) 

    def test_provincias_presentes(self):
        """Testea que se detecten todas las provincias correctamente."""
        esperado = {'MZA', 'SFE', 'BA', 'TUC'}  
        self.assertEqual(self.pais.provincias, esperado)

    def test_resumen_provincia_mza(self):
        """Testea el resumen de MZA con valores conocidos."""
        resumen = self.pais.resumen_provincia("MZA")
        self.assertEqual(resumen.cantidad, 3)
        self.assertAlmostEqual(resumen.promedio_matematica, 480.5, places=1)
        self.assertAlmostEqual(resumen.promedio_lengua, 500.2, places=1)

    def test_resumenes_pais(self):
        """Testea que se devuelvan resúmenes para todas las provincias."""
        resumenes = self.pais.resumenes_pais()
        self.assertEqual(set(resumenes.claves()), self.pais.provincias)
        for r in resumenes.valores():
            self.assertIsInstance(r.cantidad, int)

    def test_estudiantes_en_intervalo_nse(self):
        """Testea cantidad de estudiantes con NSE entre 0.0 y 0.5 en MZA y BA."""
        provincias = {"MZA", "BA"}
        cantidad = self.pais.estudiantes_en_intervalo("nse", 0.0, 0.5, provincias)
        self.assertGreaterEqual(cantidad, 1)

    def test_estudiantes_en_intervalo_len(self):
        """Testea estudiantes con puntaje de lengua en cierto rango."""
        provincias = {"SFE"}
        cantidad = self.pais.estudiantes_en_intervalo("len", 450, 550, provincias)
        self.assertGreater(cantidad, 0)

    def test_exportar_por_provincias_crea_archivo(self):
        """Testea que el archivo de resumen por provincias se genera correctamente."""
        self.pais.exportar_por_provincias("test_salida.csv", {"BA", "MZA"})
        with open("test_salida.csv", "r") as f:
            lineas = f.readlines()
        self.assertGreaterEqual(len(lineas), 2

unittest.main()
