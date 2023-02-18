import tkinter as tk
import subprocess

root = tk.Tk()
root.geometry("300x100")
root.title("Ai hub")

# Create a label
label = tk.Label(root, text="Select a engine")
label.pack()

# Create a dropdown menu
programs = {"text-babbage-001": "text_babbage_001.cmd",
            "text-davinci-001": "text_davinci_001.cmd",
            "text-davinci-002": "text_davinci_002.cmd",
            "Text-davinci-003": "text_davinci_003.cmd",
            "Text-ada-001": "text_ada_001.cmd",
            "code-davinci-002": "code-davinci-002.cmd",
            "code-cushman-001": "code-cushman-001.cmd"}  # Add your programs here
program_var = tk.StringVar(root)
program_var.set(next(iter(programs)))  # Set default program
dropdown = tk.OptionMenu(root, program_var, *programs.keys())
dropdown.pack()

# Define the function to run the selected program
def run_program():
    program = program_var.get()
    try:
        program_dir = "C:/Users/monst/OneDrive/Desktop/Ai modules/Engines";  # Modify this to the desired directory
        command = f"cd {program_dir} && {programs[program]}"
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        for line in process.stdout:
            print(line.decode().strip())
        for line in process.stderr:
            print(line.decode().strip())
        process.wait()
    except (KeyError, OSError) as e:
        tk.messagebox.showerror("Error", f"Failed to run {program}: {str(e)}")


# Create a run button
run_button = tk.Button(root, text="Run", command=run_program)
run_button.pack()

root.mainloop()
