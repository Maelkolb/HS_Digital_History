import matplotlib.pyplot as plt

# Werte für True Positives, False Positives und False Negatives
true_positives = 25
false_positives = 2
false_negatives = 9

# Berechnung von Precision, Recall und F-Score
precision = true_positives / (true_positives + false_positives)
recall = true_positives / (true_positives + false_negatives)
f_score = (2 * precision * recall) / (precision + recall)

# Runden von Precision und Recall
precision = round(precision, 4)
recall = round(recall, 4)
f_score = round(f_score, 4)

# Daten für das Diagramm
categories = ['True Positives', 'False Positives', 'False Negatives', 'Precision', 'Recall', 'F-Score']
values = [true_positives, false_positives, false_negatives, precision, recall, f_score]

# Erstellen des Balkendiagramms
plt.figure(figsize=(10, 6))
bars = plt.bar(categories, values, color=['green', 'red', 'purple', 'blue', 'orange', 'gray'])
plt.ylabel('Werte')
plt.title('Evaluierung der Klassifikation von Personennamen durch NER')

# Anpassung
plt.ylim(0, max(values) * 1.2)  # Setze die Y-Achsenbegrenzung

# Anzeigen der Werte
for bar, value in zip(bars, values):
    plt.text(bar.get_x() + bar.get_width() / 2, value, str(value), ha='center', va='bottom')

# Speicherung
plt.savefig('precision_recall_diagramm2.jpg')

plt.show()
