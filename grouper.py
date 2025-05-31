import pandas as pd

df = pd.read_excel("Dataset_Employes.xlsx")
grouped = df.groupby(['Type Contrat', 'Service', 'Contrat'])['Salaire base mensuel'].agg(['mean', 'median'])
print(round(grouped, 2))