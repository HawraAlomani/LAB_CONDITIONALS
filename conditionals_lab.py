# Create a variable for the movie.
my_movie = "Batman"

# Create a rating variable (int) 3 out 5.
rating: int= 3

# popularity score of type float equal 72.65
popularity: float= 72.65

#if statment
if rating >= 4 and popularity > 80:
    print("Highly recommended")
elif rating >= 3 and popularity > 70:
    print("I recommended it . It is good")
elif rating <= 2 and popularity > 60:
     print("You should check it out!")
elif rating <= 2 and popularity < 50:
    print("Don't watch it. It is a waste of time")
