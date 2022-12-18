import globalvariables  # Imports the global variables
import printcommon  # Imports functions from printcommon.py
import startgame  # Imports functions from startgame.py
import time
import ch1
import ch2
import ch3
import ch4
import ch5


def main():

    globalvariables.gVariables()
    globalvariables.gvars()
    startgame.start()
    printcommon.printglobalvars()

    ch1.main()
    if globalvariables.ch1_success:
        ch2.main()
        if globalvariables.ch2_success:
            ch3.main()
            if globalvariables.ch3_success:
                ch4.main()
                if globalvariables.ch4_success:
                    ch5.main()

if __name__ == '__main__':
    main()
