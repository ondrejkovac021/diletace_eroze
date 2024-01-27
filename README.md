# diletace_eroze
Tento kód vytváří 3x3 matici náhodných čísel v rozsahu 1-10 a implementuje operace dilatace a eroze na této matici.
# Funkce
# dilate(x=None, y=None)

    Provede dilataci buňky na zadaných souřadnicích (x, y), pokud jsou specifikovány.
    Pokud nejsou specifikovány žádné souřadnice, provede dilataci celé matice.

# erode(x=None, y=None)

    Provede erozi buňky na zadaných souřadnicích (x, y), pokud jsou specifikovány.
    Pokud nejsou specifikovány žádné souřadnice, provede erozi celé matice.

# Použití

    Matice je inicializována náhodnými čísly v rozsahu 1-10.
    V nekonečné smyčce program vypisuje aktuální stav matice.
    Uživatel má možnost provést dilataci, erozi nebo ukončit program.

# Volby

    (d) dilatace: Umožňuje uživateli provést dilataci na celou matici nebo na konkrétní buňku.
    (e) eroze: Umožňuje uživateli provést erozi na celou matici nebo na konkrétní buňku.
    (k) konec: Ukončí program.

# Příklad použití

    Vytištění aktuální matice.
    Uživatel zadá volbu dilatace (d).
    Uživatel zadá souřadnice dilatace nebo stiskne Enter pro dilataci celé matice.
    Matice je aktualizována podle provedené operace.
    Postup se opakuje, dokud uživatel nezvolí (k) konec.
