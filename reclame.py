from algemene_functies import mijn_functie2

def aanbieding_1(smaak,prijs,korting):
    na_korting=prijs*(1-korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {na_korting} euro."
def inkomsten_totaal(inkomsten,btw):
    totaal=0
    for getal in inkomsten:
        totaal+=getal
    getal_btw=totaal*btw
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {getal_btw} euro btw betaald dient te worden."
def laag_en_hoog(mijn_lijst):
    lijst=[]
    lijst.append(max(mijn_lijst))
    lijst.append(min(mijn_lijst))
    return lijst
def gemiddelde(mijn_lijst):
    gem=0
    for getal in mijn_lijst:
        gem+=getal
    gem/=7
    return f"De gemiddelde inkomsten deze week zijn {gem} euro."
def meervoudig(invoer_lijst):
    lijst=laag_en_hoog(invoer_lijst)
    return lijst
def combinatie(invoer_lijst_2):
    korte_lijst=laag_en_hoog(invoer_lijst_2)
    return mijn_functie2(korte_lijst[0],korte_lijst[1])