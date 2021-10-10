lista = []

while(len(lista) < 5):
    i = int(input('podaj element'))
    lista.append(i)

lista = tuple(lista)

print(lista)