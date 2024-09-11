import tkinter as tk
print(tk.TkVersion)

# BASIC STRUCTURE

# create main window
root = tk.Tk()
root.title('My TK GUI')

# Add a label to the window
label = tk.Label(root, text='Hello, Tkinter!')
label.pack()
# start tk event loop
root.mainloop()
