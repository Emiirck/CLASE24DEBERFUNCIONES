
def funcion_exterior():
    def funcion_interior(mensaje):
        print(f"Esta es la función interior: {mensaje}")

    funcion_interior("Este es un mensaje")
    print("Esta es la función exterior")

funcion_exterior()
