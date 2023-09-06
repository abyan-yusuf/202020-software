import tkinter as tk
import textwrap
import random


while True:
    def close_window():
        root.destroy()

    def close_window_after_timeout():
        root.after(20000, close_window)

    def show_window():
        root.deiconify()  # Show the window
        root.attributes('-topmost', True)  # Keep it on top

    root = tk.Tk()
    root.title("20-20-20 Rule Reminder")

    # Center the window on the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 300
    window_height = 200
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Remove window decorations (close, minimize, maximize buttons)
    root.overrideredirect(True)

    # Create a label with the wrapped message
    message = ["Please, Take a 20-Second break and look at something 20 feet away. Your Eyes Matter!",


    "Look at something 20 Feet away for 20 Seconds. If you help your Eyes, your Eyes wil help you!",


    "It's been 20 Minutes already. Stare at something 20 Feet away for 20 Seconds. Your eyes will thank you.",


    "Take a 20 Second break and stare at something 20 Feet awayfor 20 Sec onds. your Eyes will help you!",


    "Hey! Look at something 20 Feet away for 20 Seconds, because Your eyes matter!",
    
    
    "Be kind to your Eyes and stare at anything 20 Feet away for 20 Seconds. You won't regret this.",
    
    
    "If you don't want a Headache, look at anything 20 feet away for just 20 Seconds.",


    "Hey! Look at something 20 Feet away for 20 Seconds, you are doing a favour for your Eyes.",

    

    ]
    randomIndex = random.choice(message)
    wrapped_message = "\n".join(textwrap.wrap(randomIndex, width=25))
    label = tk.Label( text=wrapped_message, font=("Helvetica", 16), bg='#B7E5D6', fg='black')
    label.pack(padx=20, pady=20)

    # Create an OK button with a custom size
    ok_button = tk.Button(root, text="OK", command=close_window, width=12, height=2, bg='#1F8E7E', fg='white')
    ok_button.pack()

    # Hide the window initially
    root.withdraw()

    root.configure(bg='#B7E5D6')

    # Schedule the window to show after 20 minutes (20 * 60,000 milliSeconds)
    root.after(5000, show_window)

    # Automatically close the window after 20 Seconds (20,000 milliSeconds) if "OK" is not clicked
    root.after(20000, close_window_after_timeout)

    root.mainloop()