def gVariables():

    class character:

        def __init__(self, name, gender, age):
            self.name = name
            self.gender = gender
            self.age = age

        def get_name(self):
            return self.name

        def get_gender(self):
            return self.gender

        def get_age(self):
            return self.age

        def fullcharacter(self):
            return self.name + ' ' + self.gender + ' ' + str(self.age)

    global playername
    global charactername
    global charactergender
    global characterage
    global mycharacter

    playername = "Player"  # Default player name
    charactername = "New character"  # Default character name
    charactergender = "Boy,Girl"  # Default character gender
    characterage = "18"  # Default character age

    mycharacter = character(charactername, charactergender, characterage)

def gvars():

    global ch1_success
    global ch2_success
    global ch3_success
    global ch4_success
    global ch5_success

    ch1_success = True
    ch2_success = True
    ch3_success = True
    ch4_success = True
    ch5_success = True

if __name__=="__main__":
    main()