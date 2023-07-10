#This is for an online music library. The parent class is an artist
class Artist:
    name = 'Gigi Luigi'
    dob_creationyear = 'October 1, 2013'
    overall_genre = 'lo-fi, rock'

    #initializing the class with arguements by using the dunder method
    def __init__(self, name, dob_creationyear, overall_genre):
        self.name = name
        self.dob_creationyear = dob_creationyear
        self.overall_genre = overall_genre
new_artist = Artist('Ralph McGalph', 'March 13, 2021', 'pop, country')
        


# The first child class is an album
class Album(Artist):
    name = 'SQRL BLUES'
    no_of_songs = 7
    no_of_singles = 2
    no_of_plays = 3,386,292
    genre = 'lo-fi'

# The second child class is a song
class Song(Artist):
    name = 'Peanut  Tease'
    single = 'no'
    no_of_plays = 1,490,363 
    genre = 'lo-fi'

print(new_artist)

    
