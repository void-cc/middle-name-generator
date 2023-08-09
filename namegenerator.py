import random
import os
import tkinter as tk
from tkinter import simpledialog, messagebox

first_name = "Firstname " #you can replace these names, be sure to add a space at the end of the Firstname
last_name = "Lastname"

class NameGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Name Generator")

        self.names = self.load_names()
        self.generated_names = []
        self.current_name_index = -1

        self.name_label = tk.Label(self.master, font=('Arial', 14))
        self.name_label.pack(pady=20)

        self.save_button = tk.Button(self.master, text="Save", command=self.save_name)
        self.save_button.pack(side=tk.LEFT, padx=10)

        self.prev_button = tk.Button(self.master, text="Previous", command=self.previous_name)
        self.prev_button.pack(side=tk.LEFT, padx=10)

        self.next_button = tk.Button(self.master, text="Next", command=self.next_name)
        self.next_button.pack(side=tk.LEFT, padx=10)

        self.generate_names()

    def load_names(self):
        file_path = os.path.join(os.path.dirname(__file__), 'names.txt')
        with open(file_path, 'r') as f:
            return [line.strip() + " " for line in f]

    def generate_names(self):
        
        num_names = simpledialog.askinteger("Input", "How many names do you want to generate?", parent=self.master)
        for _ in range(num_names):
            generated_name = first_name + random.choice(self.names) + random.choice(self.names) + last_name
            self.generated_names.append(generated_name)
        self.show_next_name()

    def save_name(self):
        file_path = os.path.join(os.path.dirname(__file__), 'generated_names.txt')
        with open(file_path, 'a') as f:
            f.write(self.generated_names[self.current_name_index] + "\n")
        messagebox.showinfo("Info", "Name saved!")

    def show_next_name(self):
        if self.current_name_index < len(self.generated_names) - 1:
            self.current_name_index += 1
            self.name_label.config(text=self.generated_names[self.current_name_index])

    def show_previous_name(self):
        if self.current_name_index > 0:
            self.current_name_index -= 1
            self.name_label.config(text=self.generated_names[self.current_name_index])

    def next_name(self):
        self.show_next_name()

    def previous_name(self):
        self.show_previous_name()

if __name__ == "__main__":
    root = tk.Tk()
    app = NameGenerator(master=root)
    root.mainloop()
