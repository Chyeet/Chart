import webbrowser
import pyautogui
import time
import keyboard
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import random
#Imports


#Final Stage
def wind():
    choices = [5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    char = random.choice(choices)
    # keyboard.press_and_release('windows')
    # time.sleep(0.05)
    # keyboard.write('cmd')
    # time.sleep(0.05)
    # keyboard.press_and_release('enter')

    # time.sleep(0.25)
    # keyboard.write('tree')
    # keyboard.press_and_release('enter')
    root = tk.Tk()

    root.title('CHART 5 CHART 5 CHART 5 CHART 5')
    canvas1 = tk.Canvas(root, width=450, height=300)
    canvas1.pack()

    def ExitApplication():
        MsgBox = tk.messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                           icon='warning')
        if MsgBox == 'yes':
            root.destroy()
        else:
            tk.messagebox.showinfo('Return', 'You will now return to the application screen')

    button1 = tk.Button(root, text='Exit Application', command=ExitApplication, bg='brown', fg='white')
    canvas1.create_window(225, 150, window=button1)

    root.mainloop()

    os.system('"start chrome.exe "https://www.youtube.com/channel/UCQPLu07GoHlW80QUZ1szg5Q" "')

    for i in range(5):
        time.sleep(char)
        os.system(
            '"start chrome.exe "https://imgs.search.brave.com/sgG7tRAKXDjFlGI2gH5m_O0EW69fAj9IBrGz3SmPX3Q/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly9wbmdp/bWcuY29tL3VwbG9h/ZHMvc3Vic2NyaWJl/L3N1YnNjcmliZV9Q/Tkc1Mi5wbmc"  "')

    os.system('"shutdown /s "')



def secret():
    time.sleep(15)


#'3,2,1' Stage
def end():

    time.sleep(50)
    for i in range(1):
        webbrowser.open('https://imgs.search.brave.com/zMJJXQiOye_66NbxIkebK8vfDOeesVOx2T9MM4Sk5mI/rs:fit:438:596:1/g:ce/aHR0cHM6Ly9jbGlw/Z3JvdW5kLmNvbS9p/bWFnZXMvYS1jbGlw/YXJ0LW51bWJlci10/aHJlZS5wbmc')
        time.sleep(0.4)
        webbrowser.open('https://imgs.search.brave.com/KyNife-M9m11p7E-9qoc_etE-dGJeJndVXPbmJayDK4/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly93ZWJz/dG9ja3Jldmlldy5u/ZXQvaW1hZ2VzL2Ns/aXBhcnQtbnVtYmVy/cy1yZWQtMTcucG5n')
        time.sleep(0.4)
        webbrowser.open('https://imgs.search.brave.com/h0jOUdqGN-dXHypjg4vJD0xX0kyYwfnX2JIkZ3iO5Lo/rs:fit:1200:1200:1/g:ce/aHR0cDovL3d3dy5h/Y3Rpdml0eXNoZWx0/ZXIuY29tL3dwLWNv/bnRlbnQvdXBsb2Fk/cy8yMDE2LzA2L3Bp/Y3R1cmUtb2YtdGhl/LW51bWJlci0xLWFt/YXppbmcuanBn')
        time.sleep(1)

        for i in range(30):
            time.sleep(0.1)
            webbrowser.open('https://i.ytimg.com/vi/5YR3DaHuY-0/hqdefault.jpg')
        time.sleep(15)
        wind()

        
        
 #Starting Stage
def main():


    ws = Tk()
    ws.title("Chyeet's manifesto")
    ws.geometry('400x250')
    ws.config(bg='#000000')

    message = '''
    Dear Reader,

        Welcome to Chart4. This Program 
        aims to hack your computer. 
        
        Just kidding!
        
    Thanks & Regards,
    Chyeet      '''

    text_box = Text(
        ws,
        height=12,
        width=40
    )
    text_box.pack(expand=True)
    text_box.insert('end', message)
    text_box.config(state='disabled')

    ws.mainloop()
    print(pyautogui.size())
    webbrowser.open('https://imgs.search.brave.com/bLsnGOw82Hi7VkEicouYEv5qYS-l_-IesU9KwJaV9bQ/rs:fit:512:512:1/g:ce/aHR0cHM6Ly90aHVt/YnMuZ2Z5Y2F0LmNv/bS9BbnRpcXVlT3Ju/ZXJ5TGVtdXItc2l6/ZV9yZXN0cmljdGVk/LmdpZg.gif')
    time.sleep(0.2)
    webbrowser.open('https://i.ytimg.com/vi/5YR3DaHuY-0/hqdefault.jpg')
    webbrowser.open('https://www.youtube.com/channel/UCQPLu07GoHlW80QUZ1szg5Q')
    time.sleep(2)
    pyautogui.click(1650, 500)
    time.sleep(0.2)
    keyboard.press_and_release('control+w')
    time.sleep(1)
    keyboard.press_and_release('control+w')
    time.sleep(0.4)
    end()

main()



#dn
