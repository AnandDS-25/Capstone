#include <SPI.h>
#include <RF24.h>

#define CE_PIN 9
#define CSN_PIN 10

RF24 radio(CE_PIN, CSN_PIN);
const byte address[6] = "NODE1";

void setup() {
    Serial.begin(115200);
    radio.begin();
    
    radio.openWritingPipe(address);
    
    radio.setPALevel(RF24_PA_LOW);
    radio.stopListening();
    Serial.println("Ready to send .bin file...");
}

void loop() {
  
    if (Serial.available()) {
        char buffer[32]; // NRF24L01+ supports max 32-byte packets
        int len = Serial.readBytes(buffer, sizeof(buffer));
        radio.write(&buffer, len);
        Serial.print("Sent: ");
        Serial.write(buffer, len);
        Serial.println();
    }
}
