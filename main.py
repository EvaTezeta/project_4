#Import libraries
import tkinter as tk
import random


#Make class
class Grid:

  def __init__(self, parent):
    self.parent = parent
    self.root = tk.Frame(parent)
    self.row = 5
    self.col = 5
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
      
    # A container for the buttons
    self.container1 = tk.Frame(parent)
    self.container1.pack()
    
    #Button 1
    self.button1 = tk.Button(self.container1, text = "Find best path")
    self.button1.pack(side = "left")
    self.button1.bind("<Button-1>", self.button1Click)
    
    #Button 2
    self.button2 = tk.Button(self.container1, text="Create new random field")
    self.button2.pack(side = "left")
    self.button2.bind("<Button-1>", self.button2Click)

    #Button 3
    self.button3 = tk.Button(self.container1, text = "Exit program")
    self.button3.pack(side = "left")
    self.button3.bind("<Button-3>", self.button3Click)

  def set_start(self, row, column):
    self.buttons[row][column].config(text="S")

  def set_goal(self, row, column):
    self.buttons[row][column].config(text="G")

  def calculate_maximal_score(self):
    pass

  def choose_the_best_root(self):
    pass

  # Button 1 draws the best path
  def button1Click(self, event):
    pass

  # Button 2 makes a new random field
  def button2Click(self, event):
    self.grid = [[random.randint(0, 9) for j in range(self.col)]
                 for i in range(self.row)]
    for i in range(self.row):
      for j in range(self.col):
        self.buttons[i][j].config(text=self.grid[i][j])

  # Button 3 exits the program
  def button3Click(self):
    self.root.destroy()

# Geometry and title
root = tk.Tk()
root.geometry("500x500")
root.title("Best Path")

# Create the grid within the frame (delete later when canvas works)
Grid = Grid(root)
Grid.set_start(4, 0)
Grid.set_goal(0, 4)

root.mainloop()