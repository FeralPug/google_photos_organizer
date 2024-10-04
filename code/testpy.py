import os
import re

my_path = os.path.dirname(os.path.abspath(__file__))

print(my_path)

if(os.path.isdir("test_dir")):
    directory = os.fsencode("test_dir")
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
    print("false")
    
    
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