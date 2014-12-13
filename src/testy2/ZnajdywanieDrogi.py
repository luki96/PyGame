from test.LabyrinthPoint import LabyrinthPoint;
from collections import deque;

LABYRINTH_HEIGHT = 5;
LABYRINTH_WIDTH = 5;
LABYRINTH_WALL = 0;
LABYRINTH_ROAD = 1;
LABYRINTH_BEST_ROAD = 2
LABYRINTH_ENTRANCE = 3;
LABYRINTH_EXIT = 4;
LABYRINTH_ROAD_LEFT = 5;      'komora z nitka w lewo'
LABYRINTH_ROAD_RIGHT = 6;     'komora z nitka w prawo'
LABYRINTH_ROAD_UP = 7;        'komora z nitka w gore'
LABYRINTH_ROAD_DOWN = 8;      'komora z nitka w dol'

PROBABILITY = 0.5;

xEntrancePosition = 4;
yEntrancePosition = 3;
xExitPosition = 0;
yExitPosition = 2;

labyrinthArray = [[LabyrinthPoint() for j in range (LABYRINTH_HEIGHT)] 
                          for i in range (LABYRINTH_WIDTH)];

def initializeLabyrinth():
    for i in range(LABYRINTH_HEIGHT):
        for j in range(LABYRINTH_WIDTH):
            labyrinthArray[i][j].xPointPosition = i;
            labyrinthArray[i][j].yPointPosition = j;
            labyrinthArray[i][j].labyrinthPointType = LABYRINTH_WALL;
                            
    labyrinthArray[xEntrancePosition][yEntrancePosition].labyrinthPointType = LABYRINTH_ENTRANCE;
    labyrinthArray[xExitPosition][yExitPosition].labyrinthPointType = LABYRINTH_ROAD;
    
    labyrinthArray[1][2].labyrinthPointType = LABYRINTH_ROAD;
    labyrinthArray[1][3].labyrinthPointType = LABYRINTH_ROAD;
    labyrinthArray[2][1].labyrinthPointType = LABYRINTH_ROAD;
    labyrinthArray[2][2].labyrinthPointType = LABYRINTH_ROAD;
    labyrinthArray[3][2].labyrinthPointType = LABYRINTH_ROAD;
    labyrinthArray[3][3].labyrinthPointType = LABYRINTH_ROAD;
    
def searchRoad():
    kolejkaWierzcholkow = deque();
    
    'Oznaczamy wierzcholek wejscia jako odwiedzony i wrzucamy do kolejki'
    kolejkaWierzcholkow.append(labyrinthArray[xEntrancePosition][yEntrancePosition]);
    
    '__len__() zwraca dlugosc'
    while (kolejkaWierzcholkow.__len__() != 0):
        tmpPoint = kolejkaWierzcholkow.popleft();
        tmpX = tmpPoint.xPointPosition;
        tmpY = tmpPoint.yPointPosition;
        
        'Sprawdzamy czy x i y pobranego punktu rowna sie x i y wyjscia'
        if ((tmpX == xExitPosition) and (tmpY == yExitPosition)):
            
            while ((labyrinthArray[tmpX][tmpY].labyrinthPointType != LABYRINTH_BEST_ROAD)
                   and (labyrinthArray[tmpX][tmpY].labyrinthPointType != LABYRINTH_ENTRANCE)):
                
                if (labyrinthArray[tmpX][tmpY].labyrinthPointType == LABYRINTH_ROAD_UP):
                    labyrinthArray[tmpX][tmpY].labyrinthPointType = LABYRINTH_BEST_ROAD;
                    tmpX += 1;
                
                elif (labyrinthArray[tmpX][tmpY].labyrinthPointType == LABYRINTH_ROAD_DOWN):
                    labyrinthArray[tmpX][tmpY].labyrinthPointType = LABYRINTH_BEST_ROAD;
                    tmpX -= 1;
                
                elif (labyrinthArray[tmpX][tmpY].labyrinthPointType == LABYRINTH_ROAD_LEFT):
                    labyrinthArray[tmpX][tmpY].labyrinthPointType = LABYRINTH_BEST_ROAD;
                    tmpY += 1;
                    
                elif (labyrinthArray[tmpX][tmpY].labyrinthPointType == LABYRINTH_ROAD_RIGHT):
                    labyrinthArray[tmpX][tmpY].labyrinthPointType = LABYRINTH_BEST_ROAD;
                    tmpY -= 1;
        
        if ((tmpX - 1 >= 0) and
            (labyrinthArray[tmpX - 1][tmpY].labyrinthPointType == LABYRINTH_ROAD)):
            
            labyrinthArray[tmpX - 1][tmpY].labyrinthPointType = LABYRINTH_ROAD_UP;
            point = LabyrinthPoint();
            point.xPointPosition = tmpX - 1;
            point.yPointPosition = tmpY;
            kolejkaWierzcholkow.append(point);
            del point;
        
        if ((tmpX + 1 <= LABYRINTH_HEIGHT - 1) and
            (labyrinthArray[tmpX + 1][tmpY].labyrinthPointType == LABYRINTH_ROAD)):
            
            labyrinthArray[tmpX + 1][tmpY].labyrinthPointType = LABYRINTH_ROAD_DOWN;
            point = LabyrinthPoint();
            point.xPointPosition = tmpX + 1;
            point.yPointPosition = tmpY;
            kolejkaWierzcholkow.append(point);
            del point;
        
        if ((tmpY - 1 >= 0) and
            (labyrinthArray[tmpX][tmpY - 1].labyrinthPointType == LABYRINTH_ROAD)):
            
            labyrinthArray[tmpX][tmpY - 1].labyrinthPointType = LABYRINTH_ROAD_LEFT
            point = LabyrinthPoint();
            point.xPointPosition = tmpX;
            point.yPointPosition = tmpY - 1;
            kolejkaWierzcholkow.append(point);
            del point;
        
        if ((tmpY + 1 <= LABYRINTH_WIDTH - 1) and
            (labyrinthArray[tmpX][tmpY + 1].labyrinthPointType == LABYRINTH_ROAD)):
            
            labyrinthArray[tmpX][tmpY + 1].labyrinthPointType = LABYRINTH_ROAD_RIGHT;
            point = LabyrinthPoint();
            point.xPointPosition = tmpX;
            point.yPointPosition = tmpY + 1;
            kolejkaWierzcholkow.append(point);
            del point;

def showLabirynthWithRoad():
    for i in range(LABYRINTH_HEIGHT):
        for j in range(LABYRINTH_WIDTH):
            print("i = ", i, " j = ", j, " typ pola = ", labyrinthArray[i][j].labyrinthPointType);

def clearFlagsAfterRoadSearch():
    for i in range(LABYRINTH_HEIGHT):
        for j in range(LABYRINTH_WIDTH):
            if (labyrinthArray[i][j].labyrinthPointType in range (LABYRINTH_ROAD_LEFT, LABYRINTH_ROAD_DOWN + 1)):
                labyrinthArray[i][j].labyrinthPointType = LABYRINTH_ROAD;
    labyrinthArray[xExitPosition][yExitPosition].labyrinthPointType = LABYRINTH_EXIT;