from test.TestPyGame import TestPyGame
from test.LabyrinthCreator import LabyrinthCreator
from testy2 import ZnajdywanieDrogi;

if __name__ == '__main__':
    
    ZnajdywanieDrogi.initializeLabyrinth();
    ZnajdywanieDrogi.showLabirynthWithRoad();
    ZnajdywanieDrogi.searchRoad();
    ZnajdywanieDrogi.clearFlagsAfterRoadSearch();
    ZnajdywanieDrogi.showLabirynthWithRoad();
    
    '''
- jedyne co trzeba poprawic to to zeby po znalezieniu sciezki wymazac falgi pozostawione podczas
znajdowania sciezki - zrobione
- sprawdzic jak sie zachowa gdy wejscie bedzie na gornej krawedzi a wyjscie na dolnej - dziala
- sprawdzic jak sie zachowa gdy wejscie bedzie na dolnej krawedzi a wyjscie na gornej - dziala
    
    '''
        
    '''creator = LabyrinthCreator();
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
                             creator.yExitPosition);'''