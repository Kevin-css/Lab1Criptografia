# Importamos sys para poder acceder a los argumentos de la línea de comandos
import sys

def cifrado_cesar(mensaje, desplazamiento):
    resultado = ""
    for letra in mensaje:
        # Comprobamos si es una letra del alfabeto
        if letra.isalpha():
            # Obtenemos el código ASCII de la letra
            codigo = ord(letra)
            # Calculamos la nueva posición con el desplazamiento
            nuevo_codigo = codigo + desplazamiento
            # Manejamos el desbordamiento del alfabeto
            if letra.islower():
                if nuevo_codigo > ord('z'):
                    nuevo_codigo -= 26
                elif nuevo_codigo < ord('a'):
                    nuevo_codigo += 26
            elif letra.isupper():
                if nuevo_codigo > ord('Z'):
                    nuevo_codigo -= 26
                elif nuevo_codigo < ord('A'):
                    nuevo_codigo += 26
            # Convertimos el código ASCII modificado de nuevo a letra
            resultado += chr(nuevo_codigo)
        else:
            # Mantenemos caracteres que no son letras sin cifrar
            resultado += letra
    return resultado

if __name__ == "__main__":
    # Verificamos que se hayan pasado exactamente dos argumentos (nombre del script y mensaje)
    if len(sys.argv) != 3:
        print("Uso: python cesar.py <mensaje> <desplazamiento>")
    else:
        mensaje = sys.argv[1]
        try:
            desplazamiento = int(sys.argv[2])
            cifrado = cifrado_cesar(mensaje, desplazamiento)
            print("Mensaje cifrado:", cifrado)
        except ValueError:
            print("El desplazamiento debe ser un número entero.")
