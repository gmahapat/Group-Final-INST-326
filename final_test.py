import search_movie_database as s
import pytest

import builtins
from unittest import mock
import search_movie_database
import pytest

"""Used to test functions defined in search_movie_database.py"""

# testing find_film method
def test_find_film():
    with mock.patch("builtins.input", side_effect=["Florence Pugh"]):
        x1 = search_movie_database.Search("movies_and_cast.csv")
        assert x1.find_film() == """\n Florence Pugh stars in: ["L'uomo sul treno", 'Malevolent - La voce del male', 'Piccole donne', 'The Falling', 'Lady Macbeth', 'Una famiglia al tappeto', 'Midsommar - Il villaggio dei dannati']\n\n -**** WOULD YOU LIKE TO SELECT AGAIN? ****-\n"""

def test_find_film_two():
    with mock.patch("builtins.input", side_effect=["Jack Pickford"]):    
        x2 = search_movie_database.Search("movies_and_cast.csv")
        assert x2.find_film() == """\n Jack Pickford stars in: ['Amore di madre', 'Tom Sawyer', 'The Goose Woman', 'The Bat', 'Brown of Harvard', 'Exit Smiling']\n\n -**** WOULD YOU LIKE TO SELECT AGAIN? ****-\n"""

# testing for find_genre function
def test_find_genre():
    with mock.patch("builtins.input", side_effect=["Weird Fiction"]):
        first = search_movie_database.Search("movies_and_cast.csv")
        assert first.find_genre() == """\n Movies with the genre of Weird Fiction are: []\n\n -**** WOULD YOU LIKE TO SELECT AGAIN? ****-\n"""
                   
# testing get_cast method
def test_get_cast():
    with mock.patch("builtins.input", side_effect=["Up"]):
        y1 = search_movie_database.Search("movies_and_cast.csv")
        assert y1.get_cast() == """\n {'Up': ['Edward Asner', 'Christopher Plummer', 'Jordan Nagai', 'Bob Peterson', 'Delroy Lindo', 'Jerome Ranft', 'John Ratzenberger', 'David Kaye', 'Elie Docter', 'Jeremy Leary', 'Mickie McGowan', 'Danny Mann', 'Donald Fullilove', 'Jess Harnell', 'Josh Cooley']}\n\n -**** WOULD YOU LIKE TO SELECT AGAIN? ****-\n"""

def test_get_cast_two():
    with mock.patch("builtins.input", side_effect=["Forrest Gump"]):
        y2 = search_movie_database.Search("movies_and_cast.csv")
        assert y2.get_cast() == """\n {'Forrest Gump': ['Tom Hanks', 'Rebecca Williams', 'Sally Field', 'Michael Conner Humphreys', 'Harold G. Herthum', 'George Kelly', 'Bob Penny', 'John Randall', 'Sam Anderson', 'Margo Moorer', 'Ione M. Telech', 'Christine Seabrook', 'John Worsham', 'Peter Dobson', 'Siobhan Fallon Hogan']}\n\n -**** WOULD YOU LIKE TO SELECT AGAIN? ****-\n"""

#testing what_year method
def test_what_year():
    with mock.patch("builtins.input", side_effect=["1890"]):
        z1 = search_movie_database.Search("movies_and_cast.csv")
        assert z1.what_year() == """\n Movies in 1890 are []\n\n -**** WOULD YOU LIKE TO SELECT AGAIN? ****-\n"""

def test_what_year_two():
    with mock.patch("builtins.input", side_effect=["1911"]):
        z2 = search_movie_database.Search("movies_and_cast.csv")
        assert z2.what_year() == """\n Movies in 1911 are ['Cleopatra', 'Jesus of Nazareth', 'Omicron', 'La polizia sta a guardare', 'Kill Bill - Volume 1']\n\n -**** WOULD YOU LIKE TO SELECT AGAIN? ****-\n"""
    
#testing between_year method:
def test_between_year():
    with mock.patch("builtins.input", side_effect=["1800,1911"]):
        test = search_movie_database.Search("movies_and_cast.csv")
        assert test.between_year() == """\n Movies between 1800 and 1911 are ['Miss Jerry', 'The Story of the Kelly Gang']\n\n -**** WOULD YOU LIKE TO SELECT AGAIN? ****-\n"""
        
def test_between_year():    
    with mock.patch("builtins.input", side_effect=["1890,1912"]):
        test2 = search_movie_database.Search("movies_and_cast.csv")
        assert test2.between_year() == """\n Movies between 1890 and 1912 are ['Miss Jerry', 'The Story of the Kelly Gang', 'Cleopatra', 'Jesus of Nazareth', 'Omicron', 'La polizia sta a guardare', 'Kill Bill - Volume 1']\n\n -**** WOULD YOU LIKE TO SELECT AGAIN? ****-\n"""

# testing duration_search method
def test_duration_search():
    with mock.patch("builtins.input", side_effect=["44"]):
        x1 = search_movie_database.Search("movies_and_cast.csv")
        assert x1.duration_search() == """\n The Movies that are less or equal to 44 minutes are ['Una ragazza per bene', 'Dragon Ball Z - Il diabolico guerriero degli inferi', 'Dang wo men tong zai yi qi', 'The Overbrook Brothers']\n\n -**** WOULD YOU LIKE TO SELECT AGAIN? ****-\n"""
