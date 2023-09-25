# -*- coding: utf-8 -*-
try:
  import pygame, colorama, pick
except ImportError:
  print("Instaluji potřebný modul.\n")
  os.system('python -m pip install pygame')
  os.system('python -m pip install colorama')
  os.system('python -m pip install pick')
  os.system('python -m pip install threading')
print("Modul není třeba instalovat jelikož je již nainstalován.")

import sys,time,random,os
from pick import pick
from colorama import init, Fore

typing_speed = 50 #wpm
def print_slow(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)

def vypraveni():
   os.system("clear")
   os.system("cls")
   print_slow("Probouzíš se ve vesnici Smutín poblíž menšího městečka..")
   print_slow("\nÚplně si nejsi jistý jak jsi se tady vzal a kdo vlastně jsi.")
   print_slow("\nJediné co výš je že podle telefonu právě začala apokalipsa. \nTelefon se automaicky přepnul do nouzového režimu kdy zobrazuje pouze čas a aktuální zprávy od místní vlády. \nPodle času na displeji je aktuálně 4.24 hodin a rok 2050.")
   time.sleep(3)
   print_slow("\nZpráva z vlády která se na displeji ukazuje ti říká že se máš ukrýt doma a poslouchat rozhlas. \nOvšem ty pořádně nevíš co se děje a tvůj dům je kdo ví kde. \nPrávě teď se spustí rozhlasové hlášení 'Dobrý den, prosím zachovejte klid, najděte bezpečný ukrit a počkejte na IZS až vás přijede evakuovat. K zemi se blíží mimozemské lodě. Další hlášení proběhne v 6.00, aktuálně je 4.30. Konec hlášení'. \nA právě tady začíná tvá cesta.")
   vypraveni = input("\nPOKRAČUJ STISKNUTÍM JAKÉKOLIV KLÁVESY...")
   if vypraveni == "1":
      pass
   else:
      pass

os.system("clear")
os.system("cls") 

# Inicializace colorama pro podporu barev ve Windows
init(autoreset=True)

options = ['Spustit hru', 'Ukončit', "Debuging"]
title = f"""
███████╗███╗   ███╗███╗   ██╗ █████╗      ██████╗ ███████╗██╗   ██╗██████╗ ██╗   ██╗     
╚══███╔╝████╗ ████║████╗  ██║██╔══██╗    ██╔═══██╗██╔════╝██║   ██║██╔══██╗██║   ██║██╗  
  ███╔╝ ██╔████╔██║██╔██╗ ██║███████║    ██║   ██║███████╗██║   ██║██║  ██║██║   ██║╚═╝  
 ███╔╝  ██║╚██╔╝██║██║╚██╗██║██╔══██║    ██║   ██║╚════██║██║   ██║██║  ██║██║   ██║██╗  
███████╗██║ ╚═╝ ██║██║ ╚████║██║  ██║    ╚██████╔╝███████║╚██████╔╝██████╔╝╚██████╔╝╚═╝  
╚══════╝╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝      

   █████╗ ██████╗  ██████╗ ██╗  ██╗ █████╗ ██╗     ██╗██████╗ ███████╗ █████╗ 
  ██╔══██╗██╔══██╗██╔═══██╗██║ ██╔╝██╔══██╗██║     ██║██╔══██╗██╔════╝██╔══██╗
  ███████║██████╔╝██║   ██║█████╔╝ ███████║██║     ██║██████╔╝███████╗███████║
  ██╔══██║██╔═══╝ ██║   ██║██╔═██╗ ██╔══██║██║     ██║██╔═══╝ ╚════██║██╔══██║
  ██║  ██║██║     ╚██████╔╝██║  ██╗██║  ██║███████╗██║██║     ███████║██║  ██║
  ╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝ 
  """

selected_option, _ = pick(options, title)

if selected_option == 'Exit':
    print('Končím...')
elif selected_option == "Spustit hru":
   print_slow("Hru vytovřil LUKYMAS")
   time.sleep(3)
   vypraveni()
#   os.chdir('Data')
   exec(open('hra.py', 'r', encoding='utf-8').read())
elif selected_option == "Debuging":
#   os.chdir('Data')
   exec(open('hra-debug.py', 'r', encoding='utf-8').read())

else:
    print('Hm.. něco nefungovalo zkus to znovu.')