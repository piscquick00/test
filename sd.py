#!/usr/bin/env python3
import socket

HOST = '0.0.0.0'  # Ascolta su tutte le interfacce di rete
PORT = 4444        # La porta su cui ascoltare

# Crea il socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # Associa la porta
    s.listen(1)  # Inizia ad ascoltare
    print(f"Mi metto in ascolto sulla porta {PORT}...")

    while True:
        conn, addr = s.accept()  # Accetta connessioni
        with conn:
            print(f"Connessione ricevuta da {addr}")
            while True:
                data = conn.recv(1024)  # Ricevi i dati
                if not data:
                    break
                print(f"Dati ricevuti: {data.decode('utf-8')}")
                conn.sendall(data)  # Ritorna i dati ricevuti
