A=int(input("Ingresa el valor de A: "))
B=int(input("Ingresa el valor de B: "))
C=int(input("Ingresa el valor de C: "))
if A>B:
    if A>C:
        print(f"{A} es el numero mas grande") 
    elif A==C:
        print(f"A y C son iguales a ({A}) y son los mayores")
    else:
        print(f"{C} es el numero mas grande")
elif A==B:
    if A>C:
        print(f"A y B son los numeros mas grandes con valor ({B})")
    elif A==C:
        print(f"Los tres numeros osn iguales a ({A})")
    else:
        print(f"C ({C}) es el numero mas grande")
elif B>C:
    print(f"{B} es el mayor")
elif B==C:
    print(f"B y C ({B}) son los numeros mas grandes")
else:
    print(f"{C} es el numero mas grande")

