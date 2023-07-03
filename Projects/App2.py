import App


def print_App2():
    name = (__name__)
    return name

if __name__ == "__main__":
    #The following calling code from within this script
    print("I am running code from {}".format(print_App2()))

    #The following is calling code frm the import app.py
    print("I am running code from {}".format(App.print_App()))
