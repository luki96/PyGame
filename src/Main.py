from test.TestPyGame import TestPyGame
from test.LabyrinthCreator import LabyrinthCreator
from testy2 import TestyTestow;

if __name__ == '__main__':
    
    TestyTestow.initializeLabyrinth();
    TestyTestow.searchRoad();
    TestyTestow.showLabirynthWithRoad();
    
    '''
    wynik dzialania algorytmu
    
i =  0  j =  0  typ pola =  0
i =  0  j =  1  typ pola =  0
i =  0  j =  2  typ pola =  0
i =  0  j =  3  typ pola =  0
i =  0  j =  4  typ pola =  0
i =  1  j =  0  typ pola =  3
i =  1  j =  1  typ pola =  2
i =  1  j =  2  typ pola =  6
i =  1  j =  3  typ pola =  6
i =  1  j =  4  typ pola =  0
i =  2  j =  0  typ pola =  0
i =  2  j =  1  typ pola =  2
i =  2  j =  2  typ pola =  6
i =  2  j =  3  typ pola =  0
i =  2  j =  4  typ pola =  0
i =  3  j =  0  typ pola =  0
i =  3  j =  1  typ pola =  2
i =  3  j =  2  typ pola =  2
i =  3  j =  3  typ pola =  2
i =  3  j =  4  typ pola =  2
i =  4  j =  0  typ pola =  0
i =  4  j =  1  typ pola =  0
i =  4  j =  2  typ pola =  0
i =  4  j =  3  typ pola =  0
i =  4  j =  4  typ pola =  0

- jedyne co trzeba poprawic to to zeby po znalezieniu sciezki wymazac falgi pozostawione podczas
znajdowania sciezki
- sprawdzic jak sie zachowa gdy wejscie bedzie na gornej krawedzi a wyjscie na dolnej
- sprawdzic jak sie zachowa gdy wejscie bedzie na dolnej krawedzi a wyjscie na gornej
    
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