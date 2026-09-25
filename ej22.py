i: int = 0
suma: int = 0
for i in range(1, 21):  #enuncio que para cada numero entre el 1 y el 21
    if i % 2 == 0:  #si el numero es divisible entre 2 (par)
        suma = suma + i  #la suma se convierte en, la suma mas el numero
print(suma)
