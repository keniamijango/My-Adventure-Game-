
import time
import globalvariables
import ch3

def kitchenrecipe():
    print("You decided to start the kitchen recipe section! You will be taken to the towns recipe book.")
    time.sleep(3)
    print("loading towns recipe book...")
    time.sleep(2)
    recipe_choice = ["Baked tomato risotto(recipe 1)", "Beetroot, bean & feta salad(recipe2)"]
    print(recipe_choice)
    answer = input("You may choose between the two recipes above [recipe 1, recipe 2]:  ")
    if answer.casefold() == "recipe 1":
        print("You selected the baked tomato risotto recipe!")
        time.sleep(2)
        print("For this recipe you will need 1 onion, butter, 3 garlic cloves, risotto rice, cherry tomatos, cheese, "
              "and basil leaves")
        time.sleep(3)
        print("You are taken to collect items for your recipe...")
        time.sleep(2)
        print("You have collected all the items for the recipe, now you will participate in the tutorial!")
        print("participating in tutorial...")
        time.sleep(3)
        print("You have completed the kitchen recipe section, you may now move on to chapter 5!")
    elif answer.casefold() == "recipe 2":
        print("You selected the beetroot, bean & feta salad recipe!")
        time.sleep(2)
        print("For this recipe you will need 1 shallot, 1 garlic clove, fresh rosemary, beetroot, and feta cheese")
        time.sleep(3)
        print("You are taken to collect items for your recipe...")
        time.sleep(2)
        print("You have collected all the items for the recipe, now you will participate in the tutorial!")
        print("participating in tutorial...")
        time.sleep(3)
        print("You have completed the kitchen recipe section, you may now move on to chapter 5!")
    else:
        print("Invalid option, try again!")
        kitchenrecipe()
# kitchenrecipe()

def farmanimals():
    print("You decided to start the farm animal section!")
    time.sleep(2)
    print("Animals that are usually in farms are cows, chickens, pigs, and goats.")
    time.sleep(2)
    farm_animals = ["cows", "chickens", "pigs", "goats"]
    choice = input("Would you like to purchase animals for your farm? Note: if you don't have enough money you may enter"
                   " no and go back to chapter 3 to earn money.[yes, no]: ")
    if choice.casefold() == "yes":
        print("To purchase farm animals, you have to open the store menu and select your choice of animals")
        print("opening store menu and selecting your farm animal...")
        print(farm_animals)
        animal_choice = input("Select your choice of farm animal from the list above [cows, chickens, pigs, goats]: ")
        if animal_choice.casefold() in farm_animals:
            print("You selected", animal_choice, "!")
        else:
            print("Invalid option, try again!")
            farmanimals()
        print("You have completed the farm animal section, you may now move on to chapter 5!")
    elif choice.casefold() == "no":
        print("Transferring you back to chapter 3...")
        ch3.main()
        ch4.main()
    else:
        print("Invalid option, try again!")
        farmanimals()

# farmanimals()

def main():

    print("Let's begin chapter 4 {}!".format(globalvariables.charactername))
    time.sleep(2)
    print("You’re really close to creating your dream farm, there is just something missing…")
    print("{} unlocks farm animals, new skills, and buys more land".format(globalvariables.charactername))
    time.sleep(4)

    print("In this chapter you have two options to choose from, [1] kitchen recipe section, and [2] farm animal section")
    time.sleep(3)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        kitchenrecipe()
    elif choice == 2:
        farmanimals()
    else:
        print("Let's try this again...In this chapter you have two options to choose from, [1] kitchen recipe section, "
              "and [2] farm animal section")
        time.sleep(3)
        choice = int(input("Enter your choice: "))

    globalvariables.ch4_success = True

if __name__ == "__main__":
    main()


