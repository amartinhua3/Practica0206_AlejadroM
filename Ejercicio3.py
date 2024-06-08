import os
def buscar_linea_funcion():
    '''Esta función solicita 2 numeros y busca el fichero que contenga la tabla e imprime la linea que multiplique esos dos números, en caso de que lo exista la tabla
    imprime un mensaje de que dicho fichero con la tabla no existe.'''
    n = int(input('Escribe un número del 1 al 10: '))
    m = int(input('Escribe otro número del 1 al 10: '))
    
    if os.path.isfile(f'tabla-{n}.txt') == True:
        lectura = open(f'tabla-{n}.txt', 'r')
        linea_lectura = lectura.readlines()
        print(linea_lectura[m])
    else:
        print('No existe el fichero con la tabla del ', n, '.')
    return

buscar_linea_funcion()