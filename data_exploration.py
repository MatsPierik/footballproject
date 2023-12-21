# Imports
import numpy as np
import pandas as pd

data = pd.read_csv("data/dataset.csv")

print(data[data['Name'] == "Michel Vlap"])
print(data.columns)
print(data['Dirtiness'])