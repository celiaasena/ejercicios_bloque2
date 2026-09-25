#no sé hacerlo
suma: int = 0  #la palabra suma es igual a 0
numero: int = int(input("di un numero distinto al 0"))  #pides un numero
while numero != 0:  #si ese numero no es 0, se le añade a la suma
    suma = suma + numero  #la suma es igual  0 mas el numero
    numero: int = int(input("di un numero"))  #pides otro numero
print("la suma total es", suma)  #cuando el numero sea 0 se ejecutará toda la suma
