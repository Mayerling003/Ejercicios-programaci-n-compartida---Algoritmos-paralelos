import threading
import random

lista = [random.randint(1, 100) for _ in range(1_000_000)]
suma_total = 0
lock = threading.Lock()

def sumar_rango(inicio, fin):
    global suma_total
    suma_parcial = sum(lista[inicio:fin])
    with lock:
        suma_total += suma_parcial

def main():
    mitad = len(lista) // 2
    hilo1 = threading.Thread(target=sumar_rango, args=(0, mitad))
    hilo2 = threading.Thread(target=sumar_rango, args=(mitad, len(lista)))

    hilo1.start()
    hilo2.start()

    hilo1.join()
    hilo2.join()

    media = suma_total / len(lista)
    print(f"La media de los 1 000 000 de números es: {media:.2f}")

if __name__ == "__main__":
    main()
