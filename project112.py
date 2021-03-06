# -*- coding: utf-8 -*-
"""project112.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CS5dJpOoURkmOIVFt1ZyplDsXoPAoGbS
"""

import csv
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import pandas as pd
import statistics
import  numpy as np
#from google.colab import files 
#data_to_load=files.upload()

#plotting the graph
df=pd.read_csv('data.csv')
fig=px.scatter(df,y='quant_saved',color='highschool_completed')
fig.show()

#bar graph for people who went to highschool vs who didn't

with open('data.csv',newline="") as f:
  reader=csv.reader(f)
  savings_data=list(reader)
  savings_data.pop(0)
print(savings_data)

total_entries=len(savings_data)
total_people_highschool_completed=0

for data in savings_data:
  if int(data[2])==1:
    total_people_highschool_completed+=1

fig=go.Figure(go.Bar(x=['HighSchoolCompleted','HighSchoolNotCompleted'],
              y=[total_people_highschool_completed,
              (total_entries-total_people_highschool_completed)]))
fig.show()

#Mean.median.mode of quant_saved

all_savings=[]
for data in savings_data:
  all_savings.append(float(data[0]))

mean_of_savings=statistics.mean(all_savings)
median_of_savings=statistics.median(all_savings)
mode_of_savings=statistics.mode(all_savings)

print("Mean of Savings=",mean_of_savings)
print("Median of Savings=",median_of_savings)
print("Mode of Savings=",mode_of_savings)

#mean.median,mode for people who completed highschool who didn't
highschool_savings=[]
not_highschool_savings=[]

for data in savings_data:
  if int(data[3])==1:
    highschool_savings.append(float(data[0]))

  else:
    not_highschool_savings.append(float(data[0]))

mean_highschool=statistics.mean(highschool_savings)
median_highschool=statistics.median(highschool_savings)
mode_highschool=statistics.mode(highschool_savings)

mean_not_highschool=statistics.mean(not_highschool_savings)
median_not_highschool=statistics.median(not_highschool_savings)
mode_not_highschool=statistics.mode(not_highschool_savings)


print("Mean of highschool completed",mean_highschool)
print("Median of highschool completed",median_highschool)
print("Mode of highschool completed",mode_highschool)
print("\n\n")
print("Mean of not completed highschool",mean_not_highschool)
print("Median of not completed highschool",median_not_highschool)
print("Mode of not completed highschool",mode_not_highschool)


print(f"Standard deviation of all the data->{statistics.stdev(all_savings)}")

print(f"Standard deviation of highschool data->{statistics.stdev(highschool_savings)}")
print(f"Standard deviation of not highschool data->{statistics.stdev(not_highschool_savings)}")

#correlation
wealthy=[]
savings=[]
for data in savings_data:
  if float(data[3])!=0:
     wealthy.append(float(data[3]))
     savings.append(float(data[0]))
   


correlation=np.corrcoef(wealthy,savings)
print("Correlation ",correlation [0,1])

fig=ff.create_distplot([df['quant_saved'].tolist()],['Savings'],show_hist=False)
fig.show()