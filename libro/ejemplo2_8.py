CATE=int(input("Ingresa el tipo de categoria a la que pertenece el esclavo (1-4): "))
SUE=float(input("Ingresa el sueldo del esclavo: "))
if CATE==1:
    NSUE=SUE*1.15
elif CATE==2:
    NSUE=SUE*1.10
elif CATE==3:
    NSUE=SUE*1.08
elif CATE==4:
    NSUE=SUE*1.07
else:
    print("EROR, esta maquina explotara en 5 segundos")    
print(f"El sueldo del esclavo es de {NSUE}")

