import cv2

face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_data = cv2.CascadeClassifier('haarcascade_smile.xml')

# webcam = cv2.VideoCapture(0) # for webcam
webcam = cv2.VideoCapture('video.mp4')

def function(gray_image_face, frame):
    face_coordinates = face_data.detectMultiScale(gray_image_face)
    print(face_coordinates)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        smile_gray_image = gray_image_face[y:y + h, x:x + w]
        smile_image = frame[y:y + h, x:x + w]
        smile_coordinates = smile_data.detectMultiScale(smile_gray_image, 1.7, 20)
        print(smile_coordinates)
        for (x_, y_, w_, h_) in smile_coordinates:
            cv2.rectangle(smile_image, (x_, y_), (x_ + w_, y_ + h_), (0, 255, 0), 2)


while True:
    read_success, frame = webcam.read()

    if read_success:
        gray_image_face = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        print('frame read uncessfull')
        break

    output = function(gray_image_face, frame)
    cv2.imshow('smile', frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break

print('code complete', end=' ')
