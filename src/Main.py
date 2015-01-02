
from labyrinth.constants.Consts import Consts;
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
    
    testPyGame = TestPyGame(Consts.LABYRINTH_HEIGHT, Consts.LABYRINTH_WIDTH);
    testPyGame.showLabyrinth(Consts.LABYRINTH_HEIGHT, Consts.LABYRINTH_WIDTH, 
                             Consts.LABYRINTH_ENTRANCE, Consts.LABYRINTH_EXIT,
                             Consts.LABYRINTH_ROAD, Consts.LABYRINTH_WALL,
                             creator.labyrinthArray, creator.xEntrancePosition, 
                             creator.yEntrancePosition, creator.xExitPosition, 
                             creator.yExitPosition);