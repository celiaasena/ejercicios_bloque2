# no tengo el tablero del bloque 1
# creo que es este
fila_empieza_clara: str = (clara_ancha + oscura_ancha) * 4
fila_empieza_oscura: str = (oscura_ancha + clara_ancha) * 4
print(" ", LETRAS_COLUMNAS)
print("8", fila_empieza_clara)
print("7", fila_empieza_oscura)
print("6", fila_empieza_clara)
print("5", fila_empieza_oscura)
print("4", fila_empieza_clara)
print("3", fila_empieza_oscura)
print("2", fila_empieza_clara)
print("1", fila_empieza_oscura)