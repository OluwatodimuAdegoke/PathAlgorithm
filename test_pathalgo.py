import pytest
from pathalgo import format_maze
from pathalgo import get_points
from pathalgo import search
from node import Node

def test_format_maze():

    maze = [['#','#','#','#','#'],['#','x',' ',' ','#'],['#',' ',' ','#','#'],['#',' ',' ',' ','#'],['#','o','a','#','#']]
    tmaze = [['#','#','#','#','#'],['#','x',' ',' ','#'],['#',' ',' ','#','#'],['#',' ',' ',' ','#'],['#','o','#','#','#']]

    assert format_maze(maze,5,5) == tmaze


def test_get_points():
    tmaze = [['#','#','#','#','#'],['#','x',' ',' ','#'],['#',' ',' ','#','#'],['#',' ',' ',' ','#'],['#',' ','#','#','#']]
    with pytest.raises(SystemExit):
        assert get_points(tmaze)
    amaze = [['#','#','#','#','#'],['#','x',' ',' ','#'],['#',' ',' ','#','#'],['#',' ',' ','o','#'],['#','o','#','#','#']]
    with pytest.raises(SystemExit):
        assert get_points(amaze)
    
def test_search():
    tmaze = [['#','#','#','#','#'],['#','x',' ',' ','#'],['#','#','#','#','#'],['#',' ',' ',' ','#'],['#','o','#','#','#']]
    start = Node((4,1))
    end = Node((1,1))
    with pytest.raises(SystemExit):
        assert search(tmaze,start,end)
    