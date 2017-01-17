char bytes = 0;
char stop_letter = 'X';
String buf = "";
String state = "off";

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);

}

/*
String currentState(String cState) {
  if (cState == "State?"){
    return Serial.print(state);
  }
}
*/

void process(String cmd) {
  //Serial.print(cmd);
  //Serial.print("xxx");
  if (cmd == "on"){
    //Serial.print("command onxxx");
    buf = "";
    digitalWrite(LED_BUILTIN, HIGH);
    state = "on";
  }
  else if (cmd == "off"){
    //Serial.print("command offxxx");
    buf = "";
    digitalWrite(LED_BUILTIN, LOW);
    state = "off";
   }
}

void loop() {

  if (Serial.available() > 0){
    bytes = Serial.read();
    if (bytes == stop_letter)
    {
      if (buf == "state")
      {
        Serial.print(state);
      }
      process(buf);
      buf = "";
      //currentState(bytes);
    }
    else 
    {
      buf += bytes;
    }
  }
}


