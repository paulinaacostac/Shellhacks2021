import pygame
import pygame.camera



class Capture(object):
    pygame.init()
    pygame.camera.init()
    cam_list = pygame.camera.list_cameras()
    
    def __init__(self, resolution = (1280,720)):    
        self.cam = pygame.camera.Camera(self.cam_list[0],resolution)
        self.cam.start()

    def get_img(self):
        image = self.cam.get_image()
        #image = pygame.surfarray.array3d(image)
        #image = image.swapaxes(0,1)
        return image
    
    def stop(self):
        self.cam.stop()
        
