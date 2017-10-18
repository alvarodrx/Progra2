import threading

def contar(numero):
    contador = 0
    while contador<10:
        contador+=1
        print(numero, threading.get_ident(), contador)

for numero in range(1, 11):
    hilo = threading.Thread(target=contar,
                            args=(numero,),
                            daemon=True)
    hilo.start()

# Obtiene hilo principal

hilo_ppal = threading.main_thread()

# Recorre hilos activos para controlar estado de su ejecución

for hilo in threading.enumerate():

    # Si el hilo es hilo_ppal continua al siguiente hilo activo

    if hilo is hilo_ppal:
        continue

    # Se obtiene información hilo actual y núm. hilos activos

    print(hilo.getName(),
          hilo.ident,
          hilo.isDaemon(),
          threading.active_count())

    # El programa esperará a que este hilo finalice:

    hilo.join()