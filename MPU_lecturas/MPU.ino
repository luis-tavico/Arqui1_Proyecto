#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

Adafruit_MPU6050 mpu;

void setup() {
  Serial.begin(9600);
  
  Wire.begin();
  mpu.begin();
  
  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);

  delay(100);
}

void loop() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  Serial.print("Aceleración (m/s^2): ");
  Serial.print(a.acceleration.x);
  Serial.print("\t");
  Serial.print(a.acceleration.y);
  Serial.print("\t");
  Serial.print(a.acceleration.z);
  Serial.println();

  Serial.print("Rotación (grados/segundo): ");
  Serial.print(g.gyro.x);
  Serial.print("\t");
  Serial.print(g.gyro.y);
  Serial.print("\t");
  Serial.print(g.gyro.z);
  Serial.println();

  delay(100);
}
