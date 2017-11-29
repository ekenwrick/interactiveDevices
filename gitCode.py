import subprocess as spr
import time
import tkinter
from tkinter import messagebox

signalCheck = 1

## USED FOR PUSHING - REPLACE cwd WITH DIRECTORY OF THE GIT REPOSITORY

if signalCheck == 1:

    spr.Popen('git add .'.split(), cwd = '/Users/ethankenwrick/Documents/uni/fourthYear/technicalProject/projectWork', stdout = spr.PIPE, stderr = spr.PIPE)

    spr.Popen('git commit -m "push"'.split(), cwd = '/Users/ethankenwrick/Documents/uni/fourthYear/technicalProject/projectWork', stdout = spr.PIPE, stderr = spr.PIPE)

    spr.Popen('git push'.split(), cwd = '/Users/ethankenwrick/Documents/uni/fourthYear/technicalProject/projectWork', stdout = spr.PIPE, stderr = spr.PIPE)

    # hide main window
    root = tkinter.Tk()
    root.withdraw()

    time.sleep(2)

    messagebox.showinfo("Information","File Transferred! ")

## USED FOR PULLING - REPLACE cwd WITH DIRECTORY OF THE GIT REPOSITORY

if signalCheck == 2:

    spr.Popen('git pull'.split(), cwd = 'WORKING DIRECTORY OF GIT REPORSITORY', stdout = spr.PIPE, stderr = spr.PIPE)

    # hide main window
    root = tkinter.Tk()
    root.withdraw()

    time.sleep(2)

    messagebox.showinfo("Information","File Delivered! ")

    spr.Popen(WORKING DIRECTORY OF GIT REPOSITORY/FILE)
