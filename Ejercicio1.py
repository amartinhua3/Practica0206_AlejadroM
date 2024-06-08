

def numero():
    
    n = int(input('Introduzca un número entero entre 1 y 10: '))
    file = open(f'tabla-{n}.txt', 'w')

    for i in range(0, 11):
        file.write(str(n * i)+ '\n')

numero()
