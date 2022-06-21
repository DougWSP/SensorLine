
import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

import json 
conf_file = open('conf.json') 
conf = json.load(conf_file) 
conf_file.close() 

# Robot codes 
import machine
pinNum = 4 #D4 
sensor = machine.Pin(pinNum, machine.Pin.IN,  machine.Pin.PULL_UP)

if (sensor.value()):
    print( "não há impecilho")
    
else:
    print("há impecilho")

ssid = conf["MQTTline"]
password = conf["testeline"]
mqtt_server = conf["157.230.89.7"]
server_port = conf["1883"] 
mqtt_user = conf["mqtt"]
mqtt_password = conf["oriva_mqtt"]

client_id = ubinascii.hexlify(machine.unique_id())
topic_sub = b'TesteMQTT01/input'
topic_pub = b'TesteMQTT01/output'

last_message = 0
message_interval = 1
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())



