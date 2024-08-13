
y = 10
z = 30  

def modificar_global():
    global y
    y = 20
    print(f"Variable global y modificada dentro de la función: {y}")

def modificar_global_z():
    global z
    z = 40
    print(f"Variable global z modificada dentro de la función: {z}")

modificar_global()
print(f"Variable global y fuera de la función: {y}")

modificar_global_z()
print(f"Variable global z fuera de la función: {z}")
