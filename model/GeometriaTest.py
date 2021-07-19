import unittest
from Geometria import Geometria


class GeometriaTest(unittest.TestCase):
    def setUp(self) -> None:
        self.g = Geometria(1, 2, 3)

    def test_Geometria_constructor(self) -> None:
        self.assertEqual(self.g.a, 1)
        self.assertEqual(self.g.b, 2)
        self.assertEqual(self.g.c, 3)

    def test_areaCuadrado(self) -> None:
        self.assertEqual(self.g.areaCuadrado(3), 9)
        self.assertEqual(self.g.areaCuadrado(-3), 9)
        self.assertEqual(self.g.areaCuadrado(0), 0)

    def test_areaCirculo(self) -> None:
        self.assertEqual(round(self.g.areaCirculo(5), 2), 78.54)

    def test_areaTiangulo(self) -> None:
        self.assertEqual(self.g.areaTiangulo(2, 5), 5)

    def test_areaRectangulo(self) -> None:
        self.assertEqual(self.g.areaRectangulo(3, 8), 24)

    def test_areaPentagono(self) -> None:
        self.assertEqual(round(self.g.areaPentagono(3, 7), 2), 10.50)

    def test_areaRombo(self) -> None:
        self.assertEqual(round(self.g.areaRombo(3, 7), 2), 10.50)

    def test_areaRomboide(self) -> None:
        self.assertEqual(self.g.areaRomboide(3, 5), 15)

    def test_areaTrapecio(self) -> None:
        self.assertEqual(round(self.g.areaTrapecio(2, 5, 7), 2), 24.50)

    def test_set_figuraName(self) -> None:
        self.g.set_figuraName(12)
        self.assertEqual(self.g.figuraName, "")

        self.g.set_figuraName(1)
        self.assertEqual(self.g.figuraName, "Cuadrado")
        self.g.set_figuraName(2)
        self.assertEqual(self.g.figuraName, "Circulo")
        self.g.set_figuraName(3)
        self.assertEqual(self.g.figuraName, "Tiangulo")
        self.g.set_figuraName(4)
        self.assertEqual(self.g.figuraName, "Rectangulo")
        self.g.set_figuraName(5)
        self.assertEqual(self.g.figuraName, "Pentagono")
        self.g.set_figuraName(6)
        self.assertEqual(self.g.figuraName, "Rombo")
        self.g.set_figuraName(7)
        self.assertEqual(self.g.figuraName, "Romboide")
        self.g.set_figuraName(8)
        self.assertEqual(self.g.figuraName, "Trapecio")

    def test_switch(self) -> None:
        self.assertRaises(Exception, self.g.switch(21))

        self.assertEqual(self.g.switch(1), 1)
        self.assertEqual(round(self.g.switch(2), 2), 3.14)
        self.assertEqual(self.g.switch(3), 1)
        self.assertEqual(self.g.switch(4), 2)
        self.assertEqual(self.g.switch(5), 1)
        self.assertEqual(self.g.switch(6), 1)
        self.assertEqual(self.g.switch(7), 2)
        self.assertEqual(round(self.g.switch(8), 2), 4.50)
