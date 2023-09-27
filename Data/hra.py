# -*- coding: utf-8 -*-

import time
import threading
import pygame
from pygame import mixer
import os
from colorama import init, Fore, Back, Style
import yaml
import sys
import random

# načte config soubor
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Zjistí co je v configu zapnuté
debug_mode = config.get('debug_mode', False)
zadne_pauzy = config.get('zadne_pauzy', False)
animace_textu = config.get('animace_textu', False)

# Inicializace knihovny pygame
pygame.init()
# Nastavení fullscreen módu
pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# Inicializace autosestartování clolorama nastavení
init(autoreset = True)

# Seznam souborů s hudbou
seznam_souboru = ["hudba/hudba1.wav", "hudba/hudba2.wav", "hudba/hudba3.wav", "hudba/hudba4.wav"]

# Definice funkce pro animaci nebo standardní výpis
def text(text):
    if animace_textu:
        typing_speed = 50  # wpm
        for l in text:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(random.random() * 10.0 / typing_speed)
        print("") # Vytvoří nový čádek pro další text
    else:
        print(text)

# Podle configu bude pouzivat time.sleep nebo nic
def cekej(seconds):
    if not zadne_pauzy:
        time.sleep(seconds)

# Na přehrávnání hudby
def prehraj_hudbu(seznam_souboru):
    mixer.init()
    for soubor in seznam_souboru:
        mixer.music.load(soubor)
        mixer.music.play()  
        while mixer.music.get_busy():
            pass
        cekej(1)  # Počkej chvilku před přechodem k další písničce

# Funkce DEBUGMODE byly odstraněny aby nebyly použity pro podvádění.

def uvod():
    #text("Vítej ve hře 'Změna osudu: Apokalypsa'")
    cekej(1)
    text("Rok 2050. Země se ocitla v chaosu po příletu mimozemšťanů.")
    cekej(1.5)
    text("Začíná tvá cesta přežití a pátrání po pravdě")
    cekej(1.5)
    print("-----------------")
    text("Můžeš prozkoumat okolí aby jsi zjistil co je kolem tebe")
    text("---")

