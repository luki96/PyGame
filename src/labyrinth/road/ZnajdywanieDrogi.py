from labyrinth.constants.Consts import Consts;
from labyrinth.base.LabyrinthPoint import LabyrinthPoint;
from collections import deque;
    
def searchRoad(labyrinthArray, xEntrancePosition, yEntrancePosition, 
               xExitPosition, yExitPosition):
    
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
            
            while ((labyrinthArray[tmpX][tmpY].labyrinthPointType != Consts.LABYRINTH_BEST_ROAD)
                   and (labyrinthArray[tmpX][tmpY].labyrinthPointType != Consts.LABYRINTH_ENTRANCE)):
                
                if (labyrinthArray[tmpX][tmpY].labyrinthPointType == Consts.LABYRINTH_ROAD_UP):
                    labyrinthArray[tmpX][tmpY].labyrinthPointType = Consts.LABYRINTH_BEST_ROAD;
                    tmpX += 1;
                
                elif (labyrinthArray[tmpX][tmpY].labyrinthPointType == Consts.LABYRINTH_ROAD_DOWN):
                    labyrinthArray[tmpX][tmpY].labyrinthPointType = Consts.LABYRINTH_BEST_ROAD;
                    tmpX -= 1;
                
                elif (labyrinthArray[tmpX][tmpY].labyrinthPointType == Consts.LABYRINTH_ROAD_LEFT):
                    labyrinthArray[tmpX][tmpY].labyrinthPointType = Consts.LABYRINTH_BEST_ROAD;
                    tmpY += 1;
                    
                elif (labyrinthArray[tmpX][tmpY].labyrinthPointType == Consts.LABYRINTH_ROAD_RIGHT):
                    labyrinthArray[tmpX][tmpY].labyrinthPointType = Consts.LABYRINTH_BEST_ROAD;
                    tmpY -= 1;
        
        if ((tmpX - 1 >= 0) and
            (labyrinthArray[tmpX - 1][tmpY].labyrinthPointType == Consts.LABYRINTH_ROAD)):
            
            labyrinthArray[tmpX - 1][tmpY].labyrinthPointType = Consts.LABYRINTH_ROAD_UP;
            point = LabyrinthPoint();
            point.xPointPosition = tmpX - 1;
            point.yPointPosition = tmpY;
            kolejkaWierzcholkow.append(point);
            del point;
        
        if ((tmpX + 1 <= Consts.LABYRINTH_HEIGHT - 1) and
            (labyrinthArray[tmpX + 1][tmpY].labyrinthPointType == Consts.LABYRINTH_ROAD)):
            
            labyrinthArray[tmpX + 1][tmpY].labyrinthPointType = Consts.LABYRINTH_ROAD_DOWN;
            point = LabyrinthPoint();
            point.xPointPosition = tmpX + 1;
            point.yPointPosition = tmpY;
            kolejkaWierzcholkow.append(point);
            del point;
        
        if ((tmpY - 1 >= 0) and
            (labyrinthArray[tmpX][tmpY - 1].labyrinthPointType == Consts.LABYRINTH_ROAD)):
            
            labyrinthArray[tmpX][tmpY - 1].labyrinthPointType = Consts.LABYRINTH_ROAD_LEFT
            point = LabyrinthPoint();
            point.xPointPosition = tmpX;
            point.yPointPosition = tmpY - 1;
            kolejkaWierzcholkow.append(point);
            del point;
        
        if ((tmpY + 1 <= Consts.LABYRINTH_WIDTH - 1) and
            (labyrinthArray[tmpX][tmpY + 1].labyrinthPointType == Consts.LABYRINTH_ROAD)):
            
            labyrinthArray[tmpX][tmpY + 1].labyrinthPointType = Consts.LABYRINTH_ROAD_RIGHT;
            point = LabyrinthPoint();
            point.xPointPosition = tmpX;
            point.yPointPosition = tmpY + 1;
            kolejkaWierzcholkow.append(point);
            del point;

def clearFlagsAfterRoadSearch(labyrinthArray, xExitPosition, yExitPosition):
    for i in range(Consts.LABYRINTH_HEIGHT):
        for j in range(Consts.LABYRINTH_WIDTH):
            if (labyrinthArray[i][j].labyrinthPointType in 
                range (Consts.LABYRINTH_ROAD_LEFT, Consts.LABYRINTH_ROAD_DOWN + 1)):
                labyrinthArray[i][j].labyrinthPointType = Consts.LABYRINTH_ROAD;
    labyrinthArray[xExitPosition][yExitPosition].labyrinthPointType = Consts.LABYRINTH_EXIT;