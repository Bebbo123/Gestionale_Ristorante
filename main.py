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
        exit(),
    elif scelta == 5:
        check_blacklist(),
    elif scelta == 6:
        add_blacklist(),
    elif scelta == 7:
        remove_blacklist(),
    else:
        print("Scelta non valida, riprova"),
        menu(),
    
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