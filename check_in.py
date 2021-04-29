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
            
# initialize the Cast class with our csv file
test_search = Cast("movies_and_cast.csv")

# print find_film() list of movies based on user input
print(test_search.find_film())
print("-" * 160)

# print get_cast() dictionary with movie as key and cast as value
print(test_search.get_cast())