def zacni_hru():
    prikaz = input("> ").lower()


    if "prozkoumej" in prikaz:
        text("\nProzkoumáváš okolí...")
        cekej(1)
        text("Na severu jsi nalezl starou budovu, zdá se, že v ní něco může být.")
        text("Vypadá to že směrem na jih končí vesnice a začíná les.")
        text("\n---")
        zacni_hru()


    elif prikaz == "jdi s" or prikaz == "jdi sever" or prikaz == "jdi na sever":
        text("\n")
        text("Nacházíš se ve staré budově vypadá to že se každou chvíli zhroutí.")
        cekej(1)
        text("Vidíš lékarničku a stůl..")
        text("\n---")
        while True:
            dum = input("V domě> ")


            if "lekarnicku" in dum or "lekarnicka" in dum:
                text("\nV lékarničce je obvaz a prážky proti bolesti. Vzal jsi si je na později.")
                cekej(1)
                text("Najednou se ozve obrovská rána 'Boom' a celý barák se začne na tebe horutit.")
                cekej(1.5)
                text("Můžeš rychle vyběhnout nebo zkusit vzít notes který jsi spatřil na stole a proskočit oknem")
                text("\n---")
                while True:
                    dum_hrouceni = input("V domě> ")


                    if "notes" in dum_hrouceni:
                        text("\nVapadá to že se to podařilo..!")
                        cekej(1)
                        text("Pak si ubědomíš že v ruce držíš jen ten notes a lékárníčku jsi v tom spěchu musel upustit.")
                        cekej(1.5)
                        text("Z ruky ti teče lehce krev, ne nijak hrozně ale raději se budeš pobybovat pomaleji ať se ti nezamotá hlava.")
                        cekej(3.5)
                        text("Otevíráš notes...")
                        cekej(3)
                        text("Vypadne z něj pár stránek (asi 2) a uletí ve větru")
                        cekej(2.5)
                        text("Dozvídáš se že notes patřil jakému si Petrovi a obsahuje potvrzené konspirační teorie")
                        cekej(5.5)
                        text("""
Čteš o bermudském trojúhelníku a tajné mimozemské základně v něm:
  Bermudský trojúhelník podle konspirační teorie skrývá vstup do tajné mimozemské základny umístěné pod mořským dnem, kterou údajně postavili mimozemšťané tisíce let před naším letopočtem. Tato základna slouží jako výzkumné a monitorovací středisko, odkud údajně pozorují lidskou civilizaci a mohou být spojení s určitými vládními organizacemi.
                            """)
                        cekej(5)
                        text("Pak jsi všimneš že jsou je tam dalších asi 6 teorií ale jen 2 jsou ozančeny jako potvrzené.")
                        cekej(3.5)
                        text("Označená je první s bermunským trojúhelníkem a pak ještě jedna s názvem 'Nefilimská rada'.")
                        cekej(4)
                        text("Můžeš si dále číst notes nebo pokračovat směrem na sever, na konec vesnice.")
                        text("\n---")
                        while True:
                            notes = input("Notes> ")


                            if "pokracovat" in notes or "cist" in notes or "notes" in notes or "pokracuj" in notes:
                                text("\nDozvídáš se že: Podle konspirační teorie spolupracuje tajná organizace 'Nefilimská rada' s mimozemskými entitami Anunnaki, kteří údajně přicházejí na Zemi s úmyslem ovládnout lidstvo a vyvolat apokalyptické události.")
                                cekej(5)
                                text("Najednou se začne vedat vítr a nebe se zatahuje...")
                                cekej(3)
                                text("Zdá se že by jsi neměl ztrácet čas a vydat se nějak jinam.")
                                cekej(1.5)
                                text("Můžeš prozkoumat okolí.")
                                text("\n---")
                                while True:
                                    po_notes = input("Notes> ")
                                    

                                    if "prozkoumej" in po_notes:
                                        text("\nNacházíš se na zahradě za domem vidíš branku kterou můžeš odejít.")
                                        text("\n---")


                                    elif "branka" in po_notes or "brankou" in po_notes or "odejdi" in po_notes or "":
                                        text("\nOtvířáš branku mezitím se zamyslíš nad tím že vítr nabírá pořád větší rychlost..")
                                        cekej(4)
                                        text("Má už takovou sílu že by byl scopný odfouknout tvůj telefon.")
                                        cekej(4)
                                        text("Najednou uvdíš že někdo vedle rozsvítil baterku.. svítí na tebe.")
                                        cekej(4.5)
                                        text("Podíváš se na něja ale nevídíš mu do tváře vítr je tak silný že výří všechen prach kolem tebe, takže lze vidět pouze pár metrů před sebe.")
                                        cekej(6.5)
                                        text("Ozve se rána.. A přestaneš vnímat.")
                                        cekej(4)
                                        text("Probouzíš se svázaný k židly. Nemůžeš se hýbat ale můžeš mluvit.")
                                        cekej(4.5)
                                        text("Otevřou se dveře a do místnosti vejde člověk. Mluví na tebe ale ty mu nerozumíš..")
                                        cekej(5)
                                        text("Vypadá to že se tě na něco ptá.")
                                        text("\n---")
                                        while True:
                                            clovek = input("človek> ")
                                            

                                            if "Nechapu" in clovek or "deje" in clovek or "nerozumim" in clovek or "co" in clovek or "je" in clovek:
                                                text("\nUmíráš po necelých dvou hodinách.")
                                                time.sleep(3)
                                                text("Konec 1..")
                                                konec_hry()


                                            else:
                                                text("\nVypadá že to fungovalo.. Přisel k tobě a odvázal tě.")
                                                cekej(3)
                                                text("Člověk: Probuďte se, probuď te se!, a dá vám lehkou facku.")
                                                cekej(4.5)
                                                text("Probouzíš se v nemocnici..")
                                                cekej(3)
                                                text("Doktorka: Jste vzhůru.. No výborně řekl by jste nám jak se jmenujete?")
                                                time.sleep(4)
                                                text("Konec 2.. Celé to bylo jen sen?")
                                                konec_hry()


                                    else:
                                        print("\nNerozumím. Zkus to jinak.")


                            elif "sever" in notes or "konec" in notes or "vesnice" in notes:
                                text("\nUšel jsi asi necelé dva kilometry a až jsi opravdu vyčerpaný.")
                                cekej(5)
                                text("Silný vítr výří prach takže se ti špatně dýchá.")
                                cekej(4)
                                text("Vedle tebe asi 30 metrů je dům a vedle něho je nastartované auto, má zapnuté světla ale nevypadá že by tam někdo seděl.")
                                cekej(6)
                                text("Rozhodnul jsi se přiblížit k autu a nahlédnout jestli tam někdo je..")
                                cekej(5)
                                text("Auto je prázdné a odemčené.")
                                text("\n---")
                                while True:
                                    auto = input("Auto> ")


                                    if "nastup" in auto or "auta" in auto or "auto" in auto:
                                        text("\nNastoupil jsi do auta..")
                                        cekej(3)
                                        text("A vydal jsi se podle cedule do města.")
                                        cekej(3)
                                        text("Jedeš do města.. počkej 15s")
                                        cekej(15)
                                        text("Přijel jsi do města kde zní nouzové sirény.")
                                        cekej(3)
                                        text("Můžeš se vydat do místí samoobsluhy a najíst se tak. Nebo se mužeš rozhlédnout kolem.")
                                        text("\n---")
                                        while True:
                                            mesto = input("Město> ")
                                            
                                            
                                            if "samoobsluhy" in mesto or "samoobsluha" in mesto:
                                                text("\nPřicházíš do samoobsluhy..")
                                                cekej(2)
                                                text("Obchoj je celý poničený a vykradený.")
                                                cekej(2)
                                                text("Vedle pultu uvidíš dva lidi hádající se o tom že by bylo možné že momozemštani přicházejí z nějaké jiné třeba 4D dimenze.")
                                                cekej("7.5")
                                                text("Zahlédly tě.")
                                                cekej(3)
                                                text("Přicházíš k nim..")
                                                cekej(2)
                                                text("Podívaly se na tebe..")
                                                cekej(4)
                                                text("Jeden z nich se ptá 'Kdo jsi, a co chceš'.")
                                                text("\n---")
                                                while True:
                                                    obchod = input("Obchod> ")
                                                    
                                                    
                                                    if "co" in obchod or "pomoc" in obchod or "deje" in obchod or "delat" in obchod or "cil" in obchod or "ztraceny" in obchod:
                                                        text("\nDomlouvají se mezi sebou..")
                                                        cekej(3)
                                                        text("Druhý znich říká: 'Dobrá pomůžeme ti pod podmínkou že nás budeš na slovo poslouchat. Bereš?'")
                                                        text("\n---")
                                                        while True:
                                                            lide = input("Lidé> ")
                                                            
                                                            
                                                            if "ano" in lide or "jo" in lide or "dobre" in lide or "jasne" in lide or "ok" in lide:
                                                                text("\nPokračování příště..")
                                                                # Dodělat
                                                                print("Sleduj GitHub repozitář pro aktualizace! (www.github.com/lksmasin)")
                                                                konec_hry()
                                                                
                                                                
                                                            elif("ne" in lide):
                                                                text("\nOn: 'Dobře takže budeme muset přistoupit na jiné řešení.")
                                                                cekej(4)
                                                                text("Udělá pár kroků a popadne pádlo z potřeb pro vodáky...")
                                                                time.sleep(3)
                                                                text("Konec 3.")
                                                                text("Byl jsi umlácen pádlem.")
                                                                konec_hry()
                                                                
                                                                
                                                            else:
                                                                print("\nPokus se napsat jednodušší odpověď.")
                                                    
                                                    
                                                    else:
                                                        text("\nOn: Hele to asi nepůjde!")
                                                        time.sleep(3)
                                                        text("Konec 4...")
                                                        cekej(2)
                                                        text("Vypadá to že jsi se jim nelíbil..")
                                                        cekej(3)
                                                        text("Nápověda: Tato cesta není špatně, zkus to ale trochu jinak třeba se dostaneš dále.")
                                                        

                                            elif("rozhledni" in mesto):
                                                text("\nNedaleko je samoobsluha ta by se ti velmy hodila protože máš hlad.")
                                                cekej(5)
                                                text("Kousek od tebe je i skupinka lidí která něco volá. Asi nějací blázni nebo tak něco..")
                                            
                                            
                                            else: 
                                                text("\nNerozumím ti, zkus to jinak.")
                                                
                                                
                                    else:
                                        text("\nNechi nic říkat ale myslím že tohle nepůjde..")
                                        
                                        
                            else:
                                text("\nTohle nevypadá jako řešení, zkus to trošku jinak.")


                    elif "ven" in dum_hrouceni or "vybehni" in dum_hrouceni:
                        text("\nVyběhl jsi ven a vypadá to že jsi celý..")
                        text("Jsi spátky tam kde jsi začal můžeš jít na jih")
                        zacni_hru


                    else:
                        print("\nNerozumím co mám dělat.")
                    



            elif "stul" in dum:
                text("\nNa stole je jakýsi notes, vezmeš jej.")
                text("\n---")
                while True:
                    dum_notes = input("V domě> ")
                    
                    
                    if "precti" in dum_notes or "notes" in dum_notes or "otevri" in dum_notes:
                        text("\nZápis je velmi nečitelný, většinu z něho nemůžeš přečíst.")
                        cekej(3)
                        text("Vypadá to že obsahuje pár informací o tom co se stalo a o tom co se děje a jak mám dále postupovat.")
                        cekej(5)
                        text("Podle notesu by jsi měl nastoupit do auta a odjet do města zastavit se na tamějším úřadě pro evakuaci.")
                        text("\n---")
                        while True:
                            notes_rozhodnuti = input("Notes> ")
                            
                            
                            if "notes" in notes_rozhodnuti or "notesu" in notes_rozhodnuti or "udelej" in notes_rozhodnuti or "pokracuj" in notes_rozhodnuti:
                                text("\nMusíš se dostat do města.. Problém je v tom že nemáš jak.")
                                cekej(5)
                                text("Chtělo by to auto..")
                                cekej(3)
                                text("POZNÁMKA: Zkus se rozhlédnou kolem.")
                                
                                
                            elif("rozhledni" in notes_rozhodnuti or "prozkoumej" in notes_rozhodnuti):
                                text("\nNacházíš se ve starém domu. V místnosti která by se dala nazvat obývákem.")
                                cekej(6)
                                text("Tento dům má další dvě místnosti, koupelnu a kuchyň.")
                                cekej(5)
                                text("K domu spadá něco co vypadá jako garáž.")
                                
                                
                            elif("garaz" in notes_rozhodnuti or "garaze" in notes_rozhodnuti):
                                text("\nPřicházíš do garáže..")
                                cekej(3)
                                text("Podle očekávání tady žádné auto není ale je zde staré kolo.")
                                text("\n---")
                                while True:
                                    garaz = input("Garáž> ")
                                    
                                    
                                    if "kolo" in garaz or "bicikl" in garaz or "nasedni" in garaz or "nastup" in garaz or "jed" in garaz:
                                        text("\nTohle kolo má asi už něco za sebou..")
                                        cekej(4)
                                        text("Je celé zrezavělé, pneumatiky jsou vypuštěné.")
                                        cekej(4)
                                        text("Naštěstí kousek vedle kola je stůl a na něm pumpička, nafoukneš kolo a můžeš jet.")
                                        cekej(6)
                                        text("Nafukování kola - čekej 10s . . .")
                                        time.sleep(10.5)
                                        text("Cesta do města - čekej 25s . . .")
                                        time.sleep(12)
                                        text("Nastal problém! Při cestě jsi si všiml že se pneumatiky vyfukují velmi rychle.. už jsou skoro prázdné.")
                                        text("Ale to není jediný priblém kvůli silnému vítru se ti obtížně dýchá a musíš si dát pauzu.")
                                        cekej(6.5)
                                        text("Vypadá to že se k tobě z celého jihu něco blíží.")
                                        cekej(4)
                                        text("Odhazuje to všechno co se tomu postavý..")
                                        cekej(3)
                                        text("Podle rychlosti to během pár minut u tebe.")
                                        text("\n---")
                                        while True:
                                            vlna = input("Nebezpečí> ")
                                            
                                            
                                            if vlna == "666":
                                                text("???\n")
                                                
                                                
                                            else: 
                                                text("\nDělal jsi co jsi mohl..")
                                                text("Konec 5")
                                                text("Byl jsi rozdrcen mohutnou tlakovou vlnou.")
                                                konec_hry()
                                
                                
                                    else:
                                        text("\nVypadá že tohle nejde.")
                                
                                
                            else:
                                text("\nVypadá to že takováto možnost není.")
                        
                        
                    elif("zpatky" in dum_notes or "zpet" in dum_notes):
                        text("\nJsi spátky tam kde jsi začal.")
                        cekej(4)
                        text("Teď už můžeš jít jen a pouze na jih")
                        zacni_hru()
                        
                        
                    else:
                        text("\nTohle nevypadá že by to mělo fungovat. Zkus to jinak.")
                

            else:
                print("\nNerozumím příkazu.")

    
    elif prikaz == "jdi j" or prikaz == "jdi jih" or prikaz == "jdi na jih":
        text("\nPřišel jsi do lesa jsi vyčerpaný z té cesty...")
        cekej(1)
        text("Vypadá to že dál na jihu je něco připomínající studánku.")
        cekej(1.5)
        text("Na východě se nachází nějaké obydlý.")
        cekej(2)
        text("Můžeš se vrátit zpět na jíh do vesnice.")
        #text("\n---")
        #while True:
        print("TOHLE JEŠTĚ NĚNÍ HOTOVÉ ZKUS TO JINAK!!!")
        zacni_hru()
            #les = input("V LESE> ")
            #Dodělat

    

    elif "zapad" in prikaz or "vychod" in prikaz:
        text("\nTam to nevypadá bezpečně, radši zůstaneš.")
        text("\n---")
        zacni_hru()
        

    elif prikaz == "konec":
        konec_hry()


    else:
        print("\nNeplatný příkaz. Zkus to znovu.")
        zacni_hru()


def konec_hry():
    text("\nDěkujeme za hraní!")
    text("Hru vytvořil LUKYMAS\n")
    text("Ve hře se vyskytuje hudba od: The Owl - Your Love is my Drug, \nSzmergiel747 - Unreal soundtrack - Ending, \nLewnatic Live - joji - slow dancing in the dark, \nDiverse Matter - Doom Chillax OST Map08")
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
