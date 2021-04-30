""""Identifies the appropriate actors/actresses for a given film, 
    the appropriate film(s) for a given actor/actress or year."""

import pandas as pd
from argparse import ArgumentParser
import sys

class Cast:
    """"The purpose of this class is associating actors/actresses to a film. 
    
    Attributes:
        file_name (str): path to file.
    """
    def __init__(self, file_name):
        """ The purpose of this method is allowing the Cast class to 
            initialize the attributes of a class. 

        Args:
            file_name (str): file path
        """  
        self.df = pd.read_csv(file_name)
        self.df['title'] = self.df['title'].astype(str)
        self.df['actors'] = self.df['actors'].astype(str)
        self.df['year'] = self.df['year'].astype(str)
    
    def find_film(self):
        """Used to find the film(s) a given actor/actress stars in based on 
        the user input.
        
        Returns:
            film_list (list): list of movies the actor/actress stars in.  
    """
        film_list = []
        name = input("Enter actor/actress: ")
        for index,row in self.df.iterrows():
            if name in row['actors'].split(', '):
                film_list.append(row['title'])
        return film_list
    
    def get_cast(self):
        """Used to get the cast of a film, based off user input. 
        The key is movie and value is cast.

            
        Returns: 
            film_dict: a key:value pair of the actors/actresses along with the 
            film they are associted with. The film name as the key and a list 
            of the cast as the value. This is based off of user input.
        """
        film_dict = {}
        film = input("Enter a movie name: ")
        for index,row in self.df.iterrows():
            if film == row['title']:
                film_dict[row['title']] = row['actors'].split(', ')
                return film_dict
            
    def what_year(self):
        """Finds all movies in a given year.
        
        Returns:
            movie_list (list): list of movies in a given year."""
        movie_list = []
        year = input("Enter a year: ")
        for index,row in self.df.iterrows():
            if year in row['year']:
                movie_list.append(row['title'])
        return movie_list
            
def main(moviecastcsv):
    """Uses a file path to identify appropriate output. 
        Ask the user what they wish to find
        initializes the corresponding method.
    
    Args:
        moviecastcsv (str): csv file
        
    Side effects:
        prints the output of the method identified in the Cast class that
        stays on the console after the runs.
    """
    file = Cast(moviecastcsv)
    run = input("What method are you interested in, find_film, get_cast or what_year? ")
    chosen = False
    while not chosen:
        if run == "find_film":
            chosen = True
            print(file.find_film())
        elif run == "get_cast":
            chosen = True
            print(file.get_cast())
        elif run == "what_year":
            chosen = True
            print(file.what_year())
        else:
            None
        
def parse_args(arglist):
    """Parse command-line argument.
    
    Expect one mandatory argument:
        - moviecastcsv: the path to a CSV file containing
            movies and cast members.
    
    Args:
        arglist (str): argument from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace
    """
    parser = ArgumentParser()
    parser.add_argument("moviecastcsv",
                        help="file of movies and cast")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.moviecastcsv)
