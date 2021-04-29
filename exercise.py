""""Identifies the appropriate actors/actresses for a given film or
    the appropriate film(s) for a given actor/actress in alphabetical order."""

import pandas as pd

class Cast:
    """"The purpose of this class is associating actors/actresses to a film. 
    
    Attributes:
        file_name (str): path to file.
    """
    def __init__(self, file_name):
        """ The purpose of this method is allowing the Arrdvark class to 
            initialize the attributes of a class. 

        Args:
            file_name (str): file path
        """  
        self.df = pd.read_csv(file_name)
        self.df['title'] = self.df['title'].astype(str)
        self.df['actors'] = self.df['actors'].astype(str)
    
    def find_film(self):
        """Used to find the film(s) a given actor/actress stars in based on 
        the user input.
        
        Returns:
            file_list (list): list of movies the actor/actress stars in.  
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
        file_dict = {}
        film = input("Enter a movie name: ")
        for index,row in self.df.iterrows():
            if film == row['title']:
                file_dict[row['title']] = row['actors'].split(', ')
                return file_dict
            
# initialize the Cast class with our csv file
test_search = Cast("movies_and_cast.csv")

# print find_film() list of movies based on user input
print(test_search.find_film())
print("-" * 160)

# print get_cast() dictionary with movie as key and cast as value
print(test_search.get_cast())
        
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

if __name__ == "__main__":
    """Runs the rest of the program. Allows for files to be ran directly 
        and/or when modules are imported."""
    Data() #calling class

    
