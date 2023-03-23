#!/usr/bin python3

import socket
import datetime

HOST = "127.0.0.1"  # Hostname o  dirección IP del servidor
PORT = 5432  # Puerto del servidor
buffer_size = 1024

def busca9x9():
    print ("                 ")
    print ("        1   2   3   4   5   6   7   8   9       ")
    print ("      +---+---+---+---+---+---+---+---+---+       ")
    print ("a     | %c | %c | %c | %c | %c | %c | %c | %c | %c |      " % (N[0], N[1], N[2],N[3], N[4], N[5],N[6], N[7], N[8]) )
    print ("      +---+---+---+---+---+---+---+---+---+       ")
    print ("b     | %c | %c | %c | %c | %c | %c | %c | %c | %c |      " % (N[9], N[10], N[11],N[12], N[13], N[14],N[15], N[16], N[17]) )
    print ("      +---+---+---+---+---+---+---+---+---+       ")
    print ("c     | %c | %c | %c | %c | %c | %c | %c | %c | %c |      " % (N[18], N[19], N[20],N[21], N[22], N[23],N[24], N[25], N[26]) )
    print ("      +---+---+---+---+---+---+---+---+---+       ")
    print ("d     | %c | %c | %c | %c | %c | %c | %c | %c | %c |      " % (N[27], N[28], N[29],N[30], N[31], N[32],N[33], N[34], N[35]) )
    print ("      +---+---+---+---+---+---+---+---+---+       ")
    print ("e     | %c | %c | %c | %c | %c | %c | %c | %c | %c |      " % (N[36], N[37], N[38],N[39], N[40], N[41],N[42], N[43], N[44]) )
    print ("      +---+---+---+---+---+---+---+---+---+       ")
    print ("f     | %c | %c | %c | %c | %c | %c | %c | %c | %c |      " % (N[45], N[46], N[47],N[48], N[49], N[50],N[51], N[52], N[53]) )
    print ("      +---+---+---+---+---+---+---+---+---+       ")
    print ("g     | %c | %c | %c | %c | %c | %c | %c | %c | %c |      " % (N[54], N[55], N[56],N[57], N[58], N[59],N[60], N[61], N[62]) )
    print ("      +---+---+---+---+---+---+---+---+---+       ")
    print ("h     | %c | %c | %c | %c | %c | %c | %c | %c | %c |      " % (N[63], N[64], N[65],N[66], N[67], N[68],N[69], N[70], N[71]) )
    print ("      +---+---+---+---+---+---+---+---+---+       ")
    print ("i     | %c | %c | %c | %c | %c | %c | %c | %c | %c |      " % (N[72], N[73], N[74],N[75], N[76], N[77],N[78], N[79], N[80]) )
    print ("                 ")

def busca16x16():
    print ("                 ")
    print ("        1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  ")
    print ("      +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+       ")
    print ("a     | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c |      " % (M[0], M[1], M[2],M[3], M[4], M[5],M[6], M[7], M[8], M[9], M[10], M[11],M[12], M[13], M[14],M[15]) )
    print ("      +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+       ")
    print ("b     | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c |      " % (M[16], M[17], M[18],M[19], M[20], M[21],M[22], M[23], M[24], M[25], M[26], M[27],M[28], M[29], M[30],M[31]) )
    print ("      +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+       ")
    print ("c     | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c |      " % (M[32], M[33], M[34],M[35], M[36], M[37],M[38], M[39], M[40], M[41], M[42], M[43],M[44], M[45], M[46],M[47]) )
    print ("      +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+       ")
    print ("d     | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c |      " % (M[48], M[49], M[50],M[51], M[52], M[53],M[54], M[55], M[56], M[57], M[58], M[59],M[60], M[61], M[62],M[63]) )
    print ("      +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+       ")
    print ("e     | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c |      " % (M[64], M[65], M[66],M[67], M[68], M[69],M[70], M[71], M[72], M[73], M[74], M[75],M[76], M[77], M[78],M[79]) )
    print ("      +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+       ")
    print ("f     | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c |      " % (M[80], M[81], M[82],M[83], M[84], M[85],M[86], M[87], M[88], M[89], M[90], M[91],M[92], M[93], M[94],M[95]) )
    print ("      +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+       ")
    print ("g     | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c |      " % (M[96], M[97], M[98],M[99], M[100], M[101],M[102], M[103], M[104], M[105], M[106], M[107],M[108], M[109], M[110],M[111]) )
    print ("      +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+       ")
    print ("h     | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c |      " % (M[112], M[113], M[114],M[115], M[116], M[117],M[118], M[119], M[120], M[121], M[122], M[123],M[124], M[125], M[126],M[127]) )
    print ("      +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+       ")
    print ("i     | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c |     " % (M[128], M[129], M[130],M[131], M[132], M[133],M[134], M[135], M[136], M[137], M[138], M[139],M[140], M[141], M[142],M[143]) )
    print ("      +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+       ")
    print ("j     | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c |     " % (M[144], M[145], M[146],M[147], M[148], M[149],M[150], M[151], M[152], M[153], M[154], M[155],M[156], M[157], M[158],M[159]) )
    print ("      +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+       ")
    print ("k     | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c |     " % (M[160], M[161], M[162],M[163], M[164], M[165],M[166], M[167], M[168], M[169], M[170], M[171],M[172], M[173], M[174],M[175]) )
    print ("      +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+       ")
    print ("l     | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c |     " % (M[176], M[177], M[178],M[179], M[180], M[181],M[182], M[183], M[184], M[185], M[186], M[187],M[188], M[189], M[190],M[191]) )
    print ("      +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+       ")
    print ("m     | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c |     " % (M[192], M[193], M[194],M[195], M[196], M[197],M[198], M[199], M[200], M[201], M[202], M[203],M[204], M[205], M[206],M[207]) )
    print ("      +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+       ")
    print ("n     | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c |     " % (M[208], M[209], M[210],M[211], M[212], M[213],M[214], M[215], M[216], M[217], M[218], M[219],M[220], M[221], M[222],M[223]) )
    print ("      +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+       ")
    print ("o     | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c |     " % (M[224], M[225], M[226],M[227], M[228], M[229],M[230], M[231], M[232], M[233], M[234], M[235],M[236], M[237], M[238],M[239]) )
    print ("      +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+       ")
    print ("p     | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c | %c |     " % (M[240], M[241], M[242],M[243], M[244], M[245],M[246], M[247], M[248], M[249], M[250], M[251],M[252], M[253], M[254],M[255]) )
    print ("                 ")

