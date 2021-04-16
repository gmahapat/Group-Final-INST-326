import pandas as pd
""""Simple movie database with actors/actresses."""

class Cast:
    """"The purpose of this class is associating 
    Actors/actresses to a film. 
    
    Attributes:
        name (list): the actors/actresses name.
        film (str): name of a movie. 
    """
    def __init__(self, name, film):
        """ The purpose of this method is allowing the Cast class to 
        initialize the attributes of a class. 
        
        Args:
            name(list): name of actors/actress.
            film(str): name of film.
        
        """
        self.name = name
        self.film = film
    
    def find_film(self, name):
        """Used to find the actor/actress.
        
        Args:
            name (str): the actors/actresses name.
        
        Returns:
            actor_film(list): list of actors and actresses.  
        """
        
    def get_actor(self, film):
        """Used to find the actors and the film they are associated with. 
        
        Args:
            film (str): The title of the film
            
        Returns: 
            cast_film(tuple): a tuple of the actor/actress along with the film they are associted with. 
        """
    
    def order_cast(film):
        """Get the correct names for the movie and list in alphabetical order.
        
        Args:
            film (str): name of movie
           
        Returns:
            cast (list): returns a list of the cast who act in the given movie.
        """
    def order_film(name):
        """Get the correct movies that the actor is in and list in alphabetical order.
        
        Args:
            name (str): name of actor
           
        Returns:
            movies (list): returns a list of the movies that the actor acted in.
        """
     
 class Data:
    """This class will be used to display the information in the file with the actors 
    and their movies/ or their movie appearances."""
    
    def __init__(self, name):
        with open('movies.csv', 'w', newline='') as csvfile:
        movieInfo = ['Movie', 'Actors']
        writer = csv.DictWriter(csvfile, movieInfo = movieInfo)
    
    def display_data():
        data = pd.read_csv("filename.csv", sep = ',')
        data
        
    def count_appearance():
        appearances = pd.Series({content goes here })
        total_appearance = appearances.isin(["Actor name goes here"])
        total_appearance
        
    #This needs attention
    
    def parse_args(arglist):
   #user input


if __name__ == "__main__":
   

    
    
