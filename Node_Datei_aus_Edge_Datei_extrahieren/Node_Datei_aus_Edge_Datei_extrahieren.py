import pandas as pd

# CSV-Datei laden
csv_file = "entity_co_occurrence_analysis.csv"
df = pd.read_csv(csv_file)

# Knoten extrahieren
unique_nodes = set(df["source"]).union(set(df["target"]))

# DataFrame 
nodes_df = pd.DataFrame(list(unique_nodes), columns=["Label"])
nodes_df.reset_index(inplace=True)
nodes_df.rename(columns={"index": "Id"}, inplace=True)
nodes_df["Id"] += 1  # Nummerierung von 1 an

# Speicherung
nodes_csv_file = "nodes_people3.csv"
nodes_df.to_csv(nodes_csv_file, index=False)

print("Nodes Datei erfolgreich erstellt.")
