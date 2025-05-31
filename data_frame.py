import pandas as pd

df = pd.read_csv('Dataset_Employes.csv', sep=';')

# modifier la valeur d'une case spécifique
df.at[1,'Service'] = 'Commercial'

# modifier les éléments d'une colonne
df['Type Contrat'] = df['Type Contrat'].replace('Cadre', 'Cadre Sup')
df['Type Contrat'] = df['Type Contrat'].replace('Non Cadre', 'Cadre')
print()
print(df)