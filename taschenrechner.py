# Dies ist ein Kommentar, der vom Computer ignoriert wird
# Die folgende Zeile fragt den Benutzer nach der ersten Zahl
num1 = input("Bitte geben Sie die erste Zahl ein: ")

# Die folgende Zeile fragt den Benutzer nach der zweiten Zahl
num2 = input("Bitte geben Sie die zweite Zahl ein: ")

# Hier wird der Benutzer nach der gewünschten Rechenoperation gefragt
operation = input("Bitte geben Sie die gewünschte Rechenoperation ein (+, -, *, /): ")

# Hier wird das Ergebnis der Rechenoperation berechnet und gespeichert
if operation == "+":
  result = num1 + num2
elif operation == "-":
  result = num1 - num2
elif operation == "*":
  result = num1 * num2
elif operation == "/":
  result = num1 / num2
else:
  # Wenn die eingegebene Rechenoperation ungültig ist, wird eine Fehlermeldung ausgegeben
  print("Ungültige Rechenoperation")

# Hier wird das Ergebnis ausgegeben
print(result)
