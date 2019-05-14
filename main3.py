import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib
import squarify 

file_aus = "AUS_state.csv"
data = pd.read_csv(file_aus, thousands=",")

popColName = "June 2017[2]"

pop = data[popColName].sum()

firstFive = data.sort_values(popColName, ascending=False)[:5]

firstFiveNames = firstFive["State/Territory"].tolist()
firstFiveNames.append("Others")

firstFivePops = firstFive[popColName].tolist()
firstFivePops.append(pop - firstFive[popColName].sum())

# #Utilise matplotlib to scale our goal numbers between the min and max, then assign this scale to our values.
norm = matplotlib.colors.Normalize(vmin=min(firstFive[popColName]), vmax=pop)
colors = [matplotlib.cm.Blues(norm(value)) for value in firstFivePops]

# #Create our plot and resize it.
fig = plt.gcf()
ax = fig.add_subplot()
fig.set_size_inches(16, 4.5)

# #Use squarify to plot our data, label it and add colours. We add an alpha layer to ensure black labels show through
squarify.plot(label=firstFiveNames,sizes=firstFivePops, color = colors, alpha=.6)
plt.title("Australian Cities Population",fontsize=23,fontweight="bold")

# #Remove our axes and display the plot
plt.axis('off')
plt.show()