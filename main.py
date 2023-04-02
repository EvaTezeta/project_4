#Import libraries
import tkinter as tk
import random


#Make class
class Grid:

  def __init__(self, parent):
    self.parent = parent
    self.row = 5
    self.col = 5
    self.root = tk.Frame(parent)
    self.root.pack()

    # Create a 5x5 grid with random numbers
    self.grid = [[random.randint(0, 9) for j in range(self.col)]
                 for i in range(self.row)]

    self.buttons = []
    for i in range(self.row):
      row = []
      for j in range(self.col):
        button = tk.Button(self.root, text=self.grid[i][j])
        button["width"] = 8
        button["height"] = 3
        button.grid(row=i, column=j)
        row.append(button)
      self.buttons.append(row)

  def set_start(self, row, column):
    self.buttons[row][column].config(text="S")

  def set_goal(self, row, column):
    self.buttons[row][column].config(text="G")

  def calculate_maximal_score(self):
    pass

  def choose_the_best_root(self):
    pass

  def pathbuttonClick(self, event):
    pass

  def fieldbuttonClick(self, event):
    self.grid = [[random.randint(0, 9) for j in range(self.col)]
                 for i in range(self.row)]
    for i in range(self.row):
      for j in range(self.col):
        self.buttons[i][j].config(text=self.grid[i][j])

  # This button exits the program
  def exitbuttonClick(self, event):
    self.parent.destroy()


# Geometry and title
root = tk.Tk()
root.geometry("500x500")
root.title("Best Path")

# Create a frame to hold the grid
frame = tk.Frame(root)
frame.pack()

# Create the grid within the frame
Grid = Grid(frame)
Grid.set_start(4, 0)
Grid.set_goal(0, 4)

# Create a container for the buttons
container = tk.Frame(root)
container.pack()

# Create the Find best path button
pathbutton = tk.Button(container)
pathbutton["text"] = "Find best path"
pathbutton.pack(side="left")
pathbutton.bind("<Button-1>", Grid.pathbuttonClick)

# Create the Create new random field button
fieldbutton = tk.Button(container, text="Create new random field")
fieldbutton.pack(side="left")
fieldbutton.bind("<Button-1>", Grid.fieldbuttonClick)

# Create the Exit program button
exitbutton = tk.Button(container, text="Exit program")
exitbutton.pack(side="left")
exitbutton.bind("<Button-1>", Grid.exitbuttonClick)

root.mainloop()
