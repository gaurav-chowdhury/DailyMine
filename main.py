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



