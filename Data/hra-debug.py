# -*- coding: utf-8 -*-

import time
import threading
import pygame
from pygame import mixer
import os
from colorama import init, Fore, Back, Style
import yaml

# načte config soubor
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Zjistí co je v configu zapnuté
debug_mode = config.get('debug_mode', False)
zadne_pauzy = config.get('zadne_pauzy', False)

# Inicializace knihovny pygame
pygame.init()
# Nastavení fullscreen módu
pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# Inicializace autosestartování clolorama nastavení
init(autoreset = True)

# Seznam souborů s hudbou
seznam_souboru = ["hudba/hudba1.wav", "hudba/hudba2.wav", "hudba/hudba3.wav", "hudba/hudba4.wav"]

def cekej(seconds):
    if not zadne_pauzy:
        time.sleep(seconds)

def prehraj_hudbu(seznam_souboru):
    mixer.init()
    for soubor in seznam_souboru:
        mixer.music.load(soubor)
        mixer.music.play()  
        while mixer.music.get_busy():
            pass
        cekej(1)  # Počkej chvilku před přechodem k další písničce


def uvod():
    print("Vítej ve hře 'Změna osudu: Apokalypsa'")
    cekej(1)
    print("Rok 2050. Země se ocitla v chaosu po příletu mimozemšťanů.")
    cekej(1.5)
    print("Začíná tvá cesta přežití a pátrání po pravdě")
    cekej(1.5)
    print("-----------------")
    print("Můžeš prozkoumat okolí aby jsi zjistil co je kolem tebe")
    print("---")

