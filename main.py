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

#Sort cities' populations from largest to smallest:
Population_2017.sort(reverse = True)
print (Population_2017)
#OR
# A = sorted(Population_2017)
# print A

#Sort cities's populations from smallest to largest:
# Population_2017.sort()
# print (Population_2017)
#The difference between sort and sorted is that sort is a list method that modifies the list in place
#whereas sorted is a built-in function that creates a new list without touching the original one.

New_list_of_Population_2017
