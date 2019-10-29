N=int(input("Ingrese el numero de elementos de arreglo: "))
vec=[]
if N>=1 and N<=500:
    #logica
    for i in range(0,N,1):
        vec.append(int(input("Ingresa valor: ")))
    vec.sort()
    print("Lista de numeros sin repeticiones")
    i=0
    while i<=N-1:
        print(vec[i])
        REPET=vec[i]
        while i<=N-1 and REPET==vec[i]:
            i+=1
else:
    print("El numero de arreglos es incorrecto")

print(" Fin del puto programa ")