N=['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
M=['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',
'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']

def vividos():
    print("----------Calculadora de dias vividos----------")
    #Solicitar la fecha de nacimiento del usuario
    dia = int(input("Día de nacimiento: "))
    mes = int(input("Mes de nacimiento: "))
    anio = int(input("Año de nacimiento: "))

    # Crear un objeto de tipo datetime.datetime; con la fecha de nacimiento del usuario
    fecha_de_nacimiento = datetime.datetime(anio, mes, dia)
    # Necesitamos la fecha del 8 de marzo del 2023
    fecha_de_hoy = datetime.datetime(2023, 3 , 8)
    diferencia = fecha_de_hoy - fecha_de_nacimiento
    # con el .days unicamente se obtienen los dias de diferencia
    dias_vividos = diferencia.days
    # Preparar un mensaje
    mensaje = "Has vivido {} día(s)".format(dias_vividos)
    # Se obtiene el modulo de 3 para obtener el juego a implementar
    modulo = dias_vividos % 3
    # Imprimirlo y listo
    print(mensaje)
    # Si el modulo es 0 entonces se juega buscaminas
    if modulo == 0:
        print("---------Te toca jugar BUSCAMINAS---------")
        # Se solicita al usuario la IP y el puerto a conectarse
        global HOST
        HOST = input("Ingrese la direccion IP del servidor: ")
        global PORT
        PORT = int(input("Ingrese el puerto del servidor: "))
        
vividos()

TCPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPClientSocket.connect((HOST, PORT))
nivel = input("Ingrese el nivel: ")

if(nivel == "principiante"):
    TCPClientSocket.send(b"principiante")
    data = TCPClientSocket.recv(buffer_size)
    print(data)
    busca9x9()
    while True:
        while True:
            f=input("Fila: ")
            if (f == 'a'):
                f=1
            elif (f == 'b'):
                f=2
            elif (f == 'c'):
                f=3
            elif (f == 'd'):
                f=4
            elif (f == 'e'):
                f=5
            elif (f == 'f'):
                f=6
            elif (f == 'g'):
                f=7
            elif (f == 'h'):
                f=8
            elif (f == 'i'):
                f=9
            else:
                f=0
            if (f>0 and f<10):
                c=int(input("Columna: "))
                if (c>0 and c<10):
                    p=9*(f-1)+(c-1)
                    TCPClientSocket.send(str(p).encode('utf-8'))
                break
            print ("\n Ingrese rango correto")
        
        k=TCPClientSocket.recv(2)
        if (k=='X'):
            N[p]='X'
        else:
            N[p]='*'
        busca9x9()
        gana=TCPClientSocket.recv(1024)
        if (k==b"X"):
            print("\n BOOOOOOOOM!!")
            break
        elif (gana == True):
            print ("\n FELICITACIONES!!!")
            break

if( nivel=="avanzado"):
    TCPClientSocket.send(b"avanzado")
    data = TCPClientSocket.recv(buffer_size)
    print(data)
    busca16x16()
    while True:
        while True:
            f=input("Fila: ")
            if (f == 'a'):
                f=1
            elif (f == 'b'):
                f=2
            elif (f == 'c'):
                f=3
            elif (f == 'd'):
                f=4
            elif (f == 'e'):
                f=5
            elif (f == 'f'):
                f=6
            elif (f == 'g'):
                f=7
            elif (f == 'h'):
                f=8
            elif (f == 'i'):
                f=9
            elif (f == 'j'):
                f=10
            elif (f == 'k'):
                f=11
            elif (f == 'l'):
                f=12
            elif (f == 'm'):
                f=13
            elif (f == 'n'):
                f=14
            elif (f == 'o'):
                f=15
            elif (f == 'p'):
                f=16
            else:
                f=0
            if (f>0 and f<17):
                c=int(input("Columna: "))
                if (c>0 and c<17):
                    p=16*(f-1)+(c-1)
                    TCPClientSocket.send(str(p).encode('utf-8'))
                break
            print ("\n Ingrese rango correto")

        k=TCPClientSocket.recv(2)
        print(k)
        if (k==b'X'):
            M[p]='X'
        else:
            M[p]='*'
        busca16x16()
        gana=TCPClientSocket.recv(1024)
        if (k==b'X'):
            print("\n BOOOOOOOOM!!")
            break
        elif (gana == True):
            print ("\n FELICITACIONES!!!")
            break

print ("\n FIN DEL JUEGO")
TCPClientSocket.close()

