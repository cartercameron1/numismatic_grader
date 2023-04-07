import pandas as pd
import os

df = pd.read_csv('assets/pgcs_number_output.csv')

for x in range(len(df)):
    os.mkdir('assets/' + str(df.iloc[x]['id']))
