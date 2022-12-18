import printcommon
import globalvariables
import time

def start():
    globalvariables.playername = input("Welcome! Please enter your name!: ")
    globalvariables.charactername = input("Choose a name for your character: ")
    globalvariables.charactergender = input("Select gender for your character[Girl/Boy]: ")
    globalvariables.characterage = int(input("What's your character's age?: "))

    globalvariables.mycharacter.name = globalvariables.charactername
    globalvariables.mycharacter.gender = globalvariables.charactergender
    globalvariables.mycharacter.age = globalvariables.characterage

    print("These are your character preferences:")
    print(globalvariables.mycharacter.get_name())
    print(globalvariables.mycharacter.get_gender())
    print(globalvariables.mycharacter.get_age())
    print(globalvariables.mycharacter.fullcharacter())

    begingame = input("Would you like to begin playing?[Yes/No]: ")

    beginplay = 0
    if begingame == "No" or begingame == "no":
        print("Why did you start this up, then?")
        beginplay = 0
        time.sleep(3)
        return (exit())  # Quits the game and closes the client.

    elif begingame == "Yes":
        print("Alright, let's begin!")
        time.sleep(3)
        beginplay = 1

    else:
        print("Weird way to spell 'Yes', but that's alright!")
        time.sleep(3)
        beginplay = 1
