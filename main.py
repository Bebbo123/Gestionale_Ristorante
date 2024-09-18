import sqlite3

def menu():
    while True:
        print("1. Aggiungi prenotazione")
        print("2. Cancella prenotazione")
        print("3. Visualizza prenotazioni")
        print("4. Esci")
        print("5. Controlla numero in Blacklist")
        print("6. Aggiungi numero in Blacklist")
        print("7. Rimuovi numero dalla Blacklist")
        scelta = input("Scegli un'opzione: ")

        if scelta == '1':
            add_reservation()
        elif scelta == '2':
            delete_reservation()
        elif scelta == '3':
            show_reservations()
        elif scelta == '4':
            print("Arrivederci!")
            break
        elif scelta == '5':
            check_blacklist()
        elif scelta == '6':
            add_blacklist()
        elif scelta == '7':
            remove_blacklist()
        else:
            print("Scelta non valida, riprova.")

# Definizione delle altre funzioni
def add_reservation():
    # Codice per aggiungere una prenotazione
    pass

def delete_reservation():
    # Codice per cancellare una prenotazione
    pass

def show_reservations():
    # Codice per visualizzare le prenotazioni
    pass

def check_blacklist():
    # Codice per controllare la blacklist
    pass

def add_blacklist():
    numero = input('Inserisci il numero da aggiungere alla blacklist: ')
    conn = sqlite3.connect('blacklist.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS blacklist (telefono TEXT)''')
    cursor.execute('INSERT INTO blacklist (telefono) VALUES (?)', (numero,))
    conn.commit()
    conn.close()
    print("Numero aggiunto alla blacklist con successo.")

def remove_blacklist():
    # Codice per rimuovere un numero dalla blacklist
    pass

# Chiamata alla funzione menu
menu()
