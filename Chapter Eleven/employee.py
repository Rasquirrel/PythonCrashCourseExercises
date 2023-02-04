"""
metodo init recebe um primeiro nome, ultimo nome, e salario anual
deve existir um metodo give_raise(self) que adiciona $5000 por padrão
ao alario anual mas também aceita um valor alternativo
"""

class Employee:
    """This class simulate the building of a employee"""

    def __init__(self, first_name: str, last_name:str , annual_salary: int):
        """Initializing attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, value=5000):
        """Give a raise of $5000 by default but you can also give an alternative value"""
        self.annual_salary += value


