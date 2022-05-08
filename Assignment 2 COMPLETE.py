"""
Sophie Selk

"""
import csv

# Write remove_duplicates function to remove duplicates from an input list
def remove_duplicates(list):
    return set(list)
# Write display_counts function to display movie year counts from an input dictionary
def display_counts(d):
      # Print the names of the columns.

        print ("{:<10} {:<10}".format('Year', 'Count'))


      #Print the Year and count
        for key, value in d.items():

            print ("{:<10} {:<10}".format(key,value))

        

# Read movies_small.csv file
with open('movies_small.csv', 'r') as csv_file:
   csv_reader = csv.DictReader(csv_file)
   for row in csv_reader:
       (row['movieId'], row['title'],row['genres'])
       break
      
# Build year counts dictionary, allGenres list and allMovies dictionary from movie file

#Creating a info for counting years
year_total = {}
with open('movies_small.csv', 'r') as csv_file:
   csv_reader = csv.DictReader(csv_file)
   for row in csv_reader:
       if (row['title'] == ''):
          continue
       words = row['title'].split()[-1]
       year = words[1:-1]
       if year not in list(year_total.keys()):
           year_total[year] = 1
       else:
            year_total[year] = year_total[year]+1
            
#Making a list of allGenres
with open('movies_small.csv', 'r') as csv_file:
   csv_reader = csv.DictReader(csv_file)
   allGenre = []
   for row in csv_reader:
       genre_row =(row["genres"])
       allGenre.append(genre_row.split("|"))
#we are now flattening and sorting

allGenre = [x for list in allGenre for x in list]
allGenre = remove_duplicates(allGenre) # this is to get rid of dupilcates
allGenre = sorted(allGenre) # this is to sort into abc order

#Making allMovies dictonary with Movie as value and Id as key
with open('movies_small.csv', 'r') as csv_file:
   csv_reader = csv.DictReader(csv_file)
   allMovies = {}
   for row in csv_reader:
       key = (row["movieId"])
       allMovies[key] = row["title"]

## Part A: Display count of movies by year ###
display_counts(year_total)
### Part B: Output Movies with year by Genre Alphabetically to genre_movies.txt file ### 
fgenre = open("genre_movies.txt", "w+")
count = 0
#For loop to make sure we get every genre in Alphbetcal order then making the file and writing the genre on it
for x in allGenre:
    current_genre = allGenre[count]
    fgenre.write(current_genre+'\n')
    with open('movies_small.csv', 'r') as csv_file:
       csv_reader = csv.DictReader(csv_file)
       
       # this for loop is to get into each line from thr csv file yes yes very nice
       for row in csv_reader:
          genre_row =(row["genres"])    # this is to get the string from genre
          genre2 = genre_row.split("|") # to get each one into single genre form of a list
          
          #hey another for loop how cool but this one is to see if that movie in that row has this genre
          # then its going to write that movie title in the txt file
          for g in genre2:
              if current_genre in g:
                   title = str(row['title'])
                   fgenre.write(title+'\n')
    fgenre.write('\n')  
    count += 1
fgenre.close

## Part C: Get total rating points for each movie and write to movie_ratings.txt file ###
with open('ratings_small.csv', 'r') as csv_file:
   csv_reader = csv.DictReader(csv_file)
   rating_sum = {}
   for row in csv_reader:
        key = row['movieId']
        rating_sum[key] = rating_sum.get(key, 0) + float(row['rating'])
      

rating_file = open("movie_ratings.txt","w+")

for key in rating_sum:
    rating_file.write(allMovies[key]+','+ str(rating_sum[key])+'\n')



   