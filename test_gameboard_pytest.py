import pytest
from gameboard import GameBoard


@pytest.fixture
def dictionary():
    d = []
    with open('words.txt') as file:
        for word in file:
            d.append(word.rstrip())
    return d


def test_gameboard_size():
    g = GameBoard(width=15, height=10)
    assert len(g.data) == 10
    assert len(g.data[0]) == 15


def test_horizontal():
    """ Validate the rows members match what are in the data matrix. """
    g = GameBoard(width=5, height=5)
    for row in g.rows:
        # Convert the search string back into a list of characters
        row_list = list(row)
        assert row_list in g.data


def test_bad_args():
    """ Verify we handle dumb coding! """
    with pytest.raises(ValueError):
        GameBoard(width=-1, height=15)
    with pytest.raises(ValueError):
        GameBoard(width=1, height=0)

    g = GameBoard(width=1, height=1)
    with pytest.raises(ValueError):
        g.search(word_list=None)

    with pytest.raises(ValueError):
        g.search(word_list=[])


def test_asymmetrical_layout(dictionary):
    """ Verify searching boards that aren't symmetrical doesn't crash! """
    g = GameBoard(width=15, height=5)
    results = g.search(word_list=dictionary)
    assert results

    g = GameBoard(height=5, width=15)
    results = g.search(word_list=dictionary)
    assert results


def test_search_performance(dictionary):
    """ Verify searching a 15x15 board takes less than half a second. """
    g = GameBoard(width=15, height=15)
    g.search(word_list=dictionary)
    assert g.search_time < 0.5
