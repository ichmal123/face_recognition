import cv2
import user
import sys
sys.path.append("examples/training")
import insertData

cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
img_counter = 0

print("Tap your rfid")
rfid = user.get_rfid()
print(rfid)
nik = input('Nik : ')
username = input('Nama : ')
tempatTgl = input('Tempat Tanggal Lahir :')
tgl = input('Tanggal Lahir : ')
jenis = input('Jenis Kelamin : ')
alamat = input('Alamat : ')
agama = input('Agama : ')
status = input('Status : ')
pekerjaan = input('Pekerjaan : ')
kewarganegaraan = input('Kewarganegaraan : ')
berlaku_hingga = input('Berlaku Hingga : ')


while True:
    ret, frame = cam.read()

    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "{}_{}.jpg".format(rfid,username)
        cv2.imwrite("/home/facedection/face_recognition/examples/new-dataset/"+img_name, frame)
        print("{} written!".format(img_name))
        # training.train(img_name)
        # training.trainName(img_name)
        insertData.insertData(nik, username, tempatTgl, tgl, jenis, alamat, agama, status, pekerjaan, kewarganegaraan, berlaku_hingga, rfid)

cam.release()
cv2.destroyAllWindows()
