import string
import random

# Obtener la longitud de la contraseña del usuario y verificar que sea un entero positivo
while True:
    try:
        longitud = int(input("Ingrese el tamaño de la contraseña: "))
        if longitud > 0:
            break
        else:
            print("Por favor, ingrese un número entero positivo.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Definir los caracteres permitidos
caracteres = string.ascii_letters + string.digits + string.punctuation

# Generar la contraseña aleatoria
contraseña = "".join(random.choice(caracteres) for i in range(longitud))

# Mostrar la contraseña generada
print("La contraseña generada es: " + contraseña)
10
