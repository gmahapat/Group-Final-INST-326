"""" Simple movie database with actors/actresses. """

class Cast:
    """" Actors/actresses in a film. 
    
    Attributes:
        name (str): the actors/actresses name.
        film (set of Cast): films in which actors/actresses star in. 
    """
    def __init__(self, name, film):
        self.name = name
        self.film = set()
    