# import required libraries
from vidgear.gears import NetGear
import cv2

# Open suitable video stream, such as webcam on first index(i.e. 0)
stream = cv2.VideoCapture(0)

# define tweak flags
options = {"flag": 0, "copy": False, "track": False}

# Define Netgear Client at given IP address and define parameters
# !!! change following IP address '192.168.x.xxx' with yours !!!
client = NetGear(
    address="192.168.1.11",
    port="5454",
    protocol="tcp",
    pattern=1,
    logging=True,
    max_retries = 100,
    **options
)

# loop over until KeyBoard Interrupted
while True:

    try:
        # read frames from stream
        (grabbed, frame) = stream.read()

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # check for frame if not grabbed
        if not grabbed:
            break

        # {do something with the frame here}

        # send frame to server
        client.send(small_frame)

    except KeyboardInterrupt:
        break

# safely close video stream
stream.release()

# safely close server
client.close()
