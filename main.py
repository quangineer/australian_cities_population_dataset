import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib
import squarify 

file_aus = "AUS_state.csv"
data = pd.read_csv(file_aus)

data_2017 = data["June 2017[2]"]

#Making a list of 2017 populations cities by stripping off all commas:
Population_2017 = []
for i in data_2017:
    a = int(i.replace(",",""))
    Population_2017.append(a)

#New dataframe, containing only population of cities with more than 0 person living in:
dataPopulations = data["Population_2017">0]
print (dataPopulations)

# #Utilize matplotlib to scale our population between the min and the max, then assign this scale to our values.
# norm = matplotlib.colors.Normalize(vmin=min())