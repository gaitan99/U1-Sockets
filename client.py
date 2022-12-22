#Creación de un socket cliente que envia petición al askServer que gestiona las peticiones
#y este le responde en caso de que la petición haya sido aceptada por almenos
#dos servidores mas en caso de no recibir respuesta el socket delvolverá una 
#excepción de timeout.

import socket

#Dirección y puerto al que se va a conectar el socket.
host = '127.0.0.1'
port = 1233
#Identificador del socket para diferenciarse de los servidores dentro del servidor principal
name = 'client'

#Timeout de las peticiones
timeout = 3.0
#Número de peticiones a realizar
helpreq = 5
#Número de peticiones completadas con exito.
requestsCompleted = 0

#Bucle que envía las 5 peticiones al servidor principal
for requests in range(0, helpreq):
    print("Enviado petición número : " ,requests + 1)
    # Create a socket (SOCK_STREAM means a TCP socket)
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ClientSocket:
                #Establecemos un timeout para el socket
                ClientSocket.settimeout(timeout)
                print('Waiting for connection')
                try:
                    #Establecemos conexión socket - askServer
                    ClientSocket.connect((host, port))
                except socket.error as e:
                    print(str(e))
                Response = ClientSocket.recv(2048)
                #Enviamos identificador
                ClientSocket.send(str.encode(name))
                Response = ClientSocket.recv(2048)
                print(Response.decode('utf-8'))

                Response = ClientSocket.recv(2048)
                print(Response.decode('utf-8'))
                #Petición aceptada
                if(Response.decode('utf-8')):
                    requestsCompleted += 1
                ClientSocket.close()

    except KeyboardInterrupt:
        print("KeyboardInterrupt")

    except TimeoutError:
        print("Request timeout")

print('Numero de peticiones: ' ,helpreq)
print('Numero de peticiones aceptadas: ' ,requestsCompleted)
print('Porcentaje de peticiones aceptadas:  ', (requestsCompleted/helpreq)*100)





