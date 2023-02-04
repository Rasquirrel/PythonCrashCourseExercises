"""
Escrever dois métodos de teste.
test_give_default_raise() and
test_give_custom_raise().

Usar método setUp então eu não preciso
criar uma instância de Employee para 
cada teste
"""
import unittest
from employee import Employee


class TestEmployeeClass(unittest.TestCase):
    """Tests the Emplyee class"""

    def setUp(self):
        """Create an employee instance that I can use in every test"""
        self.my_employee = Employee('Jose', 'Isac', 3400)

    def test_give_default_raise(self):
        """The default value works?"""
        self.my_employee.give_raise()
        salary = self.my_employee.annual_salary
        self.assertEqual(salary, 8400)

    def test_give_custom_raise(self):
        """A custom value works?"""
        self.my_employee.give_raise(3000)
        salary = self.my_employee.annual_salary
        self.assertEqual(salary, 6400)


unittest.main()
