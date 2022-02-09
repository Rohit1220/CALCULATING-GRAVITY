from numpy import column_stack
import pandas as pd
import pip,csv
import plotly.express as px


df = pd.read_csv("final_data.csv")
print(df.columns)

mass = df['Mass'].to_list()
mass.pop(0)
print(mass)
new_mass = []
for i in range (0,len(mass)):
  temp = float(mass[i])
  temp2 = temp*1.989e+30
  new_mass.append(temp2)
print(new_mass)

radius = df['Radius'].to_list()
radius.pop(0)
print(radius)
new_radius = []
for i in range (0,len(radius)):
  temp3 = float(mass[i])
  temp4 = temp3*1.989e+30
  new_radius.append(temp4)
print(new_radius)

gravity = []
def gravity():
  for i in range (0,len(new_mass)):
    temp5 = float(new_mass[i])
    temp6 = float(new_radius[i])
    temp7 = temp5*temp6
    gravity.append(temp7)
  
  
#columns = []
"""with open ("final_data.csv","r") as f :
    cr = csv.reader(f)
    for column in cr :
        columns.append(column)  
print(columns)
mass = columns[10]
print (mass)
mass = mass*1.989e+30
radius = columns[4]
radius = radius*6.957e+8
planet_gravity = []"""

"""for i in range (0,len(mass)):
  mass[i] = mass[i]*1.989e+30"""


#def gravity():
 # G = 6.67*1/100000000000*N*
 # gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11
 # planet_gravity.append(gravity)

#planet_masses = []
#planet_radiuses = []
#planet_names = []
#planet_gravity = []
#for index, name in enumerate(planet_names):
 # gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11
  #planet_gravity.append(gravity)

#fig = px.scatter(x=planet_radiuses, y=planet_masses, size=planet_gravity, hover_data=[planet_names])
#fig.show()"""""""