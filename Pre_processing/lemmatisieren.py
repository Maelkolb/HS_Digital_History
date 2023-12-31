import re
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


nltk.download('wordnet')
nltk.download('punkt')

def process_and_lemmatize(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        # Text in Kleinbuchstaben umwandeln
        text_lower_case = text.lower()

        # Satzzeichen und Zahlen entfernen
        text_cleaned = re.sub(r'[^\w\s]', '', text_lower_case)  # Entfernt Satzzeichen
        text_cleaned = re.sub(r'\d', '', text_cleaned)  # Entfernt Zahlen

        # Lemmatisierung
        lemmatized_text = lemmatize_text(text_cleaned)

        # Speicherung
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(lemmatized_text)

        print("Textbereinigung und Lemmatisierung erfolgreich abgeschlossen.")
    except IOError:
        print("Fehler beim Lesen oder Schreiben der Datei.")

def lemmatize_text(text):
    lemmatizer = WordNetLemmatizer()
    words = word_tokenize(text)  # Tokenisierung
    lemmatized_words = [lemmatizer.lemmatize(word, get_pos(word)) for word in words]
    return ' '.join(lemmatized_words)

        # POS-Tagging
def get_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)  # Falls Tag nicht erkannt wird: Substantiv

if __name__ == "__main__":
    input_file_name = "extrahierter_text4.txt"
    output_file_name = "cleaned_lemmatized_text_KG-full.txt"
    process_and_lemmatize(input_file_name, output_file_name)
