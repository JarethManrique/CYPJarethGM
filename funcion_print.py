# print tiene 4 formas de uso
"""
1. Con comas
2. Con signo '+'
3. Con la funciòn format()
4. Con una variante de la funciòn format()
"""
# Con comas lo que hace print es oncatenar agregando un espacio y haciendo casting de tipo
edad=10
nombre="Juan"
estatura=1.67
print(nombre, edad, estatura)

#con '+' hace lo mismo pero no realiza el casting automatico
print(nombre + str(edad) + str(estatura))
#Funcion format()
print ("Nombre: {} Edad: {} ".format (nombre, edad))

# La forma 4 es con una variante de format() simplificado

print (f"Nombre: {nombre} Edad: {edad} ")
