import serial
import os
import re
import signal

device=""
for file in os.listdir("/dev"):
    if re.search("cu.wchusbserial?", file):
        device ="/dev/{}".format(file)
        pass


if len(device) == 0:
    print("Device could not found !")
    exit(1)

print("Trying to open '{}' device".format(device))

try:
    with serial.Serial(device, 115200, timeout=1) as ser:
        while(ser.isOpen()):
            try:
                line = ser.readline()
                if len(line) == 0:
                    continue
                # Python print command adds "\n" char in additional
                print(line.replace("\n", ""))
            except serial.serialutil.SerialException as ex:
                print("Connection is closed by reason {}".format(ex))
                break
            

except serial.serialutil.SerialException as ex:
    print("Device could not open by reason {}".format(ex))


