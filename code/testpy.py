import os
import re
import shutil
import datetime



DEST_DIR = "script_output"
TARGET_DIR = "test_dir"

def proc_dir(dirPath):
    if(os.path.isdir(dirPath)):
        directory = os.fsencode(dirPath)
        for file in os.listdir(directory):
            proc_file(file, dirPath)
            
def proc_file(file, dirPath):
    fileName = os.fsdecode(file)
    fullPath = os.path.join(dirPath, fileName)
    if(os.path.isdir(fullPath)):
        proc_dir(fullPath)
    elif(is_image_or_video(fileName)):
        fileDate = get_date_from_file_name(fileName)
        #if(fileDate == null):
            #handle no date
        #else:
            #handle date
        
        
def is_image_or_video(fileName) -> bool:
    if(fileName.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4'))):
        return True
    else:
        return False
        
def get_date_from_file_name(fileName) -> datetime.date:
    #matches any digit 1 or more times in file name and returns a list of all matches
    nums = re.findall(r'\d+', fileName)
    output = null
    if(len(nums != 0)):
        for n in nums:
            text = str(n)
            if(len(text) == 8):
                year = int(text[0:5])
                month = int(text[5:7])
                day = int(text[7:])
                if(validate_date(year, month, day)):
                    return datetime.date(year, month, day)
                
    return output
    
def validate_date(year, month, day) -> bool:
    if(year >= datetime.MINYEAR and year <= datetime.MAXYEAR):
        if(month >= 1 and month <= 12):
            if(day >= 1 and day <= 31):
                return True
    return False
    
def check_and_create_dir(path):
    if(not os.path.exists(path)):
        os.makedirs(path)
        
#def copy_file(src, dst):

# START OF SCRIPT **************************************************************************************************

#get running script path
print("Running in path: " + os.path.dirname(os.path.abspath(__file__)))

check_and_create_dir(DEST_DIR)

if(os.path.isdir(TARGET_DIR)):
    directory = os.fsencode(TARGET_DIR)
    for file in os.listdir(directory):
        fileName = os.fsdecode(file)
        if(os.path.isdir(os.path.join("test_dir", fileName))):
            print(fileName + " is directory")
        else:
            if(fileName.lower().endswith(('.jpg', '.jpeg', '.png'))):
                print(fileName + " is a image file")
                #matches any digit 1 or more times in file name and returns a list of all matches
                nums = re.findall(r'\d+', fileName)
                for n in nums:
                    if(len(str(n)) == 8):
                        print(n + " is possible data")
                    else:
                        print(n + " is not date")
            else:
                print(fileName + " is not a image file")
            
else:
    print("Script Target Directory Does Not Exist, Check Script!")
    



    
    
#for the loop logic    
#https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory

#is dir
#https://stackoverflow.com/questions/8933237/how-do-i-check-if-a-directory-exists-in-python

#current dir
#https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory

#get numbers from string
#https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python

#check file extension
#https://stackoverflow.com/questions/5899497/how-can-i-check-the-extension-of-a-file

#get month name from numbers
#https://stackoverflow.com/questions/6557553/get-month-name-from-number

#python re library and regex explination
#https://docs.python.org/3/howto/regex.html#regex-howto

#python copy files
#https://stackoverflow.com/questions/123198/how-to-copy-files

#make dir
#https://stackoverflow.com/questions/1274405/how-to-create-new-folder

#create file
#open(os.path.join(newDir, "test1.txt"), "w")