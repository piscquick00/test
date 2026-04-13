#!/usr/bin/env python3
import socket

# Impostazioni di configurazione
HOST = '0.0.0.0'  # Ascolta su tutte le interfacce di rete
PORT = 4444        # La porta su cui ascoltare

# Crea il socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Associa il socket alla porta specificata
    s.bind((HOST, PORT))
    # Inizia ad ascoltare le connessioni
    s.listen(1)
    print(f"Mi metto in ascolto sulla porta {PORT}...")

    while True:
        # Accetta una connessione
        conn, addr = s.accept()
        with conn:
            print(f"Connessione ricevuta da {addr}")
            while True:
                # Ricevi i dati
                data = conn.recv(1024)
                if not data:
                    # Se non ci sono più dati, termina la connessione
                    break
                print(f"Dati ricevuti: {data.decode('utf-8')}")
                # Invia di nuovo i dati al client (echo)
                conn.sendall(data)
