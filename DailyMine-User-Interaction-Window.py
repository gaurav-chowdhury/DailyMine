import os
import time

def logInfo(action, logLocation):
    os.chdir(logLocation)
    #complete the function - add time stamp and action 




print("Welcome to DailyMine's user interaction window!")
parentDir = os.getcwd()
run_0 = True
while run_0:
    print("What would you like to do?")
    print("Set a reminder - 1")
    print("Use system organiser  - 2")
    print("Use time manager - 3")
    print("Exit - 4")
    option_0 = input("Enter the number corresponding to the option which you want to select:")
    if option_0 == "1":
        pass
    elif option_0 == "2":
        run_1 = True
        while run_1:
            print("What would you like to do?")
            print("Remove duplicate files - 1")
            print("Group similar files into a folder - 2")
            print("Go Back - 3")
            option_1 = input("Enter the number corresponding to the option which you want to select:")
            if option_1 == "1":
                path = input("Enter the path to the files:")
                os.chdir(path)
                fileExists = []
                skipped = removed = 0
                dirFiles = os.listdir()
                for dirFile in dirFiles:
                    with open(dirFile, 'rb') as f:
                        content = f.read()
                    if content not in fileExists:
                        fileExists.append(content)
                        print(f"Skipped removing {dirFile} from the system")
                        skipped += 1
                    else:
                        os.remove(dirFile)
                        print(f"Removed {dirFile} from the system")
                        removed += 1 
                print(f"Skipped removing {skipped} files from the system")
                print(f"Removed {removed} files from the system ")
                logInfo(f"Skipped removing {skipped} files and removed {removed} files from the system", f"{parentDir}/System-Organiser")
                os.chdir(parentDir)

            elif option_1 == "2":
                pass
            elif option_1 == "3":
                run_1 = False
            else:
                print("Invalid input!")
                continue
    elif option_0 == "3":
        pass
    elif option_0 == "4":
        run_0 = False
    else:
        print("Invalid input!")
        continue
print("Thank you for using this window!")




