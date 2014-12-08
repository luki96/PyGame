from test.TestPyGame import TestPyGame
from test.LabyrinthCreator import LabyrinthCreator

if __name__ == '__main__':
    creator = LabyrinthCreator();
    creator.initializeLabyrinth();
    creator.createLabyrinthEntrance();
    creator.createLabyrinthExit();
    creator.showLab();
    
    testPyGame = TestPyGame(creator.LABYRINTH_HEIGHT, creator.LABYRINTH_WIDTH);
    testPyGame.showLabyrinth(creator.labyrinthArray, creator.LABYRINTH_HEIGHT, 
                             creator.LABYRINTH_WIDTH, creator.LABYRINTH_ENTRANCE,
                             creator.LABYRINTH_EXIT, creator.LABYRINTH_ROAD,
                             creator.LABYRINTH_WALL, creator.xEntrancePosition, 
                             creator.yEntrancePosition, creator.xExitPosition, 
                             creator.yExitPosition);