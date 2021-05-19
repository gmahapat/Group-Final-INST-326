""""Searches a database for the user's input."""

import pandas as pd
from argparse import ArgumentParser
from IPython.display import display
import sys
import csv


searches = []
class Search:
    """"The purpose of this class is to find the user's input, from films
        to cast, year and genre. 
    
    Attributes:
        file_name (str): path to file.
    """
    
    def __init__(self, file_name):
        """ The purpose of this method is allowing the Search class to 
            initialize the attributes of the class. 
        Args:
            file_name (str): file path
        """
        self.count = []
        self.df = pd.read_csv(file_name)
        self.df['title'] = self.df['title'].astype(str)
        self.df['actors'] = self.df['actors'].astype(str)
        self.df['year'] = self.df['year'].astype(str)
        self.df['genre'] = self.df['genre'].astype(str)
        
        #This function will possibly be used in order to open the file and read it into a table. Currently under maintenance
    #def display_data(self):
        #open_file = pd.read_csv("movies_and_cast.csv").head()
        #open_file
    
    def find_film(self):
        """Used to find the film(s) a given actor/actress stars in based on 
        the user input.
        
        Returns:
            film_list (list): list of movies the actor/actress stars in.  
        """
        film_list = []
        name = input("Enter actor/actress: ")
        searches.append(name)
        for index,row in self.df.iterrows():
            if name in row['actors'].split(', '):
                film_list.append(row['title'])
        count_film = self.count.append(name + ": "+ str(len(film_list)))
        count_film
        return (f'\n {name} stars in: {film_list}\n\n -**** WOULD YOU LIKE TO SELECT AGAIN? ****-\n')
    
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
        searches.append(film)
        for index,row in self.df.iterrows():
            if film == row['title']:
                film_dict[row['title']] = row['actors'].split(', ')
                count_cast = self.count.append(film + ": "+ str(len(film_dict[row['title']])))
                count_cast
                return (f'\n {film_dict}\n\n -**** WOULD YOU LIKE TO SELECT AGAIN? ****-\n')
            
    def what_year(self):
        """Finds all movies in a given year.
        
        Returns:
            movie_list (list): list of movies in a given year.
        """
        movie_list = []
        year = input("Enter a year: ")
        searches.append(year)
        for index,row in self.df.iterrows():
            if year in row['year']:
                movie_list.append(row['title'])
        count_year = self.count.append(year + ": "+ str(len(movie_list)))
        count_year
        return (f'\n Movies in {year} are {movie_list}\n\n -**** WOULD YOU LIKE TO SELECT AGAIN? ****-\n')    
    
    def find_genre(self):
        """Finds all movies in a given genre.
        
        Returns:
            genre_list (list): list of movies in a given genre.
        """
        genre_list = []
        genre = input("Enter a genre: ")
        searches.append(genre)
        for index,row in self.df.iterrows():
            if genre in row['genre'].split(', '):
                genre_list.append(row['title'])
        count_genre = self.count.append(genre + ": "+ str(len(genre_list)))
        count_genre
        return (f'\n Movies with the genre of {genre} are: {genre_list}\n\n -**** WOULD YOU LIKE TO SELECT AGAIN? ****-\n')
    
def print_search_history(input_array):
    """Used to store user inputs so then the program ends, the user has their search history.
    
    Args:
        input_array (list of str): the user's input stored in a list
        
    Side effects:
        print: prints a list of the user's input
    """
    print ("User search history:\n")
    iteration = 0
    for input in input_array:
        print (str(iteration) + ":", input)
        iteration += 1
    searches.clear()   

def display_data(moviecastcsv):
    """Displays the CSV file
    
    Args:
        moviecastcsv (file): path to the CSV file to be displayed
    """
    df = pd.read_csv(moviecastcsv)
    display(df)
    
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
    file = Search(moviecastcsv)
    while True:
        run = input("-Enter 'view' to display CSV file.\n-Enter 'done' to exit the program.\n * What method would you like to use find_film, get_cast, what_year or find_genre? ")
        if run == "find_film":
            print(file.find_film())
        elif run == "get_cast":
            print(file.get_cast())
        elif run == "what_year":
            print(file.what_year())
        elif run == "find_genre":
            print(file.find_genre())
        elif run == "view":
            display_data(moviecastcsv)
        elif run == "done":
            print("-"*50, "END OF PROGRAM", "-"*50)
            print_search_history(searches)
            print("\nOUTPUT COUNT: ", file.count)
            break
        else:
            print("-"*50, "INVALID INPUT. TRY AGAIN.", "-"*50)
        
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
