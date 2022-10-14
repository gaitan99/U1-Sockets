import socketserver
import random as rd

#Autor : Antonio Gaitán Mansilla

#Servidor que se encarga de gestionar las peticiones 
#que le llegan y las devuelve al cliente

host,port = "localhost", 5088

class answerHandler(socketserver.BaseRequestHandler):
    def handle(self):

        supportA = "NotAccepted" 
        supportB = "NotAccepted"
        supportC = "NotAccepted"

#Simulación de que los 3 servidores den soporte un 30% de tiempo aleatorio    
        timeSleepA = rd.randint(0,2)
        timeSleepB = rd.randint(0,2)
        timeSleepC = rd.randint(0,2)

        data = self.request.recv(1024).strip()

        print("Petition arrived")
        #En caso de que el agente este "observando" atiende la peticion
        if timeSleepA == 0:
            supportA  = "Accepted"
        if timeSleepB == 0:
            supportB  = "Accepted"
        if timeSleepC == 0:
            supportC  = "Accepted"
        #Send data to socket
        self.request.sendall(bytes(supportA+","+supportB+","+supportC , "utf-8"))
        print("Petition solved")

with socketserver.TCPServer(('', 5088), answerHandler) as answerServer:
    print(' Answer server is running...')
    answerServer.serve_forever()


