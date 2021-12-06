import os
import time

def logInfo(action, logLocation):
    os.chdir(logLocation)
    timeStamp = time.ctime(time.time())
    with open("logs.txt", "at") as f:
        f.write(f"[{timeStamp}]: {action}\n")

def setReminder():
    pass

print("\nWelcome to DailyMine's user interaction window!")
parentDir = os.getcwd()
run_0 = True
while run_0:
    print("\n\tWhat would you like to do?")
    print("\tSet a reminder - 1")
    print("\tUse system organiser  - 2")
    print("\tUse time manager - 3")
    print("\tExit - 4")
    welcome = input("\nEnter the number corresponding to the option which you want to select: ")
    if welcome == "1":
        run_1 = True
        while run_1:
            print("\n\tWhat would you like to do?")
            print("\tSet a daily reminder - 1")
            print("\tSet a weekly reminder - 2")
            print("\tSet a monthly reminder - 3")
            print("\tSet a yearly reminder - 4")
            print("\tGo back - 5")
            reminder = input("\nEnter the number corresponding to the option which you want to select: ")
            if reminder == "1":
                run_2 = True 
                while run_2:
                    remTime = input("\nEnter the time of the day at which you want a daily reminder in 24 (00:00) hrs format: ")
                    remTune = input("Enter the path to the audio file which you want to use as the tune for reminder: ")
                    remTitle = input("Enter a title for the reminder: ")
                    remDescription = input("Enter a desciption for the reminder: ")
                    print("\nHow often do you want to get this reminder?")
                    print("\n\tEvery hour - 1")
                    print("\tEvery 30 minutes - 2")
                    print("\tEvery 15 minutes - 3")
                    print("\tEvery 10 minutes - 4")
                    print("\tEvery 5 minutes - 5")
                    print("\tOnly once at the set time - 6")
                    remFrequency = input("\nEnter the number corresponding to the option which you want to select: ")
                    if remFrequency == "1":
                        remFrequency = 60
                    elif remFrequency == "2":
                        remFrequency = 30
                    elif remFrequency == "3":
                        remFrequency = 15
                    elif remFrequency == "4":
                        remFrequency = 10
                    elif remFrequency == "5":
                        remFrequency = 5
                    elif remFrequency == "6":
                        remFrequency = 0
                    else: 
                        print("Invalid input!")
                        continue
                    # setReminder()
                    # print("")
                    # logInfo()
                    print("\nDo you want to add another daily reminder?")
                    print("\n\tYes - 1")
                    print("\tNo - 2")
                    continuation = input("\nEnter the number corresponding to the option which you want to select:")
                    if continuation == "1":
                        run_2 = True
                    elif continuation == "2":
                        run_2 = False 
                    else:
                        print("Invalid input!")
                        run_2 = False 
            elif reminder == "2":
                pass
            elif reminder == "3":
                pass
            elif reminder == "4":
                pass
            elif reminder == "5":
                run_1 = False 
            else:
                print("Invalid input!")
                continue 
    elif welcome == "2":
        run_1 = True
        while run_1:
            print("\nWhat would you like to do?")
            print("\n\tRemove duplicate files - 1")
            print("\tGroup similar files into a folder - 2")
            print("\tGo back - 3")
            sysOrganiser = input("\nEnter the number corresponding to the option which you want to select: ")
            if sysOrganiser == "1":
                path = input("\nEnter the path to the files: ")
                print()
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
                print(f"\nSkipped removing {skipped} files from the system")
                print(f"Removed {removed} files from the system ")
                logInfo(f"Skipped removing {skipped} files and removed {removed} files from the system", f"{parentDir}/System-Organiser")
                os.chdir(parentDir)

            elif sysOrganiser == "2":
                pass
            elif sysOrganiser == "3":
                run_1 = False
            else:
                print("Invalid input!")
                continue
    elif welcome == "3":
        pass
    elif welcome == "4":
        run_0 = False
    else:
        print("Invalid input!")
        continue
print("\nThank you for using this window!\n")




