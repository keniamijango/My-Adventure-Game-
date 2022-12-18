
import time
import globalvariables

def deliverfood():
    print("You decided to start the deliver food section! ")
    time.sleep(2)
    print("You may start your delivery business! You can deliver the food you make and earn money.")
    time.sleep(3)
    print("Note: You can promote your business by visiting other farms and give away food samples, "
          "or post on the local newspaper.")
    promoting_method = ["method 1", "method 2"]
    choice = input("What promoting method would you like to use? [method 1, method 2]: ")
    if choice.casefold() == "method 1":
        print("You have selected to visit other farms and give away food samples! Be ready to get lots of orders! ")
        print("You have completed the deliver food section, You have now earned lots of money and popularity in town"
              "...you have also reached the end of the game!")
    elif choice.casefold() == "method 2":
        print("You have selected to posts on the local newspaper! Be ready to get lots of orders!")
        print("You have completed the deliver food section, You have now earned lots of money and popularity in town"
              "...you have also reached the end of the game!")
    else:
        print("Invalid option, try again!")
        deliverfood()
# deliverfood()

def keepupwithtasks():
    print("You have decided to keep up with more tasks!")
    time.sleep(2)
    print("For this quick section, the task you will complete will be to feed your animals (if you have any) "
          "and grow crops in your farm.")
    time.sleep(4)
    answer = input("press y to feed animals and/or grow crops: ")
    if answer.casefold() == "y":
        print("feeding animals and/or growing crops...")
        time.sleep(4)
        print("You have completed the keeping with tasks section and have reached the end of the game!")
    else:
        print("Invalid option, try again!")
        keepupwithtasks()
# keepupwithtasks()

def foodstand():
    print("You decided to start the foodstand section!")
    time.sleep(2)
    print("In this section you will choose your design for your foodstand and the food you will be selling.")
    time.sleep(3)
    print("The first design you may choose from is a classic foodstand to sell common and easy food, "
          "the second idea would be a sweet treats foodstand design to sell sweet baked goods. ")
    time.sleep(4)
    design_choice = input("What design would you like to choose?[design 1, design 2]: ")
    if design_choice.casefold() == "design 1":
        print("You have chosen to do a classic foodstand design, the food you sell will be common food such as Hot dogs, "
              "Fries, and Hamburgers.")
        time.sleep(4)
        print("You have completed the foodstand section, You have now earned lots of money and popularity in town"
              "...you have also reached the end of the game!")
    elif design_choice.casefold() == "design 2":
        print("You have selected the sweet treats design, the food you will sell will be sugary-sweet baked goods such "
              "as Brownies, Cake pops, Donuts, and Cupcakes.")
        time.sleep(4)
        print("You have completed the foodstand section, You have now earned lots of money and popularity in town"
              "...you have also reached the end of the game!")
    else:
        print("Invalid option, try again!")
        foodstand()
# foodstand()

def main():

    print("Let's begin chapter 5 {}!".format(globalvariables.charactername))
    time.sleep(2)
    print("You’ve made it! Now satisfied with your new farm and have made many friendships and learned many farming "
          "skills, you decide to open a small food stand")
    print("{} creates more recipes from their grown crops and sells them to other farmers".format(globalvariables.charactername))
    time.sleep(4)

    print("In this chapter you have three options to choose from, [1] deliver food, "
              " [2] keep up with tasks, and [3] food stand")
    time.sleep(3)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        deliverfood()
    elif choice == 2:
        keepupwithtasks()
    elif choice == 3:
        foodstand()
    else:
        print("Let's try this again...In this chapter you have three options to choose from, [1] deliver food, "
              " [2] keep up with tasks, and [3] food stand")
        time.sleep(3)
        choice = int(input("Enter your choice: "))

    globalvariables.ch5_success = True

if __name__ == "__main__":
    main()


