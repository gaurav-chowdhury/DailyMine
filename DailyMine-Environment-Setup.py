import os

#Installs required external modules
print("Installing required modules...")
modules = ["plyer", "schedule"]
for module in modules: 
    os.system(f"pip install {module}")
print("Finished installing required modules")

#Creates the directory structure for the program
print("Creating the required directory structure...")
parentDir = os.getcwd()
childDirs = {
    "Reminders" : ["Daily", "Weekly", "Monthly", "Yearly", "Logs"], 
    "Time-Management" : ["Available-Time", "Activities", "Logs"], 
    "System-Organiser" : ["Same-File-Type-Grouper", "Duplicate-Remover", "Logs"]
}
folders = childDirs.keys()
for folder in folders:
    path = f"{parentDir}/{folder}"
    os.mkdir(path)
    os.chdir(path)
    files = childDirs[folder]
    for f in files:
        f = open(f"{f}.txt", "xt")
        f.close()
    os.chdir(parentDir)
print("Finished creating the required directory structure")







