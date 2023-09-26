import csv
from geopy.geocoders import Nominatim

def find_matching_words(input_csv, text_file, output_csv):
   # Werte der Spalte 'country' zwischenspeichern
    with open(input_csv, 'r') as input_file:
        reader = csv.DictReader(input_file)
        countries = set(row['Country'] for row in reader)

    # Textdatei öffnen
    with open(text_file, 'r') as file:
        text = file.read()

    geolocator = Nominatim(user_agent="myGeocoder")

    with open(output_csv, 'w', newline='') as output_file:
        fieldnames = ['Modern Toponym', 'Ancient Toponym', 'Country', 'Longitude (X)', 'Latitude (Y)']
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        for country in countries:
            # Übereinstimmung = Koordinaten abfragen
            if country in text:
                location = geolocator.geocode(country)
                if location:
                    output_row = {
                        'Modern Toponym': '',
                        'Ancient Toponym': '',
                        'Country': country,
                        'Longitude (X)': location.longitude,
                        'Latitude (Y)': location.latitude
                    }
                    writer.writerow(output_row)


find_matching_words('Hanson2016_Cities.csv', 'Text_euseb_KG.txt', 'output_countries.csv')
