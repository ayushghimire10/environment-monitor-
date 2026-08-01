import csv 
import matplotlib.pyplot as plt 
from datetime import datetime 

#lists for each column of data 
timestamps = []
temps = []
humidities = []
lights = []

#read CSV file 
with open ('sensordata.csv', 'r') as f: 
    reader = csv.DictReader(f) #read CSV and use header row to name each column
    for row in reader: 
        timestamps.append(datetime.fromisoformat(row['timestamp']))
        temps.append(float(row['temperature_c']))
        humidities.append(float(row['humidity_pct']))
        lights.append(int(row['light']))

print (f"loaded {len(temps)} readings.")

fig, axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)

axes[0].plot(timestamps, temps, color='tab:blue')
axes[0].set_ylabel('Temp (C)')
axes[0].grid(True, alpha=0.3)

axes[1].plot(timestamps, humidities, color='tab:orange')
axes[1].set_ylabel('Humidity (%)')
axes[1].grid(True, alpha=0.3)

axes[2].plot(timestamps, lights, color='tab:green')
axes[2].set_ylabel('Light (raw)')
axes[2].set_xlabel('Time')
axes[2].grid(True, alpha=0.3)

fig.suptitle('Environment Monitor Readings')
fig.autofmt_xdate()         
plt.tight_layout()

plt.savefig('readings.png', dpi=150)
plt.show()