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
            hold = common.currentTime()
            print()
            print("".join(common.workFiles("learn.txt", "rt", None)))
            common.workFiles("logs.txt", "at", f"[{hold}]: Accessed learn.txt")
        #Set reminder(s)
        elif startChoice == "1":
            pass
        #Organise your system
        elif startChoice == "2":
            pass
        #Use time bank
        elif startChoice == "3":
            while True:
                print("\nWhat would you like to do with time bank?")
                print("\n\tCheck available services - 0")
                print("\tModify services - 1")
                print("\tDeposit time - 2")
                print("\tWithdraw time - 3")
                print("\tGo back - 4")
                timeBankChoice = input("\nEnter the number corresponding to the option which you want to select: ")
                #Check available services
                if timeBankChoice == "0":
                    hold = common.currentTime()
                    print("\nFollowing are the available services:\n")
                    common.changeDirectory("time-bank")
                    print("".join(common.workFiles("services.txt", "rt", None)))
                    common.changeDirectory(None)
                    common.workFiles("logs.txt", "at", f"[{hold}]: Read and printed services.txt from time bank")
                #Modify services
                elif timeBankChoice == "1":
                    while True:
                        print("\nHow would you like to modify time bank services?")
                        print("\n\tAdd a service - 0")
                        print("\tRemove a service by time stamp - 1")
                        print("\tRemove all services - 2")
                        print("\tGo back - 3")
                        modifyTimeBankServices = input("\nEnter the number corresponding to the option which you want to select: ")
                        #Add a service
                        if modifyTimeBankServices == "0":
                            addService = input("\nEnter the service you wish to add followed by the time it costs in (service - hh:mm:ss) format: ")
                            confirmation = input("\nAre you sure that you want to do this(y/n)? ")
                            if confirmation == "y" or confirmation == "Y":
                                hold = common.currentTime()
                                common.changeDirectory("time-bank")
                                common.workFiles("services.txt", "at", f"[{hold}]: {addService}")
                                common.changeDirectory(None)
                                print("\nSuccessfully added the service to time bank's available services")
                                common.workFiles("logs.txt", "at", f"[{hold}]: Added a new service to services.txt from time bank")
                            elif confirmation == "n" or confirmation == "N":
                                print("\nRequest aborted")
                            else:
                                print("\nInvalid input! Request aborted")
                        #Remove a service by time stamp
                        elif modifyTimeBankServices == "1":
                            removeThisId = input("\nEnter the time stamp for that particular service which you wish to delete from time bank's services: ")
                            common.changeDirectory("time-bank")
                            allIds = common.workFiles("services.txt", "rt", None)
                            finalIds = common.removeIds(removeThisId, allIds)
                            confirmation = input("\nAre you sure that you want to do this(y/n)? ")
                            if confirmation == "y" or confirmation == "Y":
                                hold = common.currentTime()
                                common.workFiles("services.txt", "wt", "".join(finalIds))
                                common.changeDirectory(None)
                                print("\nSuccessfully deleted the record with that time stamp from time bank's services")
                                common.workFiles("logs.txt", "at", f"[{hold}]: Deleted record with the time stamp {removeThisId} from time bank's services.txt")
                            elif confirmation == "n" or confirmation == "N":
                                print("\nRequest aborted")
                            else:
                                print("\nInvalid input! Request aborted")
                        #Remove all services
                        elif modifyTimeBankServices == "2":
                            confirmation = input("\nAre you sure that you want to do this(y/n)? ")
                            if confirmation == "y" or confirmation == "Y":
                                hold = common.currentTime()
                                common.changeDirectory("time-bank")
                                common.workFiles("services.txt", "wt", "")
                                common.changeDirectory(None)
                                print("\nSuccessfully deleted all services from time bank's services")
                                common.workFiles("logs.txt", "at", f"[{hold}]: Deleted all services from services.txt from time bank")
                            elif confirmation == "n" or confirmation == "N":
                                print("\nRequest aborted")
                            else:
                                print("\nInvalid input! Request aborted")
                        #Exit this block
                        elif modifyTimeBankServices == "3":
                            break
                        #Handles error and reruns the block when an illegal value is entered as input
                        else:
                            print("\nInvalid input!")
                            continue
                #Deposit time
                elif timeBankChoice == "2":
                    pass 
                #Withdraw time
                elif timeBankChoice == "3":
                    pass
                #Exit this block
                elif timeBankChoice == "4":
                    break 
                #Handles error and reruns the block when an illegal value is entered as input
                else:
                    print("\nInvalid input!")
                    continue
        #Access logs
        elif startChoice == "4":
            while True:
                print("\nWhat would you like to do with logs?")
                print("\n\tCheck logs - 0")
                print("\tDelete record by time stamp - 1")
                print("\tDelete all records - 2")
                print("\tGo back - 3")
                logAcessChoice = input("\nEnter the number corresponding to the option which you want to select: ")
                #Check logs
                if logAcessChoice == "0":
                    hold = common.currentTime()
                    print("\nFollowing are the log records:\n")
                    print("".join(common.workFiles("logs.txt", "rt", None)))
                    common.workFiles("logs.txt", "at", f"[{hold}]: Read and printed logs.txt")
                #Delete record by time stamp
                elif logAcessChoice == "1":
                    removeThisId = input("\nEnter the time stamp for that particular log which you wish to delete: ")
                    allIds = common.workFiles("logs.txt", "rt", None)
                    finalIds = common.removeIds(removeThisId, allIds)
                    confirmation = input("\nAre you sure that you want to do this(y/n)? ")
                    if confirmation == "y" or confirmation == "Y":
                        hold = common.currentTime()
                        common.workFiles("logs.txt", "wt", "".join(finalIds))
                        print("Successfully deleted the record with that time stamp from logs")
                        common.workFiles("logs.txt", "at", f"[{hold}]: Deleted record with the time stamp {removeThisId} from logs.txt")
                    elif confirmation == "n" or confirmation == "N":
                        print("\nRequest aborted")
                    else:
                        print("\nInvalid input! Request aborted")
                #Delete all records
                elif logAcessChoice == "2":
                    confirmation = input("\nAre you sure that you want to do this(y/n)? ")
                    if confirmation == "y" or confirmation == "Y":
                        hold = common.currentTime()
                        common.workFiles("logs.txt", "wt", "")
                        print("\nSuccessfully deleted all records from logs")
                        common.workFiles("logs.txt", "at", f"[{hold}]: Deleted all records from logs.txt")
                    elif confirmation == "n" or confirmation == "N":
                        print("\nRequest aborted")
                    else:
                        print("\nInvalid input! Request aborted")
                #Exit this block
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



