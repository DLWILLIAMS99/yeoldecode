#!/usr/bin/env python3

import shutil
import os
import time
import pathlib
from pathlib import Path
# asks for target location to create the new script.py

destpath = input("Where do you want your python script located? Please supply the absolute path.\n ")

# checking if already exists and will CD if true or MKDIR if false

if os.path.exists(destpath):
    os.chdir(destpath)

else: 
    os.mkdir(destpath)
    os.chdir(destpath)

print("You are currently in " + destpath)
time.sleep(3)
   
input_name = input("What is the name for the new python script?\n Do not include the file suffix. It will be appended automagically. ")

xname = input_name + (".py" )
# checking if file already exists

# if the file exists then it begins itterating the file name with a number until it does not match an existing file
if os.path.isfile(xname):
    expand = 1
    while True:
        expand += 1
        new_file_name = xname.split(".py")[0] + str(expand) + ".py"
        if os.path.isfile(new_file_name):
            continue
        else:
            xname = new_file_name
            break
# now checks if template exists and creates it if not 
pytemplate = ("/home/student/mycode/pythontemplate.py")
if os.path.exists(pytemplate):
    shutil.copy("/home/student/mycode/pythontemplate.py", "./" + xname ) 
    print("Your new python script template has been created for you.\n" + "It is called: " + xname + "\n and can be found in: " + destpath)
else:
    Path(pytemplate).touch()
# Open the file in append mode
    file = open(pytemplate, "a")
# Write to the file
    file.write('#!/usr/bin/env python3\n' + '"""A simple script to create a new python script with best practices prefilled at top and bottom\n' + 'Dan Williams | GitHub.com/DLWILLIAMS99"""\n' + '# standard library imports go here first (if any)\n' + '# import shutil\n' + '# import os\n' + 'def main():\n' + '    """called at runtime"""\n' + '#   first stuff goes here\n' + '    main() # this calls the actual main function')

# Close the file
    file.close()
    shutil.copy("/home/student/mycode/pythontemplate.py", "./" + xname )
    print("Your new python script template has been created for you.\n" + "It is called: " + xname + "\n and can be found in: " + destpath)

