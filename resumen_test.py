import unittest
from resumen import Resumen
from estudiante import Estudiante

class TestResumen(unittest.TestCase):

    def setUp(self):
        '''Se crean estudiantes de prueba'''
        self.e1 = Estudiante("MIS", 500.0, 480.0, 0.2,"Rural","Privado" )
        self.e2 = Estudiante("SFE",520.0,490.0,0.1,"Urbano","Estatal")
        self.e3 = Estudiante("MIS",480.0,500.0,0.3,"Rural","Estatal")
        self.estudiantes = [self.e1, self.e2, self.e3]
        self.resumen1 = Resumen(self.estudiantes)
        self.e4 = Estudiante("MIS", 600.0, 480.0, 0.2,"Rural","Privado" )
        self.e5 = Estudiante("MIS",520.0,490.0,0.1,"Urbano","Estatal")
        self.e6 = Estudiante("SFE",480.0,500.0,0.3,"Rural","Privado")
        self.e7 = Estudiante("BA", 600.0, 480.0, 0.2,"Rural","Privado" )
        self.estudiantes2 = [self.e4, self.e5, self.e6, self.e7]
        self.resumen2 = Resumen(self.estudiantes2)
        self.e8 = Estudiante("TUC", 600.0, 480.0, 0.2,"Rural","Privado" )
        self.e9 = Estudiante("BA",520.0,490.0,0.1,"Urbano","Estatal")
        self.e10 = Estudiante("SFE",480.0,500.0,0.3,"Rural","Estatal")
        self.e11 = Estudiante("MIS", 600.0, 480.0, 0.2,"Rural","Privado" )
        self.e12 = Estudiante("SFE",520.0,490.0,0.1,"Urbano","Estatal")
        self.e13 = Estudiante("BA",480.0,500.0,0.3,"Rural","Estatal")
        self.estudiantes3 = [self.e8, self.e9, self.e10, self.e11, self.e12, self.e13]
        


    def test_cantidad_correcta(self):
        self.assertEqual(self.resumen1.cantidad, 3)
        self.assertEqual(self.resumen2.cantidad, 4)


    def test_promedios(self):
        self.assertAlmostEqual(self.resumen1.promedio_matematica, (500+520+480)/3)
        self.assertAlmostEqual(self.resumen1.promedio_lengua, (480+490+500)/3)
        self.assertAlmostEqual(self.resumen1.promedio_NSE, (0.2+0.1+0.3)/3)
        self.assertAlmostEqual(self.resumen2.promedio_matematica, (600+520+480+600)/4)
        self.assertAlmostEqual(self.resumen2.promedio_lengua, (480+490+500+480)/4)
        self.assertAlmostEqual(self.resumen2.promedio_NSE, (0.2+0.1+0.3+0.2)/4)

    def test_proporciones(self):
        self.assertAlmostEqual(self.resumen1.proporcion_ambito_rural, 2/3)
        self.assertAlmostEqual(self.resumen1.proporcion_sector_estatal, 2/3)
        self.assertAlmostEqual(self.resumen2.proporcion_ambito_rural, 3/4)
        self.assertAlmostEqual(self.resumen2.proporcion_sector_estatal, 1/4)


    def test_repr(self):
        repr_result = repr(self.resumen1)
        self.assertEqual(repr_result, "Mat : " + str(round (self.resumen1.promedio_matematica, 2)) + " Leng : " + str(round(self.resumen1.promedio_lengua, 2)) + " NSE : " + str(round(self.resumen1.promedio_NSE, 2)) + " Rural : " + str(round(self.resumen1.proporcion_ambito_rural, 2)) + " Estado : " + str(round(self.resumen1.proporcion_sector_estatal, 2)) + " N : " + str(self.resumen1.cantidad))
        repr_result = repr(self.resumen2)
        self.assertEqual(repr_result, "Mat : " + str(round (self.resumen2.promedio_matematica, 2)) + " Leng : " + str(round(self.resumen2.promedio_lengua, 2)) + " NSE : " + str(round(self.resumen2.promedio_NSE, 2)) + " Rural : " + str(round(self.resumen2.proporcion_ambito_rural, 2)) + " Estado : " + str(round(self.resumen2.proporcion_sector_estatal, 2)) + " N : " + str(self.resumen2.cantidad))

    def test_igualdad(self):
        otro = Resumen(self.estudiantes)
        self.assertTrue(self.resumen1 == otro)
        self.assertFalse(self.resumen1 == self.resumen2)
    
    def test_mejor_materia(self):
        self.assertEqual(self.resumen1.mejor_materia(480), "Matematica: 2, Lengua: 1")
        self.assertEqual(self.resumen2.mejor_materia(480), "Matematica: 3, Lengua: 1")
    def test_suma_resumenes(self):
        suma = self.resumen1 + self.resumen2
        self.assertEqual(suma.cantidad, 7)
        self.assertAlmostEqual(suma.promedio_matematica, (500+520+480+600+520+480+600)/7)
        self.assertAlmostEqual(suma.promedio_lengua, (480+490+500+480+490+500+480)/7)
        self.assertAlmostEqual(suma.promedio_NSE, (0.2+0.1+0.3+0.2+0.1+0.3+0.2)/7)
        self.assertAlmostEqual(suma.proporcion_ambito_rural, 5/7)
        self.assertAlmostEqual(suma.proporcion_sector_estatal, 3/7)


    def test_mejor_materia_por_provincia(self):
        self.assertEqual(self.resumen1.mejor_materia_por_provincia(480), {'MIS': 'Matematica: 1, Lengua: 1', 'SFE': 'Matematica: 1, Lengua: 0'})
        self.assertEqual(self.resumen2.mejor_materia_por_provincia(480),{"MIS": "Matematica: 2, Lengua: 0","BA": "Matematica: 1, Lengua: 0","SFE": "Matematica: 0, Lengua: 1"}
)
        
unittest.main()
