import globalvariables


def printglobalvars():
    print("Welcome to my adventure game {}!".format(globalvariables.playername))
    print("Your character's name is {}!".format(globalvariables.charactername))
    print("Your character is a {}".format(globalvariables.charactergender))
    print("Your character is {} years old!".format(globalvariables.characterage))