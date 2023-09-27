import csv
import geopandas as gpd
import re

def find_matching_words(input_csv, text_file, output_csv):
    # Werte der Spalte 'country' zwischenspeichern
    with open(input_csv, 'r') as input_file:
        reader = csv.DictReader(input_file)
        countries = set(row['Country'] for row in reader)

    # Textdatei öffnen
    with open(text_file, 'r') as file:
        text = file.read()

    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    world['Centroid'] = world.centroid

    with open(output_csv, 'w', newline='') as output_file:
        fieldnames = ['Modern Toponym', 'Ancient Toponym', 'Country', 'Longitude (X)', 'Latitude (Y)']
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        for country in countries:
            # Verbesserte Ergebnisse
            pattern = r'\b' + re.escape(country) + r'\b'
            if re.search(pattern, text, re.IGNORECASE):
                country_data = world[world['name'] == country]
                if not country_data.empty:
                    centroid = country_data['Centroid'].iloc[0]
                    output_row = {
                        'Modern Toponym': '',
                        'Ancient Toponym': '',
                        'Country': country,
                        'Longitude (X)': centroid.x,
                        'Latitude (Y)': centroid.y
                    }
                    writer.writerow(output_row)

find_matching_words('Hanson2016_Cities.csv', 'Text_euseb_KG.txt', 'output_countries_geopandas.csv')
