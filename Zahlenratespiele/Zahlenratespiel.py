import random
import tkinter as tk

def zahlenraten():
    zielzahl = random.randint(1, 100)
    versuche = 0

    print("Willkommen beim Zahlenraten-Spiel!")
    print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Kannst du sie erraten?")


    while True:
        eingabe = int(input("Gib eine Zahl ein: "))
        versuche += 1

        if eingabe < zielzahl:
            print("Die gesuchte Zahl ist größer!")
        elif eingabe > zielzahl:
            print("Die gesuchte Zahl ist kleiner!")
        else:
            print(f"Glückwunsch! Du hast die Zahl in {versuche} Versuchen erraten!")
            break


zahlenraten()