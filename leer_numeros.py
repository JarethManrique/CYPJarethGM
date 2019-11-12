archivo=open("numeros.txt", "rt")
print(dir(archivo))

numeros1=archivo.read()
print(numeros1)
archivo.close()

archivo=open("numeros.txt" , "rt")
numeros2=archivo.readlines()
print(numeros2)
archivo.close()

archivo=open("numeros.txt" , "rt")
numeros2=archivo.readlines()
print(numeros2)
archivo.close()
