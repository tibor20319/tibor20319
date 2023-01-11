numbers = []

while True:
    input_value = input("Gib eine ganze Zahl ein oder 'q' zum Beenden: ")
    if input_value == 'q':
        break
    try:
        numbers.append(int(input_value))
    except ValueError:
        print("Eingabe war keine ganze Zahl. Bitte versuche es erneut.")

numbers.sort()
print("Sortierte Liste: ",numbers)
input ("Taste drücken um zu beenden.")