import sys
import random
import time
def strepen():
    print("="* 40)

def welkom_keuze():
    strepen()
    print("Welkom bij mijn overhoor progamma!")
    print("Tip: begin met een woordenlijst maken!")
    strepen()
    print("nieuwe lijst: n")
    print("bekijk lijst: b")
    print("wijzig lijst: w")
    print("overhoor lijst: o")
    print("Stop mijn programma: q")
    strepen()

def main():
    welkom_keuze()
    keuze = input("Welke letter geef je mij mee?:")
    woorden = {}
    if (keuze == 'q'):
        stoppen()
    while keuze != 'q':
        if (keuze == 'b'):
            bekijk_lijst(woorden)
        if (keuze == 'n'):
            woorden = nieuwe_lijst(woorden)
        if (keuze == 'w'):
            wijzig_lijst(woorden)
        if (keuze == 'o'):
            overhoren_lijst(woorden)
        strepen()
        keuze = input("Welke letter geef je mij mee?: ")


def bekijk_lijst(woorden):
    strepen()
    print("Nederlands : Engels")
    for key in woorden:
        print("{key} : {value}".format(key=key, value=woorden[key]))

def nieuwe_lijst(woorden):
    strepen()
    print("'q' om te stoppenn")
    print("Laten we beginnen!")
    woorden = {}
    key = input("Nederlands:")
    while key != "q":
        value = input("Engels:")
        woorden[key] = value
        f = open('lijstwoorden.txt', 'w')
        for key in woorden:
            f.write("{}:{} ".format(key, woorden[key]))
        key = input("Nederlands:")
    f.close()
    print("Je bent klaar met je lijst!")
    print("Als je nog meer woorden wilt wijzigen, kan dat in het menu")
    return woorden

def wijzig_lijst(woorden):
    bekijk_lijst(woorden)
    strepen()
    key = input("Woord (NL) dat je wilt veranderen:")
    newnl = input("Nieuw woord:")
    newen = input("Nieuwe vertaling:")
    woorden[newnl] = newen
    del woorden[key]
    print("De nieuwe wijziging is aangebracht in je woorden lijst!")
    return woorden

def verwijder_woord(woorden):
    bekijk_lijst(woorden)
    strepen()
    key = input("Woord (NL) die je wilt verwijderen:")
    vraag = input("Weet je zeker dat je dit woord wilt verwijderen?(ja/nee)")
    if (vraag == 'ja'):
        del woorden[key]
    return woorden

def overhoren_lijst(woorden):
    punten = 0
    while punten < len(woorden.keys())*2:
        strepen()
        nlwoord = random.choice(list(woorden))
        print("Wat is de vertaling van dit woord?")
        enwoord = input(nlwoord + ":")
        if (enwoord == woorden[nlwoord]):
            print("Dat is juist!")
            punten += 1
            print("Aantal punten: ",punten)
        elif (enwoord == 'q'):
            break
        else:
            print("Dat is helaas fout")
            print("Het goede antwoord:",woorden[nlwoord])
            punten -= 1
            print("Aantal punten: ", punten)
        while punten > 2:
            print("Je bent klaar!!", "Aantal punten:", punten)
            break

def stoppen():
    print("Dit programma sluit over 5 seconden,")
    print("5")
    time.sleep(0.5)
    print("4")
    time.sleep(0.5)
    print("3")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("1")
    time.sleep(0.5)
    print("0")
    time.sleep(0.5)
    sys.exit()

main()