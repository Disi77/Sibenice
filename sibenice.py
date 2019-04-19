from random import choice


def uvod():
    'Úvodní informace ke hře.'
    print('''
******************
*                *
*    ŠIBENICE    *   Hádej slovo, když se spleteš, staví se šibenice.
*                *
******************
    ''')


def slovo_nahoda():
    '''
    Funkce generuje náhodné slovo pro hru.
    '''
    slova = ('program', 'python', 'notebook', 'parametr', 'abeceda', 'procesor', 'funkce', 'proměnná', 'argument', 'příkaz', 'řetězec', 'cyklus')
    return choice(slova)


def nahrad_pismeno(pismeno, vybrane_slovo, pole):
    '''
    Najde pozice písmene ve slově a na stejných pozicích
    nahradí znak "-" zvoleným písmenem v poli.
    '''
    opakovani = vybrane_slovo.count(pismeno)
    hledam_od = 0
    for x in range(opakovani):
        pozice = vybrane_slovo.index(pismeno, hledam_od)
        pole = pole[:pozice] + pismeno + pole[pozice+1:]
        hledam_od = pozice+1
    return pole


def sibenice_obrazek(pocet_pokusu):
    '''
    Funkce si stáhne ze souboru obrazky pro hru šibenice
    a na základě značek (čísel), které jsou v souboru vložené,
    najde ten správný obrázek pro daný počet pokusů.
    '''
    with open('obrazky.txt', encoding='utf-8') as soubor:
        obsah = soubor.read()
    zacatek = obsah.index(str(pocet_pokusu))
    konec = obsah.index(str(pocet_pokusu+1))
    print(obsah[zacatek+1:konec])


def konec(pole, pocet_pokusu):
    '''
    Funkce po každém tahu hráče testuje, zda nastaly tyto možnosti:
      vyhra = hráč uhodl všechna písmena
      prohra = v poli jsou ještě neuhádnutá písmena (znak "-") a zároveň
               počet špatných pokusů hráče je 10 a více
      hra_pokracuje = výše uvedené možnosti zatím nanastaly
    '''
    if '-' not in pole:
        return('vyhra')
    elif pocet_pokusu >= 10:
        return('prohra')
    else:
        return('hra_pokracuje')


def uzivatel_zada_pismeno():
    while True:
        pismeno = input('Vyber písmeno: ')
        pismeno = pismeno.lower()
        if len(pismeno) != 1:
            print('Musíš vybrat jedno písmeno. Zkus to znovu.')
        elif pismeno not in 'aábcčdďeéěfghiíjklmnňopqrsštťuvwxyýzž':
            print('Musíš vybrat jedno písmeno. Zkus to znovu.')
        else:
            return pismeno


def ano_ne(question):
    '''
    Funkce, která chce po uživateli ano (vrátí True) nebo ne (vrátí False).
    '''
    while True:
        answer = input(question)
        if answer.lower().strip() in ['ano', 'a']:
            return True
        elif answer.lower().strip() in ['ne', 'n']:
            return False
        else:
            print('Nerozumím! Odpověz "ano" nebo "ne".')


def hra():
    '''
    Samotná hra, která spojuje všechny ostatní funkce.
    '''
    while True:
        uvod()
        vybrane_slovo = slovo_nahoda()
        pole = ('-'*len(vybrane_slovo))
        print('Hledáme slovo <{}>.'.format(pole))
        pocet_pokusu = 0
        while True:
            pismeno = uzivatel_zada_pismeno()
            if pismeno in vybrane_slovo:
                pole = nahrad_pismeno(pismeno, vybrane_slovo, pole)
                print('Hledáme slovo <{}>.'.format(pole))
            else:
                pocet_pokusu += 1
                print('Pismeno "{}" není ve slově. Staví se {}. část (z 10) šibenice.'.format(pismeno.upper(), pocet_pokusu))
                sibenice_obrazek(pocet_pokusu)
                print('Hledáme slovo <{}>.'.format(pole))
            if konec(pole, pocet_pokusu) == 'prohra':
                print('\nPROHRÁL JSI, ZKUS TO ZNOVU.')
                print('\nHledané slovo bylo {}.'.format(vybrane_slovo.upper()))
                break
            elif konec(pole, pocet_pokusu) == 'vyhra':
                print('\nVYHRÁL JSI. GRATULUJI.')
                break
            # Pokud nenastala výhra ani prohra, hraje se dále
        if ano_ne('Chceš hrát ještě jednou? Odpověz "ano" nebo "ne".'):
            pass
        else:
            print('Tak příště, ahoj.')
            break


hra()
