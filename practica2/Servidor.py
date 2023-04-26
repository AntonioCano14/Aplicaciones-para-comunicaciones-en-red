import socket
import struct
import selectors

# Configuración del servidor
HOST = "127.0.0.1"
PORT = 65432
BUFFER_SIZE = 1024

def receive_file_size(sck: socket.socket):
    # Esta función se asegura de que se reciban los bytes
    # que indican el tamaño del archivo que será enviado,
    # que es codificado por el cliente vía struct.pack(),
    # función la cual genera una secuencia de bytes que
    # representan el tamaño del archivo.
    fmt = "<Q"
    expected_bytes = struct.calcsize(fmt)
    received_bytes = 0
    stream = bytes()
    while received_bytes < expected_bytes:
        chunk = sck.recv(expected_bytes - received_bytes)
        if not chunk:
            # Si no se reciben datos, la conexión se ha cerrado
            raise ConnectionError("La conexión se ha cerrado inesperadamente.")
        stream += chunk
        received_bytes += len(chunk)
    filesize = struct.unpack(fmt, stream)[0]
    return filesize

def receive_file(sck: socket.socket, filename):
    # Leer primero del socket la cantidad de 
    # bytes que se recibirán del archivo.
    filesize = receive_file_size(sck)
    # Abrir un nuevo archivo en donde guardar
    # los datos recibidos.
    with open(filename, "wb") as f:
        received_bytes = 0
        # Recibir los datos del archivo en bloques de
        # 1024 bytes hasta llegar a la cantidad de
        # bytes total informada por el cliente.
        while received_bytes < filesize:
            chunk = sck.recv(BUFFER_SIZE)
            if not chunk:
                # Si no se reciben datos, la conexión se ha cerrado
                raise ConnectionError("La conexión se ha cerrado inesperadamente.")
            f.write(chunk)
            received_bytes += len(chunk)

# Crear socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
server_socket.setblocking(False)  # Establecer modo no bloqueante

# Crear objeto selector
selector = selectors.DefaultSelector()
# Registrar el socket del servidor para eventos de lectura
selector.register(server_socket, selectors.EVENT_READ)

print("Esperando clientes...")

# Esperar conexiones de clientes
while True:
    # Esperar a que se produzcan eventos de lectura o escritura
    events = selector.select()
    for key, _ in events:
        if key.fileobj == server_socket:
            # Nuevo cliente conectado
            conn, address = server_socket.accept()
            print(f"{address[0]}:{address[1]} conectado.")
            # Registrar el nuevo socket de cliente para eventos de lectura
            selector.register(conn, selectors.EVENT_READ)
        else:
            # Cliente existente listo para leer
            try:
                conn = key.fileobj
                receive_file(conn, "/home/escom/Descargas/practica2/audio-recibido.mp3")
                print("Archivo recibido.")
                conn.close()
                # Deregistrar el socket del cliente
                selector.unregister(conn)
            except BlockingIOError:
                # No hay datos para leer, continuar
                pass
            except ConnectionError as e:
                # Manejar error de conexión
                print(str(e))
                conn.close()
                # Deregistrar el socket del cliente
                selector.unregister(conn)
            except KeyboardInterrupt:
                print("Conexion Interrumpida")
        # Manejar interrupción de teclado (Ctrl + C) para cerrar