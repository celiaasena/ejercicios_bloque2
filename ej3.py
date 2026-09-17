fila: int = 6
columna: int = -8
#comprobar la fila
if 0 <= fila <= 7:
    #solo si la fila es válida evalúo la columna
    if 0 <= columna <= 7:
        print("fila y columna válida: dentro del tablero")
#este else va junto al segundo if por que pregunta por columnas
    else:
        print("fila válida pero columna invalida")
#este else va junto al primer if porque pregunta por filas
else:
    print("columna válida pero fila inválida")
