
#This is for an online music library. The parent class is an artist
class Artist:
    #initializing the class with arguements by using the dunder method
  def __init__(self, name, dob_creationyear, overall_genre):
    self.name = name
    self.dob_creationyear = dob_creationyear
    self.overall_genre = overall_genre

  def printname(self):
    print(self.name, self.dob_creationyear, self.overall_genre)

#This execute the print name method to show the artist information:

x = Artist('Ralph McGalph', 'March 13, 2021', 'pop, country')
x.printname()

# The first child class is an album
class Album(Artist):
    def __init__(self, name, dob_creationyear, overall_genre, name_a):
        super().__init__(name, dob_creationyear, overall_genre)
        self.name_a = 'SQRL BLUES'
        
    def name1(self):
        print("Name:", self.name, ";", "Creation Year:", self.dob_creationyear, ";", "Overal Genre:", self.overall_genre, ";", "Album Name", self.name_a, ".")
        

# The second child class is a song
class Song(Artist):
    def __init__(self, name, dob_creationyear, overall_genre):
        super().__init__(name, dob_creationyear, overall_genre)
        self.name_s = name_s

    def name2(self):
        print("Name:", self.name, ";", "Creation Year:", self.dob_creationyear, ";", "Overal Genre:", self.overall_genre, ";", "Album Name", self.name_s, ".")

c = Album('Ralph McGalph', 'March 13, 2021', 'pop, country', 'SQRL BLUES')
c.name1()
