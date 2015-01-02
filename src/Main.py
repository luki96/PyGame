
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
    print("---------------------------------------------------------------");
    creator.showLab();
    creator.createRoadBetweenEntranceAndExit();
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++");
    creator.showLab();
    
    ZnajdywanieDrogi.searchRoad(creator.labyrinthArray, creator.xEntrancePosition,
                                creator.yEntrancePosition, 
                                creator.xExitPosition, creator.yExitPosition);
    ZnajdywanieDrogi.clearFlagsAfterRoadSearch(creator.labyrinthArray, creator.xExitPosition,
                                               creator.yExitPosition);
    print("***************************************************************");
    creator.showLab();
    
    testPyGame = TestPyGame(creator.LABYRINTH_HEIGHT, creator.LABYRINTH_WIDTH);
    testPyGame.showLabyrinth(creator.labyrinthArray, creator.LABYRINTH_HEIGHT, 
                             creator.LABYRINTH_WIDTH, creator.LABYRINTH_ENTRANCE,
                             creator.LABYRINTH_EXIT, creator.LABYRINTH_ROAD,
                             creator.LABYRINTH_WALL, creator.xEntrancePosition, 
                             creator.yEntrancePosition, creator.xExitPosition, 
                             creator.yExitPosition);