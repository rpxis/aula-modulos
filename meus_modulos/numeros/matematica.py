import random

def sortearNumero(inicio:int, fim: int) -> int:
    return random.randint(inicio, fim)

if __name__ == '__main__':
    print(f'Execução em matematica.py: {sortearNumero(1,1000)}')



