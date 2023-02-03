import unittest
from cities import city_name

class TestCities(unittest.TestCase):
    """Classe para realizar testes"""

    def test_city_country(self):
        """Testa a função city_name"""
        formatted = city_name('santiago', 'chile')

        self.assertEqual(formatted, 'Santiago, Chile')

    def test_city_country_population(self):
        """Testa se a funçao também aceita população"""
        formatted = city_name('santiago', 'chile', 50000)

        self.assertEqual(formatted, 'Santiago, Chile population - 50000')


unittest.main()

