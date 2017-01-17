char bytes = 0;
char stop_letter = 'X';
String buf = "";


void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);

}


void process(String cmd) {
  Serial.print(cmd);
  Serial.print("xxx");
  if (cmd == "on"){
    Serial.print("command onxxx");
    buf = "";
    digitalWrite(LED_BUILTIN, HIGH);
  }
  else if (cmd == "off"){
    Serial.print("command offxxx");
    buf = "";
    digitalWrite(LED_BUILTIN, LOW);
   }
}

void loop() {

  if (Serial.available() > 0){
    bytes = Serial.read();
    if (bytes == stop_letter){
      process(buf);
      buf = "";
    }
    else {
      buf += bytes;
    }
  }
}


