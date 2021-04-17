""""Identifies the appropriate actors/actresses for a given film or
    the appropriate film(s) for a given actor/actress in alphabetical order."""

import pandas as pd

class Cast:
    """"The purpose of this class is associating 
    Actors/actresses to a film. 
    
    Attributes:
        name (str): the actors/actresses name.
        film (str): name of a movie. 
    """
    def __init__(self, name, film):
        """The purpose of this method is allowing the Cast class to 
        initialize the attributes of a class. 
        
        Args:
            name(str): name of actors/actress.
            film(str): name of film.
        """
        self.name = name
        self.film = film
    
    def find_film(self, name):
        """Used to find the film(s) a given actor/actress stars in.
        
        Args:
            name (str): the actors/actresses name.
        
        Returns:
            get_film (list): list of movies the actor/actress stars in.  
        """
        
    def get_cast(self, film):
        """Used to get the cast of a film, obtains who acts in the film given. 
        
        Args:
            film (str): the title of the film
            
        Returns: 
            film_cast (key:value pair): a key: value pair of the actors/actresses 
                                        along with the film they are associted with.
                                        with the film name as the key and a list of the 
                                        cast as the value.
        """
    
    def order_cast(film):
        """Obtains the names of the cast in a given movie and prints them
            in alphabetical order.
        
        Args:
            film (str): name of movie
           
        Side effects:
            print: prints each actor/actress name in its own line in alphabetical order by
                    first name.
        """
    def order_film(name):
        """Get the correct movies that the actor/actress is in, in alphabetical order.
        
        Args:
            name (str): name of actor
           
        Side effects:
            print: prints each movie in its own line in alphabetical order.
        """
     
 class Data:
    """This class will be used to display the information in the file with the actors 
    and their movies.
    
    Attributes:
        file (file): CSV file containing movies and their cast.
    """
    
    def __init__(self, file):
        """Opens CSV file and orders the data in a dictionary with the file title
            as the key and a list of actor/actress names as the value.
            
        Args:
            see class attributes.
        """
        with open('movies.csv', 'w', newline='') as csvfile:
            #under development
        movieInfo = ['Movie', 'Actors']
        writer = csv.DictWriter(csvfile, movieInfo = movieInfo)
    
    def display_data():
        """Creating the file into a database using Pandas to better structure
            the data."""
        data = pd.read_csv("filename.csv", sep = ',')
        data
        
    def count_appearance():
        """Identifies how many movies the actor/actress has made an appearance in."""
        appearances = pd.Series({content goes here })
        total_appearance = appearances.isin(["Actor name goes here"])
        total_appearance
        
    #This needs attention
    
def parse_args(arglist):
    """Parse command-line arguments.
    
    Args:
        arglist (list of str): a list of command-line arguments.
    
    Returns:
        namespace: the parsed command-line arguments as a namespace with
        variables (csv file name).
    """


if __name__ == "__main__":
    """Runs the rest of the program. Allows for files to be ran directly 
        and/or when modules are imported."""
    
    
