from scapy.all import *
import sys
from colorama import Fore, Style, init
import difflib

# Inicializa colorama
init(autoreset=True)

def leer_ultimo_byte_mensaje_cifrado(archivo_pcap):
    paquetes = rdpcap(archivo_pcap)
    mensaje = []

    # Filtramos solo los paquetes ICMP y extraemos el último byte de datos
    for paquete in paquetes:
        if ICMP in paquete and Raw in paquete:
            # Extraemos solo el último byte del campo 'data'
            ultimo_byte = paquete[Raw].load[-1:].decode('utf-8', errors='ignore')
            mensaje.append(ultimo_byte)

    return ''.join(mensaje)

def descifrar_cesar(mensaje_cifrado):
    resultados = []

    for corrimiento in range(26):
        descifrado = []
        for caracter in mensaje_cifrado:
            if 'A' <= caracter <= 'Z':  # Manejo de mayúsculas
                indice_descifrado = (ord(caracter) - ord('A') - corrimiento) % 26
                descifrado.append(chr(indice_descifrado + ord('A')))
            elif 'a' <= caracter <= 'z':  # Manejo de minúsculas
                indice_descifrado = (ord(caracter) - ord('a') - corrimiento) % 26
                descifrado.append(chr(indice_descifrado + ord('a')))
            else:
                descifrado.append(caracter)  # Dejar los caracteres no alfabéticos como están

        resultados.append(''.join(descifrado))

    return resultados

def es_similar(mensaje_descifrado, mensaje_objetivo):
    # Compara la similitud entre dos cadenas
    ratio = difflib.SequenceMatcher(None, mensaje_descifrado, mensaje_objetivo).ratio()
    return ratio > 0.7  # Ajusta el umbral de similitud si es necesario

if __name__ == "__main__":
    
    archivo_pcap = sys.argv[1]
    mensaje_objetivo = "criptografia y seguridad en redes"
    mensaje_cifrado = leer_ultimo_byte_mensaje_cifrado(archivo_pcap)
        
    print("Mensaje cifrado extraído:")
    print(mensaje_cifrado)

    print("\nTodas las posibles combinaciones del mensaje:")
    combinaciones = descifrar_cesar(mensaje_cifrado)
    for indice, combinacion in enumerate(combinaciones):
        if es_similar(combinacion, mensaje_objetivo):
            print(Fore.GREEN + f"{indice} {combinacion}")
        else:
            print(f"{indice} {combinacion}")
