import threading
SIZE = 1000
A=[[i+j for j in range(SIZE)] for i in range(SIZE)]
B=[[i-j for j in range(SIZE)] for i in range(SIZE)]
C=[[0] * SIZE for _ in range(SIZE)]
lock = threading.Lock()
def sumar_fila(i):
    global C
    for j in range(SIZE):
        suma = A[i][j] + B[i][j]
        with lock:
            C[i][j] = suma
hilos = []
for i in range(SIZE):
    hilo = threading.Thread(target=sumar_fila, args=(i,))
    hilos.append(hilo)
    hilo.start()
for hilo in hilos:
    hilo.join()
print("Matriz resultado (primeras 5 filas):")
for fila in C[:5]:
    print(fila[:5])