import time, sys # For typing effect
import colorama # For styling
import datetime, os # Required modules for DailyMine

def typeWriter(printLine):
    """A function for generating type-writing effect

    Args:
        printLine (str): Line to be typed out
    Returns:
        None: Returns nothing
    """
    for i in printLine:
        # sys.stdout.write doesn't create a new line for each print
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.01)
    return None

def workWithFiles(fileName, openMode, passedContent):
    """A function for reading / writing to text files

    Args:
        fileName (str): Name of the file to be opened and written to / read
        openMode (str): Mode in which the file has to be opened 
        passedContent (str): Content to be added to the opened file

    Returns:
        str / None: Returns the file's contents when reading files / Returns nothing when writing to the file
    """
    with open(fileName, openMode) as f:
        if passedContent == None:
            fileContent = f.readlines()
            return fileContent
        else:
            f.writelines(passedContent)
            return None

if __name__ == "__main__":
    colorama.init()
    print(colorama.Fore.GREEN, end="")  
    print(colorama.Style.BRIGHT, end="")
    homeDirectory = os.getcwd() # Contains path where DailyMine.py is stored
    # Introduction to DailyMine
    # print("")
    typeWriter("\nWelcome to DailyMine!")
    time.sleep(.8)
    showTutorial = "".join(workWithFiles("showTutorial.txt", "rt", None))
    if showTutorial == "0":
        typeWriter("\n\nKindly refer to the tutorial given below for learning how to use DailyMine:\n\n")
        time.sleep(.8)
        print(colorama.Fore.YELLOW, end="")
        print("".join(workWithFiles("tutorial.txt", "rt", None)))
        print(colorama.Fore.GREEN, end="") 
        time.sleep(.8)
        workWithFiles("showTutorial.txt", "wt", "1")
    else:
        typeWriter("\n\nLooks like this is not the first time that this program has been accessed on this device, so we skipped the tutorial to DailyMine.")
        time.sleep(.8)
        typeWriter("\n\nIn case you want to continue ahead, ENTER 0")
        time.sleep(.5)
        typeWriter("\nIn case you are a different user, or the same user but want to see the tutorial again, ENTER 1")
        time.sleep(.8)
        typeWriter("\n\n\tYour choice: ")
        showTutorialAgain = input()
        if showTutorialAgain == "0":
            time.sleep(.8)
            typeWriter("\nTutorial skipped successfully!\n")
        elif showTutorialAgain == "1":
            time.sleep(.8)
            typeWriter("\nHere is the tutorial:\n\n")
            time.sleep(.8)
            print(colorama.Fore.YELLOW, end="")
            print("".join(workWithFiles("tutorial.txt", "rt", None)))
            print(colorama.Fore.GREEN, end="") 
        else:
            time.sleep(.8)
            typeWriter("\nInvalid input! Showing the tutorial anyway:\n\n")
            time.sleep(.8)
            print(colorama.Fore.YELLOW, end="")
            print("".join(workWithFiles("tutorial.txt", "rt", None)))
            print(colorama.Fore.GREEN, end="") 
    time.sleep(.8)
    typeWriter("\nTo continue with the program, PRESS Enter key")
    proceed = input()
    time.sleep(.8)
    typeWriter("\nNow that you have learnt how to use the program, let's continue with actually using it's functions:")
    # Main Program starts here
    while True:
        # Reorganize your system
        try:
            time.sleep(.8)
            typeWriter("\n\n\tEnter the path to the target Directory: ")
            targetDirectory = input()
            os.chdir(targetDirectory)
        except:
            time.sleep(.8)
            typeWriter("\nInvalid input! Enter a valid path")
            continue
        while True:
            directoryFiles = os.listdir() 
            time.sleep(.8)  
            typeWriter("\nHow would you like to reorganize files in the directory?")
            time.sleep(.8)
            typeWriter("\n\nTo delete duplicate files, ENTER 0")
            time.sleep(.5)
            typeWriter("\nTo filter through files, ENTER 1 ")
            time.sleep(.5)
            typeWriter("\nTo rename all files using similar keyword, ENTER 2")
            time.sleep(.5)
            typeWriter("\nTo exit this block, ENTER 3")
            time.sleep(.8)
            typeWriter("\n\n\tYour choice: ")
            reorganizeDirectory = input()
            # Delete duplicate files
            if reorganizeDirectory == "0":
                time.sleep(.8)
                typeWriter("\nRemoving duplicate files from the folder...")
                crossCheck = []
                for directoryFile in directoryFiles:
                    try:
                        fileContents = workWithFiles(directoryFile, "rb", None)
                        if fileContents not in crossCheck:
                            crossCheck.append(fileContents)
                        else:
                            os.remove(directoryFile)
                    except:
                        time.sleep(.8)
                        typeWriter(f"\n\nCould not access {directoryFile}, skipping the file")
                time.sleep(.8)
                typeWriter("\n\nSuccessfully removed all duplicate files from the folder\n")
            # Filter through files
            elif reorganizeDirectory == "1":
                while True:
                    time.sleep(.8)
                    typeWriter("\nSelect a filter criteria: ")
                    time.sleep(.8)
                    typeWriter("\n\nTo filter on the basis of date of creation, ENTER 0")
                    time.sleep(.5)
                    typeWriter("\nTo filter on the basis of a common keyword in file name / one file type, ENTER 1")
                    time.sleep(.5)
                    typeWriter("\nTo exit this block, ENTER 2")
                    time.sleep(.8)
                    typeWriter("\n\n\tYour Choice: ")
                    filterCriteria = input()
                    time.sleep(.8)
                    # Filter on the basis of date of creation
                    if filterCriteria == "0":
                        typeWriter("\n\tEnter the date of creation in YYYY-MM-DD format: ")
                        creationDate = input()
                        time.sleep(.8)
                        typeWriter("\nBeginning the filtering process...")
                        shiftTo = homeDirectory + "/" + creationDate
                        try:
                            os.mkdir(shiftTo)
                        except:
                            pass
                        for directoryFile in directoryFiles:
                            createdOn = str(datetime.datetime.fromtimestamp(os.stat(directoryFile).st_ctime))
                            if creationDate in createdOn:
                                os.rename(targetDirectory + "/" + directoryFile, shiftTo + "/" + directoryFile)
                        time.sleep(.8)
                        typeWriter(f"\n\nSucessfully filtered the files with the entered creation date to {shiftTo}\n")
                    # Filter on the basis of a common keyword in file name / one file type
                    elif filterCriteria == "1":
                        typeWriter("\n\tEnter the common keyword in file name / one file type: ")
                        commonKey = input()
                        time.sleep(.8)
                        typeWriter("\nBeginning the filtering process...")
                        shiftTo = homeDirectory + "/" + commonKey
                        try:
                            os.mkdir(shiftTo)
                        except:
                            pass
                        for directoryFile in directoryFiles:
                            if commonKey in directoryFile:
                                os.rename(targetDirectory + "/" + directoryFile, shiftTo + "/" + directoryFile) 
                        time.sleep(.8)
                        typeWriter(f"\n\nSucessfully filtered the files with the entered keyword / one file type to {shiftTo}\n")
                    elif filterCriteria == "2":
                        typeWriter("\nSuccessfully exitted this block\n")
                        break
                    else:
                        typeWriter("\nInvalid input! Rerunning the block...\n")
            # Rename all files using similar keyword
            elif reorganizeDirectory == "2":
                time.sleep(.8)
                typeWriter("\n\tEnter the similar keyword for renaming all files in this directory: ")
                similarKey = input()
                time.sleep(.8)
                typeWriter("\n\tEnter the file extension: ")
                extensionType = input()
                time.sleep(.8)
                typeWriter("\nBeginning the renaming process...")
                count = 1
                for directoryFile in directoryFiles:
                    os.rename(directoryFile, similarKey + " - " + str(count) + "." + extensionType)
                    count += 1
                time.sleep(.8)
                typeWriter("\n\nSuccessfully renamed all files using the given keyword and extension\n")
            elif reorganizeDirectory == "3":
                time.sleep(.8)
                typeWriter("\nSuccessfully exitted this block")
                break
            else:
                time.sleep(.8)
                typeWriter("\nInvalid input! Rerunning the block\n")
        time.sleep(.8)
        typeWriter("\n\n\tDo you want to continue using DailyMine (y/n)? ")
        continueRunning = input().lower()
        time.sleep(.8)
        # Confirming exit from DailyMine
        if continueRunning == "y":
            typeWriter("\nRerunning DailyMine as per user request...")
            continue
        elif continueRunning == "n":
            typeWriter("\nSuccessfully exitted, Thank you for using DailyMine!\n\n")
            break
        else:
            typeWriter("\nInvalid input! Rerunning DailyMine...")
