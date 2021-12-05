import os

#Installs required external modules
print()
modules = ["plyer", "schedule"]
for module in modules: 
    os.system(f"pip install {module}")

#Creates the directory structure for the program
parentDir = os.getcwd()
childDirs = {
    "Reminders" : ["Daily", "Weekly", "Monthly", "Yearly", "Logs"], 
    "Time-Management" : ["Available-Time", "Activities", "Logs"], 
    "System-Organiser" : ["Same-File-Type-Grouper", "Duplicate-Remover", "Logs"]
}
folders = childDirs.keys()
for folder in folders:
    path = os.path.join(parentDir, folder)
    os.mkdir(path)
    os.chdir(path)
    files = childDirs[folder]
    for f in files:
        f = open(f"{f}.txt", "xt")
        f.close()
    os.chdir(parentDir)
print()






