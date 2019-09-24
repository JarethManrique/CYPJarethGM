n1=float(input("Escribe el primer numero: "))
n2=float(input("Escribe el segundo numero: "))
n3=float(input("Escribe el tercer numero: "))
if n1>n2 and n1>n3:
    print(f"{n1} es el numero mas grande")
if n2>n1 and n2>n3:
    print(f"{n2} es el numero mas grande")
if n3>n1 and n3>n2:
    print(f"{n3} es el numero mas grande")
print("Fin del programa")
