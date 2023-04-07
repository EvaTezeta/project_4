#Import libraries
import tkinter as tk
import random


#Make class for the Pathfinder
class Grid:

  def __init__(self, parent):
    self.parent = parent
    self.root = tk.Frame(parent)
    self.row = 5
    self.col = 5
    self.root.pack()
    self.cell_size = 60
    self.canvas_width = self.col * self.cell_size
    self.canvas_height = self.row * self.cell_size
    self.canvas = tk.Canvas(parent,
                            width=self.canvas_width,
                            height=self.canvas_height)
    self.canvas.pack()

    # Create a 5x5 grid with random numbers
    self.grid = [[random.randint(0, 9) for j in range(self.col)]
                 for i in range(self.row)]
    self.rects = []
    for i in range(self.row):
      row = []
      for j in range(self.col):
        x0 = j * self.cell_size
        y0 = i * self.cell_size
        x1 = x0 + self.cell_size
        y1 = y0 + self.cell_size
        rect = self.canvas.create_rectangle(x0, y0, x1, y1, fill="white")
        text = self.canvas.create_text(x0 + self.cell_size // 2,
                                       y0 + self.cell_size // 2,
                                       text=str(self.grid[i][j]))
        row.append((rect, text))
      self.rects.append(row)

    # Create a 5x5 grid with random numbers
    # self.grid = [[random.randint(0, 9) for j in range(self.col)]
    #              for i in range(self.row)]
    # self.buttons = []
    # for i in range(self.row):
    #   row = []
    #   for j in range(self.col):
    #     button = tk.Button(self.root, text=self.grid[i][j])
    #     button["width"] = 8
    #     button["height"] = 3
    #     button.grid(row=i, column=j)
    #     row.append(button)
    #   self.buttons.append(row)

    # A container for the buttons
    self.container1 = tk.Frame(parent)
    self.container1.pack()

    #Button 1
    self.button1 = tk.Button(self.container1, text="Find best path", activebackground = "grey")
    self.button1.pack(side="left")
    self.button1.bind("<Button-1>", self.button1Click)

    #Button 2
    self.button2 = tk.Button(self.container1, text="Create new random field", activebackground = "grey")
    self.button2.pack(side="left")
    self.button2.bind("<Button-1>", self.button2Click)

    #Button 3
    self.button3 = tk.Button(self.container1, text="Exit program", activebackground = "red")
    self.button3.pack(side="left")
    self.button3.bind("<Button-1>", self.button3Click)

  def set_start(self, row, column):
    rect, _ = self.rects[row][column]
    self.canvas.itemconfig(rect, fill="green")

  def set_goal(self, row, column):
    rect, _ = self.rects[row][column]
    self.canvas.itemconfig(rect, fill="red")

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
    self.buttons[4][0].config(text="S")
    self.buttons[0][4].config(text="G")

  # Button 3 exits the program
  def button3Click(self, event):
    self.parent.destroy()


# Geometry and title
root = tk.Tk()
root.geometry("500x500")
root.title("Pathfinder")

# Create the grid within the frame (delete later when canvas works)
Grid = Grid(root)
Grid.set_start(4, 0)
Grid.set_goal(0, 4)

root.mainloop()
