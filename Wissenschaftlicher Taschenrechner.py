import math

# Funktion zum Berechnen von Sinus, Kosinus und Tangens
def trig_calc_all(angle):
    sin = math.sin(math.radians(angle))
    cos = math.cos(math.radians(angle))
    tan = sin / cos
    return sin, cos, tan

# Hauptschleife
while True:
    # Benutzeraktionen abfragen
    action = input("Bitte geben Sie eine Aktion ein (sin, cos, tan, all, quit): ")

    # Aktion ausführen
    if action == "sin":
        angle = float(input("Bitte geben Sie den Winkel ein: "))
        result = trig_calc_all(angle)
        print(f"Der Sinus von {angle}° ist {result[0]:.2f}")
    elif action == "cos":
        angle = float(input("Bitte geben Sie den Winkel ein: "))
        result = trig_calc_all(angle)
        print(f"Der Kosinus von {angle}° ist {result[1]:.2f}")
    elif action == "tan":
        angle = float(input("Bitte geben Sie den Winkel ein: "))
        result = trig_calc_all(angle)
        print(f"Der Tangens von {angle}° ist {result[2]:.2f}")
    elif action == "all":
        angle = float(input("Bitte geben Sie den Winkel ein: "))
        result = trig_calc_all(angle)
        print(f"Der Sinus von {angle}° ist {result[0]:.2f}")
        print(f"Der Kosinus von {angle}° ist {result[1]:.2f}")
        print(f"Der Tangens von {angle}° ist {result[2]:.2f}")
    elif action == "all":
        print("Taschenrechner wird beendet.")
        break
    else:
        print("Ungültige Aktion.")
