#import modulos

#modulos.mi_print("Hola")

from modulos import *
import time
import sys
from asciistuff import Banner

mi_print("Hoola de nuevo")
otro_print("otro print usado")
print(sumar(10, 5))
print(restar(7, 3))

for i in range(10,0,-1):
    print(i,"...")
    time.sleep(0.25)
print(Banner("ICO"))

print(sys.platform)
print(Banner("ICO"))
