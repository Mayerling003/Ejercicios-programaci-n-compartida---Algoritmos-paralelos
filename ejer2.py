import threading
primos = []
lock = threading.Lock()

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def contar_primos(rango):
    for num in rango:
        if es_primo(num):
            with lock:
                primos.append(num)
def sumar_primos():
    while True:
        with lock:
            if terminar_evento.is_set() and not primos:
                break
            suma = sum(primos)
            primos.clear()
        if suma > 0:
            print(f"Suma parcial de primos: {suma}")

terminar_evento = threading.Event()

def main():
    rango = range(1, 10000)  # ajustar el rango aquí

    hilo_contador = threading.Thread(target=contar_primos, args=(rango,))
    hilo_suma = threading.Thread(target=sumar_primos)

    hilo_contador.start()
    hilo_suma.start()

    hilo_contador.join()
    terminar_evento.set()  
    hilo_suma.join()

    print("Proceso completo.")

if __name__ == "__main__":
    main()
