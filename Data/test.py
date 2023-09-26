import yaml
import random
import sys
import time

# načte config soubor
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

animace_textu = config.get('animace_textu', False)

# Definice funkce pro animaci nebo standardní výpis
def print_text(t):
    if animace_textu:
        typing_speed = 50  # wpm
        for l in t:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(random.random()*10.0/typing_speed)
        print("")
    else:
        print(t)

# Použití funkce
print_text("Toto je testovací text.")
print_text("A toto je další řádek")
