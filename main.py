from tkinter import * 
import time

state = {
    0: '#1b1811',
    1: '#b8c3fd'
}

directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

transition_table = {
    0: [0, 0, 0, 1, 0, 0, 0, 0, 0],
    1: [0, 0, 1, 1, 0, 0, 0, 0, 0]
}

def compute_neighbours(GRID, r, c):
    neighbors = 0
    for dir in directions:
        dc, dr = dir
        if(0 <= r+dr <= ROWS-1 and 0 <= c+dc <= COLS-1):
            neighbors += GRID[r+dr][c+dc]
    return neighbors 

def compute_nextGen(grid):
    global GRID
    new_grid = [[0]*COLS for _ in range(ROWS)]

    for i in range(ROWS):
        for j in range(COLS):
            neighbors = compute_neighbours(grid, i, j)
            new_grid[i][j] = transition_table[grid[i][j]][neighbors]

    GRID = new_grid.copy()

    
ROWS = 80
COLS = 80
GRID = [[0]*COLS for _ in range(ROWS)]

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800
SIZE = CANVAS_WIDTH/ROWS


class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Game of Life")
        self.playing = True
        self.canvas = Canvas(self, height=CANVAS_HEIGHT, width=CANVAS_WIDTH, bg="#ff5050")
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.handle_click)
        self.draw_grid(GRID)
        self.btn = Button(self, text="start", command=self.play)
        self.btn.pack()
        self.rbtn = Button(self, text="Reset", command=self.reset)
        self.rbtn.pack()
        self.update()

    def draw_grid(self, gird):
        for i in range(ROWS):
            for j in range(COLS):
                self.canvas.create_rectangle(i*SIZE, j*SIZE, i*SIZE+SIZE, j*SIZE+SIZE, fill=state[GRID[i][j]], outline=state[GRID[i][j]])

    def handle_click(self, event):
        GRID[int(event.x/SIZE)][int(event.y/SIZE)] = 1
        self.draw_grid(GRID)

    def animate_canvas(self):
        if self.playing:
            compute_nextGen(GRID)
            self.draw_grid(GRID)
            self.canvas.update()
            self.canvas.after(10, self.animate_canvas)
    
    def play(self):
        self.playing = True
        self.animate_canvas()

    def reset(self):
        global GRID
        GRID = [[0] * COLS for _ in range(ROWS)]
        self.draw_grid(GRID)
        self.playing = False

def main():
    app = App()
    app.mainloop()

if __name__=="__main__":
    main()
