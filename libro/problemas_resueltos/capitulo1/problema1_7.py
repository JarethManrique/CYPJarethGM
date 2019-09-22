L1=float(input("Dame el primer lado: "))
L2=float(input("Dame el segundo lado: "))
L3=float(input("Dame el tercer lado: "))
S=(L1+L2+L3)/2
AREA=(S*(S-L1)*(S-L2)*(S-L3))**0.5
print(f"El area del triangulo es de {AREA}")
