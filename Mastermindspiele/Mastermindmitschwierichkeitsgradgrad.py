import random

# Funktion zur Generierung einer geheimen Zahlenkombination basierend auf der Schwierigkeit
def generate_secret_code(difficulty):
    if difficulty == "easy":
        return generate_code(4, 6)  # 4-stelliger Code mit Zahlen von 1 bis 6
    elif difficulty == "medium":
        return generate_code(5, 8)  # 5-stelliger Code mit Zahlen von 1 bis 8
    elif difficulty == "hard":
        return generate_code(6, 9) # 6-stelliger Code mit Zahlen von 1 bis 9
    else:
        raise ValueError("Ungültige Schwierigkeitsstufe.")

# Funktion zur Generierung eines Codes mit bestimmter Länge und maximal zwei gleichen Ziffern
def generate_code(length, max_digit):
    code = []
    for _ in range(length):
        digit = random.randint(1, max_digit)
        while code.count(digit) >= 2:  # Überprüfen, ob die gleiche Ziffer bereits zweimal im Code vorhanden ist
            digit = random.randint(1, max_digit)
        code.append(digit)
    return code

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
def validate_input(guess, difficulty):
    if len(guess) != len(generate_secret_code(difficulty)):
        return False
    for digit in guess:
        if not digit.isdigit() or int(digit) < 1 or int(digit) > 10:
            return False
    return True

# Funktion zum Ausdrucken der Anleitung
def print_instructions():
    print("Mastermind Spiel")
    print("Errate die geheime Zahlenkombination.")
    print("Die Zahlen liegen zwischen 1 und der maximalen Farbenzahl des gewählten Schwierigkeitsgrades.")
    print("Nach jedem Zug erhältst du Feedback:")
    print("  - Eine 0 bedeutet, dass keine Zahlen richtig sind.")
    print("  - Eine Zahl größer als 0 bedeutet, dass eine Zahl richtig ist, aber nicht an der richtigen Stelle.")
    print("  - Eine Zahl gleich der Länge der geheimen Kombination bedeutet, dass du alle Zahlen richtig erraten hast.")
    print("Viel Spaß!")

# Hauptfunktion des Spiels
def play_mastermind(difficulty):
    print_instructions()
    secret_code = generate_secret_code(difficulty)
    attempts = 0

    while True:
        guess = input("Gib deine Vermutung ein: ")
        
        if not validate_input(guess, difficulty):
            print(f"Ungültige Eingabe. Bitte gib {len(secret_code)} Zahlen zwischen 1 und der maximalen Farbenzahl des gewählten Schwierigkeitsgrades ein.")
            continue
        
        guess = [int(digit) for digit in guess]
        correct_color_and_position, correct_color_only = check_guess(secret_code, guess)
        attempts += 1

        print(f"Feedback: {correct_color_and_position} Zahlen an der richtigen Stelle, {correct_color_only} Zahlen an der falschen Stelle.")
        
        if correct_color_and_position == len(secret_code):
            print(f"Herzlichen Glückwunsch! Du hast die geheime Zahlenkombination in {attempts} Versuchen erraten!")
            break

    return attempts

# Starte das Spiel
difficulty = input("Wähle den Schwierigkeitsgrad (easy (Zwischen1 und 6 und 4 Zahlen), medium (Zwischen1 und 8 und 5 Zahlen), hard (Zwischen1 und 9 und 6 Zahlen)): ").lower()
attempts = play_mastermind(difficulty)
print(f"Anzahl der Versuche: {attempts}")

input()
