lista = [1, 2, 3,  4, 5, 6, 2, 0, 1, 2, 1, "Hola"]
print(lista)

conjuntos = {1, 2, 3,  4, 5, 6, 2, 0, 1, 2, 1, "Hola"}
print(conjuntos)

tuplas = (1, 2, 3,  4, 5, 6, 2, 0, 1, 2, 1, "Hola")
print(tuplas)

diccionario = {"Estudiante": "Juanito", "sexo":"Hombre", "nota": 85}

print(diccionario["nota"])

nuevalista= []
nuevalista.append(lista)
nuevalista.append(conjuntos)
nuevalista.append(tuplas)
nuevalista.append(diccionario)
print(nuevalista)

for item in nuevalista:
    print(item)


for item in nuevalista:
    print(item)

for item in nuevalista:
    print(type(nuevalista))

with open("texto.txt", "w", encoding="utf-8") as archivo:
    for item in nuevalista:
        archivo.write(str(item) + "\n")
        
    for item in nuevalista:
        print(type(nuevalista))
