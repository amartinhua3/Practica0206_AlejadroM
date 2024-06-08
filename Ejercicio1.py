

def numero():
    '''Esta función recibe un numero introducido por el usuario y crea una tabla de '''
    n = int(input('Introduzca un número entero entre 1 y 10: '))
    file = open(f'tabla-{n}.txt', 'w')

    for i in range(0, 11):
        file.write(str(f'{n} x {i} =  {n * i}') + '\n')

numero()
