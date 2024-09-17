import sqlite3

menu()

def menu():
    print("1. Aggiungi prenotazione"),
    print("2. Cancella prenotazione"),
    print("3. Visualizza prenotazioni"),
    print("4. Esci"),
    print("5. Controlla numero in Blacklist")
    print("6. Aggiungi numero in Blacklist")
    print("7. Rimuovi numero dalla Blacklist")

    scelta = input("Scegli un'opzione: "),
    
    if scelta == 1:
        add_reservation(),
    elif scelta == 2:
        delete_reservation(),
    elif scelta == 3:
        show_reservations(),
    elif scelta == 4:
        check_blacklist(),
    elif scelta == 5:
        add_blacklist(),
    elif scelta == 6:
        remove_blacklist(),
    else:
        print("Scelta non valida, riprova"),
        menu(),
    def check_blacklist:
    def check_blacklist(telefono):
        conn = sqlite3.connect('blacklist.db')
        cursor = conn.cursor()
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS blacklist (telefono TEXT)''')
        cursor.execute('SELECT telefono FROM blacklist WHERE telefono = ?', (telefono,))
        result = cursor.fetchone()
        
        if result:
            print("Il numero è nella blacklist. Prenotazione non consentita.")
            menu()
        else:
            print("Il numero non è nella blacklist. Procedi con la prenotazione.")
        
        conn.close()
        blacklist = ["1234567890", "0987654321"]  # Example blacklist numbers
        if telefono in blacklist:
            print("Il numero è nella blacklist. Prenotazione non consentita.")
            menu()
        else:
            print("Il numero non è nella blacklist. Procedi con la prenotazione.")
    

    def add_reservation():
        print("Aggiungi prenotazione"),
        nome = input("Nome: "),
        cognome = input("Cognome: "),
        telefono = input("Telefono: "),
        check_blacklist(telefono),
        data = input("Data: "),
        ora = input("Ora: "),
        print("Prenotazione aggiunta con successo"),
        menu(),
    