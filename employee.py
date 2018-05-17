'''11.3 – Funcionário: Escreva uma classe chamada Employee. O método
__init__() deve aceitar um primeiro nome, um sobrenome e um salário anual, e
deve armazenar cada uma dessas informações como atributos. Escreva um método
de nome give_raise() que some cinco mil dólares ao salário anual, por default,
mas que também aceite um valor diferente de aumento.
Escreva um caso de teste para Employee. Crie dois métodos de teste,
test_give_default_raise() e test_give_custom_raise(). Use o método
setUp() para que não seja necessário criar uma nova instância de funcionário em
cada método de teste. Execute seu caso de teste e certifique-se de que os dois
testes passem.'''
class Employee():
    def __init__(self, first_name, last_name, annual_income):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_income = annual_income
    def give_raise(self, raise_income = 5000):
        self.annual_income += raise_income
        #print('You gave the employee a income raise of U${}, his new income is U${}.'.format(raise_income, self.annual_income))
        return raise_income
       