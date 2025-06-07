const int waterSensorPin = A0;

void setup() {
  Serial.begin(9600);
  pinMode(waterSensorPin, INPUT);
}

void loop() {
  int sensorValue = analogRead(waterSensorPin);

  Serial.print("Sensor Reading: ");
  Serial.print(sensorValue);
  Serial.print(" --> Level ");

  if (sensorValue >= 0 && sensorValue <= 50) {
    Serial.println("1");
  }
  else if (sensorValue <= 100) {
    Serial.println("2");
  }
  else if (sensorValue <= 200) {
    Serial.println("3");
  }
  else if (sensorValue <= 400) {
    Serial.println("4");
  }
  else if (sensorValue <= 500) {
    Serial.println("5");
  }
  else if (sensorValue <= 700) {
    Serial.println("6");
  }
  else {
    Serial.println("Invalid reading");
  }

  Serial.println("---------------------------");
  delay(2000);
}
