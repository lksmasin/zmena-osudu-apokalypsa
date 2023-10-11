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

#TODO: predcitaní

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

# Autoaticky resetuje barvy
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

def nejde():
    jinak = random.randint(0,200)
    if jinak <= 10:
        text(Fore.RED + "\nVypadá to, že takhle to asi nepůjde..")
    elif jinak >= 20 and jinak <= 30:
        text(Fore.RED + "\nTakováto možnost asi není.")
    elif jinak >= 30 and jinak <= 40:
        text(Fore.RED + "\nTohle nejde.")
    elif jinak >= 40 and jinak <= 50:
        text(Fore.RED + "\nTakto to nepůjde.")
    elif jinak >= 50 and jinak <= 60:
        text(Fore.RED + "\nNe, ne. Tohle nejde.")
    elif jinak >= 60 and jinak <= 70:
        text(Fore.RED + "\nTakto to nefunguje.")
    elif jinak >= 70 and jinak <= 80:
        text(Fore.RED + "\nHele tohle nebude fungovat. Zkus to jinak.")
    elif jinak >= 80 and jinak <= 90:
        text(Fore.RED + "\nZkus to jinak")
    elif jinak >= 90 and jinak <= 100:
        text(Fore.RED + "\nTakto to nepůjde.")
    elif jinak >= 100 and jinak <= 110:
        text(Fore.RED + "\nTakhle by to asi nefungovalo.")
    elif jinak >= 120 and jinak <= 130:
        text(Fore.RED + "\nTakto to asi autor nezamýšlel zkus to jinak")
    elif jinak >= 130 and jinak <=140:
        text(Fore.RED + "\nNe, ne. Tkato to mepůjde!")
    elif jinak >= 140 and jinak <=150:
        text(Fore.RED + "\nVypadá že to takto nepůjde, pokus se o to jinak.")
    elif jinak >= 150 and jinak <=160:
        text(Fore.RED + "\nTohle nyvypadá jako řešení. Pokus se to vyřešit jinak.")
    elif jinak >= 160 and jinak <=170:
        text(Fore.RED + "\nNerozumím ti takto to asi nepůjde.")
    elif jinak >= 170 and jinak <=180:
        text(Fore.RED + "\nNerozumím příkazu.")
    elif jinak >= 180 and jinak <=190:
        text(Fore.RED + "\nTohle neznám. zkus to jinak.")
    else:
        text(Fore.RED + "\nPokus se o to jinak.")

def uvod():
    #text("Vítej ve hře 'Změna osudu: Apokalypsa'")
    cekej(1)
    text(Fore.BLUE + "Rok 2050. Země se ocitla v chaosu po příletu mimozemšťanů.")
    cekej(1.5)
    text(Fore.BLUE + "Začíná tvá cesta přežití a pátrání po pravdě")
    cekej(1.5)
    print("-----------------")
    text(Fore.YELLOW + "Můžeš prozkoumat okolí aby jsi zjistil co je kolem tebe")
    text("---")

