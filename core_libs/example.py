#!/usr/bin/python3

import os
import shutil
import datetime

today=datetime.date.today()
text='{today.day}_{today.month}_{today.year}'.format(today=today)

dir="temp"
cwd=os.getcwd()
output_filename="bkp_"+text


if os.path.exists(dir):
    print("TRUE : removing the temp folder")
    shutil.rmtree(dir)
    print("Creating a temp dir")
    os.makedirs(dir)
    for file in os.listdir(cwd):
        if file.endswith(".txt"):
            shutil.copy(file, dir)


    shutil.make_archive(output_filename, 'zip', dir)

else:
    print("No such temp dir in current path")
    
