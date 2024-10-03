import os

my_path = os.path.dirname(os.path.abspath(__file__))

print(my_path)

if(os.path.isdir("test_dir")):
    directory = os.fsencode("test_dir")
    for file in os.listdir(directory):
        fileName = os.fsdecode(file)
        if(os.path.isdir(os.path.join("test_dir", fileName))):
            print(fileName + " is directory")
        else:
            print(fileName + " is file")
else:
    print("false")
    
    
#for the loop logic    
#https://stackoverflow.com/questions/10377998/how-can-i-iterate-over-files-in-a-given-directory

#is dir
#https://stackoverflow.com/questions/8933237/how-do-i-check-if-a-directory-exists-in-python

#current dir
#https://stackoverflow.com/questions/3430372/how-do-i-get-the-full-path-of-the-current-files-directory