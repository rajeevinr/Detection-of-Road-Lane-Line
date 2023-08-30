import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the video file or camera feed
cap = cv2.VideoCapture('test_video_2.mp4')  # Change to 0 for live camera feed

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Combine the original frame with the detected lines
    combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 0)

    # Convert BGR image to RGB (for matplotlib display)
    combo_image_rgb = cv2.cvtColor(combo_image, cv2.COLOR_BGR2RGB)

    # Display the result using matplotlib
    plt.imshow(combo_image_rgb)
    plt.title('Lane Detection')
    plt.axis('off')  # Hide axis labels
    plt.show()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
