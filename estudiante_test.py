import unittest

# Importamos el codigo a testear.
from estudiante import Estudiante

####################################################################

class TestEstudiante(unittest.TestCase):
#testear que los valores se asignan de la forma correcta:
    def test_self(self):
        est1 = Estudiante("MZA", 1,1,1,"Urbano","Estatal")
        self.assertEqual(est1.provincia, "MZA")
        self.assertEqual(est1.puntaje_matematica, 1)
        self.assertEqual(est1.puntaje_lengua, 1)
        self.assertEqual(est1.puntaje_NSE, 1)
        self.assertEqual(est1.ambito, "Urbano")
        self.assertEqual(est1.sector, "Estatal")
        

    def test_repr(self):
        est1 = Estudiante("MZA", 1.0,1.0,1.0,"Urbano","Estatal")
        self.assertEqual(repr(est1), "Mat 1.0 Leng 1.0 NSE 1.0 Urbano Estatal MZA")
        est2 = Estudiante("CRR", 500.0,123.0,451.0,"Rural","Privado")
        self.assertEqual(repr(est2), "Mat 500.0 Leng 123.0 NSE 451.0 Rural Privado CRR")
        
    def test_eq(self):
        est1 = Estudiante("MZA", 123.45,123.56,123.78,"Urbano","Estatal")
        est2 = Estudiante("MZA", 123.45,123.56,123.78,"Urbano","Estatal")
        self.assertTrue(est1 == est2)
        est3 = Estudiante("CRR", 199.45,178.56,156.78,"Urbano","Privado")
        est4 = Estudiante("CRR", 199.45,178.56,156.78,"Urbano","Privado")
        self.assertTrue(est3 == est4)
        #test de falso
        est5 = Estudiante("MZA", 123.45,123.56,123.78,"Urbano","Estatal")
        est6 = Estudiante("CRR", 199.45,178.56,156.78,"Urbano","Privado")
        self.assertFalse(est5 == est6)
        


        
####################################################################

unittest.main()
