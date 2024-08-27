from scapy.all import *
import sys

def enviar_mensaje_cifrado(mensaje_cifrado):
    # Cada paquete ICMP tiene un encabezado de 8 bytes, necesitamos 40 bytes de datos
    tamano_data = 48
    
    for caracter in mensaje_cifrado:
        # Rellenar con bytes para alcanzar los 40 bytes de datos
        padding = 'X' * (tamano_data - 1)  # 1 byte para el carácter del mensaje
        data = padding + caracter
        
        # Crear un paquete ICMP con el data ajustado
        paquete = IP(dst="192.168.1.1")/ICMP()/Raw(load=data)
        
        # Enviar el paquete
        send(paquete)

if __name__ == "__main__":
    
    mensaje_cifrado = sys.argv[1]

    enviar_mensaje_cifrado(mensaje_cifrado)

