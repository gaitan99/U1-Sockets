import socket
import socketserver
import socket
import time
#Autor : Antonio Gaitán Mansilla

#Cliente que envia un número fijo de peticiones (creación de sockets) y
#según la respuesta del servidor se da como ayudado o no
#se guarda un el número de peticiones que han sido atendidas
#y se calcula el porcentaje

host,port = "localhost", 5088
data = "ayuda"
requests = 5
requestsTime = 6
requestsCompleted = 0

for petitions in range(0, requests):    
    #Create a socket who asks
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sockAsking:

        socket.setdefaulttimeout(requestsTime)
        try:
            #Connect to server and sen data
            sockAsking.connect((host, port))
            print('Asking help to server...')
            sockAsking.sendall(bytes(data +"\n", "utf-8")) #coding
            #receive data from server
            received = str(sockAsking.recv(1024), "utf-8")
            #print(received)
        except (socket.timeout):
            print('Petition  time expired')

        finally:
            #split our data received
            x = received.split(',')
            #print(x)
            cont = 0
            if x[0] == "Accepted":
                cont = cont + 1
            if x[1] == "Accepted": 
                cont = cont + 1
            if x[2] == "Accepted": 
                cont = cont + 1
            if cont >= 2 : 
                print("Petition accepted by atleast 2 \n")
                requestsCompleted = requestsCompleted + 1
            else: print("Petition ignored \n")

print('Number of petitions: ' ,requests)
print('Number of petitions supported: ' ,requestsCompleted)
print('Percentatge of petitions supported: ', (requestsCompleted/requests)*100)



