#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import datetime
import shutil

# läuft      2017-03-07
# optimiert  2017-03-08
# produktiv  2017-03-11

def main():
    files = os.listdir()
    if not "backup" in files and not os.path.isdir("backup"):
        os.mkdir("backup")
        
    backup_files = [file for file in files if file.endswith(".xlsx")]
    backup_files = [file for file in files if os.path.isfile(file)]

    date = datetime.date.today()

    # create a folder for today
    backupdirs = os.listdir("backup")
    if not str(date) in backupdirs:
        os.mkdir("backup/{}".format(date))

    # backup 
    for backup_file in backup_files:
        src = os.path.join(os.getcwd(), backup_file)
        dst = os.path.join(os.getcwd(), "backup", str(date), backup_file)
        shutil.copyfile(src, dst)
    

if __name__ == "__main__":

    main()

    input(">>> Exit?")
    exit()
