ARSU=0
ARCE=0
MARSU=50000
ARNO=0
MES=0
for i in range(1,13,1):
    print(f"Mes {i}")
    RNO=int(input("Promedio de las lluvias del norte: "))
    RCE=int(input("Promedio de las lluvias del centro: "))
    RSU=int(input("Promedio de las lluvias del sur: "))

    ARNO=ARNO+RNO
    ARCE=ARCE+RCE
    ARSU=ARSU+RSU

    if RSU < MARSU:
        MARSU=RSU
        MES=1

PROCE=ARCE/12
print(f"Promedio region centro: {PROCE}")
print(f"Mes con menor lluvia en region sur: {MES}")
print(f"Registro del mes con menor lluvia es: {MARSU}") 

if ARNO>ARCE:
    if ARNO<ARSU:
        print("La region con mayor lluvia es la region norte")
    else:
        print("La region con mayor lluvia es la region sur")
elif ARCE>ARSU:
    print("La region con mayor lluvia es la region centro")
else:
    print("La region con mayor lluvia es la region sur")
