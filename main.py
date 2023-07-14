import time
from tkinter import *
from tkinter import messagebox
window = Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
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
minutes = 20
seconds = 0
total_seconds = minutes * 60 + seconds
alarm(total_seconds)
messagebox.showwarning('20 solution', '20+20+20!')
window.deiconify()
window.destroy()
window.quit()