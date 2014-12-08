import pygame;
import os;
import string


class TestPyGame(object):
    
    LABYRINTH_HEIGHT = 20;
    LABYRINTH_WIDTH = 20;
    LABYRINTH_WALL = 0;
    IMAGE_HEIGHT = 20;
    IMAGE_WIDTH = 20;
    IMAGES_FOLDER_NAME = "images";
    IMAGES_EXTENSION = ".png";
    screenSize = None;
    done = False;
    labyrinthArray = None;
    
    def __init__(self):
        self.labyrinthArray = [[0 for j in range (self.LABYRINTH_WIDTH)] 
                          for i in range (self.LABYRINTH_HEIGHT)];
        self.screenSize = (self.LABYRINTH_HEIGHT * self.IMAGE_HEIGHT, 
                           self.LABYRINTH_WIDTH * self.IMAGE_WIDTH);
        pygame.init();
        self.imagePath = os.getcwd();
        r = self.imagePath.rfind("\\");
        self.imagePath = self.imagePath[0 : r + 1] + self.IMAGES_FOLDER_NAME; '''wycinamy stringa od poczatku do ostatniego \\'''
        self.wallImage = pygame.image.load(self.imagePath + "\\wall.png");
        
    def loop(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
        pygame.quit();
    
    def showSomething(self):
        self.surface = pygame.display.set_mode(self.screenSize, pygame.DOUBLEBUF);
        for i in range(self.LABYRINTH_HEIGHT):
            for j in range(self.LABYRINTH_WIDTH):
                self.surface.blit(self.wallImage, (i * self.IMAGE_WIDTH, j * self.IMAGE_HEIGHT));
        pygame.display.flip();
        self.loop();
        
    def getImagesNamesFromDirectory(self):
        files = os.listdir(self.imagePath);
        index = files.index("wall.PNG");
        print(index);
        