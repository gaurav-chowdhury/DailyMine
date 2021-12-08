import os
import time

parentDirectory = os.getcwd()
def changeDirectory(changeTo):
    """A function for switching path of the python interpreter between various directories

    Args:
        changeTo (str): Name of the directory to which the path of the python interpreter has to be changed

    Returns:
        None: Returns nothing
    """
    if changeTo is None:
        os.chdir(parentDirectory)
    else:
        os.chdir(f"{parentDirectory}\{changeTo}")
    return None 

def workFiles(fileName, openMode, content):
    """A function for reading / writing to text files

    Args:
        fileName (str): Name of the file to be opened and modified / used
        openMode (str): Mode in which the file has to be opened 
        content (str): Content to be added to the opened file

    Returns:
        str / None: Returns the file's contents when reading files / Returns nothing when writing to the file
    """
    with open(fileName, openMode) as f:
        if content == None:
            content = f.readlines()
            return content
        else:
            f.write(f"{content}\n")
            return None

def currentTime():
    """A function which returns the time at which it is run

    Returns:
        str: Returns the time at which the function is run
    """
    return time.ctime(time.time())

def removeIds(removeId, allIds):
    """Removes the statement with the same time stamp as the entered time stamp from the text file

    Args:
        removeId (str): Time stamp of the statement to be removed
        allIds (list): List of statements in the text file to be modified

    Returns:
        list: Returns the list of all statements after removing the statement with the same time stamp as the entered time stamp from the text file
    """
    for id in allIds:
        if removeId in id:
            allIds.remove(id)
    return allIds


if __name__ == "__main__":
    pass

