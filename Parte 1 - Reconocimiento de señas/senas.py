import cv2
import mediapipe as mp
import os

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

with mp_hands.hands(
        static_image_mode=true,
        max_num_hands=1,
        min_detection_confidence=0.5) as hands:
    image = cv2.imread("imagen02.jpg")
    height, width, _ = image.shape
    image = cv2.flip(image, 1)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = hands.process(image_rgb)

    print("Handedness: ", results.multi_handedness)
    

    image = cv2.flip(image, 1)
cv2.imshow("Image", image)
cv2.waitkey(0)
cv2.destroyAllWindows()