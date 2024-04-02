import cv2
import numpy as np
from keras.models import load_model

model = load_model('model_file_30epochs.h5')
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

labels_dict = {0: 'Angry', 1: 'Disgust', 2: 'Fear', 3: 'Happy', 4: 'Neutral', 5: 'Sad', 6: 'Surprise'}

# Load the new image
frame = cv2.imread("disgusting.jpg")

# Get the screen dimensions
screen_height, screen_width = 850, 1200  # Set your screen dimensions here

# Resize the frame to fit the screen size
frame = cv2.resize(frame, (screen_width, screen_height))

# Convert to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = faceDetect.detectMultiScale(gray, 1.3, 3)

for x, y, w, h in faces:
    sub_face_img = gray[y:y + h, x:x + w]
    resized = cv2.resize(sub_face_img, (48, 48))
    normalize = resized / 255.0
    reshaped = np.reshape(normalize, (1, 48, 48, 1))
    result = model.predict(reshaped)
    label = np.argmax(result, axis=1)[0]
    print(label)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)
    cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 2)
    cv2.rectangle(frame, (x, y - 40), (x + w, y), (50, 50, 255), -1)
    cv2.putText(frame, labels_dict[label], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

# Display the image
cv2.imshow("Frame", frame)

# Wait for a key press
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
