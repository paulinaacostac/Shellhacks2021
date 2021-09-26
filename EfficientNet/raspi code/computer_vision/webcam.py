import pygame
import time
import pygame.camera
from pygame.locals import *

def start(device, maxSize=(1280,720)):
        
        print("Using camera: %s", device)

        # Open Camera
        cam = pygame.camera.Camera(device, maxSize)

        # Start Camera
        cam.start()

        # Get actual capture size
        self.size = self.cam.get_size()

        # Init surface buffer
        self.buffer = pygame.surface.Surface(self.size)
        print("Detected size: %d*%d", self.size[0], self.size[1])

        # Start polling at 50hz
        self.setMaxFPS(fps=50)
        self.sigPlaying.emit(True)
        
        
pygame.init()
pygame.camera.init()
cam_list = pygame.camera.list_cameras()
DEVICE = cam_list[0]
SIZE = (640, 480)
FILENAME = 'capture{}.png'

def camstream():
    display = pygame.display.set_mode(SIZE, 0)
    camera = pygame.camera.Camera(DEVICE, SIZE)
    camera.start()
    size = camera.get_size()
    screen = pygame.surface.Surface(SIZE, 0, display)
    print("Detected size: %d*%d", size[0], size[1])
    capture = True
    while capture:
        screen = camera.get_image(screen)
        display.blit(screen, (0,0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                capture = False
            elif event.type == KEYDOWN and event.key == K_s:
                pygame.image.save(screen, FILENAME.format(time.time()))
    camera.stop()
    pygame.quit()
    return

if __name__ == '__main__':
    camstream()