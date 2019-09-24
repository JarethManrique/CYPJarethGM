edad=  int(  input("Escribe tu edad: "))
INE=  bool(  int(  input("Tienes INE (0=No/1=Si): ")))
if edad>=18 and INE == True:
    print("Es mayor de edad")
    print("Puedes entrar al table dance")
else:
    print("Eres menor de edad")
    print("No puedes entrar al table dance")
print("fin del programa")

