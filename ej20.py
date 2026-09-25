frase: str = "Celia tiene una cobaya"  #enuncio una frase str
letra: str = "a"  #enuncio la letra que quiero buscar
contador: int = 0  #quiero que el contador empiece en el 0
for letra in frase:  #empieza el bucle donde busca las letras (a) en las frases
    if letra == "a":
        contador = contador + 1  #si la letra es a, vulevo a definir contador
print(contador)