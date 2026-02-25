print("")
eingabe = input("Was möchtest du machen? ")

while True:
    if == 1:

    elif == 2

    elif == 0:
        break

noten = {}



while True:
    print("Notenverwaltung")
    print("1 ... Fächer mit zugehörigen Noten eingeben")
    print("2 ... Notendurchschnitt berechnen")
    print("3 ... Drei besten Fächer mit Noten ausgeben und den zugehörigen Notendurchschnitt berechnen.")
    print("4 ... Drei schlechtesten Fächer mit Noten ausgeben und den zugehörigen Notendurchschnitt berechnen.")
    print("5 ... Bonus: Nach Fächern suchen und den zugehörigen Notendurschnitt berechnen.")
    print("0 ... Exit")

    eingabe = int(input("Ihre eingabe"))

    if eingabe == 0:
        break

    elif eingabe == 1:
        fach = input("Fach: ")
        note = float(input("Note: "))
        noten[fach] = note
    
    elif eingabe == 2:
        durchschnitt = sum(noten.values()) / len(noten)
        print("Durchschnitt:", durchschnitt)

#Dies sortiert den Inhalt des Dictionaries, lambda ist ein Schlüsselwort zur Erstellung kleiner, 
#anonymer Funktionen die nur eine Zeile lang sind, Direkt definiert, meistens mit map(), filter() oder sorted() verwendet. automatisch zurückgegeben.

    elif eingabe == 3:
        beste = sorted(noten.items(), key=lambda x: x[1], reverse=True)
        top3 = beste[:3]
        for fach, note in top3:
            print(fach, note)
    
    elif eingabe == 4:
        schlecht = sorted(noten.items(), key=lambda x: x[1])
        bot3 = schlecht[:3]
        for fach, note in bot3:
            print(fach, note)

    elif eingabe == 5:
        suchtext = input("Suchbegriff fürs Fach: ").strip().lower()
        treffer = [(fach, note) for fach, note in noten.items()
                   if suchtext in fach.lower()]