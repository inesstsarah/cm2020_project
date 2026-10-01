from zaber_motion import Library
from zaber_motion.binary import Connection, BinarySettings
import time 

Library.enable_device_db_store()

# serial port 
with Connection.open_serial_port("COM5", 9600) as connection:
    #connection.enable_alerts()

    device_list = connection.detect_devices()
    print("Found {} devices".format(len(device_list)))
    if device_list:
        device = device_list[0]
        device.move_absolute(950000)
        #device.home()
