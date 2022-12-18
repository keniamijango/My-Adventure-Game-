
import time
import globalvariables

def designandmenu():
    print("You decided to start the design and menu section!")
    time.sleep(2)
    print("The design and menu section has many designs to choose from for your farm, you may design your farmhouse, "
          "buy new equipment and furniture.")
    time.sleep(4)
    print("starting the design and menu tutorial...")
    time.sleep(3)
    print("In the design and menu section you may choose different types of color option, shapes, wallpapers, purchase "
          "furniture and many farm equipments.")
    time.sleep(4)
    print("Right now you may choose from 2 farm designs")
    time.sleep(2)
    print("A diverse design where you have many things going around your farm, or a more central desgin focused on "
          "a certain aspect of your farm")
    time.sleep(4)
    design_choice = input("Choose from the 2 designs above [diverse or central]?: ")
    if design_choice.casefold() == "diverse":
        print("You have chosen a diverse design for your farm!")
        print("You have completed the design and menu section, you may now move on to the next section of this chapter!")
    elif design_choice.casefold() == "central":
        print("You have chosen a central design for your farm!")
        print("You have completed the desgin and menu section, you may now move on to the next section of this chapter!")
    else:
        print("Invalid option, try again!")
        designandmenu()

# designandmenu()

def tasksection():
    print("To keep improving and leveling up your farm, you will have to take on "
          "tasks to earn money. ")
    time.sleep(3)
    tasks = ["organize other farms", "collect tools from your or other farms", "meet with more locals to learn "
                                                                     "about their farms"]
    task_num = ["task 1", "task 2", "task 3"]
    print(tasks)
    task_chosen = input("From the list above, choose a task to complete! [task 1, task 2, task 3]: ")
    if task_chosen.casefold() in task_num:
        print("Great job at completing a task, you just earned 50 coins!")
        print("You have completed the tasks section, you may now move on to chapter 4! ")
    else:
        print("Invalid option, try again!")
        tasksection()
# tasksection()

def main():

    print("Let's begin chapter 3 {}!".format(globalvariables.charactername))
    time.sleep(2)
    print("Your farm is looking good! Keep adding more of your own touch and decorations to your place.")
    print("{} unlocks more items on the store menu".format(globalvariables.charactername))
    time.sleep(4)

    print("In this chapter you have two options to choose from, [1] design and menu, and [2] tasks")
    time.sleep(3)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        designandmenu()
    elif choice == 2:
        tasksection()
    else:
        print("Let's try this again...In this chapter you have two options to choose from, [1] design and menu, "
              "and [2] tasks")
        time.sleep(3)
        choice = int(input("Enter your choice: "))

    globalvariables.ch3_success = True


if __name__ == "__main__":
    main()

