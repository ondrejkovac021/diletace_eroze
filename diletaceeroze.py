import random

# Generování 3x3 matice náhodných čísel v rozsahu 1-10
matice = [[random.randint(1, 10) for j in range(3)] for i in range(3)]

def dilate(x=None, y=None):
    # Dilatace prvku na zadané pozici (x, y)
    if x is not None and y is not None:
        if matice[x][y] < 10:
            matice[x][y] += 1
    else:
        # Dilatace celé matice
        for i in range(3):
            for j in range(3):
                if matice[i][j] < 10:
                    matice[i][j] += 1

def erode(x=None, y=None):
    # Eroze prvku na zadané pozici (x, y)
    if x is not None and y is not None:
        if matice[x][y] > 1:
            matice[x][y] -= 1
    else:
        # Eroze celé matice
        for i in range(3):
            for j in range(3):
                if matice[i][j] > 1:
                    matice[i][j] -= 1

while True:
    # Výpis aktuálního stavu matice
    print("matice:")
    for row in matice:
        print(row)
    
    # Uživatelský vstup pro volbu operace
    choice = input(":(d) dilatace, (e) eroze, (k) konec: ")
    
    # Rozhodovací blok pro provádění dilatace, eroze nebo ukončení programu
    if choice == 'd':
        # Uživatelský vstup pro souřadnice pro dilataci
        pos = input("souřadnice pro dilataci (x,y), Enter pro dilataci celé matice: ")
        if pos:
            x, y = map(int, pos.split(","))
            dilate(x, y)
        else:
            dilate()
    elif choice == 'e':
        # Uživatelský vstup pro souřadnice pro erozi
        pos = input("souřadnice pro erozi (x,y), Enter pro erozi celé matice: ")
        if pos:
            x, y = map(int, pos.split(","))
            erode(x, y)
        else:
            erode()
    elif choice == 'k':
        # Ukončení programu
        break
    else:
        # Neplatná volba
        print("špatně")
