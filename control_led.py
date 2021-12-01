from boltiot import Bolt
import conf
mybolt = Bolt(conf.api_key,conf.device_id)
while True:
    inp = input("enter whether to LED ON or OFF? :")
    if inp == "ON" or inp== "on":
        msg1 = "you enter on"
        response1 = mybolt.digitalWrite('0','HIGH')
        print(msg1)
        print(response1)
    elif inp == "OFF" or inp == "off":
        msg2 = "you enter off"
        response2 = mybolt.digitalWrite('0','LOW')
        print(msg2)
        print(response2)
    else:
        msg3 = "invalid"
        print(msg3)
