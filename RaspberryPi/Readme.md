# Raspberry Pi

* botbook_mcp3002.py
  * Provides function to interact with smoke sensor.
* buzzer.py
* buzzer_off.py
* smoke_detector.py
* smoke_detector_tester.py 
  * Send dummpy ppm data to server.


# Usage

1. Clone scripts on your pi's home directory (/home/pi/)

2. Run `python smoke_detector.py`

3. Modify `/etc/rc.local` to execute script when startup.

   1. Paste under text to file

      ```sh
      #!/bin/sh -e
      #
      # rc.local
      #
      # This script is executed at the end of each multiuser runlevel.
      # Make sure that the script will "exit 0" on success or any other
      # value on error.
      #
      # In order to enable or disable this script just change the execution
      # bits.
      #
      # By default this script does nothing.
      # Print the IP address
      _IP=$(hostname -I) || true
      if [ "$_IP" ]; then
        printf "My IP address is %s\n" "$_IP"
      fi
      service ssh restart
      screen -dm python /home/pi/Desktop/buzzer_off.py &
      sleep 1
      screen -dm python /home/pi/Desktop/smoke_detector.py &
      exit 0
      ```

