#include <Firebase.h>
#include <FirebaseArduino.h>
#include <FirebaseCloudMessaging.h>
#include <FirebaseError.h>
#include <FirebaseHttpClient.h>
#include <FirebaseObject.h>

#include <ESP8266WiFi.h>
#include <FirebaseArduino.h>

// Config Firebase
#define FIREBASE_HOST "handclap-2100f.firebaseio.com"
#define FIREBASE_AUTH "JMs6zIlrHjJ61SWy0OnZ1bqLgnEnlupYvTc3IY3b"

// Config connect WiFi
#define WIFI_SSID "BiBi"
#define WIFI_PASSWORD "asdfghjkl"

#define LED0_PIN 8
#define LED1_PIN 9
#define LED2_PIN 10

int8 led1_stat;
int8 led2_stat;
int8 led3_stat;

void setup() {
  Serial.begin(115200);

  WiFi.mode(WIFI_STA);
  // connect to wifi.
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("connecting");
  
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println();
  Serial.print("connected: ");
  Serial.println(WiFi.localIP());

  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.stream("light/LED1");

}

void loop() {
  if (Firebase.failed()){
    Serial.println("streaming error");
    Serial.println(Firebase.error());
  }
  
  if (Firebase.available()) {
     Serial.print("avaiable");
     FirebaseObject event = Firebase.readEvent();
     
     String eventType = event.getString("type");
     eventType.toLowerCase();
     
     if (eventType == "") 
      {
        return ;
      }
     
     Serial.print("event: ");
     Serial.println(eventType);
     
     if (eventType == "put") {
       String path = event.getString("path");
       int data = event.getInt("data");
       Serial.println("[" + path + "] " + String(data));
     }
  }
  led1_stat = Firebase.getInt("light/LED1");
  led2_stat = Firebase.getInt("light/LED2");
  led3_stat = Firebase.getInt("light/LED3");
  Serial.print(led1_stat);
  Serial.print("\n");
  delay(500);

}
