from numpy import column_stack
import pandas as pd
import pip
import plotly.express as px
import csv

columns = []
with open ("final_data.csv","r") as f :
    cr = csv.reader(f)
    for column in cr :
        columns.append(column)  
mass = columns[4]
print (mass)
mass = mass*1.989e+30
radius = columns[5]
radius = radius*6.957e+8
planet_gravity = []

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
#fig.show()