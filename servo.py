'''
Developed abstract way to manage multiple servos connected
to an Arduino
'''
import platform
import serial

#Arduino connections
if platform.os == "Linux":
    port = '/dev/ttyUSB0'
elif platform.os == "Windows":
    port = 'COM3'
else:
    port = '/dev/tty.usbmodem00022331'

#bauds rate use, generally 9600
baudRate = 9600

servos = serial.Serial(port, baudRate, timeout=1)

def send_raw_data(data):
    '''Send value to the direct channel of communication
        with the servo
        Parameters
        ----------
    data: float
        value to send directly to servo no more than 5 digits'''
    servos.write(chr(data))

def move(servo, angle):
    '''Movement of servos according to an angle.
       Parameters
       -----------
    servo: int
        servo number to work on
    angle: int
        the angle to move the servo, an integer from 0 to 180"'''

    if (0 <= angle <= 180):
        servos.write(chr(255))
        servos.write(chr(servo))
        servos.write(chr(angle))
    else:
        raise (Exception("Incorrect servo angle, must be between 0 to 180.\n"))