from collections import deque
import random
import time
import threading
import os
from history import *

gc()


# Inicializa las colas
queue_init = deque()
queue_end = deque()
tiempo_retraso = 5

def generar_numero_aleatorio(rango_inicial=1, rango_final=10):
    return random.randint(rango_inicial, rango_final)


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def add_vehiculo(queue):
    nr = generar_numero_aleatorio()
    # BORRAR
    print(f"numero ramdon: {nr}")

    for i in range(nr):
        queue.append("Vehículo " + str(i + 1))


def vaciar_vehiculos(queue_init, queue_end, tiempo_retraso):
    while queue_init:
        # Agrega un retraso aleatorio en la cola final (entre 1 y 5 segundos)\
        vehiculo_salida = queue_init.popleft()
        queue_end.append(vehiculo_salida)
        
        time.sleep(tiempo_retraso)
        print(f"Vehículo que salió de la cola init: {vehiculo_salida}")


def retirar_vehiculos(queue_end, tiempo_retraso):
    while queue_end:
        # Agrega un retraso aleatorio en la cola final (entre 1 y 5 segundos)
        time.sleep(tiempo_retraso)
        print(f"Vehículo que salió de la cola final: {queue_end.popleft()}")


            
def coloaVehiculo(nr, tiempo_retraso):
    cls()
    # Agrega vehículos
    add_vehiculo(queue_init)

    # Crea un hilo para retirar vehículos
    vaciar_thread = threading.Thread(target=vaciar_vehiculos, args=(queue_init, queue_end, tiempo_retraso))
    vaciar_thread.start()

    # Espera el pirmer tiempo para evitar conflictos
    time.sleep(tiempo_retraso)

    # Crea un hilo para retirar vehículos
    retirar_thread = threading.Thread(target=retirar_vehiculos, args=(queue_end, tiempo_retraso))
    retirar_thread.start()

    # Espera a que ambos hilos terminen
    vaciar_thread.join()
    retirar_thread.join()
