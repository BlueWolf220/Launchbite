#imports
import keyboard
import time
from tkinter import *
from tkinter import ttk
import time
import Launchbite_settings as s
time.sleep(2)

#general setup
window = Tk()
style = ttk.Style()
window.title('Launchdesk')
time.sleep(2)

#image setup

#function setup
def open_chrome():
    keyboard.press_and_release('windows+5')
def open_gitkraken():
    keyboard.press_and_release('windows+6')
def open_fusion():
    keyboard.press_and_release('windows+3')
def open_eagle():
    keyboard.press_and_release('windows+4')
def open_githubDesk():
    keyboard.press_and_release('windows+7')
def open_atom():
    keyboard.press_and_release('windows+8')
def open_mu():
    keyboard.press_and_release('windows+9')

#button setup
chromebutton = Button(window, text = 'chrome', command = open_chrome)
gitkrakenButton = Button(window, text = 'GitKraken', command = open_gitkraken)
fusionButton = Button(window, text='Fusion 360', command = open_fusion)
eagleButton = Button(window, text='Eagle', command = open_eagle)
githubDeskButton = Button(window, text='Github Desktop', command = open_githubDesk)
atomButton = Button(window, text='Atom', command = open_atom)
muButton = Button(window, text='Mu', command = open_mu)

#size settings
if s.shape=='slim':
    if s.size=='medium':
        window.geometry('200x250')
    if s.size=='large':
        window.geometry('300x350')
if s.shape=='square':
    if s.size=='micro':
        window.geometry('175x175')
    if s.size=='medium':
        window.geometry('275x275')
    if s.size=='large':
        window.geometry('375x375')

#load and launch
chromebutton.pack()
gitkrakenButton.pack()
eagleButton.pack()
githubDeskButton.pack()
atomButton.pack()
muButton.pack()
window.mainloop()
