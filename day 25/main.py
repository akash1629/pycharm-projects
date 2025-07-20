import csv

from numpy.ma.extras import average

with open("weather_data.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)       # create reader object
    temperature = []
    for row in reader:
        print(row[1])
        temperature.append(row[1])
    print(temperature)

import pandas
data = pandas.read_csv("weather_data.csv")
print(data['temp'])
data_dict=data.to_dict()
print(data_dict)
print(average(data['temp']))
print(data.temp.max())
data_dic={
          "student":["james","rahul"],"scores":[56,65]
}
print(pandas.DataFrame(data_dic))
dac=pandas.DataFrame(data_dic)
dac.to_csv("new.csv")