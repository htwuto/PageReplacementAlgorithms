import tkinter as tk
from tkinter import ttk, messagebox
from fifo import fifo
from lfu import lfu
from lru import lru
from mru import mru
from opt import opt


def run_algorithm():
    try:

        algorithm = algorithm_var.get()
        reference_string = reference_var.get()
        reference_string = list(map(int, reference_string.split()))
        frames = int(frames_var.get())

        result_label_frame = tk.LabelFrame(root, text="Result", width=3000, height=2000)
        result_label_frame.grid(row=4, columnspan=2, padx=20, pady=5)
        result_treeview = ttk.Treeview(result_label_frame, show="tree")
        result_treeview.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

        fault_label = tk.Label(result_label_frame, text="")
        fault_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Clear previous results
        for item in result_treeview.get_children():
            result_treeview.delete(item)

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

        # Insert data into treeview
        num_references = len(matrix[0])
        columns = [f"Reference {i + 1}" for i in range(num_references)]
        result_treeview["columns"] = columns
        result_treeview.heading("#0", text="Frame")
        for i, column in enumerate(columns, start=1):
            result_treeview.heading(column, text=column)
        for i, frame in enumerate(matrix, start=1):
            result_treeview.insert("", tk.END, text=reference_string[i - 1], values=frame)

        fault_label.config(text=f"Faults: {fault}")
    except:
        messagebox.showinfo("Error", f"Please insert values")


root = tk.Tk()
root.title("Page Replacement Algorithm")

algorithm_label = tk.Label(root, text="Algorithm:")
algorithm_label.grid(row=0, column=0, padx=10, pady=5)
algorithm_var = tk.StringVar(root)
algorithm_var.set("FIFO")
algorithm_option = tk.OptionMenu(root, algorithm_var, "FIFO", "LRU", "OPT", "MRU", "LFU")
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



root.mainloop()
