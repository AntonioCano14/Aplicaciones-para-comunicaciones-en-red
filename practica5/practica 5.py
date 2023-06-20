import smtplib
import os

def enviar_correo(destinatario, mensaje):
    servidor_smtp = 'smtp.gmail.com'    #conecta al servidor SMTP de gmail
    puerto_smtp = 587 #Cifrado (TLS) / 465 (SSL)
    usuario_smtp = 'antoniocncortazar@gmail.com'    #Remitente
    contraseña_smtp = 'nluhuywfcnxopmve'            #Contraseña

    conexion_smtp = smtplib.SMTP(servidor_smtp, puerto_smtp) #Establece la conexion con el servidor SMTP establecido
    conexion_smtp.starttls()    #Se inicia la conexion segura con TLS
    conexion_smtp.login(usuario_smtp, contraseña_smtp)  #Se logea el remitente

    print(f"Server: {conexion_smtp.ehlo()[1]}") #ehlo sirve para identificarse y mostrar informacion sobre sus capacidades, [1] es el segundo elemento de la tupla y es el mensaje de respuesta 
    print(f"Client: HELO {servidor_smtp}") #muestra el servidor SMPT al que esta conectado
    print(f"Server: {conexion_smtp.helo()[1]}") #lo mismo que ehlo pero no tan detallado

    print(f"Client: MAIL FROM:<{usuario_smtp}>") #muestra el remitente
    print(f"Server: {conexion_smtp.mail(usuario_smtp)[1]}") #verifica si se acepto correctamente el correo del remitente

    print(f"Client: RCPT TO:<{destinatario}>") #muestra el destinatario
    print(f"Server: {conexion_smtp.rcpt(destinatario)[1]}") #verifica si se acepto correctamente el correo del destinatario

    print(f"Client: DATA")
    print(f"Server: {conexion_smtp.data(mensaje)[1]}") #verifica si se acepto correctamente el MENSAJE que se envio

    print("Client: ...sends body of mail message, which can contain")
    print("Client: ...arbitrarily many lines of text")
    print("Client: <CR><LF>.<CR><LF>")

    # Crear la carpeta de bandeja de entrada del usuario si no existe
    carpeta_usuario = destinatario.split('@')[0] #se elimina todo despues del @
    if not os.path.exists(carpeta_usuario):
        os.mkdir(carpeta_usuario)

    # Guardar el mensaje en un archivo dentro de la carpeta del usuario
    archivo_mensaje = os.path.join(carpeta_usuario, 'mensaje.txt')
    with open(archivo_mensaje, 'w') as archivo:
        archivo.write(mensaje)

    conexion_smtp.sendmail(usuario_smtp, [destinatario], mensaje) #se envia el remitente, destinatario y el mensaje

    print(f"Server: {conexion_smtp.quit()[1]}") #se cierra la conexion

destinatario = 'antoniocncrtzr91@gmail.com'
mensaje = '''
De: antoniocncortazar@gmail.com
Para: antoniocncrtzr91@gmail.com
Asunto: Prueba de correo

Hola,

Este es un ejemplo de mensaje de correo enviado mediante Python.

Saludos,
Tu Nombre
'''

enviar_correo(destinatario, mensaje)
