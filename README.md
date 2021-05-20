# Group-Final-INST-326

### Explanation of Files
-   The search_movie_database.py file is the python scrpit of our main code. This file contains the code to run the program successfully.
-   The movies_and_cast.csv file is a CSV file that contains the data the program will be pulling from, it contains movies, cast, genre of the movie, the year the movie was released, the country the movie originated and the duration of the movie.
-   The final_test.py is the pytest to check if our program is running successfully with the correct outputs.
-   The README.md file is a markdown file that contains necessary information to successfully run the program and detailed description of each output.
### Instructions
1. In order to run the program successful from the comand line you will need to input the following prompt:
##### If on Mac - python3 search_movie_database.py movies_and_cast.csv
##### If on Windows - python search_movie_database.py movies_and_cast.csv
2. The program will ask you a question, input the method you would like to run exactly as it shows in the question and press enter.
3. According to the method you have choosen the program will ask you to provide the necessary information to successfully run the method.
4. Please type your second input in general Title and Name characters. 
##### Ex. Movie title = Cinderella - with the first letter of each word in the title capitalized.
##### Ex. Actor/Actress = Megan Fox - with the first letter of the first and last name capitalized.
##### Ex. Genre = Romance - with the first letter capitalized.
7. You will be able to display the CSV file by entering 'view', this will output the CSV file so you are aware of possible items you can search for. 
6. If you would like to end the program enter 'done' this will exit the program and output your search history along with the count of outputs for each input.
### Possible Inputs
(All outputs are obtained from the CSV file)
- 'find_film': this input will ask you for an actor/actress name, then output all movies that actor/actress was casted in (Megan Fox)
- 'get_cast': this input will ask you for a movie title, then output all the cast members associated with that movie (Cinderella)
- 'what_year': this input will ask you for a year, then output all movies released in that year (1975)
- 'between_year': this input will ask you for two years seperated by a comma with no spaces, then outputs movies between the two years. Make sure that the lesser year comes      before the greater year. (1890,1920)
- 'find_genre': this input will ask for a genre, then output all movies with the identified genre. (Romance)
- 'duration_search': this input will ask for an integar, then output any movie with the number of minutes given or less. Ex. 50, the output will be any movie that is 50 minutes  or less. (50)
- 'review': this will output the CSV file so users have an idea of what possible searches can be. (review)
- 'done': this will end the program and output the user's search history along with the number of outputs each search had. (done)
### Annotated Bibliography
Kaggle - 

Leone, S. (2020, September 14). IMDb movies extensive dataset. Kaggle. https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset?select=IMDb%2Bmovies.csv. 

This source was used to obtain the CSV file
