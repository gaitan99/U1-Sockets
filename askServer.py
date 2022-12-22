#Autor: Antonio Gaitán Mansilla
#Servidor principal que se encarga de la comunicación
#entre los sockets clientes y los sockets servidores

import socket
import threading
from _thread import *
import time
import random

#Dirección y puerto del servidor
host = '127.0.0.1'
port = 1233

#Contador de Threads
ThreadCount = 0

#Contador de servidores activos
ServerCount = 0

#Correspondiente a "Servidor 1, Servidor 2 y Servidor 3" 
#y nos va a indicar si el respectivo servidor ha aceptado la petición del cliente
buff = [False,False,False]

#Nos va a indicar cuando un servidor ha aceptado una petición de un cliente
update = False


def client_handler(connection):
    connection.send(str.encode('You are now connected to the replay server... Type BYE to stop'))

    global ThreadCount
    global ServerCount
    global buff
    global update

    ThreadCount += 1
    print ("Thread num"+ str(ThreadCount))
    print(buff)
    print(f'Numero de servidores {ServerCount} : ')
    print(buff)

    data = connection.recv(2048)
    message = data.decode('utf-8')

    #En caso de que la connexión sea de un socket servidor
    if message == 'server':

        ServerCount += 1
        ServerNum = ServerCount

        if(ServerCount > 3):
            ServerCount -= 1
            print("Capacidad de servidores llena")
            return
            
        reply = f'Server: {message}'

        connection.sendall(str.encode(reply))
        print(f'Numero de servidores {ServerNum} : ')
        print(f'Servidor {ServerNum} pendiente de ayuda')


        while True:
            #Dormimos al servidor por un tiempo aleatorio
            time.sleep(random.randrange(0,10))

            #Una vez despierta el servidor acepta la petición
            buff[ServerNum - 1] = True
            print(f'Servidor {ServerNum} está operativo')
            print(f'Servidor {ServerNum} ofrece ayuda')
            update = True
            print(f'Servidor {ServerNum} está dormido')

    #en caso de que la conexión se ha un socket cliente
    elif message == 'client':
        #Reiniciamos la petición ya que solo nos interesa la última petición recibida
        buff = [False,False,False]

        reply = f'Server: {message}'
        connection.sendall(str.encode(reply))
        print("Cliente pidiendo ayuda")
        print(buff)

        #En caso de que algún servidor acepte la petición
        #el flag update será True y en caso de que almenos
        #dos servidores hayan aceptado la petición se le enviará
        #una confimación de la petición.
        while True:
            cont = 0
            if update == False:
                update = False
                #print ("Nadie actualiza")
            else:
                print(buff)
                for x in range(len(buff)):
                        if(buff[x] == True):
                            cont += 1
                if(cont >= 2):
                    print("La petición del cliente ha sido aceptada")
                    reply = 'aceptada'
                    connection.sendall(str.encode(reply))
                    cont = 0
                    break
                else:
                    update = False

#Función que permite a los sockets cliente y servidor conectarse
#Crea un nuevo hilo para cada socket cada vez que hay una conexión.
def accept_connections(ServerSocket):
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(client_handler, (Client, ))

#Definición de askServer 
def start_server(host, port):
    ServerSocket = socket.socket()
    try:
        ServerSocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    print(f'Server is listing on the port {port}...')
    ServerSocket.listen()
    ThreadCount = 0  
    #Bucle infinito que nos permite que se conecten siempre     
    while True:
            accept_connections(ServerSocket)

start_server(host, port)

    
