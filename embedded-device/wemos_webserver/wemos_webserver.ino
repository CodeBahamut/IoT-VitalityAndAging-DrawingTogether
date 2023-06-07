#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

// Set WiFi credentials
#define WIFI_SSID "Drawbot"
#define WIFI_PASS "drawbot123"
#include <Servo.h>

int position = 0;
Servo servo_9;

// Create a new web server
ESP8266WebServer webserver(80);

// Handle Root
void setPenUp() {
  Serial.print("Set pen up has been called");
  servo_9.write(180);
  webserver.send(200, "text/json", "{\"isUp\": True}");
}

// Handle Root
void setPenDown() {
  Serial.print("Set pen down has been called");
  servo_9.write(0);
  webserver.send(200, "text/json", "{\"isUp\": False}");
}

// Handle 404
void notfoundPage() {
  webserver.send(404, "text/plain", "404: Not found");
}

void setup() {
  // Setup serial port
  Serial.begin(115200);
  Serial.println();
  servo_9.attach(D4);

  //Begin WiFi
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  while (WiFi.status() != WL_CONNECTED) { delay(100); }

  // WiFi Connected
  Serial.print("Connected! IP address: ");
  Serial.println(WiFi.localIP());

  // Start Web Server
  webserver.on("/up", setPenUp);
  webserver.on("/down", setPenDown);

  webserver.onNotFound(notfoundPage);
  webserver.begin();
}

void loop() {
  webserver.handleClient();
}
