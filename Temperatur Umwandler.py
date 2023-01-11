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

# Beispielnutzung
print("Wähle eine der folgenden Optionen:")
print("(1) Umrechnung von Celsius nach Kelvin")
print("(2) Umrechnung von Celsius nach Fahrenheit")
print("(3) Umrechnung von Kelvin nach Celsius")
print("(4) Umrechnung von Kelvin nach Fahrenheit")
print("(5) Umrechnung von Fahrenheit nach Celsius")
print("(6) Umrechnung von Fahrenheit nach Kelvin")

option = int(input())
temperature = float(input("Temperatur eingeben: "))

if option == 1:
    print(f"{temperature} °C entspricht {celsius_to_kelvin(temperature)} K")
elif option == 2:
    print(f"{temperature} °C entspricht {celsius_to_fahrenheit(temperature)} °F")
elif option == 3:
    print(f"{temperature} K entspricht {kelvin_to_celsius(temperature)} °C")
elif option == 4:
    print(f"{temperature} K entspricht {kelvin_to_fahrenheit(temperature)} °F")
elif option == 5:
    print(f"{temperature} °F entspricht {fahrenheit_to_celsius(temperature)} °C")
elif option == 6:
    print(f"{temperature} °F entspricht {fahrenheit_to_kelvin(temperature)} K")
else:
    print("Ungültige Eingabe")
input ("Belibige Taste drücken zum Beenden.")