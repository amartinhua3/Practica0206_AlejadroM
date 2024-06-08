import tsv

with open('sdg_08_10.tsv', 'r') as file:
    P = input('Escriba las iniciales del país del que quiera sabes su PIB: ').upper()
    for PIB in file:
        linea = file.readline()
        print(linea.strip())