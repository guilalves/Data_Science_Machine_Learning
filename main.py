import pandas as pd
#import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt
#import plotly.express as px

"""Exploração dos dados"""
  
base_credit = pd.read_csv('credit_data.csv', index_col='clientid').head(7)


print(base_credit)
