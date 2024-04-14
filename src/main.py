import tkinter as tk
from tkinter import ttk, messagebox
from fifo import fifo
from lfu import lfu
from lru import lru
from mfu import mfu
from mru import mru
from opt import opt
from sc import sc
import random


def generate_random_reference():
    num_references = int(num_references_var.get())
    reference_string = ' '.join(str(random.randint(0, 9)) for _ in range(num_references))
    reference_var.set(reference_string)


def run_algorithm():
    try:
        for widget in result_label_frame.winfo_children():
            widget.destroy()

        algorithm = algorithm_var.get()
        reference_string = reference_var.get()
        reference_string = list(map(int, reference_string.split()))
        frames = int(frames_var.get())

        result_label_frame.grid(row=4, columnspan=5, padx=20, pady=20, ipady=5, sticky="nsew")  # Sticky để co dãn

        fault_label = tk.Label(root, text="", font=("Arial", 12))
        fault_label.grid(row=5, padx=10, pady=5, sticky="w")
        fault_label.config(text="")

        matrix = []
        fault = 0

        if algorithm == "LRU":
            matrix, fault = lru(reference_string, frames)
        elif algorithm == "FIFO":
            matrix, fault = fifo(reference_string, frames)
        elif algorithm == "OPT":
            matrix, fault = opt(reference_string, frames)
        elif algorithm == "MRU":
            matrix, fault = mru(reference_string, frames)
        elif algorithm == "LFU":
            matrix, fault = lfu(reference_string, frames)
        elif algorithm == "MFU":
            matrix, fault = mfu(reference_string, frames)
        elif algorithm == "SC":
            matrix, fault = sc(reference_string, frames)

        # Display the matrix
        for col, frame_list in enumerate(matrix):
            if frame_list[0] != '':
                color = "#ff6961"
            else:
                color = "#00e4b1"
            block = tk.Frame(result_label_frame, width=150, height=150, bd=1, relief="groove")
            block.grid(row=0, column=col, padx=5, pady=5)
            label = tk.Label(block, text=str(reference_string[col]), width=6, height=3, bg=color, font=("Arial", 12))
            label.pack(fill="both", expand=True)
            for row, frame in enumerate(frame_list):
                if frame_list[0] == '':
                    continue
                block = tk.Frame(result_label_frame, width=150, height=150, bd=1, relief="raised")
                block.grid(row=row + 1, column=col, padx=5, pady=0)
                label = tk.Label(block, text=str(frame) if frame != '' else "-", width=6, height=3,
                                 font=("Arial", 12))
                label.pack(fill="both", expand=True)

        fault_label.config(text=f"Faults: {fault}   ")

    except Exception as e:
        messagebox.showinfo("Error", f"Error!: " + str(e))


root = tk.Tk()
root.title("Page Replacement Algorithm")

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

input_label = tk.LabelFrame(root)
input_label.grid(row=1, columnspan=5, padx=20, pady=20, ipady=5, sticky="ew")

algorithm_label = tk.Label(input_label, text="Algorithm:", font=("Arial", 12))
algorithm_label.grid(row=0, column=0, padx=10, pady=5)
algorithm_var = tk.StringVar(input_label)
algorithm_var.set("FIFO")
algorithm_option = tk.OptionMenu(input_label, algorithm_var, "FIFO", "LRU", "OPT", "MRU", "LFU", "MFU", "SC")
algorithm_option.grid(row=0, column=1, padx=10, pady=5, columnspan=2)

reference_label = tk.Label(input_label, text="Reference String:", font=("Arial", 12))
reference_label.grid(row=1, column=0, padx=10, pady=5)

reference_var = tk.StringVar(input_label)
reference_entry = tk.Entry(input_label, textvariable=reference_var, font=("Arial", 12))
reference_entry.grid(row=1, column=1, padx=10, pady=5)

limit_string = tk.Label(input_label, text="Limit:", font=("Arial", 12))
limit_string.grid(row=1, column=2, padx=5, pady=5)

num_references_var = tk.StringVar(input_label, value="10")  # Giá trị mặc định là 10
num_references_entry = tk.Entry(input_label, textvariable=num_references_var, width=5, font=("Arial", 12))
num_references_entry.grid(row=1, column=3, padx=5, pady=5)

dice_png = tk.PhotoImage(file="media/dice.png")

photo_image = dice_png.subsample(6, 6)

generate_button = tk.Button(input_label, image=photo_image, command=generate_random_reference, font=("Arial", 12))
generate_button.grid(row=1, column=4, padx=5, pady=5)

frames_label = tk.Label(input_label, text="Number of Frames:", font=("Arial", 12))
frames_label.grid(row=2, column=0, padx=10, pady=5)
frames_var = tk.StringVar(input_label)
frames_entry = tk.Entry(input_label, textvariable=frames_var, font=("Arial", 12))
frames_entry.grid(row=2, column=1, padx=10, pady=5)

run_button = tk.Button(input_label, text="Run Algorithm", command=run_algorithm, font=("Arial", 12))
run_button.grid(row=3, columnspan=5, padx=10, pady=10)

result_label_frame = tk.LabelFrame(root, text="Result", font=("Arial", 12))

root.mainloop()
