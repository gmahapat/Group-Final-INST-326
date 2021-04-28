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
            file_list (list): list of movies the actor/actress stars in.  
        """
        file_dict = {}
        file_list = []
        
        with open(name, "r", encoding="utf-8") as name_csv:
            read_file = name_csv.readlines()
            for line in read_file:
                detail = line.split(",")
                file_list.append(detail[0]) # movie title is at index zero 
            return file_list
       
    def get_cast(self, film):
        """Used to get the cast of a film, obtains who acts in the film given. 
        
        Args:
            film (str): the title of the film
            
        Returns: 
            film_dict (key:value pair): a key: value pair of the 
            actors/actresses along with the film they are associted with 
            the film name as the key and a list of the cast as the value.
        """
        file_dict = {}
        with open(film, "r", encoding="utf-8") as title:
            read_title = title.readlines()
            for line in read_title:
                title_list = line.split(",")
                file_dict[title_list[0]] = title_list[1].strip()
            return file_dict
        
    def order_cast(film):
        """Obtains the names of the cast in a given movie and prints them
            in alphabetical order.
        
        Args:
            film (str): name of movie
           
        Side effects:
            print: prints each actor/actress name in its own line in alphabetical order by
                    first name.
        """
        #if film is not in csv return 
        if film not in df.keys():
            return "Information for this film is not available"
        #retrieve the string containing all the actors in film
        film_cast = df[film].split(',')
        film_cast.sort()
        for actor in film_cast:
            print (actor,'\n')
            
    def order_film(name):
        """Get the correct movies that the actor/actress is in, in alphabetical order.
        
        Args:
            name (str): name of actor
           
        Side effects:
            print: prints each movie in its own line in alphabetical order.
        """
        result = []
        #assuming our dataframe is converted into a python dictionary
        #iterate through each movie and its list of actors
        for movie, names in df.items(): 

            #convert the string of actors into a list
            name_list = names.split(",")
            #if the desired actor is in the list of actors add the movie to result
            if name in name_list:
                result.append(movie)
        if not result:
            return "This actor is not featured in the current list of movies"
        #sort the movies by alphabetical order and print line by line
        result.sort()
        for movie in result:
            print (movie,'\n')

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
    
    Two arguments are expected, the file name of a CSV file containing film names
    along with the names of the cast members. Text values.
    
    Args:
        arglist (list of str): a list of command-line arguments.
    
    Returns:
        namespace: an object with file name and the name of a movie or actor/actress.
    
    Reference:
        Example code obtained from Aric Bills from previous exercise assignments.
    """
    parser = ArgumentParser()
    parser.add_argument("file", help="path to movies CSV file")
    parser.add_argument("name", help="name of actor/actress")
    parser.add_argument("film", help="name of movie")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    """Runs the rest of the program. Allows for files to be ran directly 
        and/or when modules are imported."""
    args = parse_args(sys.argv[1:])
    #NEEDS ATTENTION
    #movies = best_movies(args.movie_csv, args.rating_csv)
    #print(movies.head())
    
    
