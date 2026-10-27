palabra: str = "celia"  #declaro una variable que sea una palabra
contador_vocales: int = 0  #siempre se empieza desde el 0
for letra in palabra:  #al ser str el rango es una palabra
    if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):  #si la letra es a o e o i...
        contador_vocales = contador_vocales + 1  #si es así añade 1 al ccontador de vocales
print(contador_vocales)