noten = {}

while True:
    print("\nNotenverwaltung")
    print("1 ... Fächer mit zugehörigen Noten eingeben")
    print("2 ... Notendurchschnitt berechnen")
    print("3 ... Drei besten Fächer mit Noten ausgeben")
    print("4 ... Drei schlechtesten Fächer mit Noten ausgeben")
    print("5 ... Bonus: Nach Fächern suchen und Durchschnitt der Treffer berechnen")
    print("0 ... Exit")

    eingabe = input("Ihre Eingabe: ").strip()

    if not eingabe.isdigit():
        print("Bitte eine Zahl eingeben.")
        continue

    eingabe = int(eingabe)

    if eingabe == 0:
        break

    elif eingabe == 1:
        fach = input("Fach: ").strip()
        note = float(input("Note: "))
        noten[fach] = note

    elif eingabe == 2:
        if len(noten) == 0:
            print("Noch keine Noten erfasst.")
        else:
            durchschnitt = sum(noten.values()) / len(noten)
            print("Durchschnitt:", round(durchschnitt, 2))

    elif eingabe == 3:
        if len(noten) == 0:
            print("Noch keine Noten erfasst.")
        else:
            top3 = sorted(noten.items(), key=lambda x: x[1], reverse=True)[:3]
            for fach, note in top3:
                print(fach, note)

    elif eingabe == 4:
        if len(noten) == 0:
            print("Noch keine Noten erfasst.")
        else:
            bot3 = sorted(noten.items(), key=lambda x: x[1])[:3]
            for fach, note in bot3:
                print(fach, note)

    elif eingabe == 5:
        if len(noten) == 0:
            print("Noch keine Noten erfasst.")
        else:
            suchtext = input("Suchbegriff fürs Fach: ").strip().lower()
            treffer = [(fach, note) for fach, note in noten.items() if suchtext in fach.lower()]

            if not treffer:
                print("Keine Treffer.")
            else:
                print("Treffer:")
                for fach, note in treffer:
                    print(fach, note)

                avg = sum(note for _, note in treffer) / len(treffer)
                print("Durchschnitt der Treffer:", round(avg, 2))

    else:
        print("Ungültige Eingabe.")