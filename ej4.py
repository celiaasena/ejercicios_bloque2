anio: int = 2021
if (anio % 4 == 0) and (anio % 100 != 0) or (anio % 400 == 0):
    print("bisiesto")
else:
    print("no bisiesto")