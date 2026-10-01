from zaber_motion import Library
from zaber_motion.binary import Connection, BinarySettings
import time 

Library.enable_device_db_store()

# serial port 
with Connection.open_serial_port("COM5", 9600) as connection:
    #connection.enable_alerts()

    device_list = connection.detect_devices()
    print("Found {} devices".format(len(device_list)))

    #device = device_list[0]


    if device_list:
        device = device_list[0]
        #device.move_absolute(950000)

        device.settings.set(BinarySettings.TARGET_SPEED, 20000)
        i = 0
        while i<100:   
            #device.move_velocity(10000)
            if (i%2==1):
                device.move_relative(-40000)
                time.sleep(1)
            else:
                device.move_relative(40000)
                time.sleep(1)
            
            i+=1



    """ axis = device.get_axis(1)
    if not axis.is_homed():
        axis.home()

    # Move to 10mm
    axis.move_absolute(10, "mm")

    # Move by an additional 5mm """
    #axis.move_relative(5, "mm")

