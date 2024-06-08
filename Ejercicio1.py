file = open('tabla-n.txt', 'w')

def numero(num):
    #n = int(input('Introduzca un número entero entre 1 y 10: '))
    for i in range(0, 11):
        file.write(str(num * i)+ '\n')

numero(7)
