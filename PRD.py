# PRD.py

# Importa las bibliotecas necesarias
import socket
import os


# Define una función para limpiar la consola
def cls():
    os.system("cls" if os.name == "nt" else "clear")


# Define la dirección IP y el puerto del servidor
HOST = "192.168.1.11"
PORT = 6666

# Crea un nuevo socket, lo vincula a la dirección IP y puerto especificados, y comienza a escuchar conexiones
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(random.randint(1, 10))

    exit = False
    while exit == False:
        cls()
        print(f"Servidor escuchando en {HOST}:{PORT}...")
        connection, client_address = sock.accept()
        print(f"Cliente conectado desde {client_address}")

        # Entra en un bucle hasta que reciba "s" del cliente
        while True:
            data = connection.recv(1024).decode("utf-8")

            if data != "":
                print(f"Recibido {data} de {client_address}")

            if data.lower() == "s":
                print(f"El cliente {client_address} se ha desconectado")
                if input("Quiere seguir esperando por conexiones (S/N)").lower() == "n":
                    exit = True
            connection.sendall(data.encode("utf-8"))

# Maneja la interrupción del usuario para detener el servidor
except KeyboardInterrupt:
    print("\nServidor detenido por el usuario.")
finally:
    # Cierra la conexión y termina el programa
    connection.close()
    sock.close()
    print("Servidor desconectado")
