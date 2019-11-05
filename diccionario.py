#Diccionarios ['llave':'valor']
alumno={'num_cta':'315649524',
        "nombre":"jose",
        "paterno":"perez",
        "semestre": 1,
        "promedio":0.0,
        "materias":["CYP", "algebra", "calculo", "geometria", "int"],
        'regular':True,
        'lagrimas_por_examen':10,
        'direccion':{
            'calle':'rancho escondido',
            'numero':'69',
            'colonia':'impulsora',
            'cp':'07570',
            'municipio':'nezayork',
            'estado':{
                'id':'15',
                'nombre':'estado de mexico',
                'nombre corto':'edomex',
                }
            }
        }
print(alumno['materias'][1].upper())
print(alumno["nombre"])
print(alumno)
print(alumno['paterno'][1])
print(alumno['direccion']['cp'])
print(alumno['direccion']['estado']['nombre corto'])
print(alumno['materias'][3::])
print(alumno['direccion']['estado']['nombre'][10::1].upper())
alumno['lagrimas_por_examen']=10
print(alumno)




mi_lista=[['a', 'b'],['c', 10],['d', True]]
diccionario=dict(mi_lista)
print(diccionario)


#son mutables
alumno['cursa_ingles']=True
print(alumno)

#funcion keys
llaves=alumno.keys()
print(llaves)
for llave in llaves:
    print("_______________")
    print(llave)
    print("...............")
    print(alumno[llave])
    print("_______________")

#funcion val
for val in alumno.values():
    print("_______________")
    print(val)
    print("_______________")

































