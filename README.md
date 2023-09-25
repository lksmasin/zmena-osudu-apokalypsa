# Hra v Pythonu

Kód napsal LUKYMAS

### Instrukce

1. Nejdříve je nutné nainstalovat potřebné moduly. Pokud nejsou nainstalovány, program provede jejich instalaci automaticky.
   ```
   $ python -m pip install pygame
   $ python -m pip install colorama
   $ python -m pip install pick
   $ python -m pip install threading
   ```
2. (Dobrovolné) Upravte si soubor config.yaml podle svého.

3. Spusťte hru pomocí otevření souboru `spustit`.

### Popis hry

- Začíná v malé vesnici Smutín poblíž menšího města. Probouzíš se s amnézií v době apokalypsy v roce 2050. Tvůj jediný spojenec je telefon, který zobrazuje pouze čas a zprávy od místní vlády. Apokalypsa je způsobena příletem mimozemských lodí, což tě nutí hledat útočiště. Tvá cesta začíná a je na tobě, jak bude pokračovat.

## Možné problémy

1. **Problém:** Soubor `spustit` nelze otevřít.
   **Řešení:** Přejdi do složky `Data` a otevři soubor `spustit.py`. Pokud i s tím jsou problémy nainstaluj si všechny potřebné moduly a otevři soubor `hra.py` ve stejném umístění.
2. **Problém:** Aplikace blabla neodpovída/nereaguje.
   **Řešení:** Stiskni počkat na odpověď programu, a zbytek ignoruj, nebo restartuj hru.


---

Poznámky:
- Před spuštěním si ověřte, zda máte nainstalované potřebné moduly (`pygame`, `colorama`, `pick`, `threading`).
- Pro spuštění hry se vyžaduje soubor `hra.py` (měl by se nacházet ve složce Data).
- Soubor `hra.py` vyžaduje další doplňkové soubory (hudbu) která by se měla nacházet ve složce Data/hudba


![Logo](data/obrazky/logo.png)