import nltk
from nltk.corpus import stopwords
import csv

input_entities_file_path = "PERSON_entities.txt"  #  Datei mit den Entitäten
input_text_file_path = "cleaned_lemmatized_text_KG-full.txt"  # Textdatei
output_file_path = "5entity_co_occurrence_analysis.csv"  # Ausgabedatei

# Entitäten aus der Datei + case-folding
with open(input_entities_file_path, 'r', encoding='utf-8') as entities_file:
    entities = [entity.strip().lower() for entity in entities_file.readlines()]


# Funktion zur Kookkurrenzanalyse 
def entity_co_occurrence_analysis(text, entities, min_frequency, max_distance):
    entity_co_occurrence_matrix = {entity: {co_entity: 0 for co_entity in entities if co_entity != entity}
                                  for entity in entities}

    sentences = nltk.sent_tokenize(text.lower())

    for sentence in sentences:
        tokens = nltk.word_tokenize(sentence)
        stop_words = set(stopwords.words('english'))
        filtered_words = [word for word in tokens if word.isalpha() and word not in stop_words]

        for i in range(len(filtered_words)):
            word_i = filtered_words[i]
            for source_entity in entities:
                if word_i == source_entity:
                    for j in range(i + 1, min(i + max_distance + 1, len(filtered_words))):
                        word_j = filtered_words[j]
                        for target_entity in entities:
                            if word_j == target_entity and source_entity != target_entity:
                                entity_co_occurrence_matrix[source_entity][target_entity] += 1
                                entity_co_occurrence_matrix[target_entity][source_entity] += 1
                                break  # Beende die innere Schleife, da die Entität bereits gefunden wurde

    # Filterung basierend auf max_distance & min_frequency
    filtered_entity_co_occurrence_matrix = {entity: {co_entity: co_occurrence
                                                     for co_entity, co_occurrence in co_occurrences.items()
                                                     if co_occurrence >= min_frequency}
                                           for entity, co_occurrences in entity_co_occurrence_matrix.items()}

    return filtered_entity_co_occurrence_matrix

# Text einlesen
with open(input_text_file_path, 'r', encoding='utf-8') as file:
    text = file.read()

min_frequency = 10
max_distance = 15
entity_co_occurrence_matrix = entity_co_occurrence_analysis(text, entities, min_frequency, max_distance)

# Speicherung
with open(output_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["source", "target", "weight"])
    for source_entity, co_occurrences in entity_co_occurrence_matrix.items():
        for target_entity, co_occurrence in co_occurrences.items():
            writer.writerow([source_entity, target_entity, co_occurrence])

print("Kookkurrenzanalyse abgeschlossen. Die Ergebnisse wurden in '{}' gespeichert.".format(output_file_path))
