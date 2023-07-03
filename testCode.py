

mySentence = 'loves the color'

color_list =['red','blue','green','pink','purple']

def color_function(name):
    lst = []
    for i in color_list:
        msg = "{} {} {}".format(name, mySentence, i)
        lst.append(msg)
    return lst


def gets_name():
    name = input('What is your name?')
    lst = color_function(name)
    for i in lst:
        print(i)


gets_name()

cars = ["Ford", "Volvo", "BMW"]
