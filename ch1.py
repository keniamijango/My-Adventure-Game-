
import time
import globalvariables

def reparingfarm():
    print("You decided to repair your farm!")
    time.sleep(2)
    print("These are some of the repairs that your farm needs...")
    time.sleep(3)
    broken_structure = ["windmill", "fence", "chicken house", "barn"]
    print(broken_structure)
    chosen_structure = input("Select from the list above what you would like to repair: ")
    if chosen_structure.casefold() in broken_structure:
        list_of_tools = ["shovel", "hand fork", "axe", "crowbar"]
        print("These are some of the tools you may use", list_of_tools)
        tools_used = input("select a tool you want to use: ")
    else:
        print("that is not one of the choices, try again!")
        reparingfarm()

    if tools_used.casefold() == "shovel":
        print("You selected a shovel to help you repair the",chosen_structure,"! A shovel can help you dig and/or move granular material from one spot to another.")
        print("You did such a great job at reparing the", chosen_structure,"! You may now move on to the next chapter!")
    elif tools_used.casefold() == "hand fork":
        print("You selected a hand fork to repair the", chosen_structure,"this can be used to dig up weeds.")
        print("You did such a great job at reparing the", chosen_structure,
              "! You may now move on to the next chapter!")
    elif tools_used.casefold() == "axe":
        print("You selected an axe to repair the", chosen_structure,"this can be used to shape, split, and cut wood")
        print("You did such a great job at reparing the", chosen_structure,
              "! You may now move on to the next chapter!")
    elif tools_used.casefold() == "crowbar":
        print("You selected a crowbar to repair the", chosen_structure,"this can be used to pry objects apart and/or remove nails")
        print("You did such a great job at reparing the", chosen_structure,
              "! You may now move on to chapter 2!")
    else:
        print("That's not one of the choices, try again!!")
        reparingfarm()

# reparingfarm()

def futureidea():
    print("You decided to start the future idea section!")
    time.sleep(3)
    print("In this section you will choose between 3 ideas you are likely to do for your farm in the future.")
    time.sleep(3)
    idea_1 = "buying a new structure or barnhouse,"
    idea_2 = "caring for farm animals,"
    idea_3 = "creating a marketplace"

    print("You can choose between (idea 1)", idea_1, "(idea 2)" ,idea_2, "or (idea 3)", idea_3)
    time.sleep(2)
    future_idea_choice = input("Which idea sounds good to you for your future farm [idea 1, idea 2, idea 3]?:  ")

    if future_idea_choice == "idea 1":
        print("You selected", idea_1, "in the future you may choose from different structures to improve your farm or purchase a new barnhouse!")
        valid_choice = True
    elif future_idea_choice == "idea 2":
        print("You selected", idea_2, "caring for farm animals is such an important part of your farm!")
        valid_choice = True
    elif future_idea_choice == "idea 3":
        print("You selected", idea_3,"it is a great way to meet new people in town and earn money!")
    else:
        print("invalid option, try again!")
        futureidea()
    time.sleep(3)
    print("You did a great job at selecting an idea for your future farm, you may now move on to chapter 2!")

# futureidea()

def exploringtowncrops():
    print("You decided to start the exploring town crops section!")
    time.sleep(3)
    print("Farms in your town are leading producers of soybeans, corn and swine. Many farmers "
          "grow and raise wheat, oats, hay, fruits, vegetables and many other crops")
    time.sleep(3)
    invalid_option = True
    while invalid_option == True:
        player_choice = input("Would you like to choose the kind of crops to grown in your farm [yes,no]?: ")
        if player_choice == "yes":
            invalid_option = False
            print("This is a list of crops you may choose to grow")
            crops_list = ["wheat", "soybeans", "corn", "fruits", "vegetables"]
            print(crops_list)
            crops_chosen = input("From the list above choose what kind of crops you would like to grow?: ")
            if crops_chosen in crops_list:
                print("Great choice!")
                print("You have completed the exploring town crops section, you may now move on to chapter 2!")
            else:
                print("Invalid option, try again!")
                exploringtowncrops()

        elif player_choice == "no":
            invalid_option = False
            print("Looks like you don't want to explore town crops, you are now going to tranfer to the future idea section...")
            futureidea()
        else:
            print("Invalid option, try again!")
            invalid_option = True

# exploringtowncrops()

def main():

    print("Let's begin chapter 1 {}!".format(globalvariables.charactername))
    time.sleep(2)
    print("The new farmer in town just bought some land to start growing crops, help them get adjusted to their land")
    print("{} arrives to their new farm which is in awful conditions".format(globalvariables.charactername))
    time.sleep(4)

    print("To start off, you have three options, [1] to start reparing your farm, [2] to start future ideas, or [3]"
          " to start exploring in town")
    time.sleep(3)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        return reparingfarm()
    elif choice == 2:
        return futureidea()
    elif choice == 3:
        return exploringtowncrops()
    else:
        print("Let's try this again...to start off, you have three options, [1] to start reparing your farm, [2] to start future ideas, or [3]"
          " to start exploring in town")
        time.sleep(3)
        choice = int(input("Enter your choice: "))

    globalvariables.ch1_success = True

if __name__ == "__main__":
    main()



