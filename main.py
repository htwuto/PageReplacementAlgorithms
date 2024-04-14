import tkinter as tk
from tkinter import ttk, messagebox
from fifo import fifo
from lfu import lfu
from lru import lru
from mfu import mfu
from mru import mru
from opt import opt
from sc import sc


def run_algorithm():
    try:

        for widget in result_label_frame.winfo_children():
            widget.destroy()

        algorithm = algorithm_var.get()
        reference_string = reference_var.get()
        reference_string = list(map(int, reference_string.split()))
        frames = int(frames_var.get())

        result_label_frame.grid(row=4, columnspan=2, padx=20, pady=20, ipady=5)

        # for i, reference in enumerate(reference_string):
        #     block = tk.Frame(result_label_frame, width=50, height=50, bd=1, relief="flat")
        #     block.grid(row=0, column=i, padx=5, pady=5)
        #     label = tk.Label(block, text=str(reference), width=4, height=2, bg="#00FFFF")
        #     label.pack(fill="both", expand=True)

        fault_label = tk.Label(root, text="")
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
            block = tk.Frame(result_label_frame, width=50, height=50, bd=1, relief="groove")
            block.grid(row=0, column=col, padx=5, pady=5)
            label = tk.Label(block, text=str(reference_string[col]), width=4, height=2, bg=color)
            label.pack(fill="both", expand=True)
            for row, frame in enumerate(frame_list):
                if frame_list[0] == '':
                    continue
                block = tk.Frame(result_label_frame, width="100", height="100", bd="1", relief="raised")
                block.grid(row=row + 1, column=col, padx=5, pady=0)
                label = tk.Label(block, text=str(frame) if frame != '' else "-", width=4, height=2)
                label.pack(fill="both", expand=True)

        fault_label.config(text=f"Faults: {fault}   ")
    except Exception as e:
        messagebox.showinfo("Error", f"Error!: " + str(e))


root = tk.Tk()
root.title("Page Replacement Algorithm")

algorithm_label = tk.Label(root, text="Algorithm:")
algorithm_label.grid(row=0, column=0, padx=10, pady=5)
algorithm_var = tk.StringVar(root)
algorithm_var.set("FIFO")
algorithm_option = tk.OptionMenu(root, algorithm_var, "FIFO", "LRU", "OPT", "MRU", "LFU", "MFU", "SC")
algorithm_option.grid(row=0, column=1, padx=10, pady=5)

reference_label = tk.Label(root, text="Reference String:")
reference_label.grid(row=1, column=0, padx=10, pady=5)
reference_var = tk.StringVar(root)
reference_entry = tk.Entry(root, textvariable=reference_var)
reference_entry.grid(row=1, column=1, padx=10, pady=5)

frames_label = tk.Label(root, text="Number of Frames:")
frames_label.grid(row=2, column=0, padx=10, pady=5)
frames_var = tk.StringVar(root)
frames_entry = tk.Entry(root, textvariable=frames_var)
frames_entry.grid(row=2, column=1, padx=10, pady=5)

run_button = tk.Button(root, text="Run Algorithm", command=run_algorithm)
run_button.grid(row=3, columnspan=2, padx=10, pady=10)

result_label_frame = tk.LabelFrame(root, text="Result")

root.mainloop()
