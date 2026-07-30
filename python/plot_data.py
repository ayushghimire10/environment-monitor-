import csv 
import matplotlib.pyplot as plt 

#lists for each column of data 
temps = []
humidities = []
lights = []

#read CSV file 
with open ('sensordata.csv', 'r') as f: 
    reader = csv.DictReader(f) #read CSV and use header row to name each column
    for row in reader: 
        temps.append(float(row['temperature_c']))
        humidities.append(float(row['humidity_pct']))
        lights.append(int(row['light']))

print (f"loaded {len(temps)} readings.")

#Plot the three lists in one chart 
plt.plot(temps, label = 'Temperature (C)')
plt.plot(humidities, label = 'Humidity (%)')
plt.plot(lights, label = 'Light (raw)')

plt.xlabel('Reading number')
plt.ylabel('Value')
plt.title('Environment Monitor readings')
plt.legend()
plt.savefig('readings.png')
plt.show()