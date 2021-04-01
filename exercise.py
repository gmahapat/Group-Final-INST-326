
""""Simple movie database with actors/actresses."""

class Cast:
    """"Actors/actresses in a film. 
    
    Attributes:
        name (str): the actors/actresses name.
        film (set of Cast): films in which actors/actresses star in. 
    """
    def __init__(self, name, film):
        self.name = name
        self.film = film
    
    def find_film(self, name):
        """Used to find the film(s) an actor/actress is in.
        
        Attributes:
            name (str): the actors/actresses name.
        
        Returns:
            The film(s) that the actor/actress stars in.
        """
        #enter code below
        
    def get_actor(self, film):
        """Used to find the actors and the film they are associated with. 
        
        Attributes:
            film (str): The title of the film
            
        Returns: 
            The set of the actor/actress that is in the film.
        """
        #enter code below

 class Movies:
    """ Movies from the csv file
    Attributes:
    title(str): the title of the movies
    actors(str): all of the actors from each respective movie
    
    """
    def __init__(self, name):
        with open('movies.csv', 'w', newline='') as csvfile:
        movieInfo = ['Movie', 'Actors']
        writer = csv.DictWriter(csvfile, movieInfo = movieInfo)
    """
    read in the csv file of movies with their attached actors
    
    """
    
    
