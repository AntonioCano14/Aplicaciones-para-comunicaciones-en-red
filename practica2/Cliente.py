import os
import socket
import struct
import errno
import time

HOST = "127.0.0.1"
PORT = 65432

def send_file(sck: socket.socket, filename):
    # Obtener el tamaño del archivo a enviar.
    filesize = os.path.getsize(filename)
    # Informar primero al servidor la cantidad
    # de bytes que serán enviados.
    sck.sendall(struct.pack("<Q", filesize))
    # Enviar el archivo en bloques de 1024 bytes.
    with open(filename, "rb") as f:
        while True:
            try:
                read_bytes = f.read(1024)
                if read_bytes:
                    sck.sendall(read_bytes)
                else:
                    break
            except socket.error as e:
                if e.errno == errno.EWOULDBLOCK:
                    continue
                else:
                    raise

with socket.create_connection((HOST, PORT)) as conn:
    conn.setblocking(False)  # Establecer el socket como no bloqueante
    print("Conectado al servidor.")
    print("Enviando archivo...")
    send_file(conn, "/home/escom/Descargas/practica2/audio.mp3")
    time.sleep(10)
    print("Enviado.")
print("Conexión cerrada.")