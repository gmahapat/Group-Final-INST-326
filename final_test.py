import search_movie_database as s
import pytest

"""Used to test functions defined in electricity.py"""

def test_main():
    assert s.main('find_film') == 'Enter actor/actress: '
    assert s.main('get_cast') == 'Enter a movie name: '
    assert s.main('what_year') == 'Enter a year: '

