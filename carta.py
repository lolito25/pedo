nombre = input("Escribe tu nombre: ")
docente = ("Rippe")


print("Buenos dias " + nombre + ", por favor responde a las siguientes preguntas ")


años = int(input("¿Cuantos años tienes?: "))
nacio = input("¿En que parte de Colombia vives?: ")


como_se_ve = input("1. " + nombre + " ¿Como te vez en 4 años laburando como cientifico de datos?: ")
vivir = input ("2. ¿En donde te imaginas viviendo con esta profesion?: ")
ganancias = input("3. ¿Cuanto aspiras ganar?: ")
love = input("¿Trabajarias gratis en la empresa del profesor Rippe solo por amor a lo que haces? SI-NO , ¿por que?")
print("Muchas gracias" + nombre + "por tu tiempo, cuidate las tapas")

estudiante = "Santiago Florez"
materia = float(input("¿Profesor Rippe cuanto le coloca a esta Carta del estudiante " + estudiante + "?: "))

promedio = (materia) / 3
promedio = float(materia)

if promedio >= 3:
    print("Felicidades " + estudiante + " APROBO el trabajo con un promedio de:", promedio)
    print("FELICIDADES " + estudiante + "APROBO el trabajo con un promedio de: ", (promedio,2))

else:
    print("lo sientimos " + estudiante + "has reprobado el trabajo con un promedio de: ", promedio)
    print("lo sientimos " + estudiante + "has reprobado el trabajo con un promedio de:  ", (promedio,2))
    


print( docente , "Ya puede seguir durmiendo " )



