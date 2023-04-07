#Import libraries
import tkinter as tk
import random
import copy

#Make class    
   
class Grid:

  def __init__(self, parent):
    self.parent = parent
    self.row = 5
    self.col = 5
    self.root = tk.Frame(parent)
    self.root.pack()
    
    # Create a frame to hold the grid
    self.frame = tk.Frame(parent)
    self.frame.pack()
    
    # Create a container for the buttons
    self.container = tk.Frame(parent)
    self.container.pack()
    
    # Print the maximum score
    self.score_label = tk.Label(self.container)
    self.score_label["text"] = self.get_maximum_possible_score()
    self.score_label.configure(text=self.score_label["text"])
    self.score_label.pack(side="top")
    
    # Create the Find best path button
    self.pathbutton = tk.Button(self.container)
    self.pathbutton["text"] = "Find best path"
    self.pathbutton.pack(side="left")
    self.pathbutton.bind("<Button-1>", self.pathbuttonClick)

    # Create the Create new random field button
    self.fieldbutton = tk.Button(self.container, text="Create new random field")
    self.fieldbutton.pack(side="left")
    self.fieldbutton.bind("<Button-1>", self.fieldbuttonClick) 
    
    # Create the Exit program button
    self.exitbutton = tk.Button(self.container, text="Exit program")
    self.exitbutton.pack(side="left")
    self.exitbutton.bind("<Button-1>", self.exitbuttonClick)
    
    # Create a 5x5 grid with random numbers
    self.grid = [[random.randint(0, 9) for j in range(self.col)]
                 for i in range(self.row)]
    self.grid[0][4] = 0
    self.grid[4][0] = 0
    self.grid[::-1]
    self.canvas_collection = []
    
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
    self.buttons[4][0].configure(text="S")
    self.buttons[0][4].configure(text="G")
    
#    for i in range(self.row):
#      row = []
#      for j in range(self.col):
#        canvas= tk.Canvas(self.frame, width= 8, height= 3, bg="White")
#        canvas.create_text(4, 1.5, text=self.grid[i][j] ,fill="black",font=('Helvetica 15 bold'))
#        row.append(canvas)
#      self.canvas_collection.append(row)
#    self.canvas_collection[4][0].configure(text="S")
#    self.canvas_collection[0][4].configure(text="G")
    
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
          result = self.grid[current_row][current_column]
      print(result_max, best_root)
      return result_max, best_root

  def get_maximum_possible_score(self):
    maximum_score = list(self.choose_best_root())[0]
    text = "Possible maximum score: " + str(maximum_score)
    print(text)
    return text      
    
  def show_best_path(self):
    best_path = list(self.choose_best_root())[1]
    x_coordinate = 150
    y_coordinate = 300
    x_coordinates = [x_coordinate]
    y_coordinates = [y_coordinate]
    for direction in best_path:
        if direction == "up":
            y_coordinate -= 10
            x_coordinates.append(x_coordinate)
            y_coordinates.append(y_coordinate)
        else:
            x_coordinate += 10
            x_coordinates.append(x_coordinate)
            y_coordinates.append(y_coordinate)
    self.canvas = tk.Canvas(self.root)
    self.canvas.create_line(x_coordinates[0], y_coordinates[0],
                            x_coordinates[1], y_coordinates[1],
                            x_coordinates[2], y_coordinates[2],
                            x_coordinates[3], y_coordinates[3],
                            x_coordinates[4], y_coordinates[4],
                            x_coordinates[5], y_coordinates[5],
                            x_coordinates[6], y_coordinates[6],
                            x_coordinates[7], y_coordinates[7])
    self.canvas.bind("<Button-1>", self.pathbuttonClick)
    
  def pathbuttonClick(self, event):
    self.show_best_path()

  def fieldbuttonClick(self, event):
    self.grid = [[random.randint(0, 9) for j in range(self.col)]
                 for i in range(self.row)]
    for i in range(self.row):
      for j in range(self.col):
        self.buttons[i][j].config(text=self.grid[i][j])
    self.buttons[4][0].config(text="S")
    self.buttons[0][4].config(text="G")

  # This button exits the program
  def exitbuttonClick(self, event):
    self.parent.destroy()

#print(Grid.get_maximum_possible_score())

# Geometry and title
root = tk.Tk()

#print(Grid.choose_best_root())
root.title("Best Path")
root.geometry("500x500")
find_best_path = Grid(root)

root.mainloop()