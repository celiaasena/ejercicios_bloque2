#estamos definiendo un ACUMULADOR, es una variable que normalmente empieza en 0 (desde lo que queremos sumar), y va sumando valores dentro de un bucle, al final contiene el total de todo lo anterior
suma_total: int = 0   #lo inicializo
for numero in range(1, 11):  #recorres un conjunto de valores
    suma_total = suma_total + numero  #vas sumando
print(suma_total)  #usas el total al final