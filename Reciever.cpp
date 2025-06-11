#include <SPI.h>
#include <RF24.h>

#define CE_PIN 9
#define CSN_PIN 10

RF24 radio(CE_PIN, CSN_PIN);
const byte address[6] = "NODE1";

void setup() {
    Serial.begin(115200);
    radio.begin();
    radio.openReadingPipe(1, address);
    radio.setPALevel(RF24_PA_LOW);
    radio.startListening();
    Serial.println("Receiver ready...");
}

void loop() {
    if (radio.available()) {
        char buffer[32] = {0};
        radio.read(&buffer, sizeof(buffer));
        Serial.write(buffer, sizeof(buffer));  // Send raw data to PC
    }
}
