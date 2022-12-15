datenbank = []

# Funktion zum Hinzufügen eines neuen Datensatzes zur Datenbank
def füge_hinzu(name, adresse, alter, kontaktdetails, familienstand):
    neuer_datensatz = {
        "name": name,
        "adresse": adresse,
        "alter": alter,
        "kontaktdetails": kontaktdetails,
        "familienstand": familienstand
    }
    datenbank.append(neuer_datensatz)

# Funktion zum Abfragen eines Datensatzes aus der Datenbank
def frage_ab(name):
    for datensatz in datenbank:
        if datensatz["name"] == name:
            return datensatz
    return None

# Funktion zum Bearbeiten eines Datensatzes in der Datenbank
def bearbeite(name, neuer_name=None, neue_adresse=None, neues_alter=None, neue_kontaktdetails=None, neuer_familienstand=None):
    datensatz = frage_ab(name)
    if datensatz is not None:
        if neuer_name is not None:
            datensatz["name"] = neuer_name
        if neue_adresse is not None:
            datensatz["adresse"] = neue_adresse
        if neues_alter is not None:
            datensatz["alter"] = neues_alter
        if neue_kontaktdetails is not None:
            datensatz["kontaktdetails"] = neue_kontaktdetails
        if neuer_familienstand is not None:
            datensatz["familienstand"] = neuer_familienstand
    return datensatz

# Beispiel-Nutzung:
füge_hinzu("Jane Doe", "123 Main Street", 30, "jane.doe@gmail.com", "single")
füge_hinzu("John Doe", "456 Park Avenue", 35, "john.doe@gmail.com", "verheiratet")

datensatz = frage_ab("Jane Doe")
print(datensatz)

datensatz = bearbeite("Jane Doe", neues_alter=31)
print(datensatz)
