#Import libraries
import tkinter as tk
import random


#Make class
class Grid:

    def __init__(self, row, column):
        self.row = row
        self.col = column

        # Create a 5x5 grid with random numbers
        self.grid = [[random.randint(0, 9) for j in range(self.col)]
                     for i in range(self.row)]

    def generate(self):
        for i in range(5):
            for j in range(5):
                button = tk.Button(self.root, text="")
                button = tk.Button(self.root, text=random.randint(0, 9))
                button["width"] = 8
                button["height"] = 3
                button.grid(row=i, column=j)

    def set_start(self, row, column):
        button = self.root.grid_slaves(row=row, column=column)[0]
        button.config(text="S")

    def set_goal(self, row, column):
        button = self.root.grid_slaves(row=row, column=column)[0]
        button.config(text="G")

    def calculate_maximal_score(self):
        pass

    def choose_the_best_root(self):
        pass

    def __init__(self, parent):
        self.parent = parent

        self.container1 = tk.Frame(parent)
        self.container1.pack()

        self.scoretext = tk.Label(self.container1)
        self.scoretext.configure(text="Maximal possible score: ",
                                 background="white")
        self.scoretext.pack(side="left")

        self.container2 = tk.Frame(parent)
        self.container2.pack()

        self.pathbutton = tk.Button(self.container2)
        self.pathbutton["text"] = "Find best path"
        self.pathbutton.pack(side="left")
        self.pathbutton.bind("<Button-1>", self.pathbuttonClick)

        self.fieldbutton = tk.Button(self.container2,
                                     text="Create new random field")
        self.fieldbutton.pack(side="left")
        self.fieldbutton.bind("<Button-2>", self.fieldbuttonClick)

        self.exitbutton = tk.Button(self.container2, text="Exit program")
        self.exitbutton.pack(side="left")
        self.exitbutton.bind("<Button-3>", self.exitbuttonClick)

    def generateNewField(self):
        rows = 10
        columns = 10
        field = []
        for i in range(rows):
            row = []
            for j in range(columns):
                row.append(random.randint(0, 9))
            field.append(row)
        return field

    def pathbuttonClick(self, event):
        self.hwtext.configure()
        #This button should generate best path

    def fieldbuttonClick(self, event):
        new_field = self.generateNewField()
        self.scoretext.configure(
            text=
            f"Maximal possible score: {sum([max(row) for row in new_field])}",
            background="white")

    # This button exits the program (should already work)
    def exitbuttonClick(self, event):
        self.parent.destroy()


#Root should be at bottom of all code
root = tk.Tk()
root.geometry("500x500")

# Create a frame to hold the grid
frame = tk.Frame(root)
# 80 pixels depends on your systems font size, 80px is a gamble
frame.grid(row=0, column=0, padx=80, pady=0)

# Create the grid within the frame
Grid = Grid(frame)
Grid.generate()
Grid.set_start(4, 0)
Grid.set_goal(0, 4)

root.mainloop()
