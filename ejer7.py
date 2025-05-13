import threading
import random
lista1 = [random.randint(1, 10) for _ in range(10)]
lista2 = [random.randint(1, 10) for _ in range(10)]
producto_total=1
lock = threading.Lock()

def calcular_producto(inicio, fin):
    global producto_total
    producto_parcial = 1
    for i in range(inicio, fin):
        producto_parcial *= lista1[i] * lista2[i]
    with lock:
        producto_total *= producto_parcial

def main():
    mitad = len(lista1)// 2
    hilo1 = threading.Thread(target=calcular_producto, args=(0, mitad))
    hilo2 = threading.Thread(target=calcular_producto, args=(mitad, len(lista1)))

    hilo1.start()
    hilo2.start()

    hilo1.join()
    hilo2.join()

    print(f"Producto total de los elementos emparejados: {producto_total}")

if __name__ == "__main__":
    main()