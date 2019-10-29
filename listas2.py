#arreglo
#lectura
#escritura

#escritura
frutas = ["Zapote","Manzana", "Pera", "Aguacate", "Durazno", "Uva", "Sandia"]
#lectura; si el selector [indice]
print(frutas[2])

#lectura con for

#for opcion 1
for indice in range (0,7,1):
    print(frutas[indice])
print("---------")

#for opcion 2
for fr in frutas:
    print(fr)
print("----------")

#asignacion
frutas[2]="Melon"
print(frutas)
print("----------")

#incersion al final
frutas.append("Naranja")
print(frutas)
print(len(frutas))
frutas.insert(2, "Limon")
print(frutas)
print(len(frutas))
frutas.insert(0, "Mamey")
print(frutas)

#eliminacion con pop
print(frutas.pop())
print(frutas)
frutas.append("Limon")
frutas.append("Limon")
frutas.remove("Limon")
print(frutas)

#ordenamiento
frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)

#busqueda
print(f"El Limon esta en la posicion {frutas.index('Limon')}")
print(f"La Uva esta en la posicion {frutas.index('Uva')}")
print(f"El Limon esta {frutas.count('Limon')} veces en la lista")

#concatenar
print(frutas)
otras_frutas=["Rambutan", "Pithaya", "Nispero", "Liche"]
frutas.extend(otras_frutas)
print(frutas)

#copiar
copia=frutas
copia.append("Naranja")
print(frutas)
print(copia)

otra_copia=frutas.copy()
otra_copia.append("Fresa")
otra_copia.append("Fresa")
print(frutas)
print(copia)

