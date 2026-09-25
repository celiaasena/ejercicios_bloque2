for fila in range(5):  # quiero que haya 5 filas
    for columna in range(fila + 1):  # quiero que haya una columna mas que la fila anterior
        print("*", end ="")  # imprime *, todo junto
    print("")  # pasa a la siguiente linea cuando termine la fila