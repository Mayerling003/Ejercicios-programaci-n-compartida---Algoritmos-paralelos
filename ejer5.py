import threading
import random
import heapq
lista = [random.randint(1, 1000000) for _ in range(1_000_000)]
sublistas_ordenadas = []
lock = threading.Lock()

def ordenar_sublista(sublista):
    ordenada = sorted(sublista)
    with lock:
        sublistas_ordenadas.append(ordenada)

def fusionar_listas(listas):
    return list(heapq.merge(*listas))

def main():
    num_hilos = 4
    tamaño = len(lista) // num_hilos
    hilos = []
    for i in range(num_hilos):
        inicio = i * tamaño
        fin = (i + 1) * tamaño if i != num_hilos - 1 else len(lista)
        sublista = lista[inicio:fin]
        hilo = threading.Thread(target=ordenar_sublista, args=(sublista,))
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

    lista_ordenada = fusionar_listas(sublistas_ordenadas)

    print("Primeros 20 elementos ordenados:", lista_ordenada[:20])

if __name__ == "__main__":
    main()