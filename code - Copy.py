import  pymysql as PyMySQL  #libraries 
import pandas as pd
import numpy as np
import os
import random
import math
import operator
from numpy import array
# Open database connection
db = PyMySQL.connect("localhost","root","usbw","test" )



# to run queries
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT Air_temp_mean, Relative_humidity, Global_rad, Reflective_rad, Net_Rad, Soil_temp_5, Soil_temp_30, soil_temp_50, Wind_direction_from_north, WindDir_SD1_WVT, WindSpeed, Rain, SnowDepth, Pressure,	AirTempMax, AirTempMin FROM table2"
totalElement=cursor.execute(sql)


# Fetch all the rows in a list of lists.
results = cursor.fetchall()
results = results[4:]
#print(results)

#defining BaseSequence

BaseSequence=[]
lines = results
dataset = list(lines)

for y in range(0,30):
    BaseSequence.append(dataset[-1*y])
#print(len(BaseSequence))
index=[]
#Defining allSequence
allSequence = list(set(dataset)-set(BaseSequence))

max_month_size = 31 
march = allSequence[0:30]
while(len(march) != max_month_size):
    march.append(0)    

feb = allSequence[30:58]
while(len(feb) != max_month_size):
    feb.append(0)    

jan = allSequence[58:89]
while(len(jan) != max_month_size):
    jan.append(0)    

months = [march, feb, jan]
#Splitting data into test dataset and train dataset randomly

#Applying Euclidean Distance


def euclideanDistance(instance1, instance2, length):
    distance = []
    for z in range (len(instance2)):
        for x in range(len(instance1)):
            dist=[]
            d=0
            for y in range(len(instance1[x])):
                #print(instance1[x][y], instance2[x][y])
                d+=( pow(float(instance1[x][y]) - float(instance2[x][y]), 2))
            #print(d)
                
            dist.append(math.sqrt(float(d)))
            #print(dist)
            distance.append(dist)
        return distance
    instance2[-30:]
distance = euclideanDistance(BaseSequence, allSequence, 2)
print ('Distance: ' + repr(distance))


    
#print('Distance: ' + str(len(distance)))









