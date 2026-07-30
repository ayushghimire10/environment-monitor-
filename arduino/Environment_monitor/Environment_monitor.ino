#include <DHT.h>
#include <LiquidCrystal.h>
#define DHTPIN 7 //S wire connected to pin 7 
#define DHTTYPE DHT11  //Sensor model 
#define LIGHTPIN A0 //analog pin w/ output node 

DHT dht(DHTPIN, DHTTYPE); //DHT object 
LiquidCrystal lcd(12,11,5,4,3,2);

void setup() {
  Serial.begin(9600);
  dht.begin();
  lcd.begin(16,2); 
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

  Serial.print(temperature);
  Serial.print(",");
  Serial.print(humidity);
  Serial.print(",");
  Serial.print(lightLevel);
  lcd.clear();
  lcd.setCursor(0,0); //rows 0 - 1, cols 0 - 15
  lcd.print(temperature,1);
  lcd.print("C ");
  lcd.print(humidity, 0);
  lcd.print("%RH");
  lcd.setCursor(0,1);
  lcd.print("Light: ");
  lcd.print(lightLevel);
}
