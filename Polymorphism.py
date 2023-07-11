
#media will be the parent class since it is a broader term
class Media:
    name = "TBA"
    year = "DATE"
    medium = "TBA"
        

    def play(self):
        string = "Action! The amazing {}({}) can be watched on {}! ".format(self.name, self.year, self.medium)
        return string

#the first child class will display a tv show to show that it is a type of media
class TV_Show(Media):
    name = "Adventure Time"
    year = 2010
    medium = "cable or Hulu"

    def episodes(self):
        string = "Who doesn't love Finn and Jake?!\n"
        return string

#the second child class will display a movie to show that it is a type of media
class Movie(Media):
    name = "Hereditary"
    year = 2018
    medium = "OnDemand, Amazon Prime, or Max"

    def films(self):
        string = "Hopefully you don't get too scared..."
        return string

if __name__=="__main__":
    show = TV_Show()
    print(show.play())
    print(show.episodes())

    movie = Movie()
    print(movie.play())
    print(movie.films())
