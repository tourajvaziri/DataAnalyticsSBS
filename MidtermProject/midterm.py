# Midterm: SBS Data Analytics
# The HollywoodMovies.csv file contains movie data from the years 2007 to 2013.
# It contains the following columns: Movie,LeadStudio,RottenTomatoes,AudienceScore,Story,Genre,TheatersOpenWeek,OpeningWeekend,BOAvgOpenWeekend,DomesticGross,ForeignGross,WorldGross,Budget,Profitability,OpenProfit,Year
# Complete the tasks (1 to 11) by adding code after the lines marked by # ADD CODE HERE

# Open the file containing the movies data
file = open ('HollywoodMovies.csv', 'r')

# Extra read for the first line that contains columns names 
file.readline()

# Create variables of type list to hold movies data
names: str = []
rottenTomatoesScores: float = []
genres: str = []
budgets: float = []

# Read every line of file, parse it, and add the data to the correct list
for l in file:
   # This code splits each line by ',' so that after executing this code:
   # data[0] has each movie name
   # data[2] has each movie score
   # data[5] has each movie genre
   # data[12] has each movie budget
   #
   # Example:  Spider-Man 3,Sony,61,54,Metamorphosis,Action,4252,151.1,35540,336.53,554.34,890.87,258,345.3,58.57,2007
   # data[0] = 'Spider-Man 3'
   # data[2] = '61'
   # data[5] = 'Action'
   # data[12] = '258'
   data = l.split(',')

   # Task 1: Add data[0] to names list.
   # ADD CODE HERE

   
   # Task 2: Add data[2] to rottenTomatoesScores list.
   # Hint 1: You may need to use casting
   # Hint 2: For some movies the score value is missing (i.e. score is empty). For that you need to use conditions (if .. else ..) and assign a random value in case there is no score
   # ADD CODE HERE

   
   # Task 3: Add data[5] to genres list.
   # Hint 1: For some movies the genre value is missing. For that you need to use conditions and assign a random value when it is missing
   # ADD CODE HERE


   # Task 4: Add data[12] to budgets list.
   # Hint 1: For some movies the budget value is missing. For that you need use conditions and assigg a random value when it is missing.
   # ADD CODE HERE


# Closes the file
file.close()

# If you do not see the correct values printed, go back and fix the code above
print('***************names**************')
print()
print(names)
print()

# If you do not see the correct values printed, go back and fix the code above
print('**************scores**************')
print()
print(rottenTomatoesScores)
print()

# If you do not see the correct values printed, go back and fix the code above
print('***************genres*************')
print()
print(genres)
print()

# If you do not see the correct values printed, go back and fix the code above
print('****************budgets************')
print()
print(budgets)
print()

# Now that we have the data populated in the lists, let's perform some data analysis!

# Example: Print all the movie names with Rotten Tomatoes score higher than 90
moviesWithScoreAbove90 = [ (name,score) for (name,score) in zip(names,rottenTomatoesScores) if score > 90 ]
for (name,score) in moviesWithScoreAbove90:
  print(name + ': ' + str(score))

# Task 5: Print all the movie names with genres: 'Thriller' or 'Horror'
# ADD CODE HERE


# Task 6: Print all the movie names that have budgets between 100 and 200 inclusive
# ADD CODE HERE


# Task 7: Print the count of the movies with Genre: Comedy (i.e. How many movies are Comedy?)
# ADD CODE HERE  


# Task 8: Print all the movie names that have the letter 'p' in the name (Can be lower-case 'p' or upper-case 'P')
# ADD CODE HERE


# Task 9: Print all the movie names that start with letter 'G'
# ADD CODE HERE


# Task 10: Print all the movie names that have exactly 3 words in the name. (i.e. 'Shrek The Third' , 'The Simpson Movies')
# ADD CODE HERE


# Task 11: Print all the movie names order by Rotten Tomatoes score in descending order (i.e. highest score first)
# ADD CODE HERE