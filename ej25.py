#EJERCICIO 2
# numero: int = 0
# if numero < 0:
#    print("Negativo")
# elif numero > 0:
#    print("positivo")
# else:
#    print("Cero")

#en este ejercicio, vulevo a hacer el ejercicio 2, pero con valores concretos
#EJERCICIO 25
numero: int = -1  #match y case solo se pueden utilizar con valores concretos (en este caso -1, 1, 0)
match numero:
    case -1:
        print("negativo")
    case 1:
        print("positivo")
    case 0:
        print("cero")