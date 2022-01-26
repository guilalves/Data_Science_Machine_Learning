from httpx import head
import pandas as pd
#import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt
#import plotly.express as px

"""Exploração dos dados"""
  
base_credit = pd.read_csv('credit_data.csv', index_col='clientid')

# É para trazer as 5 primeiras linhas
#base_credit = base_credit.head()

# É para trazer as 5 ultimas linhas
#base_credit = base_credit.tail()

# Retorna a descrição dos dados numéricos do DataFrame
base_credit = base_credit.describe()
print(base_credit)

""" Filtrando """
# base_credit = base_credit[base_credit['income'] >= 66952.688845] 

# base_credit = base_credit[base_credit['loan'] <= 1.377630]

print(base_credit)
