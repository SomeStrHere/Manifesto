# Program to scroll a manifesto on the command line.
# V: 0.9.0

import sys
import time

from colorama import init
init()

from colorama import Fore, Back, Style


def clearConsole(wait) : #function to clear console on Linux or Windows
    """Clears console, with optional time delay.

    Will attempt to clear the console for Windows, should that fail it will attempt to clear the
    console for Linux.
    """

    # produces a delay based on the argument given to clearConsole()
    time.sleep(wait) 
    
    import os

    try :
       os.system('cls') #clears console on Windows

    except :
       os.system('clear') #clears console on Linux


def changeEnvironment() : 
    """Make changes to console environment"""

    # Use colorama (needs installing via CLI) to change Windows console
    # Moved code to import and initialize colorama outside of function so fore.RESET
    # can be used if an error occurs.

    print(Fore.GREEN)
    print(Back.BLACK)
    print(Style.BRIGHT)

    #COLORNAME can be :
    #BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    #RESET will reset the color to the default.

    return()
    
def cleanUp() :
    """Undo changes to console environment"""

    print(Fore.RESET)
    print(Back.RESET)
    print(Style.NORMAL)

def timeDelay(amount) :
    """Add a delay to code execution"""

    time.sleep(amount)


def readManifesto() : 
    """Open and read file manifesto.txt""" 

    READ = 'r'
    fileName = "manifesto.txt"
    linesList = []

    try :

        with open(fileName, READ) as file :
            for line in file :
                linesList = [(line)]

                # Iterate over list of lines in the manifesto file and print each line.
                for line in linesList :
                    print(line)
                    timeDelay(1.65)

    except FileNotFoundError :
            cleanUp()
            print('\nFile not found...')
            print('Please create file "manifesto.txt')
            print('Exiting program...')
            clearConsole(5)
            sys.exit()

    except : 
        cleanUp()
        print('\nSorry there was an error')
        print('Exiting program...')
        clearConsole(4)
        sys.exit()

    finally :
        cleanUp() # Ensures console text is returned to state before program execution began

    sys.exit()


def main() : 

    clearConsole(0)
    changeEnvironment()
    readManifesto()


if __name__ == "__main__" :
    main()

