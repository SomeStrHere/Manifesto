# Program to scroll a manifesto on the command line.
# V0.01

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
                #print(linesList)

                for line in linesList :
                    print(line)

    except FileNotFoundError :
            print('\nFile not found...')
            print('Please create file "manifesto.txt')
            # TODO

    except : 
        print('\nSorry there was an error')
        # TODO


def main() : 

    clearConsole(0)
    readManifesto()


if __name__ == "__main__" :
    main()