def zacni_hru():
    prikaz = input("> ").lower()


    if "prozkoumej" in prikaz:
        print("\nProzkoumáváš okolí...")
        cekej(1)
        print("Na severu jsi nalezl starou budovu, zdá se, že v ní něco může být.")
        print("Vypadá to že směrem na jih končí vesnice a začíná les.")
        print("\n---")
        zacni_hru()


    elif prikaz == "jdi s" or prikaz == "jdi sever" or prikaz == "jdi na sever":
        print("\n")
        print("Nacházíš se ve staré budově vypadá to že se každou chvíli zhroutí.")
        cekej(1)
        print("Vidíš lékarničku a stůl..")
        print("\n---")
        while True:
            dum = input("V DOMĚ> ")


            if "lekarnicku" in dum or "lekarnicka" in dum:
                print("\nV lékarničce je obvaz a prážky proti bolesti. Vzal jsi si je na později.")
                cekej(1)
                print("Najednou se ozve obrovská rána 'Boom' a celý barák se začne na tebe horutit.")
                cekej(1.5)
                print("Můžeš rychle vyběhnout nebo zkusit vzít notes který jsi spatřil na stole a proskočit oknem")
                print("\n---")
                while True:
                    dum_hrouceni = input("V DOMĚ> ")


                    if "notes" in dum_hrouceni:
                        print("\nVapadá to že se to podařilo..!")
                        cekej(1)
                        print("Pak si ubědomíš že v ruce držíš jen ten notes a lékárníčku jsi v tom spěchu musel upustit.")
                        cekej(1.5)
                        print("Z ruky ti teče lehce krev, ne nijak hrozně ale raději se budeš pobybovat pomaleji ať se ti nezamotá hlava.")
                        cekej(3.5)
                        print("Otevíráš notes...")
                        cekej(3)
                        print("Vypadne z něj pár stránek (asi 2) a uletí ve větru")
                        cekej(2.5)
                        print("Dozvídáš se že notes patřil jakému si Petrovi a obsahuje potvrzené konspirační teorie")
                        cekej(5.5)
                        print("""
Čteš o bermudském trojúhelníku a tajné mimozemské základně v něm:
  Bermudský trojúhelník podle konspirační teorie skrývá vstup do tajné mimozemské základny umístěné pod mořským dnem, kterou údajně postavili mimozemšťané tisíce let před naším letopočtem. Tato základna slouží jako výzkumné a monitorovací středisko, odkud údajně pozorují lidskou civilizaci a mohou být spojení s určitými vládními organizacemi.
                            """)
                        cekej(5)
                        print("Pak jsi všimneš že jsou je tam dalších asi 6 teorií ale jen 2 jsou ozančeny jako potvrzené.")
                        cekej(3.5)
                        print("Označená je první s bermunským trojúhelníkem a pak ještě jedna s názvem 'Nefilimská rada'.")
                        cekej(4)
                        print("Můžeš si dále číst notes nebo pokračovat směrem na sever, na konec vesnice.")
                        print("\n---")
                        while True:
                            notes = input("Notes> ")


                            if "pokracovat" in notes or "cist" in notes or "notes" in notes or "pokracuj" in notes:
                                print("\nDozvídáš se že: Podle konspirační teorie spolupracuje tajná organizace 'Nefilimská rada' s mimozemskými entitami Anunnaki, kteří údajně přicházejí na Zemi s úmyslem ovládnout lidstvo a vyvolat apokalyptické události.")
                                cekej(5)
                                print("Najednou se začne vedat vítr a nebe se zatahuje...")
                                cekej(3)
                                print("Zdá se že by jsi neměl ztrácet čas a vydat se nějak jinam.")
                                cekej(1.5)
                                print("Můžeš prozkoumat okolí.")
                                print("\n---")
                                while True:
                                    po_notes = input("Notes> ")
                                    

                                    if "prozkoumej" in po_notes:
                                        print("\nNacházíš se na zahradě za domem vidíš branku kterou můžeš odejít.")
                                        print("\n---")


                                    elif "branka" in po_notes or "brankou" in po_notes or "odejdi" in po_notes or "":
                                        print("\nOtvířáš branku mezitím se zamyslíš nad tím že vítr nabírá pořád větší rychlost..")
                                        cekej(4)
                                        print("Má už takovou sílu že by byl scopný odfouknout tvůj telefon.")
                                        cekej(4)
                                        print("Najednou uvdíš že někdo vedle rozsvítil baterku.. svítí na tebe.")
                                        cekej(4.5)
                                        print("Podíváš se na něja ale nevídíš mu do tváře vítr je tak silný že výří všechen prach kolem tebe, takže lze vidět pouze pár metrů před sebe.")
                                        cekej(6.5)
                                        print("Ozve se rána.. A přestaneš vnímat.")
                                        cekej(4)
                                        print("Probouzíš se svázaný k židly. Nemůžeš se hýbat ale můžeš mluvit.")
                                        cekej(4.5)
                                        print("Otevřou se dveře a do místnosti vejde člověk. Mluví na tebe ale ty mu nerozumíš..")
                                        cekej(5)
                                        print("Vypadá to že se tě na něco ptá.")
                                        print("\n---")
                                        while True:
                                            clovek = input("človek> ")
                                            

                                            if "Nechapu" in clovek or "deje" in clovek or "nerozumim" in clovek or "co" in clovek or "je" in clovek:
                                                print("\nUmíráš po necelých dvou hodinách.")
                                                cekej(1)
                                                print("Konec 1..")
                                                konec_hry()


                                            else:
                                                print("\nVypadá že to fungovalo.. Přisel k tobě a odvázal tě.")
                                                cekej(3)
                                                print("Člověk: Probuďte se, probuď te se!, a dá vám lehkou facku.")
                                                cekej(4.5)
                                                print("Probouzíš se v nemocnici..")
                                                cekej(3)
                                                print("Doktorka: Jste vzhůru.. No výborně řekl by jste nám jak se jmenujete?")
                                                cekej(6)
                                                print("Konec 2.. Celé to bylo jen sen?")
                                                konec_hry()


                                    else:
                                        print("\nNerozumím. Zkus to jinak.")


                            elif "sver" in notes or "konec" in notes or "vesnice" in notes:
                                print("\nUšel jsi asi necelé dva kilometry a až jsi opravdu vyčerpaný.")
                                cekej(5)
                                print("Silný vítr výří prach takže se ti špatně dýchá.")
                                cekej(4)
                                print("Vedle tebe asi 30 metrů je dům a vedle něho je nastartované auto, má zapnuté světla ale nevypadá že by tam někdo seděl.")
                                cekej(6)
                                print("Rozhodnul jsi se přiblížit k autu a nahlédnout jestli tam někdo je..")
                                cekej(5)
                                print("Auto je prázdné a odemčené.")
                                print("\n---")
                                while True:
                                    auto = input("Auto> ")


                                    if "nastup" in auto or "auta" in auto or "auto" in auto:
                                        print("\nNastoupil jsi do auta..")
                                        cekej(3)
                                        print("A vydal jsi se podle cedule do města.")
                                        cekej(3)
                                        print("Jedeš do města.. počkej 15s")
                                        cekej(15)
                                        print("Přijel jsi do města kde zní nouzové sirény.")
                                        cekej(3)
                                        print("Můžeš se vydat do místí samoobsluhy a najíst se tak. Nebo se mužeš rozhlédnout kolem.")
                                        print("\n---")
                                        while True:
                                            mesto = input("Město> ")
                                            
                                            
                                            if "samoobsluhy" in mesto or "samoobsluha" in mesto:
                                                print("\nPřicházíš do samoobsluhy..")
                                                cekej(2)
                                                print("Obchoj je celý poničený a vykradený.")
                                                cekej(2)
                                                print("Vedle pultu uvidíš dva lidi hádající se o tom že by bylo možné že momozemštani přicházejí z nějaké jiné třeba 4D dimenze.")
                                                cekej("7.5")
                                                print("Zahlédly tě.")
                                                cekej(3)
                                                print("Přicházíš k nim..")
                                                cekej(2)
                                                print("Podívaly se na tebe..")
                                                cekej(4)
                                                print("Jeden z nich se ptá 'Kdo jsi, a co chceš'.")
                                                print("\n---")
                                                while True:
                                                    obchod = input("Obchod> ")
                                                    #Dodělat


                    elif "ven" in dum_hrouceni or "vybehni" in dum_hrouceni:
                        print("\nVyběhl jsi ven a vypadá to že jsi celý..")
                        print("Jsi spátky tam kde jsi začal můžeš jít na jih")
                        #Dodělat


                    else:
                        print("\nNerozumím co mám dělat.")
                    



            elif "stul" in dum:
                print("\nNa stole je jakýsi notes, vezmeš jej.")
                dum_notes = input("V DOMĚ> ")
                #Dodělat


            else:
                print("\nNerozumím příkazu.")

    
    elif prikaz == "jdi j" or prikaz == "jdi jih" or prikaz == "jdi na jih":
        print("\nPřišel jsi do lesa jsi vyčerpaný z té cesty...")
        cekej(1)
        print("Vypadá to že dál na jihu je něco připomínající studánku.")
        cekej(1.5)
        print("Na východě se nachází nějaké obydlý.")
        cekej(2)
        print("Můžeš se vrátit zpět na jíh do vesnice.")
        print("\n---")
        while True:
            les = input("V LESE> ")
            #Dodělat

    

    elif "zapad" in prikaz or "vychod" in prikaz:
        print("\nTam to nevypadá bezpečně, radši zůstaneš.")
        print("\n---")
        zacni_hru()
        

    elif prikaz == "konec":
        konec_hry()


    else:
        print("\nNeplatný příkaz. Zkus to znovu.")
        zacni_hru()


def konec_hry():
    print("\nDěkujeme za hraní!")
    print("Hru vytvořil LUKYMAS\n")
    print("Ve hře se vyskytuje hudba od: The Owl - Your Love is my Drug (8bit slowed), Szmergiel747 - Unreal soundtrack - Ending, Lewnatic Live - joji - slow dancing in the dark (True 8-bit Remix), Diverse Matter - Doom Chillax OST Map08 (WAD soundtrack)")
    exit()


# Vytvoř vlákno pro přehrávání hudby
hudba_thread = threading.Thread(target=prehraj_hudbu, args=(seznam_souboru,))
hudba_thread.start()

os.system("clear")
os.system("cls")

# Debug mode zpráva + spuštění hry
if debug_mode:
    uvod()
    print("REŽIM DEBUGMODE JE ZAPNUTÝ!")
    zacni_hru()
    print("REŽIM DEBUGMODE JE ZAPNUTÝ!")
    print("REŽIM DEBUGMODE JE ZAPNUTÝ!")
else:
    uvod()
    zacni_hru()
