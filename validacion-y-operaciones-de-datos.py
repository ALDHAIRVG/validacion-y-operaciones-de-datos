def longitud_palabra(palabra):
    longitud = len(palabra)
    
    if 4 <= longitud <= 8:
        print("La palabra es correcta.")
    elif longitud < 4:
        print(f"Hacen falta letras. Solo tiene {longitud} letras.")
    else:
        print(f"Sobran letras. Tiene {longitud} letras.")

def encontrar_cuadrante(x, y):
    if x == 0 or y == 0:
        print("Las coordenadas no pueden ser 0.")
        return
    
    if x > 0:
        if y > 0:
            print("El punto se encuentra en el cuadrante I.")
        else:
            print("El punto se encuentra en el cuadrante IV.")
    else:
        if y > 0:
            print("El punto se encuentra en el cuadrante II.")
        else:
            print("El punto se encuentra en el cuadrante III.")

# Solicitar la palabra al usuario
palabra = input("Ingrese una palabra: ")
longitud_palabra(palabra)

# Solicitar las coordenadas al usuario
x = float(input("Ingrese la coordenada X: "))
y = float(input("Ingrese la coordenada Y: "))
encontrar_cuadrante(x, y)
