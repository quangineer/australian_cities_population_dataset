import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib
import squarify 

file_aus = "AUS_state.csv"
data = pd.read_csv(file_aus)

data_2017 = data["June 2017[2]"]
data_State = data["State/Territory"]
#Making a list of 2017 populations cities by stripping off all commas:
Population_2017 = []
for i in data_2017:
    a = int(i.replace(",",""))
    Population_2017.append(a)

State_to_Population = []
for i in range(len(data_State)):
    State_to_Population.append([data_State[i],data_2017[i]])
# print (State_to_Population)

#Sort cities' populations from largest to smallest:
Population_2017.sort(reverse = True)
# print (Population_2017)
#OR
# A = sorted(Population_2017)
# print A

#Sort cities's populations from smallest to largest:
# Population_2017.sort()
# print (Population_2017)
#The difference between sort and sorted is that sort is a list method that modifies the list in place
#whereas sorted is a built-in function that creates a new list without touching the original one.

New_list_of_Population_2017 = []
K = 0
for i in range(len(Population_2017)):
    if i < 5:
        New_list_of_Population_2017.append(Population_2017[i])
    elif i >= 5:
        K = K + Population_2017[i]
New_list_of_Population_2017.append(K)
# print (New_list_of_Population_2017)



New_list_of_State = []
for i in range(len(State_to_Population)):
    if i < 5:
        New_list_of_State.append(State_to_Population[i][0])
New_list_of_State.append("Other")

# print (New_list_of_State)

# #Utilise matplotlib to scale our goal numbers between the min and max, then assign this scale to our values.
norm = matplotlib.colors.Normalize(vmin=min(New_list_of_Population_2017), vmax=max(New_list_of_Population_2017))
colors = [matplotlib.cm.Oranges(norm(value)) for value in New_list_of_Population_2017]

# #Create our plot and resize it.
fig = plt.gcf()
ax = fig.add_subplot()
fig.set_size_inches(16, 4.5)

# #Use squarify to plot our data, label it and add colours. We add an alpha layer to ensure black labels show through
squarify.plot(label=New_list_of_State,sizes=New_list_of_Population_2017, color = colors, alpha=.6)
plt.title("Australian Cities Population",fontsize=23,fontweight="bold")

# #Remove our axes and display the plot
plt.axis('off')
plt.show()