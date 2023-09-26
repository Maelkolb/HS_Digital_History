import csv

def find_matching_words(input_csv, text_file, output_csv):
    with open(input_csv, 'r') as input_file:
        reader = csv.DictReader(input_file)
        words = set(row['Modern Toponym'] for row in reader)

    with open(text_file, 'r') as file:
        text = file.read()

    with open(output_csv, 'w', newline='') as output_file:
        fieldnames = ['Modern Toponym', 'Ancient Toponym', 'Country', 'Longitude (X)', 'Latitude (Y)']
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()

        for word in words:
            if word in text:
                with open(input_csv, 'r') as input_file:
                    reader = csv.DictReader(input_file)
                    matching_rows = [row for row in reader if row['Modern Toponym'] == word]

                for row in matching_rows:
                    output_row = {fieldname: row[fieldname] for fieldname in fieldnames}
                    writer.writerow(output_row)


find_matching_words('Hanson2016_Cities.csv', 'Text_euseb_KG.txt', 'output_locations7.csv')
