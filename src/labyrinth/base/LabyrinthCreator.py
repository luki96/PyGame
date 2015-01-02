import random;
from labyrinth.base.LabyrinthPoint import LabyrinthPoint;
from collections import deque;

class LabyrinthCreator():

    LABYRINTH_HEIGHT = 5;
    LABYRINTH_WIDTH = 5;
    LABYRINTH_WALL = 0;
    LABYRINTH_ROAD = 1;
    LABYRINTH_BEST_ROAD = 2
    LABYRINTH_ENTRANCE = 3;
    LABYRINTH_EXIT = 4;
    PROBABILITY = 0.5;
    xEntrancePosition = 0;
    yEntrancePosition = 0;
    xExitPosition = 0;
    yExitPosition = 0;
    labyrinthArray = None;

    def __init__(self):
        self.labyrinthArray = [[LabyrinthPoint() for j in range (self.LABYRINTH_WIDTH)] 
                          for i in range (self.LABYRINTH_HEIGHT)];
    
    def initializeLabyrinth(self):
        for i in range(self.LABYRINTH_HEIGHT):
            for j in range(self.LABYRINTH_WIDTH):
                self.labyrinthArray[i][j].xPointPosition = i;
                self.labyrinthArray[i][j].yPointPosition = j;
                self.labyrinthArray[i][j].labyrinthPointType = self.LABYRINTH_WALL;
                
    def createLabyrinthEntrance(self):        
        self.labyrinthArray[4][3].labyrinthPointType = self.LABYRINTH_ENTRANCE;
        self.xEntrancePosition = 4;
        self.yEntrancePosition = 3;
        
        self.labyrinthArray[0][2].labyrinthPointType = self.LABYRINTH_EXIT;
        self.xExitPosition = 0;
        self.yExitPosition = 2;
        
        self.labyrinthArray[1][2].labyrinthPointType = self.LABYRINTH_ROAD;
        self.labyrinthArray[1][3].labyrinthPointType = self.LABYRINTH_ROAD;
        self.labyrinthArray[2][1].labyrinthPointType = self.LABYRINTH_ROAD;
        self.labyrinthArray[2][2].labyrinthPointType = self.LABYRINTH_ROAD;
        self.labyrinthArray[3][2].labyrinthPointType = self.LABYRINTH_ROAD;
        self.labyrinthArray[3][3].labyrinthPointType = self.LABYRINTH_ROAD;
        
        '''self.xEntrancePosition = random.randrange(self.LABYRINTH_HEIGHT);
        if ((self.xEntrancePosition == 0) or (self.xEntrancePosition == self.LABYRINTH_HEIGHT - 1)):
            self.yEntrancePosition = random.randrange(self.LABYRINTH_WIDTH);
            self.labyrinthArray[self.xEntrancePosition][self.yEntrancePosition].labyrinthPointType = self.LABYRINTH_ENTRANCE;
        elif (self.xEntrancePosition in range(1, self.LABYRINTH_HEIGHT - 1)):
            if (random.random() < self.PROBABILITY):
                self.yEntrancePosition = 0;        
                self.labyrinthArray[self.xEntrancePosition][self.yEntrancePosition].labyrinthPointType = self.LABYRINTH_ENTRANCE;
            else:
                self.yEntrancePosition = self.LABYRINTH_WIDTH - 1;
                self.labyrinthArray[self.xEntrancePosition][self.yEntrancePosition].labyrinthPointType = self.LABYRINTH_ENTRANCE;
           '''     
    def createLabyrinthExit(self):
        if (self.yEntrancePosition == 0):
            self.xExitPosition = random.randrange(self.LABYRINTH_HEIGHT);
            self.yExitPosition = self.LABYRINTH_WIDTH - 1;
            self.labyrinthArray[self.xExitPosition][self.yExitPosition].labyrinthPointType = self.LABYRINTH_EXIT;
        elif (self.yEntrancePosition == self.LABYRINTH_WIDTH - 1):
            self.xExitPosition = random.randrange(self.LABYRINTH_HEIGHT);
            self.yExitPosition = 0;
            self.labyrinthArray[self.xExitPosition][self.yExitPosition].labyrinthPointType = self.LABYRINTH_EXIT;
        elif (self.yEntrancePosition in range(1, self.LABYRINTH_WIDTH - 1)):
            self.xExitPosition = self.LABYRINTH_HEIGHT - 1;
            self.yExitPosition = random.randrange(self.LABYRINTH_WIDTH - 1);
            self.labyrinthArray[self.xExitPosition][self.yExitPosition].labyrinthPointType = self.LABYRINTH_EXIT;
            
    def createLabyrinthRoads(self):
        visitedLabyrinthPoints = 0;
        totalLabyrinthPoints = self.LABYRINTH_WIDTH * self.LABYRINTH_HEIGHT;
        stackOfPoints = deque();
        neighboursList = deque();
        
        'Oznaczamy wierzcholek wejscia jako odwiedzony i wrzucamy na stos'
        currentPoint = self.labyrinthArray[self.xEntrancePosition][self.yEntrancePosition];
        
        while(visitedLabyrinthPoints < totalLabyrinthPoints):
            
            self.checkIfCurrentPointHasNeighbours(neighboursList, currentPoint);
                
            if (neighboursList.__len__() != 0):
                'Wybierz losowego sasiada rozpatrywanego punktu'
                neighbourPoint = neighboursList[random.randrange(neighboursList.__len__())];
                neighbourX = neighbourPoint.xPointPosition;
                neighbourY = neighbourPoint.yPointPosition;
                
                'Robimy droge pomiedzy punktami'
                self.labyrinthArray[neighbourX][neighbourY].labyrinthPointType = self.LABYRINTH_ROAD;
                
                stackOfPoints.append(currentPoint);
                currentPoint = neighbourPoint;
                neighboursList.clear();
                visitedLabyrinthPoints += 1;
            else:
                currentPoint = stackOfPoints.pop();
    
    def checkIfCurrentPointHasNeighbours(self, neighboursList, point):
        tmpX = point.xPointPosition;
        tmpY = point.yPointPosition;
        'Sprawdzamy czy biezacy punkt ma jakis sasiadow ktorzy sa nieodwiedzeni jeszcze'
        if ((tmpX - 1 >= 0) and
        (self.labyrinthArray[tmpX - 1][tmpY].labyrinthPointType != self.LABYRINTH_ROAD)):
            newPoint = LabyrinthPoint();
            newPoint.xPointPosition = tmpX - 1;
            newPoint.yPointPosition = tmpY;
            neighboursList.append(newPoint);
            del newPoint;
            
        if ((tmpX + 1 <= self.LABYRINTH_HEIGHT - 1) and
        (self.labyrinthArray[tmpX + 1][tmpY].labyrinthPointType != self.LABYRINTH_ROAD)):
            newPoint = LabyrinthPoint();
            newPoint.xPointPosition = tmpX + 1;
            newPoint.yPointPosition = tmpY;
            neighboursList.append(newPoint);
            del newPoint;
            
        if ((tmpY - 1 >= 0) and
        (self.labyrinthArray[tmpX][tmpY - 1].labyrinthPointType != self.LABYRINTH_ROAD)):
            newPoint = LabyrinthPoint();
            newPoint.xPointPosition = tmpX;
            newPoint.yPointPosition = tmpY - 1;
            neighboursList.append(newPoint);
            del newPoint;
            
        if ((tmpY + 1 <= self.LABYRINTH_WIDTH - 1) and
        (self.labyrinthArray[tmpX][tmpY + 1].labyrinthPointType != self.LABYRINTH_ROAD)):
            newPoint = LabyrinthPoint();
            newPoint.xPointPosition = tmpX;
            newPoint.yPointPosition = tmpY + 1;
            neighboursList.append(newPoint);
            del newPoint;
        
    def showLab(self):
        for i in range(self.LABYRINTH_HEIGHT):
            for j in range(self.LABYRINTH_WIDTH):
                print("i = ", i, " j = ", j,
                 "typ pola = ", self.labyrinthArray[i][j].labyrinthPointType);
