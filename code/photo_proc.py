import os
import re
import shutil
import datetime
import calendar

DEST_DIR = "script_output"
TARGET_DIR = "test_dir"

OTHER_PHOTOS_DIR = "other"

def proc_dir(dirPath):
    if(os.path.isdir(dirPath)):
        directory = os.fsencode(dirPath)
        for file in os.listdir(directory):
            proc_file(file, dirPath)
    else:
        print("Directory at " + dirPath + " is not a directory!")
            
def proc_file(file, dirPath):
    fileName = os.fsdecode(file)
    fullPath = os.path.join(dirPath, fileName)
    if(os.path.isdir(fullPath)):
        proc_dir(fullPath)
    elif(is_image_or_video(fileName)):
        fileDate = get_date_from_file_name(fileName)
        if(fileDate == None):
            #handle no date
            print(fileName + " has no date associated")
            othersDir = os.path.join(DEST_DIR, OTHER_PHOTOS_DIR)
            check_and_create_dir(othersDir)
            outputFilePath = os.path.join(othersDir, fileName)
            if(check_if_file_exists(outputFilePath)):   
                newName = create_double_file_name(fileName)
                if(len(newName) != 0):
                    newOutputFilePath = os.path.join(othersDir, newName)
                    print("File already exists at " + outputFilePath + " Creating double at " + newOutputFilePath)
                    shutil.copy(fullPath, newOutputFilePath)  
                else:
                    print("File already exists at " + outputFilePath + " and has no extension, skipping")
            else:
                shutil.copy(fullPath, othersDir)          
        else:
            #handle date
            #check if year folder exists
            yearDir = os.path.join(DEST_DIR, str(fileDate.year))
            check_and_create_dir(yearDir)
            #check if month folder exists
            monthStr = calendar.month_name[fileDate.month]
            monthDir = os.path.join(yearDir, monthStr)
            check_and_create_dir(monthDir)
            #copy file
            outputFilePath = os.path.join(monthDir, fileName)
            if(check_if_file_exists(outputFilePath)):
                newName = create_double_file_name(fileName)
                if(len(newName) != 0):
                    newOutputFilePath = os.path.join(monthDir, newName)
                    print("File already exists at " + outputFilePath + " Creating double at " + newOutputFilePath)
                    shutil.copy(fullPath, newOutputFilePath) 
                else:
                    print("File already exists at " + outputFilePath + " and has no extension, skipping")
            else:
                shutil.copy(fullPath, monthDir)        
        
def is_image_or_video(fileName) -> bool:
    if(fileName.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4'))):
        return True
    else:
        return False
        
def get_date_from_file_name(fileName) -> datetime.date:
    #matches any digit 1 or more times in file name and returns a list of all matches
    nums = re.findall(r'\d+', fileName)
    output = None
    if(len(nums) != 0):
        for n in nums:
            text = str(n)
            if(len(text) == 8):
                year = int(text[0:4])
                month = int(text[4:6])
                day = int(text[6:])
                if(validate_date(year, month, day)):
                    return datetime.date(year, month, day)
                
    return output
    
def create_double_file_name(fileName) -> str:
    dotIndex = fileName.find('.')
    if(dotIndex >= 0):
        newName = fileName[:dotIndex]
        newName += "1"
        newName += fileName[dotIndex:]
        return newName
    else:
        return ""
    
def validate_date(year, month, day) -> bool:
    if(year >= datetime.MINYEAR and year <= datetime.MAXYEAR):
        if(month >= 1 and month <= 12):
            if(day >= 1 and day <= 31):
                return True
    return False
    
def check_and_create_dir(path):
    if(not os.path.exists(path)):
        print("Creating dir at " + path)
        os.makedirs(path)
        
def check_if_file_exists(path) -> bool:
    if(os.path.exists(path)):
        return True
    else:
        return False
        
#def copy_file(src, dst):

# START OF SCRIPT **************************************************************************************************

#get running script path
print("Running in path: " + os.path.dirname(os.path.abspath(__file__)))

check_and_create_dir(DEST_DIR)

if(os.path.isdir(TARGET_DIR)):
    proc_dir(TARGET_DIR)
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