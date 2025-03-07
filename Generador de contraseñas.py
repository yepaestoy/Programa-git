import random
import string

def generar_contrasena(longitud=12):
    """Genera una contraseña aleatoria."""
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

# Ejemplo de uso:
contrasena_generada = generar_contrasena()
print(contrasena_generada)

# Puedes especificar la longitud si lo deseas:
contrasena_larga = generar_contrasena(20)
print(contrasena_larga)