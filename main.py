import time
from tkinter import *
from tkinter import messagebox
import pyautogui
window = Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
def minimize_all_windows():
    pyautogui.hotkey('winleft', 'd')
def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_elapsed // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Time left: {minutes_left:02d}:{seconds_left:02d}")

icon = PhotoImage(file="headerImage.png")

window.iconphoto(window, icon)

minutes = 20
seconds = 0
total_seconds = minutes * 60 + seconds
alarm(total_seconds)
minimize_all_windows()
time.sleep(0.5)
messagebox.showwarning('20 rule', '20+20+20')
window.deiconify()
window.destroy()
window.quit()