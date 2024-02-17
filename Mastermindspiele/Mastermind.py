import random

# Funktion zur Generierung einer geheimen Zahlenkombination
def generate_secret_code():
    return [random.randint(1, 6) for _ in range(4)]

# Funktion zur Überprüfung der Eingabe und Berechnung der Anzahl von korrekten Farben und Positionen
def check_guess(secret_code, guess):
    correct_color_and_position = 0
    correct_color_only = 0

    for i in range(len(secret_code)):
        if guess[i] == secret_code[i]:
            correct_color_and_position += 1
        elif guess[i] in secret_code:
            correct_color_only += 1

    return correct_color_and_position, correct_color_only

# Funktion zur Überprüfung, ob die Eingabe gültig ist
def validate_input(guess):
    if len(guess) != 4:
        return False
    for digit in guess:
        if not digit.isdigit() or int(digit) < 1 or int(digit) > 6:
            return False
    return True

# Funktion zum Ausdrucken der Anleitung
def print_instructions():
    print("Mastermind Spiel")
    print("Errate die geheime Zahlenkombination.")
    print("Die Zahlen liegen zwischen 1 und 6.")
    print("Nach jedem Zug erhältst du Feedback:")
    print("  - Eine 0 bedeutet, dass keine Zahlen richtig sind.")
    print("  - Eine Zahl größer als 0 bedeutet, dass eine Zahl richtig ist, aber nicht an der richtigen Stelle.")
    print("  - Eine Zahl gleich 4 bedeutet, dass du alle Zahlen richtig erraten hast.")
    print("Viel Spaß!")

# Hauptfunktion des Spiels
def play_mastermind():
    print_instructions()
    secret_code = generate_secret_code()
    attempts = 0

    while True:
        guess = input("Gib deine Vermutung ein (4 Zahlen zwischen 1 und 6, z.B. 1234): ")
        
        if not validate_input(guess):
            print("Ungültige Eingabe. Bitte gib 4 Zahlen zwischen 1 und 6 ein.")
            continue
        
        guess = [int(digit) for digit in guess]
        correct_color_and_position, correct_color_only = check_guess(secret_code, guess)
        attempts += 1

        print(f"Feedback: {correct_color_and_position} Zahlen an der richtigen Stelle, {correct_color_only} Zahlen an der falschen Stelle.")
        
        if correct_color_and_position == 4:
            print(f"Herzlichen Glückwunsch! Du hast die geheime Zahlenkombination in {attempts} Versuchen erraten!")
            break

# Starte das Spiel
play_mastermind()
