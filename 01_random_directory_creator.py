from datetime import datetime, date, time, timedelta
from math import sqrt, trunc, floor, ceil
from random import randint, randrange, choice, shuffle
import os, os.path

def directory_count():
    dt = datetime.today()
    minute = dt.minute
    total_dir = trunc(sqrt(minute) + 15)
    return total_dir

def name_generator():
    date = datetime.today()
    dir_name = date.strftime("%m_%d_%y_") + str(randrange(10000,50000))
    #os.mkdir(dir_name)
    return dir_name

def directory_creator(name):
    os.mkdir(name)

def create():
    for x in range (1, directory_count()):
        directory_creator(name_generator())

# Change working directory to `parent_dir` or `create`
if("parent_dir" not in os.getcwd()):
    if os.path.exists("./parent_dir"):
        print("Changing working dir to parent_dir")
        os.chdir("parent_dir")
    else:
        os.mkdir(os.getcwd() + "./parent_dir")
        print("Changing working dir to parent_dir")
        os.chdir("parent_dir")
else:
    # so the code can run multiple times 
    # while directory not ending with 'parent_dir' move up the path ..\
    while "parent_dir" not in os.getcwd()[-11:]:
        # move up in dir to find 'parent_dir'
        os.chdir("..")
        print("moved up", os.getcwd())
        
# print the current working directory (should be "parent_dir")
print("The current working directory is:", os.getcwd())

# check for randoms_directory if not present, create new
if os.path.exists(os.getcwd() + "/randoms_directory") != True:
    os.mkdir("randoms_directory")

# change the current working directory to randoms_directory
print("Changing working dir to randoms_directory")
os.chdir("randoms_directory")
# print the current working directory (should be "randoms_dir")
print("The current working directory is:", os.getcwd())

# create directories inside "randoms_directory"
create()
    
# list the content of the current directory
print("Current directory content:", os.listdir())
