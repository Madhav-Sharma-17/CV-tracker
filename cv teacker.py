import cv2
import mediapipe as mp  
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue
        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                h, w, c = image.shape
                cx, cy = int(index_finger_tip.x * w), int(index_finger_tip.y * h)
                cv2.circle(image, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
                print(f"Index Finger Tip: {cx}, {cy}")
        cv2.imshow('Hand Tracking', image)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
