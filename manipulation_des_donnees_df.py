import pandas as pd

df = pd.read_csv('Dataset_Employes.csv', sep=';')

# Renomer les colonnes
df.rename(columns={'Niveau de satisfaction' : 'Niv Sat'}, inplace=True)
df.rename(columns={'Salaire base mensuel' : 'Salaire/Mois'}, inplace=True)
df.rename(columns={'Distance domicile/Travail' : 'Distance Travail'}, inplace=True)
df.rename(columns={'id_salarié' : 'Id'}, inplace=True)

# Modifier des valeurs dans une colonne par balayage
df['Service'] = df['Service'].replace('Compta Finances', 'Finances')

print(df)