def zacni_hru():
    prikaz = input(Fore.GREEN + "> ").lower()

    if "prozkoumej" in prikaz:
        text(Fore.YELLOW + "\nProzkoumáváš okolí...")
        cekej(1)
        text(Fore.YELLOW + "Na severu jsi nalezl starou budovu, zdá se, že v ní něco může být.")
        text(Fore.YELLOW + "Vypadá to že směrem na jih končí vesnice a začíná les.")
        text("\n---")
        zacni_hru()


    elif prikaz == "jdi s" or prikaz == "jdi sever" or prikaz == "jdi na sever":
        text("\n")
        text(Fore.YELLOW + "Nacházíš se ve staré budově vypadá to že se každou chvíli zhroutí.")
        cekej(1)
        text(Fore.YELLOW + "Vidíš lékarničku a stůl..")
        text("\n---")
        while True:
            dum = input(Fore.GREEN + "V domě> ")


            if "lekarnicku" in dum or "lekarnicka" in dum:
                text(Fore.YELLOW + "\nV lékarničce je obvaz a prážky proti bolesti. Vzal jsi si je na později.")
                cekej(1)
                text(Fore.YELLOW + "Najednou se ozve obrovská rána 'Boom' a celý barák se začne na tebe horutit.")
                cekej(1.5)
                text(Fore.YELLOW + "Můžeš rychle vyběhnout nebo zkusit vzít notes který jsi spatřil na stole a proskočit oknem")
                text("\n---")
                while True:
                    dum_hrouceni = input(Fore.GREEN + "V domě> ")


                    if "notes" in dum_hrouceni:
                        text(Fore.YELLOW + "\nVapadá to že se to podařilo..!")
                        cekej(1)
                        text(Fore.YELLOW + "Pak si ubědomíš že v ruce držíš jen ten notes a lékárníčku jsi v tom spěchu musel upustit.")
                        cekej(1.5)
                        text(Fore.YELLOW + "Z ruky ti teče lehce krev, ne nijak hrozně ale raději se budeš pobybovat pomaleji ať se ti nezamotá hlava.")
                        cekej(3.5)
                        text(Fore.YELLOW + "Otevíráš notes...")
                        cekej(3)
                        text(Fore.YELLOW + "Vypadne z něj pár stránek (asi 2) a uletí ve větru")
                        cekej(2.5)
                        text(Fore.YELLOW + "Dozvídáš se že notes patřil jakému si Petrovi a obsahuje potvrzené konspirační teorie")
                        cekej(5.5)
                        text(Fore.YELLOW + """
Čteš o bermudském trojúhelníku a tajné mimozemské základně v něm:
  Bermudský trojúhelník podle konspirační teorie skrývá vstup do tajné mimozemské základny umístěné pod mořským dnem, kterou údajně postavili mimozemšťané tisíce let před naším letopočtem. Tato základna slouží jako výzkumné a monitorovací středisko, odkud údajně pozorují lidskou civilizaci a mohou být spojení s určitými vládními organizacemi.
                            """)
                        cekej(5)
                        text(Fore.YELLOW + "Pak jsi všimneš že jsou je tam dalších asi 6 teorií ale jen 2 jsou ozančeny jako potvrzené.")
                        cekej(3.5)
                        text(Fore.YELLOW + "Označená je první s bermunským trojúhelníkem a pak ještě jedna s názvem 'Nefilimská rada'.")
                        cekej(4)
                        text(Fore.YELLOW + "Můžeš si dále číst notes nebo pokračovat směrem na sever, na konec vesnice.")
                        text("\n---")
                        while True:
                            notes = input(Fore.GREEN + "Notes> ")


                            if "pokracovat" in notes or "cist" in notes or "notes" in notes or "pokracuj" in notes:
                                text(Fore.YELLOW + "\nDozvídáš se že: Podle konspirační teorie spolupracuje tajná organizace 'Nefilimská rada' s mimozemskými entitami Anunnaki, kteří údajně přicházejí na Zemi s úmyslem ovládnout lidstvo a vyvolat apokalyptické události.")
                                cekej(5)
                                text(Fore.YELLOW + "Najednou se začne vedat vítr a nebe se zatahuje...")
                                cekej(3)
                                text(Fore.YELLOW + "Zdá se že by jsi neměl ztrácet čas a vydat se nějak jinam.")
                                cekej(1.5)
                                text(Fore.YELLOW + "Můžeš prozkoumat okolí.")
                                text("\n---")
                                while True:
                                    po_notes = input(Fore.GREEN + "Notes> ")
                                    

                                    if "prozkoumej" in po_notes:
                                        text(Fore.YELLOW + "\nNacházíš se na zahradě za domem vidíš branku kterou můžeš odejít.")
                                        text("\n---")


                                    elif "branka" in po_notes or "brankou" in po_notes or "odejdi" in po_notes or "":
                                        text(Fore.YELLOW + "\nOtvířáš branku mezitím se zamyslíš nad tím že vítr nabírá pořád větší rychlost..")
                                        cekej(4)
                                        text(Fore.YELLOW + "Má už takovou sílu že by byl scopný odfouknout tvůj telefon.")
                                        cekej(4)
                                        text(Fore.YELLOW + "Najednou uvdíš že někdo vedle rozsvítil baterku.. svítí na tebe.")
                                        cekej(4.5)
                                        text(Fore.YELLOW + "Podíváš se na něja ale nevídíš mu do tváře vítr je tak silný že výří všechen prach kolem tebe, takže lze vidět pouze pár metrů před sebe.")
                                        cekej(6.5)
                                        text(Fore.YELLOW + "Ozve se rána.. A přestaneš vnímat.")
                                        cekej(4)
                                        text(Fore.YELLOW + "Probouzíš se svázaný k židly. Nemůžeš se hýbat ale můžeš mluvit.")
                                        cekej(4.5)
                                        text(Fore.YELLOW + "Otevřou se dveře a do místnosti vejde člověk. Mluví na tebe ale ty mu nerozumíš..")
                                        cekej(5)
                                        text(Fore.YELLOW + "Vypadá to že se tě na něco ptá.")
                                        text("\n---")
                                        while True:
                                            clovek = input(Fore.GREEN + "človek> ")
                                            

                                            if "Nechapu" in clovek or "deje" in clovek or "nerozumim" in clovek or "co" in clovek or "je" in clovek:
                                                text(Fore.YELLOW + "\nUmíráš po necelých dvou hodinách.")
                                                time.sleep(3)
                                                text("Konec 1..")
                                                konec_hry()


                                            else:
                                                text(Fore.YELLOW + "\nVypadá že to fungovalo.. Přisel k tobě a odvázal tě.")
                                                cekej(3)
                                                text(Fore.YELLOW + "Člověk: Probuďte se, probuď te se!, a dá vám lehkou facku.")
                                                cekej(4.5)
                                                text(Fore.YELLOW + "Probouzíš se v nemocnici..")
                                                cekej(3)
                                                text(Fore.YELLOW + "Doktorka: Jste vzhůru.. No výborně řekl by jste nám jak se jmenujete?")
                                                time.sleep(4)
                                                text("Konec 2.. Celé to bylo jen sen?")
                                                konec_hry()


                                    else:
                                        nejde()


                            elif "sever" in notes or "konec" in notes or "vesnice" in notes:
                                text(Fore.YELLOW + "\nUšel jsi asi necelé dva kilometry a až jsi opravdu vyčerpaný.")
                                cekej(5)
                                text(Fore.YELLOW + "Silný vítr výří prach takže se ti špatně dýchá.")
                                cekej(4)
                                text(Fore.YELLOW + "Vedle tebe asi 30 metrů je dům a vedle něho je nastartované auto, má zapnuté světla ale nevypadá že by tam někdo seděl.")
                                cekej(6)
                                text(Fore.YELLOW + "Rozhodnul jsi se přiblížit k autu a nahlédnout jestli tam někdo je..")
                                cekej(5)
                                text(Fore.YELLOW + "Auto je prázdné a odemčené.")
                                text("\n---")
                                while True:
                                    auto = input(Fore.GREEN + "Auto> ")


                                    if "nastup" in auto or "auta" in auto or "auto" in auto:
                                        text(Fore.YELLOW + "\nNastoupil jsi do auta..")
                                        cekej(3)
                                        text(Fore.YELLOW + "A vydal jsi se podle cedule do města.")
                                        cekej(3)
                                        text(Fore.YELLOW + "Jedeš do města.. počkej 15s")
                                        cekej(15)
                                        text(Fore.YELLOW + "Přijel jsi do města kde zní nouzové sirény.")
                                        cekej(3)
                                        text(Fore.YELLOW + "Můžeš se vydat do místí samoobsluhy a najíst se tak. Nebo se mužeš rozhlédnout kolem.")
                                        text("\n---")
                                        while True:
                                            mesto = input(Fore.GREEN + "Město> ")
                                            
                                            
                                            if "samoobsluhy" in mesto or "samoobsluha" in mesto:
                                                text(Fore.YELLOW + "\nPřicházíš do samoobsluhy..")
                                                cekej(2)
                                                text(Fore.YELLOW + "Obchoj je celý poničený a vykradený.")
                                                cekej(2)
                                                text(Fore.YELLOW + "Vedle pultu uvidíš dva lidi hádající se o tom že by bylo možné že momozemštani přicházejí z nějaké jiné třeba 4D dimenze.")
                                                cekej("7.5")
                                                text(Fore.YELLOW + "Zahlédly tě.")
                                                cekej(3)
                                                text(Fore.YELLOW + "Přicházíš k nim..")
                                                cekej(2)
                                                text(Fore.YELLOW + "Podívaly se na tebe..")
                                                cekej(4)
                                                text(Fore.YELLOW + "Jeden z nich se ptá 'Kdo jsi, a co chceš'.")
                                                text("\n---")
                                                while True:
                                                    obchod = input(Fore.GREEN + "Obchod> ")
                                                    
                                                    
                                                    if "co" in obchod or "pomoc" in obchod or "deje" in obchod or "delat" in obchod or "cil" in obchod or "ztraceny" in obchod:
                                                        text(Fore.YELLOW + "\nDomlouvají se mezi sebou..")
                                                        cekej(3)
                                                        text(Fore.YELLOW + "Druhý znich říká: 'Dobrá pomůžeme ti pod podmínkou že nás budeš na slovo poslouchat. Bereš?'")
                                                        text("\n---")
                                                        while True:
                                                            lide = input(Fore.GREEN + "Lidé> ")
                                                            
                                                            
                                                            if "ano" in lide or "jo" in lide or "dobre" in lide or "jasne" in lide or "ok" in lide:
                                                                text(Fore.YELLOW + "\nPokračování příště..")
                                                                # Dodělat
                                                                print("Sleduj GitHub repozitář pro aktualizace! (www.github.com/lksmasin)")
                                                                konec_hry()
                                                                
                                                                
                                                            elif("ne" in lide):
                                                                text(Fore.YELLOW + "\nOn: 'Dobře takže budeme muset přistoupit na jiné řešení.")
                                                                cekej(4)
                                                                text(Fore.YELLOW + "Udělá pár kroků a popadne pádlo z potřeb pro vodáky...")
                                                                time.sleep(3)
                                                                text("Konec 3.")
                                                                text("Byl jsi umlácen pádlem.")
                                                                konec_hry()
                                                                
                                                                
                                                            else:
                                                                nejde()
                                                    
                                                    
                                                    else:
                                                        text(Fore.YELLOW + "\nOn: Hele to asi nepůjde!")
                                                        time.sleep(3)
                                                        text("Konec 4...")
                                                        cekej(2)
                                                        text("Vypadá to že jsi se jim nelíbil..")
                                                        cekej(3)
                                                        text("Nápověda: Tato cesta není špatně, zkus to ale trochu jinak třeba se dostaneš dále.")
                                                        

                                            elif("rozhledni" in mesto):
                                                text(Fore.YELLOW + "\nNedaleko je samoobsluha ta by se ti velmy hodila protože máš hlad.")
                                                cekej(5)
                                                text(Fore.YELLOW + "Kousek od tebe je i skupinka lidí která něco volá. Asi nějací blázni nebo tak něco..")
                                            
                                            
                                            else: 
                                                nejde()
                                                
                                                
                                    else:
                                        nejde()
                                        
                                        
                            else:
                                nejde()


                    elif "ven" in dum_hrouceni or "vybehni" in dum_hrouceni:
                        text(Fore.YELLOW + "\nVyběhl jsi ven a vypadá to že jsi celý..")
                        text(Fore.YELLOW + "Jsi spátky tam kde jsi začal můžeš jít na jih")
                        zacni_hru


                    else:
                        nejde()
                    



            elif "stul" in dum:
                text(Fore.YELLOW + "\nNa stole je jakýsi notes, vezmeš jej.")
                text("\n---")
                while True:
                    dum_notes = input(Fore.GREEN + "V domě> ")
                    
                    
                    if "precti" in dum_notes or "notes" in dum_notes or "otevri" in dum_notes:
                        text(Fore.YELLOW + "\nZápis je velmi nečitelný, většinu z něho nemůžeš přečíst.")
                        cekej(3)
                        text(Fore.YELLOW + "Vypadá to že obsahuje pár informací o tom co se stalo a o tom co se děje a jak mám dále postupovat.")
                        cekej(5)
                        text(Fore.YELLOW + "Podle notesu by jsi měl nastoupit do auta a odjet do města zastavit se na tamějším úřadě pro evakuaci.")
                        text("\n---")
                        while True:
                            notes_rozhodnuti = input(Fore.GREEN + "Notes> ")
                            
                            
                            if "notes" in notes_rozhodnuti or "notesu" in notes_rozhodnuti or "udelej" in notes_rozhodnuti or "pokracuj" in notes_rozhodnuti:
                                text(Fore.YELLOW + "\nMusíš se dostat do města.. Problém je v tom že nemáš jak.")
                                cekej(5)
                                text(Fore.YELLOW + "Chtělo by to auto..")
                                cekej(3)
                                text(Fore.YELLOW + "POZNÁMKA: Zkus se rozhlédnou kolem.")
                                
                                
                            elif("rozhledni" in notes_rozhodnuti or "prozkoumej" in notes_rozhodnuti):
                                text(Fore.YELLOW + "\nNacházíš se ve starém domu. V místnosti která by se dala nazvat obývákem.")
                                cekej(6)
                                text(Fore.YELLOW + "Tento dům má další dvě místnosti, koupelnu a kuchyň.")
                                cekej(5)
                                text(Fore.YELLOW + "K domu spadá něco co vypadá jako garáž.")
                                
                                
                            elif("garaz" in notes_rozhodnuti or "garaze" in notes_rozhodnuti):
                                text(Fore.YELLOW + "\nPřicházíš do garáže..")
                                cekej(3)
                                text(Fore.YELLOW + "Podle očekávání tady žádné auto není ale je zde staré kolo.")
                                text("\n---")
                                while True:
                                    garaz = input(Fore.GREEN + "Garáž> ")
                                    
                                    
                                    if "kolo" in garaz or "bicikl" in garaz or "nasedni" in garaz or "nastup" in garaz or "jed" in garaz:
                                        text(Fore.YELLOW + "\nTohle kolo má asi už něco za sebou..")
                                        cekej(4)
                                        text(Fore.YELLOW + "Je celé zrezavělé, pneumatiky jsou vypuštěné.")
                                        cekej(4)
                                        text(Fore.YELLOW + "Naštěstí kousek vedle kola je stůl a na něm pumpička, nafoukneš kolo a můžeš jet.")
                                        cekej(6)
                                        text(Fore.YELLOW + "Nafukování kola - čekej 10s . . .")
                                        time.sleep(10.5)
                                        text(Fore.YELLOW + "Cesta do města - čekej 25s . . .")
                                        time.sleep(12)
                                        text(Fore.YELLOW + "Nastal problém! Při cestě jsi si všiml že se pneumatiky vyfukují velmi rychle.. už jsou skoro prázdné.")
                                        text(Fore.YELLOW + "Ale to není jediný priblém kvůli silnému vítru se ti obtížně dýchá a musíš si dát pauzu.")
                                        cekej(6.5)
                                        text(Fore.YELLOW + "Vypadá to že se k tobě z celého jihu něco blíží.")
                                        cekej(4)
                                        text(Fore.YELLOW + "Odhazuje to všechno co se tomu postavý..")
                                        cekej(3)
                                        text(Fore.YELLOW + "Podle rychlosti to během pár minut u tebe.")
                                        text("\n---")
                                        while True:
                                            vlna = input(Fore.GREEN + "Nebezpečí> ")
                                            
                                            
                                            if vlna == "666":
                                                text(Fore.YELLOW + "???\n")
                                                
                                                
                                            else: 
                                                text(Fore.YELLOW + "\nDělal jsi co jsi mohl..")
                                                text("Konec 5")
                                                text("Byl jsi rozdrcen mohutnou tlakovou vlnou.")
                                                konec_hry()
                                
                                
                                    else:
                                        nejde()


                            else:
                                nejde()


                    elif("zpatky" in dum_notes or "zpet" in dum_notes):
                        text(Fore.YELLOW + "\nJsi spátky tam kde jsi začal.")
                        cekej(4)
                        text(Fore.YELLOW + "Teď už můžeš jít jen a pouze na jih")
                        zacni_hru()


                    else:
                        nejde()


            else:
                nejde()


    elif prikaz == "jdi j" or prikaz == "jdi jih" or prikaz == "jdi na jih":
        text(Fore.YELLOW + "\nPřišel jsi do lesa jsi vyčerpaný z té cesty...")
        cekej(1)
        text(Fore.YELLOW + "Vypadá to že dál na jihu je něco připomínající studánku.")
        cekej(1.5)
        text(Fore.YELLOW + "Na východě se nachází nějaké obydlý.")
        cekej(2)
        text(Fore.YELLOW + "Můžeš se vrátit zpět na sever do vesnice.")
        text("\n---")
        while True:
            les = input(Fore.GREEN + "V LESE> ")


            if "studanka" in les or "studance" in les or "studanku" in les:
                text(Fore.YELLOW + "\nPřišel jsi k lesní studánce.. je vyschlá. Vypadá že tady už voda dlouho nebyla.")
                cekej(7)
                text(Fore.YELLOW + "Nic moc tady není. Vrátil jsi se zpátky na cestu.")


            elif("obydly" in les or "obydlimu" in les):
                text(Fore.YELLOW + "\nPokračuješ cestou na jih. ")
                cekej(4)
                text(Fore.YELLOW + "Přicházíš k plotu.")
                text("\n---")
                while True:
                    plot = input(Fore.GREEN + "Plot> ")


                    if "prelez" in plot:
                        text(Fore.YELLOW + "\nPlot nelze přelézt. Je vysoký a na vrcholu ostnatý.")
                        cekej(5)
                        text(Fore.YELLOW + "Tip: Zkus najít nějaký vchod nebo branku.")


                    elif("branku" in plot or "vchod" in plot or "otevři" in plot or "obejdi" in plot or "najdi" in plot):
                        text(Fore.YELLOW + "\nPokusíš se najít nějaký vchod.")
                        cekej(4)
                        text(Fore.YELLOW + "Našel jsi vchod, je to spíše vjezd. Je opravu veliký.")
                        text("\n---")
                        while True:
                            vstup = input(Fore.GREEN + "Vstup> ")
                            print("ZDE NENÍ KÓD JEŠTĚ HOTOVÝ!!! AUTOMATICKY SE VRACÍŠ NA ZAČÁTEK..")
                            text("\nJsi tam kde jsi začal.")
                            zacni_hru()
                        
                        
                    elif("podivej" in plot or "nahledni" in plot):
                        text(Fore.YELLOW + "\nVypadá že za plotem se nachází nějaká hlídaná zóna.")
                        cekej(5)
                        text(Fore.YELLOW + "Vypadá to jako nějaký hlídací systém. Jaké si kamery hlídají celý prostor.")
                        cekej(6)
                        text(Fore.YELLOW + "Vypadá to že tam nikdo jiný není je tam naprosté ticho.")
                        cekej(4)
                        text(Fore.YELLOW + "Asi tam můžeš vejít.")
                        
                        
                    elif("zpet" in plot or "zpatky" in plot):
                        text(Fore.YELLOW + "\nNemohl jsi najít přesnou cestu zpátky, chvíli ti to trvalo ale jsi zase ve vesnici.")
                        zacni_hru()


                    else:
                        nejde()


            else:
                nejde()


    elif "zapad" in prikaz or "vychod" in prikaz:
        text(Fore.RED + "\nTam to nevypadá bezpečně, radši zůstaneš.")
        text("\n---")
        zacni_hru()



    else:
        print(Fore.RED + "\nNeplatný příkaz. Zkus to znovu.")
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
else:
    uvod()
    zacni_hru()
