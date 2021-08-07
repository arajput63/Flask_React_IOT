from picamera import PiCamera
from time import sleep

cam = PiCamera()
# cam.rotation = 180
cam.resolution = (2028, 1523)
print("framerate: " + str(cam.framerate))

cam.start_preview()
sleep(5)
cam.capture('img.jpg')