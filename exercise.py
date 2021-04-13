
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
    #This needs attention
    
    def parse_args(arglist):
    """ Process command line arguments.
    
    Expect one mandatory argument (a frequency) and one optional argument,
    preceded by "-a4" (the value to use as the frequency of A4).
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("freq", type=float, help="a frequency in Hz")
    parser.add_argument("-a4", type=float, default=440.0,
                        help="frequency to use for A4")
    args = parser.parse_args(arglist)
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.freq, a4=args.a4)

    
    
