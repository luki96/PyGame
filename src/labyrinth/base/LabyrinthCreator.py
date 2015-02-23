import random;
from labyrinth.base.LabyrinthPoint import LabyrinthPoint;
from labyrinth.constants.Consts import Consts;
from collections import deque;

class LabyrinthCreator():

    xEntrancePosition = 0;
    yEntrancePosition = 0;
    xExitPosition = 0;
    yExitPosition = 0;
    labyrinthArray = None;

    def __init__(self):
        self.labyrinthArray = [[LabyrinthPoint() for j in range (Consts.LABYRINTH_WIDTH)] 
                          for i in range (Consts.LABYRINTH_HEIGHT)];
    
    def initializeLabyrinth(self):
        for i in range(Consts.LABYRINTH_HEIGHT):
            for j in range(Consts.LABYRINTH_WIDTH):
                self.labyrinthArray[i][j].xPointPosition = i;
                self.labyrinthArray[i][j].yPointPosition = j;
                self.labyrinthArray[i][j].labyrinthPointType = Consts.LABYRINTH_WALL;
                
    def createLabyrinthEntrance(self):
        self.xEntrancePosition = 0;
        self.yEntrancePosition = 0;       
        self.labyrinthArray[self.xEntrancePosition][self.yEntrancePosition].labyrinthPointType = Consts.LABYRINTH_ENTRANCE;
        
        self.xExitPosition = 4;
        self.yExitPosition = 4;
        self.labyrinthArray[self.xExitPosition][self.yExitPosition].labyrinthPointType = Consts.LABYRINTH_EXIT;

        self.labyrinthArray[2][2].labyrinthPointType = Consts.LABYRINTH_ROAD;
        self.labyrinthArray[2][3].labyrinthPointType = Consts.LABYRINTH_ROAD;
        self.labyrinthArray[3][0].labyrinthPointType = Consts.LABYRINTH_ROAD;
        '''self.labyrinthArray[3][1].labyrinthPointType = Consts.LABYRINTH_ROAD;
        self.labyrinthArray[3][2].labyrinthPointType = Consts.LABYRINTH_ROAD;
        self.labyrinthArray[3][3].labyrinthPointType = Consts.LABYRINTH_ROAD;
        self.labyrinthArray[4][1].labyrinthPointType = Consts.LABYRINTH_ROAD;
        self.labyrinthArray[4][2].labyrinthPointType = Consts.LABYRINTH_ROAD;
        self.labyrinthArray[4][3].labyrinthPointType = Consts.LABYRINTH_ROAD;
        '''
        '''self.xEntrancePosition = random.randrange(Consts.LABYRINTH_HEIGHT);
        if ((self.xEntrancePosition == 0) or (self.xEntrancePosition == Consts.LABYRINTH_HEIGHT - 1)):
            self.yEntrancePosition = random.randrange(Consts.LABYRINTH_WIDTH);
            self.labyrinthArray[self.xEntrancePosition][self.yEntrancePosition].labyrinthPointType = Consts.LABYRINTH_ENTRANCE;
        elif (self.xEntrancePosition in range(1, Consts.LABYRINTH_HEIGHT - 1)):
            if (random.random() < Consts.PROBABILITY):
                self.yEntrancePosition = 0;        
                self.labyrinthArray[self.xEntrancePosition][self.yEntrancePosition].labyrinthPointType = Consts.LABYRINTH_ENTRANCE;
            else:
                self.yEntrancePosition = Consts.LABYRINTH_WIDTH - 1;
                self.labyrinthArray[self.xEntrancePosition][self.yEntrancePosition].labyrinthPointType = Consts.LABYRINTH_ENTRANCE;
           '''     
    def createLabyrinthExit(self):
        if (self.yEntrancePosition == 0):
            self.xExitPosition = random.randrange(Consts.LABYRINTH_HEIGHT);
            self.yExitPosition = Consts.LABYRINTH_WIDTH - 1;
            self.labyrinthArray[self.xExitPosition][self.yExitPosition].labyrinthPointType = Consts.LABYRINTH_EXIT;
        elif (self.yEntrancePosition == Consts.LABYRINTH_WIDTH - 1):
            self.xExitPosition = random.randrange(Consts.LABYRINTH_HEIGHT);
            self.yExitPosition = 0;
            self.labyrinthArray[self.xExitPosition][self.yExitPosition].labyrinthPointType = Consts.LABYRINTH_EXIT;
        elif (self.yEntrancePosition in range(1, Consts.LABYRINTH_WIDTH - 1)):
            self.xExitPosition = Consts.LABYRINTH_HEIGHT - 1;
            self.yExitPosition = random.randrange(Consts.LABYRINTH_WIDTH - 1);
            self.labyrinthArray[self.xExitPosition][self.yExitPosition].labyrinthPointType = Consts.LABYRINTH_EXIT;
                    
    def showLab(self):
        for i in range(Consts.LABYRINTH_HEIGHT):
            for j in range(Consts.LABYRINTH_WIDTH):
                print("i = ", i, " j = ", j,
                 "typ pola = ", self.labyrinthArray[i][j].labyrinthPointType);
    
    def createRoadBetweenEntranceAndExit(self):
        currentX = self.xEntrancePosition;
        currentY = self.yEntrancePosition;
        newX = self.generateRandomValue(currentX);
        newY = currentY;
        self.connectPoints(currentX, currentY, newX, newY);
        
        while (newY != self.yExitPosition - 1):
            currentX = newX;
            currentY = newY;
            newX = currentX;
            newY = currentY + 1;
            self.connectPoints(currentX, currentY, newX, newY);
            newX = self.generateRandomValue(newX);
            self.connectPoints(currentX, currentY, newX, newY);
        
        newY = currentY + 1;
        self.connectPoints(newX, newY, self.xExitPosition, self.yExitPosition);
        
    def generateRandomValue(self, currentValue):
        newValue = random.randrange(0, Consts.LABYRINTH_WIDTH);
        while (newValue == currentValue):
            newValue = random.randrange(0, Consts.LABYRINTH_WIDTH);
        return newValue;
    
    def connectPoints(self, startX, startY, stopX, stopY):
        self.labyrinthArray[stopX][stopY].labyrinthPointType = Consts.LABYRINTH_ROAD;
        
        while (startX != stopX):
            if (stopX > startX):        #Idziemy w prawa strone
                startX += 1;
                self.labyrinthArray[startX][stopY].labyrinthPointType = Consts.LABYRINTH_ROAD;
            elif (stopX < startX):        #Idziemy w lewa strone
                startX -= 1;
                self.labyrinthArray[startX][stopY].labyrinthPointType = Consts.LABYRINTH_ROAD;

'''def createLabyrinthRoads(self):
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
'''