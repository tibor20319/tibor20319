# Konstanten definieren
ABSOLUTER_NP_C = -273.15
FEHLERMELDUNG_TEMP = "Fehler: die Temperatur muss größer oder gleich dem absoluten Nullpunkt sein."

# Funktionen für die Umrechnung
def celsius_to_kelvin(c):
    return c + 273.15

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

# Funktion um sicherzustellen, dass der Benutzer eine gültige Zahl eingibt
def get_float(msg = "Bitte Zahl eingeben: "):
    while True:
        try:
            f = float(
input(msg))
            return f
        except ValueError:
            print("Ops! Ungültige Eingabe. Bitte nochmals probieren: ")

# Hauptprogramm
print("Wähle eine der folgenden Optionen:")
print("(1) Umrechnung von Celsius nach Kelvin")
print("(2) Umrechnung von Celsius nach Fahrenheit")
print("(3) Umrechnung von Kelvin nach Celsius")
print("(4) Umrechnung von Kelvin nach Fahrenheit")
print("(5) Umrechnung von Fahrenheit nach Celsius")
print("(6) Umrechnung von Fahrenheit nach Kelvin")
print("(7) Programm beenden")

while True:
    option = int(input("Ihre Auswahl: "))
    if option == 7:
        break

    temperature = get_float("Temperatur eingeben: ")

    if option == 1:
        if temperature >= ABSOLUTER_NP_C:
            print(f"{temperature} °C entspricht {celsius_to_kelvin(temperature)} K")
        else:
            raise TypeError(FEHLERMELDUNG_TEMP)
    elif option == 2:
        if temperature >= ABSOLUTER_NP_C:
            print(f"{temperature} °C entspricht {celsius_to_fahrenheit(temperature)} °F")
        else:
            raise TypeError(FEHLERMELDUNG_TEMP)
    elif option == 3:
        if temperature >= ABSOLUTER_NP_C:
            print(f"{temperature} K entspricht {kelvin_to_celsius(temperature)} °C")
        else:
            raise TypeError(FEHLERMELDUNG_TEMP)
    elif option == 4:
        if temperature >= ABSOLUTER_NP_C:
            print(f"{temperature} K entspricht {kelvin_to_fahrenheit(temperature)} °F")
        else:
            raise TypeError(FEHLERMELDUNG_TEMP)
    elif option == 5:
        print(f"{temperature} °F entspricht {fahrenheit_to_celsius(temperature)} °C")
    elif option == 6:
        print(f"{temperature} °F entspricht {fahrenheit_to_kelvin(temperature)} K")
    else:
        print("Ungültige Eingabe")

print("Programm beendet.")
input ("Belibige Taste drücken um zu beenden.")