import PyPDF2


def extrahiere_text_von_seite(pdf_datei, startseite, endseite, ausgabe_datei):
    try:
        # PDF-Datei öffnen
        pdf = PyPDF2.PdfReader(pdf_datei)

        # Initialisiere eine leere Zeichenfolge, um den extrahierten Text zu speichern
        extrahierter_text = ""

        # Überprüfe, ob die Start- und Endseiten im gültigen Bereich liegen
        if startseite >= 0 and endseite < len(pdf.pages):
            # Extrahiere den Text von den Seiten
            for seite_num in range(startseite, endseite + 1):
                seite = pdf.pages[seite_num]
                extrahierter_text += seite.extract_text()

            # Speichere den Text in einer Textdatei
            with open(ausgabe_datei, "w", encoding="utf-8") as textdatei:
                textdatei.write(extrahierter_text)

            return f"Extrahierter Text wurde in {ausgabe_datei} gespeichert."
        else:
            return "Ungültige Seitenangaben. Bitte überprüfe die Seitenzahlen."

    except Exception as e:
        return f"Fehler beim Extrahieren und Speichern des Textes: {str(e)}"


# Beispielaufruf
pdf_datei = "euseb_text_pdf.pdf"
startseite = 149  # Hier die Startseite angeben
endseite = 633  # Hier die Endseite angeben
ausgabe_datei = "extrahierter_text4.txt"

ergebnis = extrahiere_text_von_seite(pdf_datei, startseite, endseite, ausgabe_datei)
print(ergebnis)
