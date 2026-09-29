from zaber_motion import Library
from zaber_motion.ascii import Connection

Library.enable_device_db_store()

# serial port 
with Connection.open_serial_port("COM6") as connection:
    connection.enable_alerts()

    device_list = connection.detect_devices()
    print("Found {} devices".format(len(device_list)))

    device = device_list[0]

    axis = device.get_axis(1)
    if not axis.is_homed():
        axis.home()

    # Move to 10mm
    axis.move_absolute(10, "mm")

    # Move by an additional 5mm
    axis.move_relative(5, "mm")

