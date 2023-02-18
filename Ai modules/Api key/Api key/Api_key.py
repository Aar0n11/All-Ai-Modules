import tkinter as tk
import os

def submit_api_key():
    api_key = api_key_entry.get()
    directory = "C:\\Users\\monst\\OneDrive\\Desktop\\Ai modules\\Engines"  # replace with the directory where the file should be saved
    file_name = os.path.join(directory, "Api key.txt")
    with open(file_name, "w") as f:
        f.write(api_key)

# Create the GUI
root = tk.Tk()

api_key_label = tk.Label(root, text="API Key:")
api_key_label.pack()

api_key_entry = tk.Entry(root)
api_key_entry.pack()

submit_button = tk.Button(root, text="Submit", command=submit_api_key)
submit_button.pack()

root.mainloop()