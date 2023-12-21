//bluetooth hc-05
int state = 0;   // Variable lectrura dato serial

void setup() {
  Serial.begin(9600);
}
 
void loop() {

  if (Serial.available() > 0) {
    state = Serial.read();
  } 

  if (state == 'E') {
    state = 0;
  } else if (state == 'A') {
    state = 0;
  } else if (state == 'F') {
    state = 0;
  }

}