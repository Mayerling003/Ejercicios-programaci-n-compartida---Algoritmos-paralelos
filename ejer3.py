import threading
import random

lista = [random.randint(1, 10) for _ in range(10_000_000)]
suma_total = 0
lock = threading.Lock()  # Para proteger el acceso a suma_total

def sumar_parte(inicio, fin):
    global suma_total
    subtotal = sum(lista[inicio:fin])
    with lock:
        suma_total += subtotal

def main():
    mitad = len(lista) // 2
    hilo1 = threading.Thread(target=sumar_parte, args=(0, mitad))
    hilo2 = threading.Thread(target=sumar_parte, args=(mitad, len(lista)))

    hilo1.start()
    hilo2.start()

    hilo1.join()
    hilo2.join()

    print(f"Suma total: {suma_total}")
    suma_correcta = sum(lista)
    print(f"Suma correcta: {suma_correcta}")

    if suma_total != suma_correcta:
        print("ERROR por condicion de carrera detectado")
    else:
        print("No se detecto condicion de carrera.")

if __name__ == "__main__":
    main()
