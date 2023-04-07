#Import libraries
import tkinter as tk
import random
import copy

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
                            width = self.canvas_width,
                            height = self.canvas_height)
    self.canvas.pack()

    # Create a 5x5 grid with random numbers
    self.grid = [[random.randint(0, 9) for j in range(self.col)]
                 for i in range(self.row)]
    self.grid[0][4] = 0
    self.grid[4][0] = 0
    self.grid[::-1]
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
    self.set_start(0, 4)
    self.set_goal(4, 0)
    
    # A container for the buttons
    self.container1 = tk.Frame(parent)
    self.container1.pack()

    # Print the maximum score
    self.score_label = tk.Label(self.container1)
    self.score_label["text"] = self.get_maximum_possible_score()
    self.score_label.configure(text = self.score_label["text"])
    self.score_label.pack(side = "top")
    
    #Button 1
    self.findPathButton = tk.Button(self.container1, text = "Find best path", activebackground = "grey")
    self.findPathButton.pack(side = "left")
    self.findPathButton.bind("<Button-1>", self.PathButton)

    #Button 2
    self.newFieldButton = tk.Button(self.container1, text ="Create new random field", activebackground = "grey")
    self.newFieldButton.pack(side = "left")
    self.newFieldButton.bind("<Button-1>", self.FieldButton)

    #Button 3
    self.exitButton = tk.Button(self.container1, text = "Exit program", activebackground = "red")
    self.exitButton.pack(side = "left")
    self.exitButton.bind("<Button-1>", self.ExitProgramButton)

  def set_start(self, row, column):
    rect, _ = self.rects[row][column]
    self.canvas.itemconfig(rect, fill = "green")

  def set_goal(self, row, column):
    rect, _ = self.rects[row][column]
    self.canvas.itemconfig(rect, fill = "red")

  @staticmethod
  def create_path_options():
    root_1 = []
    root_2 = []
    root_3 = []
    root_final = []
    root_unique = []
    choice = ["up", "up", "up", "up"]
    for position1 in range(len(choice)+1):
        choice_1 = copy.deepcopy(choice)
        choice_1.insert(position1, "right")
        root_1.append(choice_1)
        for position2 in range(len(choice_1)+1):
            choice_2 = copy.deepcopy(choice_1)
            choice_2.insert(position2, "right")
            root_2.append(choice_2)
            for position3 in range(len(choice_2)+1):
                choice_3 = copy.deepcopy(choice_2)
                choice_3.insert(position3, "right")
                root_3.append(choice_3)
                for position4 in range(len(choice_3)+1):
                    choice_final = copy.deepcopy(choice_3)
                    choice_final.insert(position4, "right")
                    root_final.append(choice_final)
    for root in root_final:
        if root not in root_unique:
            root_unique.append(root)
    return root_unique
            
  def choose_best_root(self):
      path_options = self.create_path_options()
      current_row = 4
      current_column = 0
      result = self.grid[4][0]
      result_max = result
      for path in path_options:
          for direction in path:
              if direction == "up":   
                  current_row -= 1
                  current_grid = self.grid[current_row][current_column]
                  result += current_grid
                  if result > result_max:
                      result_max = result
                      best_root = path
              else:
                  current_column += 1
                  current_grid = self.grid[current_row][current_column]
                  result += current_grid
                  if result > result_max:
                      result_max = result
                      best_root = path
          current_row = 4
          current_column = 0
          result = self.grid[4][0]
      return result_max, best_root

  def get_maximum_possible_score(self):
    maximum_score = list(self.choose_best_root())[0]
    text = "Possible maximum score: " + str(maximum_score)
    return text      
    
  def show_best_path(self):
    best_path = list(self.choose_best_root())[1]
    x_coordinate = 120
    y_coordinate = 300
    x_coordinates = [x_coordinate]
    y_coordinates = [y_coordinate]
    for direction in best_path:
        if direction == "up":
            y_coordinate -= 60
            x_coordinates.append(x_coordinate)
            y_coordinates.append(y_coordinate)
        else:
            x_coordinate += 60
            x_coordinates.append(x_coordinate)
            y_coordinates.append(y_coordinate)
    for i in range(len(x_coordinates)-1):
       self.canvas.create_line(x_coordinates[i], y_coordinates[i],
                               x_coordinates[i+1], y_coordinates[i+1])
    self.canvas.pack()
    #self.canvas.bind("<Button-1>", self.PathButton())

  # Button 1 draws the best path
  def PathButton(self, event):
    self.show_best_path()

  # Button 2 makes a new random field - doesn't work yet
  def FieldButton(self, event):
    self.grid = [[random.randint(0, 9) for j in range(self.col)] for i in range(self.row)]
    self.grid[0][4] = 0
    self.grid[4][0] = 0
    self.grid[::-1]

    for i in range(self.row):
        for j in range(self.col):
            self.canvas.itemconfig(self.rects[i][j][1], text=str(self.grid[i][j]))

    # Get new label text
    self.score_label["text"] = self.get_maximum_possible_score()

     # Printi


  # Button 3 exits the program
  def ExitProgramButton(self, event):
    self.parent.destroy()


# Geometry and title
root = tk.Tk()
root.geometry("500x500")
root.title("Pathfinder")

# Create the grid within the frame (delete later when canvas works)
Grid = Grid(root)
#Grid.set_start(4, 0)
#Grid.set_goal(0, 4)

root.mainloop()
