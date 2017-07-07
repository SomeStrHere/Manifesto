# Program to scroll a manifesto on the command line.
# V: 0.9.0

import sys

def clearConsole(wait) : #function to clear console on Linux or Windows
    """Clears console, with optional time delay.

    Will attempt to clear the console for Windows, should that fail it will attempt to clear the
    console for Linux.
    """

    import time
    time.sleep(wait) 
    # produces a delay based on the argument given to clearConsole()
    
    import os

    try :
       os.system('cls') #clears console on Windows

    except :
       os.system('clear') #clears console on Linux


def readManifesto() : 
    """Open and read file manifesto.txt""" 

    READ = 'r'
    fileName = "manifesto.txt"
    linesList = []

    try :

        with open(fileName, READ) as file :
            for line in file :
                linesList = [(line)]
                #print(linesList) #Print line used in initial testing

                # Iterate over list of lines in the manifesto file and print each line.
                for line in linesList :
                    print(line)

    except FileNotFoundError :
            print('\nFile not found...')
            print('Please create file "manifesto.txt')
            print('Exiting program...')
            clearConsole(5)
            sys.exit()

    except : 
        print('\nSorry there was an error')
        print('Exiting program...')
        clearConsole(4)
        sys.exit()


def main() : 

    clearConsole(0)
    readManifesto()

    # TO DO LIST
    # Slow down the speed of the scrolling text, ideally line by line
    # Change console text
    # Create a program exit function to ensure changes to console variables are reset to as before
    

if __name__ == "__main__" :
    main()

