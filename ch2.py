
import time
import globalvariables
import ch1

def earnmoney():
    print("You decided to start the earn money section!")
    time.sleep(3)
    print("You may choose between 3 tasks to earn money.")
    time.sleep(2)
    print("Task 1 requires you to pick up broken pieces from structures in your farm, "
          "Task 2 requires you to help deliver orders from and to other farms, "
          "Task 3 requires you to feed other farm animals in local farms.")
    time.sleep(4)
    answer = input("Would you like to choose a task to earn money [yes,no]? "
                   "(Note: if you choose "
                   "no, you will be transfered to the previous chapter): ")
    if answer.casefold() == "yes" :
        print("Good choice! You decided to take on a task to earn money!")
        invalid_option = True
        while invalid_option == True:
            chosen_task = input("Choose the task you would like to take on [task 1, task 2, task 3]: ")
            if chosen_task.casefold() == "task 1":
                invalid_option = False
                print("You may go around your farm and pick up broken structure to make your farm look cleaner!")
                print("You have completed the exploring town crops section, you may now move on to chapter 3!")
            elif chosen_task.casefold() == "task 2":
                print("You may go around your town and deliver orders from and to other farms!")
                print("You have completed the exploring town crops section, you may now move on to chapter 3!")
                invalid_option = False
            elif chosen_task.casefold() == "task 3":
                print("You may go to other farms and help feed their farm animals!")
                print("You have completed the exploring town crops section, you may now move on to chapter 3!")
                invalid_option = False
            else:
                invalid_option = True
                print("Invalid option, try again!")

    elif answer.casefold() == "no" :
        print("transferring you to chapter 1...")
        ch1.main()
        main()
    else :
        print("Invalid option, try again!")
        earnmoney()
# earnmoney()

def meetinglocals():
    print("You decided to start the meeting locals section!")
    time.sleep(3)
    option_a = "hire help for the farm"
    option_b = "make friendships with the local farmers"
    print("You may choose between option a,", option_a,"or option b,",option_b)
    time.sleep(3)
    answer = input("What would you like to choose [option a, option b]?: ")
    if answer.casefold() == "option a":
        print("Hiring help will help improve your farm a lot!")
    elif answer.casefold() == "option b":
        print("Making frienships with local farmers will help you learn more about farming!")
        time.sleep(3)
    else:
        print("Invalid option, try again!")
        meetinglocals()

    print("You have completed the meeting locals section, you may now move on to chapter 3!")

# meetinglocals()

def growingcrops():
    print("You decided to start the growing crops section!")
    time.sleep(2)
    print("To grow crops you need to prepare a growing bed, prepare the plants you want to "
          "grow, and plant your seedlings")
    time.sleep(3)
    choice = input("Would you like to participate in the tutorial [yes,no]?(Note: if you "
                   "choose 'no' you will be transferred to choosing another action.): ")
    if choice.casefold() == "yes":
        print("participating in growing crops tutorial...")
        print("You have completed the growing crops section, you may now move on to chapter 3!")
    elif choice.casefold() == "no":
        print("back to choosing other actions...")
        main()
    else:
        print("Invalid option, try again!")
        growingcrops()

# growingcrops()

def main():

    globalvariables.ch1_success = True

    print("Let's begin chapter 2 {}!".format(globalvariables.charactername))
    time.sleep(2)
    print("You’ve made some great improvement to the farmland, now it’s time to start trading or selling with other farmers and hire some help!")
    print("{} grows vegetables and fruits".format(globalvariables.charactername))
    time.sleep(4)

    print("To start off, you have three options, [1] earn money, [2] meet locals, or [3]"
          " grow crops")
    time.sleep(3)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        earnmoney()
    elif choice == 2:
        meetinglocals()
    elif choice == 3:
        growingcrops()
    else:
        print("Let's try this again...to start off, you have three options, [1] earn money, [2] meet locals, or [3]"
          " grow crops")
        time.sleep(3)
        choice = int(input("Enter your choice: "))

    globalvariables.ch2_success = True

if __name__ == "__main__":
    main()







