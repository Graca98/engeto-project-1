ukoly = ['ukol 1 - teeeeest', 'ukol 2 - ahooooj']
# ukoly = []

def hlavni_menu():
    while True:
        print()
        print('Správce úkolů - Hlavní menu')
        print('1. Přidat nový úkol')
        print('2. Zobrazit všechny úkoly')
        print('3. Odstranit úkol')
        print('4. Konec programu')

        try:
            volba = int(input('Vyberte možnost (1-4) '))
            print()
        except ValueError:
            print()
            print("Neplatné číslo, zkuste to znova")
            continue


        if volba == 1:
            return pridat_ukol()
        elif volba == 2:
            return zobrazit_ukoly()
        elif volba == 3:
            return odstranit_ukol()  
        elif volba == 4:
            print('Konec programu.')
            print()
            return
        else:
            print('Neplatná volba, zkuste to znovu.')

def pridat_ukol():
    while True:
        nazev = input('Zadejte název úkolu: ').strip().capitalize()
        popis = input('Zadejte popis úkolu: ').strip()

        if nazev == "" or popis == "":
            print('Název nebo popis nemůže být prázdný!')
        else:
            ukoly.append(f'{nazev} - {popis}')
            print(f"Úkol '{nazev}' byl přidán.")
            return hlavni_menu()

def zobrazit_ukoly():
    if len(ukoly) == 0:
        print('Seznam úkolů je prázdný. Přidejte nový úkol pomocí čísla 1')
        return hlavni_menu()

    print('Seznám úkolů:')
    index = 1
    for ukol in ukoly:
        print(f'{index}. {ukol}')
        index += 1

    return hlavni_menu()

def odstranit_ukol():
    if len(ukoly) == 0:
        print('Není možné odstranit úkol, seznam úkolů je prázdný!')
        return hlavni_menu()

    while True:
        print('Seznám úkolů:')
        index = 1
        for ukol in ukoly:
            print(f'{index}. {ukol}')
            index += 1
        print()

        cislo = int(input('Zadejte číslo úkolu, který chcete odstranit: '))
        cislo_ukolu = cislo - 1

        if cislo > len(ukoly) or cislo <= 0:
            print('Neplatné číslo úkolu, zkuste to znovu.')
            print()
        else:
            print(f"Úkol '{ukoly[cislo_ukolu].split(" - ")[0]}' byl odstraněn.")
            ukoly.pop(cislo_ukolu)
            return hlavni_menu()
    
hlavni_menu()