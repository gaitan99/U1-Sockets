#Creación del socket servidor que acepta las peticiones de los clientes.
import socket

#Dirección y puerto al que se va a conectar el host.
host = '127.0.0.1'
port = 1233
#Identificador del socket para diferenciarse de los clientes dentro del servidor principal
name = 'server'
# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ClientSocket:
    ClientSocket = socket.socket()

    print('Waiting for connection')
    try:
        ClientSocket.connect((host, port))
    except socket.error as e:
        print(str(e))
    Response = ClientSocket.recv(2048)
    while True:
        ClientSocket.send(str.encode(name))
        Response = ClientSocket.recv(2048)
        print(Response.decode('utf-8'))
        