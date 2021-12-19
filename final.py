import csv
dataset1 = []
dataset2 = []
file = open("bright_stars.csv","r")
csv_reader = csv.reader(file)
for row in csv_reader :
    dataset1.append(row)

file = open("unit_converted_stars.csv","r")
csv_reader = csv.reader(file)

for row in csv_reader:
    dataset2.append(row)

headers1 = dataset1[0]
planet_data1 = dataset1[1:]
headers2 = dataset2[0]
planet_data2 = dataset2[1:]
headers = headers1 + headers2
planet_data = []
for index,data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])

file = open("final2.csv","a+")
csvwriter = csv.writer(file)
csvwriter.writerow(headers)
csvwriter.writerows(planet_data)