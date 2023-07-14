
#media will be the parent class since it is a broader term
class Media:
    name = "TBA"
    year = "DATE"
    medium = "TBA"
        

    def play(self):
        string = "Action! The amazing {}({}) can now be watched on {}!\n".format(self.name, self.year, self.medium)
        return string

#the first child class will display a tv show to show that it is a type of media
class TV_Show(Media):
    name = "Adventure Time"
    year = 2010
    medium = "cable or Hulu"

    def play(self):
        string = "Hint: This show highlights the unbreakable bond between a boy and his older brother. \n"
        return string

#the second child class will display a movie to show that it is a type of media
class Movie(Media):
    name = "Hereditary"
    year = 2018
    medium = "OnDemand, Amazon Prime, or Max"

    def play(self):
        string = "Hint: While popular at it's release for it's scare factor, this movie regained popularity at a later time for making fun of filters and photoshop.\n\nCan you guess what is new to watch?"
        return string

if __name__=="__main__":
    general = Media()
    print(general.play())

    show = TV_Show()
    print(show.play())

    movie = Movie()
    print(movie.play())
    
