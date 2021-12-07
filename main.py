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
            common.workFiles("logs.txt", "at", f"[{common.currentTime()}]: Accessed logs.txt")
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
            pass 
        #Exit this block
        elif startChoice =="5":
            break 
        #Handles error and reruns the block when an illegal value is entered as input
        else:
            print("\nInvalid input!")
            continue
    print("\nThank you for using DailyMine!\n")



