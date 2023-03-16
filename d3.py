import cv2
import numpy as np

# Set camera parameters
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
camera.set(cv2.CAP_PROP_FPS, 30)

# Set camera settings
brightness = 50
contrast = 50
saturation = 50
sharpness = 50

# Set camera settings through the OpenCV interface
camera.set(cv2.CAP_PROP_BRIGHTNESS, brightness / 100.0)
camera.set(cv2.CAP_PROP_CONTRAST, contrast / 100.0)
camera.set(cv2.CAP_PROP_SATURATION, saturation / 100.0)
camera.set(cv2.CAP_PROP_SHARPNESS, sharpness / 100.0)

# Show video stream
while True:
    ret, frame = camera.read()

    # Adjust image settings
    frame = cv2.convertScaleAbs(frame, alpha=(contrast / 50.0), beta=(brightness - 50))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv[:,:,1] = np.clip(hsv[:,:,1] * (saturation / 50.0), 0, 255)
    frame = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    # Display video stream
    cv2.imshow('Camera', frame)

    # Handle key presses
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('b'):
        brightness = (brightness - 10) % 101
        camera.set(cv2.CAP_PROP_BRIGHTNESS, brightness / 100.0)
    elif key == ord('c'):
        contrast = (contrast - 10) % 101
        camera.set(cv2.CAP_PROP_CONTRAST, contrast / 100.0)
    elif key == ord('s'):
        saturation = (saturation - 10) % 101
        camera.set(cv2.CAP_PROP_SATURATION, saturation / 100.0)
    elif key == ord('h'):
        sharpness = (sharpness - 10) % 101
        camera.set(cv2.CAP_PROP_SHARPNESS, sharpness / 100.0)

# Release camera and close windows
camera.release()
cv2.destroyAllWindows()
