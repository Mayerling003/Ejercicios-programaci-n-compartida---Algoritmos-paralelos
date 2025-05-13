import threading
suma_total=0

lock=threading.Lock()

def sumar_rango(inicio, fin):
    global suma_total
    suma_parcial = sum(range(inicio, fin + 1))
    with lock:
        suma_total += suma_parcial

def main():
    mitad = 500_000
    hilo1 = threading.Thread(target=sumar_rango, args=(1, mitad))
    hilo2 = threading.Thread(target=sumar_rango, args=(mitad + 1, 1_000_000))
    hilo1.start()
    hilo2.start()
    hilo1.join()
    hilo2.join()

    print(f"La suma total de los primeros 1,000,000 números es: {suma_total}")

if __name__ == "__main__":
    main()
