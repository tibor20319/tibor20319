def final_grade(exam_grade, eye_color, hair_length, weather):
    # Prüfungsnote anpassen
    if eye_color == "dunkel":
        if hair_length == "kurze Haare":
            exam_grade += exam_grade * 0.1
        else:
            exam_grade -= exam_grade * 0.1
    else:
        if hair_length == "kurze Haare":
            exam_grade -= exam_grade * 0.1
        else:
            exam_grade += exam_grade * 0.1

    # Wetter berücksichtigen
    if weather == "schön":
        exam_grade -= 1

    # Runden auf halbe Noten
    return round(exam_grade * 2) / 2

# Beispielaufruf
exam_grade = 5.5
eye_color = "dunkel"
hair_length = "lange Haare"
weather = "schön"
final_note = final_grade(exam_grade, eye_color, hair_length, weather)
print("Die abschließende Note beträgt:", final_note)
def final_grade(exam_grade, eye_color, hair_length, weather, gender, age, missed_exams):
    # Prüfungsnote anpassen
    if eye_color == "dunkel":
        if hair_length == "kurze Haare":
            exam_grade += exam_grade * 0.1
        else:
            exam_grade -= exam_grade * 0.1
    else:
        if hair_length == "kurze Haare":
            exam_grade -= exam_grade * 0.1
        else:
            exam_grade += exam_grade * 0.1

    # Wetter berücksichtigen
    if weather == "schön":
        exam_grade -= 1

    # Geschlecht des Prüflings berücksichtigen
    if gender == "weiblich":
        exam_grade += exam_grade * 0.05
        
    # Alter des Prüflings berücksichtigen
    if age == 1:
        exam_grade += 0.5
    elif age == 2:
        exam_grade += 1
    elif age == 3:
        exam_grade += 1.5
        
    # Anzahl der versäumten Prüfungen berücksichtigen
    if missed_exams == 1:
        exam_grade -= 0.5
    elif missed_exams == 2:
        exam_grade -= 1
    elif missed_exams >= 3:
        exam_grade -= 1.5
    
    # Runden auf halbe Noten
    return round(exam_grade * 2) / 2
input ("Belibige Taste drücken um zu beenden.")
