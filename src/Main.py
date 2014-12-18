
from labyrinth.base.LabyrinthCreator import LabyrinthCreator;
from labyrinth.road import ZnajdywanieDrogi;
from labyrinth.display.TestPyGame import TestPyGame;

if __name__ == '__main__':
    
    '''ZnajdywanieDrogi.initializeLabyrinth();
    ZnajdywanieDrogi.showLabirynthWithRoad();
    ZnajdywanieDrogi.searchRoad();
    ZnajdywanieDrogi.clearFlagsAfterRoadSearch();
    ZnajdywanieDrogi.showLabirynthWithRoad();
'''
        
    creator = LabyrinthCreator();
    creator.initializeLabyrinth();
    creator.createLabyrinthEntrance();
    #creator.createLabyrinthExit();
    creator.showLab();
    creator.createLabyrinthRoads();
    creator.showLab();
    '''
    testPyGame = TestPyGame(ZnajdywanieDrogi.LABYRINTH_HEIGHT, ZnajdywanieDrogi.LABYRINTH_WIDTH);
    testPyGame.showLabyrinth(ZnajdywanieDrogi.labyrinthArray, ZnajdywanieDrogi.LABYRINTH_HEIGHT, 
                             ZnajdywanieDrogi.LABYRINTH_WIDTH, ZnajdywanieDrogi.LABYRINTH_ENTRANCE,
                             ZnajdywanieDrogi.LABYRINTH_EXIT, ZnajdywanieDrogi.LABYRINTH_ROAD,
                             ZnajdywanieDrogi.LABYRINTH_WALL, ZnajdywanieDrogi.xEntrancePosition, 
                             ZnajdywanieDrogi.yEntrancePosition, ZnajdywanieDrogi.xExitPosition, 
                             ZnajdywanieDrogi.yExitPosition);
                             
                             '''