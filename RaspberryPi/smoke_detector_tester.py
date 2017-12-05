import time
import botbook_mcp3002 as mcp #
import os
import requests
import threading
import random

INTERVAL = 2
TARGET_CTS = "Zone"
TARGET_CT = "Zone1"

def header_parser(header_str):
        # Convert HEAD_str to dict.
	headers = {}
	header_str_lst = header_str.split("\n")
	for head in header_str_lst:
		if ":" in head:
			tmp = head.split(": ")
			key = tmp[0]
			value = "".join(tmp[1:])
			headers[key] = value
	return headers

# Send sensor's data to Mobuis server
def send_data(target_ct, ppm):
	header_str = """X-M2M-RI: 12345
X-M2M-Origin: /0.2.481.1.21160310105204806
Content-Type: application/vnd.onem2m-res+xml; ty=4
Cache-Control: no-cache"""

        # Building payload to send server.
	POST = """<?xml version="1.0" encoding="UTF-8"?>
<m2m:cin xmlns:m2m="http://www.onem2m.org/xml/protocols" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<con>"""+str(ppm)+""" ppm</con>
</m2m:cin>"""

        # Parse header to interact with Mobius server
	headers = header_parser(header_str)
        try:
            # Send seonsor's data to Mobius server
	    req = requests.post("http://says.zeroday.me:7579/Mobius/SaysNode/"+target_ct+"/Sensor", POST, headers=headers)
	    if req.status_code == "200":
                # If success,
    	    	return True
	    else:
		return False
        except:
            print("[-] An error occured. Check your internet connection..")

def getSmokeLevel():
    smokeLevel= mcp.readAnalog()
    return smokeLevel

def send_data_stub(target_ct, ppm):
    while(1):
        time.sleep(INTERVAL)
        send_data(target_ct, ppm)

def main():
    for i in range(1, 1000):
        t = threading.Thread(target=send_data, args=(TARGET_CTS+str(i % 6), random.randint(50, 250)))
        t.start()
        time.sleep(0.5)

main()
