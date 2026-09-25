for fila in range(8):
    for columna in range(8):
        if (fila == 0 or fila == 7) and (columna == 0 or columna == 7):
            print("Esquina", end=" ")
        elif (fila == 0 or fila == 7) or (columna == 0 or columna == 7):
            print("Borde", end=" ")
        else:
            print("Centro", end=" ")
    print("")