import cv2

face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_data = cv2.CascadeClassifier('haarcascade_smile.xml')

# ebcam = cv2.VideoCapture(0) # for webcam
webcam = cv2.VideoCapture('video.mp4')

def function(gray_image_face, frame):
    face_coordinates = face_data.detectMultiScale(gray_image_face)
    print(face_coordinates)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        smile_gray_image = gray_image_face[y:y + h, x:x + w]
        smile_coordinates = smile_data.detectMultiScale(smile_gray_image, 1.7, 20)
        if len(smile_coordinates) > 0:
            cv2.putText(frame, 'smileing', (x, y + h + 40), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3,
                        color=(0, 255, 0), thickness=2)


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