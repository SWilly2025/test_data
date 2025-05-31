import pandas as pd

df = pd.read_excel('Dataset_Employes.xlsx')

#Renommer des colonnes
df.rename(columns={'Niveau de satisfaction' : 'Satisfaction'}, inplace=True)
df.rename(columns={'Salaire base mensuel' : 'Salaire'}, inplace=True)
df.rename(columns={'id_salarié' : 'Id'}, inplace=True)
df.rename(columns={'Distance domicile/Travail' : 'Distance Domicile'}, inplace=True)
df.rename(columns={'Type Contrat' : 'Statut'}, inplace = True)
df.rename(columns={'Ancienneté_an' : 'Ancienneté'}, inplace = True)

#Balayer une colonne pour y modifier des valeurs
df['Service'] = df['Service'].replace('Compta Finances', 'Finances')
df['Service'] = df['Service'].replace('Technicien', 'Tech')
print(df)

# Faire pivoter des données
pivot = df.pivot_table(index = 'Contrat', columns = 'Service', values = 'Salaire', aggfunc = 'mean')
pivot_reset = pivot.reset_index()
print(pivot_reset.head)