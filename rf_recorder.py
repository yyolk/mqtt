import sys

import paho.mqtt.client as mqtt


MQTT_HOST = "homeassistant.localdomain"
MQTT_TOPIC = "tele/RFBridge/RESULT"

LOG_FILE = open(f"results/{__file__.split('/')[-1]}.txt", "a")


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    log_line = f"{msg.topic} {msg.payload.decode('utf-8')}"
    print(log_line)
    LOG_FILE.write(f"{log_line}\n")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_HOST, 1883, 60)

try: 
    client.loop_forever()
except KeyboardInterrupt:
    LOG_FILE.close()
    sys.exit()
