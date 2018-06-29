import time
import picamera
import os

camera = picamera.PiCamera()

def picture():
    camera.start_preview()
    time.sleep(3)
    camera.capture('temp/picture.jpg')
    camera.stop_preview()
    

def video():
    camera.start_preview()
    time.sleep(3)
    camera.start_recording('temp/video.h264')
    camera.wait_recording(10)
    camera.stop_recording()
    camera.stop_preview()
    os.system('MP4Box -add video.h264 video.mp4')
    os.remove('temp/video.h264')
