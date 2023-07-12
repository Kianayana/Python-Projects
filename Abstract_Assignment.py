from abc import ABC, abstractmethod
#this parent 
class Food(ABC):
    def types(self, example):
        print("There are a few types of diet that are most common in the animal kingdom:",example, "\n")
        #I am passing the argument below because I only want the method in carnivore to print
    @abstractmethod 
    def specialty(self, example):
            pass
#this cild class will show what type of food a carnivore will eat      
class carnivore(Food):
    def specialty(self, example):
        print('Carnivores like to only eat meat such as {}.'.format(example))

#this will print out strings by using abstraction to use the same method in different ways for different classes
obj = carnivore()
obj.types("(vvv Read Below vvv)")
obj.specialty("raw meat")

          
        
