# U1-Sockets

Programa de python basado en sockets que simula una comunicación asincrona entre agentes en un canal compartido. Este programa está basado en hilos y cada conexión con el servidor representa una hilo de ejecución.

  Agentes:
**-Cliente.** Realiza varias peticiones de ayuda, cada una con un tiempo de expiración      aleatorio, que que buscan recibir respuesta de almenos dos servidores diferentes

**-Servidor.** Estos solo leen el canal entre intervalos de tiempo aleatorios y únicamente responden a la última petición recibida.

** -Servidor Principal.** Es el que se encarga de realizar todo el procesado de información entre cliente-servidor.

**Funcionamiento**:
1. Ejecutar en un terminal el programa askServer.py que es el servidor principal
2. Ejecutar en terminales diferentes tantos server.py queremos, cabe indicar que el número mínimo de servidores para que una petición sea aceptada es de 2, y el máximo número de servidores en activo a la vez es 3.
3. Ejecutar client.py este realizará 5 peticiones a askServer y posteriormente indicará el porcentaje de peticiones aceptadas.
