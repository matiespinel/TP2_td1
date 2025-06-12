import unittest
from resumen import Resumen
from estudiante import Estudiante

class TestResumen(unittest.TestCase):

    def setUp(self):
        '''Se crean 3 estudiantes de prueba'''
        self.e1 = Estudiante(
            "MIS",        
            500.0,        
            480.0,        
            0.2,          
            "rural",      
            "privado"     
        )
        self.e2 = Estudiante(
            "MIS",
            520.0,
            490.0,
            0.1,
            "urbano",
            "estatal"
        )
        self.e3 = Estudiante(
            "MIS",
            480.0,
            500.0,
            0.3,
            "rural",
            "estatal"
        )
        self.estudiantes = [self.e1, self.e2, self.e3]
        self.resumen = Resumen(self.estudiantes)

    def test_cantidad_correcta(self):
        self.assertEqual(self.resumen.cantidad, 3)

    def test_promedios(self):
        self.assertAlmostEqual(self.resumen.promedio_matematica, (500+520+480)/3, places=3)
        self.assertAlmostEqual(self.resumen.promedio_lengua, (480+490+500)/3, places=3)
        self.assertAlmostEqual(self.resumen.promedio_NSE, (0.2+0.1+0.3)/3, places=3)

    def test_proporciones(self):
        self.assertAlmostEqual(self.resumen.proporcion_ambito_rural, 2/3, places=3)
        self.assertAlmostEqual(self.resumen.proporcion_sector_estatal, 2/3, places=3)

    def test_repr(self):
        repr_result = repr(self.resumen)
        self.assertTrue(repr_result.startswith("<Mat:"))
        self.assertIn("NSE:", repr_result)
        self.assertIn("N:3", repr_result)

    def test_igualdad(self):
        otro = Resumen(self.estudiantes.copy())
        self.assertTrue(self.resumen == otro)

        modificado = self.estudiantes.copy()
        modificado[0] = Estudiante(
            "MIS",
            600.0, 
            480.0,
            0.2,
            "rural",
            "privado"
        )
        distinto = Resumen(modificado)
        self.assertFalse(self.resumen == distinto)

if __name__ == "__main__":
    unittest.main()
