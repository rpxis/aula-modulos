from meus_modulos.numeros.divisao import dividir
from meus_modulos.numeros.soma import somar
from meus_modulos.numeros.subtracao import subtrair
from meus_modulos.numeros.multiplicacao import multiplicar


functions = {
    1: somar,
    2: subtrair,
    3: dividir,
    4: multiplicar
}
def menu():
    while True:
        print('----- Calculadora -----')
        print('1 - Somar \n'
              '2 - Subtrair \n'
              '3 - Dividir \n'
              '4 - Multiplicar ')
        option = int(input(">> "))
        print('\n')

        if option in functions:
            print(f'Opção selecionada: {functions[option].__name__.capitalize()}')
            numberOne = float(input('Valor um: '))
            numberTwo = float(input('Valor dois: '))
            print(f'Resultado: {functions[option](numberOne, numberTwo)}')
            print('\n')

        else:
            break

menu()