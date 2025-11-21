import cv2
from deepface import DeepFace
import pyttsx3
import threading

try:
    engine = pyttsx3.init()
except:
    import os
    os.environ['PYTTSX3_DRIVER'] = 'dummy'
    engine = None
if engine:
    engine.setProperty('rate', 150)

def speak(emotion):
    if engine:
        engine.say(f"You seem {emotion}")
        engine.runAndWait()
    else:
        print(f"You seem {emotion}")

cap = cv2.VideoCapture(0)
last_emotion = ""
while True:
    key, img = cap.read()
    if not key:
        break
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = DeepFace.analyze(rgb_img, actions=['emotion'], enforce_detection=False)
    emotion = results['dominant_emotion']

    cv2.putText(img, f'Emotion: {emotion}', (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    cv2.imshow("Emotion Recognition", img)

 
    if emotion != last_emotion:
        threading.Thread(target=speak, args=(emotion,), daemon=True).start()
        last_emotion = emotion

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()