#include <DHT.h>
#define DHTPIN 7 //S wire connected to pin 7 
#define DHTTYPE DHT11  //Sensor model 

DHT dht(DHTPIN, DHTTYPE); //DHT object 

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop(){
  delay (2000); //the DHT11 cooldown

  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Error reading from the DHT sensor.");
    return; //end the loop if any reads fail 
  }

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.print(" C   Humidity: ");
  Serial.print(humidity);
  Serial.println(" %");
}
