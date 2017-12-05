import time
import botbook_mcp3002 as mcp #
import os
import requests

INTERVAL = 2
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
def send_data(target_ct ,ppm):
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
	    req = requests.post("http://says.zeroday.me:7579/Mobius/SaysNode/Zone1/Sensor", POST, headers=headers)
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

def main():
    while True:
        time.sleep(INTERVAL)
        smokeLevel = getSmokeLevel()
        print("[ ] Current smoke level is %i " % smokeLevel)
	send_data(TARGET_CT, smokeLevel) 
        if smokeLevel > 150:
            print("[!] Smoke detected")
            # Active buzzer for n seconds.
            os.system("python /home/pi/Desktop/buzzer.py 1")

main()
