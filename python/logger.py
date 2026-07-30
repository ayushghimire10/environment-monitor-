import serial
import csv 
from datetime import datetime 

PORT = 'COM7'
BAUD = 9600  #serial.begin(9600) in the sketch 
OUTPUT_FILE = 'sensordata.csv'

ser = serial.Serial(PORT,BAUD, timeout = 2)
print(f"Connected to {PORT}. Now logging data to {OUTPUT_FILE}.")

with open(OUTPUT_FILE, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['timestamp','temperature_c','humidity_pct','light'])
    try: 
        while True: 
            line = ser.readline().decode('utf-8').strip() #wait for a full line 

            if not line : 
                continue 

            parts = line.split(',')
            if len(parts) != 3: #skip anything that isnt all 3 vals 
                continue 
            try:
                temp, humidity, light = float (parts[0]),float(parts[1]),int(parts[2])
            except ValueError: #skip corrupted readings 
                continue 

            #timestamp from PC 
            timestamp = datetime.now().isoformat()
            writer.writerow([timestamp,temp,humidity,light])
            #write to disk incase script is stopped mid run 
            f.flush()

            print(f"{timestamp}   {temp}C   {humidity}%   {light}")
    except KeyboardInterrupt:
        print("\nStopped logging")
    finally:
        ser.close() #release the port 