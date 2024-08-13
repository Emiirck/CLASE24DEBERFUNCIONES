x = 10

def mi_funcion():
    global x
    x = 5
    print(f"Variable global x dentro de la función: {x}")

mi_funcion()
print(f"Variable global x fuera de la función: {x}")