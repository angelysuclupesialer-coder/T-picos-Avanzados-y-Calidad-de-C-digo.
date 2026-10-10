
import unittest
from primo import es_primo


class TestNumeroPrimo(unittest.TestCase):

    def test_numero_primo(self):
        self.assertTrue(es_primo(7))

    def test_numero_no_primo(self):
        self.assertFalse(es_primo(8))

    def test_numero_menor_que_dos(self):
        self.assertFalse(es_primo(1))

    def test_numero_negativo(self):
        self.assertFalse(es_primo(-5))


if __name__ == "__main__":
    unittest.main()
