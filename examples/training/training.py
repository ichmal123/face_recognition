import face_recognition
import numpy as np
import os

arung_image = face_recognition.load_image_file("/home/facedection/face_recognition/examples/new-dataset/150911110a020d130c13131a0205150801_arung.jpg")
arung_face_encoding = face_recognition.face_encodings(arung_image)[0]
ichmal_image = face_recognition.load_image_file("/home/facedection/face_recognition/examples/new-dataset/15091105051a19130a040105150801_ichmal.jpg")
ichmal_face_encoding = face_recognition.face_encodings(ichmal_image)[0]
hakkan_image = face_recognition.load_image_file("/home/facedection/face_recognition/examples/new-dataset/150911151a050d0a1d0a040105150801_hakkan.jpg")
hakkan_face_encoding = face_recognition.face_encodings(hakkan_image)[0]

known_face_encodings = [
    arung_face_encoding,
    ichmal_face_encoding,
    hakkan_face_encoding
]

np.save("examples/training/imageTrain.npy", known_face_encodings)

name_list = [
    ['150911110a020d130c13131a0205150801', 'arung'],
    ['15091105051a19130a040105150801', 'ichmal'],
    ['150911151a050d0a1d0a040105150801', 'hakkan']
]

np.save("examples/training/nameTrain.npy", name_list)

print(np.load("examples/training/imageTrain.npy"))

# test = np.load("test.npy")


# print(test)

# def train(img_name):
#     face = face_recognition.load_image_file("/home/facedection/face_recognition/examples/new-dataset/{}".format(img_name))
#     face_encoding = face_recognition.face_encodings(face)[0]
#     known_face = np.load("examples/training/imageTrain.npy")
#     known_face = np.append(known_face, face_encoding, axis=0)
#     np.save("examples/training/imageTrain.npy", known_face)
#     print("Train image berhasil")


# def trainName(image_name):
#     result_list = np.load("examples/training/nameTrain.npy")
#     parts = image_name.split('_')
#     correct = parts[1].split('.')[0]
#     result_list = np.append(result_list, [parts[0], correct])

#     np.save("examples/training/nameTrain.npy", result_list)
#     print("Train name berhasil")

# test = np.empty((1, 128))
# test2 = np.empty((1, 2))
# np.save("examples/training/imageTrain.npy", test)
# np.save("examples/training/nameTrain.npy", test)

# test = train("15091105051a19130a040105150801_ichmal.jpg")
# # face = face_recognition.load_image_file("/home/facedection/face_recognition/examples/new-dataset/15091105051a19130a040105150801_ichmal.jpg")
# # face_encoding = face_recognition.face_encodings(face)[0]

# # print(face_encoding.shape)

# print(np.load("/home/facedection/face_recognition/examples/training/imageTrain.npy"))