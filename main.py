import pandas as pd 
import os
import matplotlib.pyplot as plt 
import squarify 

cityfile = "AUS_state.csv"
data = pd.read_csv(cityfile, usecols=["State/Territory","June 2017[2]"])
print (data)
list_of_cities = data["State/Territory"].tolist()
list_of_populations = data["June 2017[2]"].tolist()

