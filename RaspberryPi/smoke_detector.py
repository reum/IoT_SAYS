import time
import botbook_mcp3002 as mcp #
import os
import requests


smokeLevel= 0

def header_parser(header_str):
	headers = {}

	header_str_lst = header_str.split("\n")
	for head in header_str_lst:
		if ":" in head:
			tmp = head.split(": ")
			key = tmp[0]
			value = "".join(tmp[1:])
			headers[key] = value
	return headers

def send_data(ppm):
	header_str = """X-M2M-RI: 12345
X-M2M-Origin: /0.2.481.1.21160310105204806
Content-Type: application/vnd.onem2m-res+xml; ty=4
Cache-Control: no-cache"""


	POST = """<?xml version="1.0" encoding="UTF-8"?>
<m2m:cin xmlns:m2m="http://www.onem2m.org/xml/protocols" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<con>"""+str(ppm)+""" ppm</con>
</m2m:cin>"""

	headers = header_parser(header_str)
        try:
	    req = requests.post("http://says.zeroday.me:7579/Mobius/pi_1/sensor", POST, headers=headers)
	    if req.status_code == "200":
    	    	return True
	    else:
		return False
        except:
            print("Error")

def readSmokeLevel():
    global smokeLevel
    smokeLevel= mcp.readAnalog()

def main():
    while True:
        time.sleep(2)
        readSmokeLevel() #
        print("Current smoke level is %i " % smokeLevel)
	send_data(smokeLevel) 
        if smokeLevel > 150:
            print("Smoke detected")
            # TODO : send smoke data to server
            os.system("python /home/pi/Desktop/buzzer.py 1")
            time.sleep(1)

main()
