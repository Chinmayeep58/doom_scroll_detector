import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

model_path="face_landmarker.task"
head_down_threshold=0.23

base_options=python.BaseOptions(model_asset_path=model_path)
options=vision.FaceLandmarkerOptions(base_options=base_options, num_faces=1)

landmarker=vision.FaceLandmarker.create_from_options(options)

print("face landmarker loaded")

cap=cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()
    if not ret:
        break

    rgb=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image=mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)

    result=landmarker.detect(mp_image)

    if result.face_landmarks:
        # cv2.putText(frame,"face detected", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),2)

        lm=result.face_landmarks[0]
        nose=lm[1]
        left_eye=lm[33]
        right_eye=lm[263]

        eye_avg=(left_eye.y+right_eye.y)/2

        if nose.y>eye_avg+head_down_threshold:
            status="head down"
            color=(0,0,255)
        else:
            status="head up"
            color=(0,255,0)

        cv2.putText(frame,status, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,0),2)
    

    cv2.imshow("Face detection",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()