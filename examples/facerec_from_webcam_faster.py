import face_recognition
import cv2
import numpy as np
import serial
from multiprocessing import Process , Queue
from vidgear.gears import NetGear
# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)


video_capture = cv2.VideoCapture(0)

known_face_encodings = np.load("examples/training/imageTrain.npy")

known_face_names = np.load("examples/training/nameTrain.npy")

# Initialize some variables
rfid = Queue(2)
q_data = Queue(2)

def read_rfid(rfid):
    try:
        port_arduino = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)
    except Exception as error:
        print(error)
    while True:
        data = port_arduino.read(128)
        rawdata = str(data.hex())
        value = len(data)
        if value >= 1:
            if not rfid.full():
                rfid.put(rawdata)

th_rfid = Process(target=read_rfid,args=(rfid,))
th_rfid.start()


def run():
    face_locations = []
    face_encodings = []
    process_this_frame = True
    while True:
        face_names = []
        matching = ""
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Only process every other frame of video to save time
        if process_this_frame:
            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]
            
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)

                if matches[best_match_index]:
                    people = known_face_names[best_match_index]
                    name = people[1]
                    id = people[0]
                    # print(name)
                    # print(id)
                    if not rfid.empty():
                        d_rfid = rfid.get(True)
                        # print(d_rfid)
                        if id == d_rfid:
                            matching = "Mactched"
                        else:
                            matching = "Not Matched"
                face_names.append(name)

        process_this_frame = not process_this_frame


        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face   
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        # cv2.imshow('Video', frame)
        if not q_data.full() and ret:
            q_data.put([frame, matching])

        # Hit 'q' on the keyboard to quit!
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     th_rfid.terminate()
        #     break

def stream_server():
    options = {"flag": 0, "copy": False, "track": False, "bidirectional_mode": True}
    server = NetGear (
        address = "192.168.1.22",
        port = "5454",
        protocol = "tcp",
        pattern = "1",
        logging = True,
        max_retries = 100,
        **options 
    )
    while True:
        print("hello")
        if not q_data.empty():
            frame, matching = q_data.get(True)
            print(frame)
            # server.send(frame=frame, message=matching)

# Release handle to the webcam
if __name__ == "__main__":
    server_run = Process(target=stream_server)
    run_run = Process(target=run)
    try:
        server_run.start()
        run_run.start()
    except KeyboardInterrupt:
        th_rfid.terminate()
        video_capture.release()
        server_run.close()
        run_run.close()
    # video_capture.release()
    # cv2.destroyAllWindows()
