print("Ingresa 3 numeros diferentes")
A=int(input("Ingresa el primer numero: "))
B=int(input("Ingresa el segundo numero: "))
C=int(input("Ingresa el tercer numero: "))
if A>B:
    if A>C:
        if B>C:
            print(f"{A} > {B} > {C}")
        else:
            print(f"{A} > {C} > {B}")
    else:
        print(f"{C} > {A} > {B}")
else:
    if B>C:
        if A>C:
            print(f"{B} > {A} > {C}")
        else:
            print(f"{B} > {C} > {A}")
    else: 
        print(f"{C} > {B} > {A}")
print("Fin del programa")
