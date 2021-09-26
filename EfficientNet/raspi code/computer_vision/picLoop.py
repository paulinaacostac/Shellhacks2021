from takePic2 import Capture
import time
import matplotlib.pyplot as plt
import pygame
from datetime import datetime

run = int(input("Enter duration to run the code (1 = 6 pics) \n"))
cam = Capture()

while run >= 0:
    img = cam.get_img()
    current_time = time.time()
    img_name = "./data/"+str(current_time)+".png"
    print("saving image -> " + img_name)
    pygame.image.save(img, img_name)
    run -= 0.2

cam.stop()
    



























