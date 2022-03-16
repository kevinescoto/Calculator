import tkinter as tk

window = tk.Tk()
greeting = tk.Label(
    text="Welcome to Number Cruncher",
    foreground="white",
    background="black"
)
greeting.pack()

button = tk.Button(
    text = "Click Me",
    width = 25,
    height = 5,
    bg="black",
    fg="white"

)
button.pack()

name_label = tk.Label(text="Your Name:")
entry = tk.Entry(fg ="white", bg="black", width=50 )
name_label.pack()
name = entry.get()
name
entry.pack()








window.mainloop()
