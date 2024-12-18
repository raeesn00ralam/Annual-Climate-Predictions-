import  pymysql as PyMySQL
import math
# Open database connection
db = PyMySQL.connect("localhost","root","usbw","test")
# to run queries
cursor = db.cursor()
# Prepare SQL query to INSERT a record into the database.
sql = "SELECT Air_temp_mean, Relative_humidity, Global_rad, Reflective_rad, Net_Rad, Soil_temp_5, Soil_temp_30, soil_temp_50, Wind_direction_from_north, WindDir_SD1_WVT, WindSpeed, Rain, SnowDepth, Pressure,	AirTempMax, AirTempMin FROM table2"
totalElement=cursor.execute(sql)
num_fields = len(cursor.description)
field_names = [i[0] for i in cursor.description]
# Fetch all the rows in a list of lists.
results = cursor.fetchall()
results = results[4:]
#print(results)

#defining BaseSequence
index=[]
BaseSequence=[]
lines = results
dataset = list(lines)
length=15
k=2
for y in range(0,length):
    BaseSequence.append(dataset[-1*y])

numOfSequence = (len(results)-length)//length
#]print("number",numOfSequence)
indexArray=[]
for i in range(numOfSequence):
    indexArray.append((i*length))
print(indexArray)
distances={}
for i in range(numOfSequence):
    start = indexArray[i]
    dist=0
    for j in range(length):
        d=0
        for y in range(len(BaseSequence[j])):
                d+=( pow(float(BaseSequence[j][y]) - float(results[start+j][y]), 2))
        dist+=math.sqrt(float(d))
    distances[i] = (dist)
selectedSequences=[]
values = list(distances.values())
values.sort()

print("Values :",values)
values = values[:k]
for i in range(k):
    for j in distances.keys():
        if distances[j]==values[i]:
            selectedSequences.append(i)
            break
attributes = len(results[0])
print("Attributes: ",attributes)
predictedValues=[[0]*attributes]*length
for j in range(k):
    index = indexArray[selectedSequences[j]]
    for l in range(length):
        print("index : ",index+l,end =' ')
        for i in range(attributes):
                    print("Prediction for ",l," ",i,": ",results[index+l][i]," value: ",predictedValues[l][i])
                    predictedValues[l][i]+=results[index+l][i]

#print(predictedValues)
#for j in range(length):
 #   for i in range(attributes):
  #      predictedValues[j][i] = predictedValues[j][i]/k
#for i in range(length):
 #   print("Day ",i+1)
  #  for j in range(attributes):
   #     print(field_names[j],": ",predictedValues[i][j],end= ' ')
    #print()
