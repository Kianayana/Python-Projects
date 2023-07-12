class Donut:
    def __init__(self):
        #this is a protected variable
        self._Tonutvar = "Toppings"
        #this is a private variable
        self.__Rinutvar = "Rise Type"
        print(self._Tonutvar,"\n")
        print (self.__Rinutvar,"\n")
              

#the code below access the protected and private variables
obj = Donut()
obj._Tonutvar = 'Maple Bacon\n'
obj.__Rinutvar = "Yeast"
print(obj._Tonutvar)
print (obj.__Rinutvar)
print ( "This donut is a ",obj.__Rinutvar, "donut with a ", obj._Tonutvar, "topping.")
