import threading
import queue
import time
import random
cola_tareas=queue.Queue()
NUM_HILOS=5
print_lock=threading.Lock()

def procesar_tarea(tarea_id):
    tiempo = random.uniform(0.1, 0.5)
    time.sleep(tiempo)
    with print_lock:
        print(f"Hilo {threading.current_thread().name} procesó tarea {tarea_id} en {tiempo:.2f} segundos")

def trabajador():
    while True:
        try:
            tarea = cola_tareas.get(timeout=1) 
            procesar_tarea(tarea)
            cola_tareas.task_done()
        except queue.Empty:
            break

def main():
    for i in range(10):
        cola_tareas.put(i)
    hilos = []
    for i in range(NUM_HILOS):
        hilo = threading.Thread(target=trabajador, name=f"Trabajador-{i+1}")
        hilos.append(hilo)
        hilo.start()

    cola_tareas.join()
    print("Todas las tareas han sido procesadas.")

if __name__ == "__main__":
    main()