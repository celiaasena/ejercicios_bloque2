estado: str = "turno blancas"  #estado comienza siendo turno blancas
contador: int = 0  #creo un contador que empieza en 0 (contar cuantos turnos se han jugado)
while estado != "fin_partida":  #mientras el estado no sea fin de la partida, el bucle se ejecutará
    if estado == "turno blancas":
        print("turno blancas")
        contador = contador + 1  # más 1 turno al contador
        if contador == 4:  # si el contador es 4, fin de la partida
            estado = "fin_partida"
        else: 
            estado = "turno negras"
    elif estado == "turno negras":  #solo entra aquí si el estado es turno negras
        print("turno negras")
        contador = contador + 1
        if contador == 4:
            estado = "fin_partida" 
        else:
            estado = "turno blancas"
print("fin_partida")  #está fuera del bucle, para que se ejecute solo cuando el bucle ya ha terminado