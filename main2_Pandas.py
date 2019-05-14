import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib
import squarify 

# 2 ways to access a column in pandas/SQL:
#print(data.Growth)
#print(data["Growth"])
#Because sometime the tittle of the columns come from # style that may include comma, space, semicol

file_aus = "AUS_state.csv"
data = pd.read_csv("AUS_state.csv", thousands=",")

# New dataframe, containing only players with more than 0 goals.
dataPopulations = data[data["June 2017[2]"] > 0]["June 2017[2]"]

# #Utilise matplotlib to scale our goal numbers between the min and max, then assign this scale to our values.
norm = matplotlib.colors.Normalize(vmin=min(dataPopulations), vmax=max(dataPopulations))
colors = [matplotlib.cm.Blues(norm(value)) for value in dataPopulations]

# #Create our plot and resize it.
fig = plt.gcf()
ax = fig.add_subplot()
fig.set_size_inches(16, 4.5)

# #Use squarify to plot our data, label it and add colours. We add an alpha layer to ensure black labels show through
squarify.plot(label=data["State/Territory"],sizes=dataPopulations, color = colors, alpha=.6)
plt.title("Australian Cities Population",fontsize=23,fontweight="bold")

# #Remove our axes and display the plot
plt.axis('off')
plt.show()