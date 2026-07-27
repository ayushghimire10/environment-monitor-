#include <DHT.h>
#define DHTPIN 7 //S wire connected to pin 7 
#define DHTTYPE DHT11  //Sensor model 
#define LIGHTPIN A0 //analog pin w/ output node 

DHT dht(DHTPIN, DHTTYPE); //DHT object 

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop(){
  delay (2000); //the DHT11 cooldown

  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  int lightLevel = analogRead(LIGHTPIN); //gets voltage at A0

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Error reading from the DHT sensor.");
    return; //end the loop if any reads fail 
  }

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.print(" C   Humidity: ");
  Serial.print(humidity);
  Serial.println(" %   Light: ");
  Serial.print(lightLevel);
}
