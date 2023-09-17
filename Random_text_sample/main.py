import random

text_datei = 'Text_euseb_KG_full.txt'

with open(text_datei, 'r', encoding='utf-8') as text_datei:
    dein_text = text_datei.read().split()

sample_proportion = 0.01
sample_size = int(len(dein_text) * sample_proportion)

# Zufällige Auswahl der Tokens für das Sample
random_sample = random.sample(dein_text, sample_size)

sample_text = ' '.join(random_sample)
sample_datei_pfad = 'random_sample.txt'
with open(sample_datei_pfad, 'w', encoding='utf-8') as sample_datei:
    sample_datei.write(sample_text)
print(sample_text)
