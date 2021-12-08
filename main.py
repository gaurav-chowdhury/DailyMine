# import os
# import time

# def logInfo(action, logLocation):
#     os.chdir(logLocation)
#     timeStamp = time.ctime(time.time())
#     with open("logs.txt", "at") as f:
#         f.write(f"[{timeStamp}]: {action}\n")

# def setReminder(action, remLocation, remFile):
#     os.chdir(remLocation)
#     with open(remFile, "at") as f:
#         f.write(f"{action}\n")

# print("\nWelcome to DailyMine's user interaction window!")
# parentDir = os.getcwd()
# run_0 = True
# while run_0:
#     print("\n\tWhat would you like to do?")
#     print("\tSet a reminder - 1")
#     print("\tUse system organiser  - 2")
#     print("\tUse time manager - 3")
#     print("\tExit - 4")
#     welcome = input("\nEnter the number corresponding to the option which you want to select: ")
#     if welcome == "1":
#         run_1 = True
#         while run_1:
#             print("\n\tWhat would you like to do?")
#             print("\tSet a daily reminder - 1")
#             print("\tSet a weekly reminder - 2")
#             print("\tSet a monthly reminder - 3")
#             print("\tSet a yearly reminder - 4")
#             print("\tGo back - 5")
#             reminder = input("\nEnter the number corresponding to the option which you want to select: ")
#             if reminder == "1":
#                 run_2 = True 
#                 while run_2:
#                     remTime = input("\nEnter the time of the day at which you want a daily reminder in 24 (00:00) hrs format: ")
#                     remTune = input("Enter the path to the audio file which you want to use as the tune for reminder: ")
#                     remTitle = input("Enter a title for the reminder: ")
#                     remDescription = input("Enter a desciption for the reminder: ")
#                     print("\nHow often do you want to get this reminder?")
#                     print("\n\tEvery hour - 1")
#                     print("\tEvery 30 minutes - 2")
#                     print("\tEvery 15 minutes - 3")
#                     print("\tEvery 10 minutes - 4")
#                     print("\tEvery 5 minutes - 5")
#                     print("\tOnly once at the set time - 6")
#                     remFrequency = input("\nEnter the number corresponding to the option which you want to select: ")
#                     if remFrequency == "1":
#                         remFrequency = 60
#                     elif remFrequency == "2":
#                         remFrequency = 30
#                     elif remFrequency == "3":
#                         remFrequency = 15
#                     elif remFrequency == "4":
#                         remFrequency = 10
#                     elif remFrequency == "5":
#                         remFrequency = 5
#                     elif remFrequency == "6":
#                         remFrequency = 0
#                     else: 
#                         print("Invalid input!")
#                         continue        
#                     action = f"{remTime} {remTune} {remTitle} {remDescription} {remFrequency}"
#                     setReminder(action, f"{parentDir}/Reminders", "Daily.txt")
#                     os.chdir(parentDir)
#                     print("\nThe reminder has been set succesfully!")
#                     logInfo(f"Set a daily reminder for {remTime} hrs", f"{parentDir}/Reminders")
#                     print("\nDo you want to add another daily reminder?")
#                     print("\n\tYes - 1")
#                     print("\tNo - 2")
#                     continuation = input("\nEnter the number corresponding to the option which you want to select:")
#                     if continuation == "1":
#                         run_2 = True
#                     elif continuation == "2":
#                         run_2 = False 
#                     else:
#                         print("Invalid input!")
#                         run_2 = False 
#             elif reminder == "2":
#                 pass
#             elif reminder == "3":
#                 pass
#             elif reminder == "4":
#                 pass
#             elif reminder == "5":
#                 run_1 = False 
#             else:
#                 print("Invalid input!")
#                 continue 
#     elif welcome == "2":
#         run_1 = True
#         while run_1:
#             print("\nWhat would you like to do?")
#             print("\n\tRemove duplicate files - 1")
#             print("\tGroup similar files into a folder - 2")
#             print("\tGo back - 3")
#             sysOrganiser = input("\nEnter the number corresponding to the option which you want to select: ")
#             if sysOrganiser == "1":
#                 path = input("\nEnter the path to the files: ")
#                 print()
#                 os.chdir(path)
#                 fileExists = []
#                 skipped = removed = 0
#                 dirFiles = os.listdir()
#                 for dirFile in dirFiles:
#                     with open(dirFile, 'rb') as f:
#                         content = f.read()
#                     if content not in fileExists:
#                         fileExists.append(content)
#                         print(f"Skipped removing {dirFile} from the system")
#                         skipped += 1
#                     else:
#                         os.remove(dirFile)
#                         print(f"Removed {dirFile} from the system")
#                         removed += 1 
#                 print(f"\nSkipped removing {skipped} files from the system")
#                 print(f"Removed {removed} files from the system ")
#                 logInfo(f"Skipped removing {skipped} files and removed {removed} files from the system", f"{parentDir}/System-Organiser")
#                 os.chdir(parentDir)

#             elif sysOrganiser == "2":
#                 pass
#             elif sysOrganiser == "3":
#                 run_1 = False
#             else:
#                 print("Invalid input!")
#                 continue
#     elif welcome == "3":
#         pass
#     elif welcome == "4":
#         run_0 = False
#     else:
#         print("Invalid input!")
#         continue
# print("\nThank you for using this window!\n")

import common 

if __name__ == "__main__":
    print("\nWelcome to DailyMine!")
    #Main program starts here
    while True:
        print("\nWhat would you like to do?")
        print("\n\tLearn how to use DailyMine - 0")
        print("\tSet reminder(s) - 1")
        print("\tOrganise your system - 2")
        print("\tUse time bank - 3")
        print("\tAccess logs - 4")
        print("\tExit - 5")
        startChoice = input("\nEnter the number corresponding to the option which you want to select: ")
        #Learn how to use the program
        if startChoice == "0":
            common.workFiles("logs.txt", "at", f"[{common.currentTime()}]: Accessed learn.txt")
            print()
            print("".join(common.workFiles("learn.txt", "rt", None)))
        #Set reminder(s)
        elif startChoice =="1":
            pass
        #Organise your system
        elif startChoice =="2":
            pass
        #Use time bank
        elif startChoice =="3":
            pass
        #Access logs
        elif startChoice == "4":
            while True:
                print("\nWhat would you like to do with logs?")
                print("\n\tCheck logs - 0")
                print("\tDelete record(s) by time stamp - 1")
                print("\tDelete all records - 2")
                print("\tGo back - 3")
                logAcessChoice = input("\nEnter the number corresponding to the option which you want to select: ")
                #Check logs
                if logAcessChoice == "0":
                    hold = common.currentTime()
                    print("\nFollowing are the log records:\n")
                    print("".join(common.workFiles("logs.txt", "rt", None)))
                    common.workFiles("logs.txt", "at", f"[{hold}]: Read and printed logs.txt")
                #Delete record(s) by time stamp
                elif logAcessChoice == "1":
                    pass
                #Delete all records
                elif logAcessChoice == "2":
                    hold = common.currentTime()
                    common.workFiles("logs.txt", "wt", "")
                    print("\nDeleted all records from logs")
                    common.workFiles("logs.txt", "at", f"[{hold}]: Deleted all records from logs.txt")
                #Exits this block
                elif logAcessChoice == "3":
                    break 
                #Handles error and reruns the block when an illegal value is entered as input
                else:
                    print("\nInvalid input!")
                    continue
        #Exit this block
        elif startChoice =="5":
            break 
        #Handles error and reruns the block when an illegal value is entered as input
        else:
            print("\nInvalid input!")
            continue
    print("\nThank you for using DailyMine!\n")



