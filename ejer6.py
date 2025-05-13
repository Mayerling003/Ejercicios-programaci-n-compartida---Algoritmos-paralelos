import threading
contador=0
lock = threading.Lock()
def incrementar_contador():
    global contador
    for _ in range(100):
        with lock:
            contador += 1

def main():
    hilos = []
    for _ in range(1000):
        hilo = threading.Thread(target=incrementar_contador)
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print(f"Valor final del contador: {contador}")

if __name__ == "__main__":
    main()