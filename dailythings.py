"""
 Script to start daily apps like Notepad++, OneNote, Teams, Outlook
"""
import subprocess
import os
from sys import argv
from time import sleep
import ctypes


app_list = ['notepad++', 'Skype', 'Teams', 'Outlook']
app_location = {app_list[0]: 'C:\\Program Files\\Notepad++\\notepad++.exe',
                app_list[1]: 'C:\\Program Files (x86)\\Microsoft\\Skype for Desktop\\Skype.exe',
                app_list[2]: 'C:\\Users\\Umore\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe',
                app_list[3]: 'C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE'}
processes = []


def main():
    argument = argv
    if "hi" in argument:
        print("Hello Udhav, Starting your daily Apps...")
        start_app()
        print("Done...Have a Good Day!!!")
    elif "bye" in argument:
        close_app()
    elif "goodbye" in argument:
        sys_shutdown()
    else:
        print("No argument passed...try \n"
              "To Start apps - <filename> hi\n"
              "To Stop apps and Log off - <filename> bye\n"
              "To shutdown the system - <filename> goodbye\n")


def start_app():
    for i in range(len(app_list)):
        print("Starting " + app_list[i])
        processes.append(subprocess.Popen(app_location.get(app_list[i])))
        sleep(2)


def close_app():
    for i in range(len(app_list)):
        print("Closing " + str(app_list[i]))
        os.system("TASKKILL /F /IM " + str(app_list[i]).lower() + ".exe")
        sleep(2)
    print("Logging Off...Sayonara!!!")
    sleep(5)
    ctypes.windll.user32.LockWorkStation()


def sys_shutdown():
    for i in range(len(app_list)):
        print("Closing " + str(app_list[i]))
        os.system("TASKKILL /F /IM " + str(app_list[i]).lower() + ".exe")
        sleep(2)
    print('Shutting down system in 5 seconds...GoodBye')
    os.system("shutdown /s /t 1")


if __name__ == '__main__':
    main()
