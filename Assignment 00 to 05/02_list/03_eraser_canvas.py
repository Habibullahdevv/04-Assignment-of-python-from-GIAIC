import tkinter as tk
import time

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

CELL_SIZE = 40
ERASER_SIZE = 20

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Eraser Grid")
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()

        self.eraser = None
        self.create_grid()

        self.canvas.bind("<Button-1>", self.create_eraser)

        # Mouse tracking
        self.mouse_x = 0
        self.mouse_y = 0
        self.canvas.bind("<Motion>", self.update_mouse_position)

    def create_grid(self):
        num_rows = CANVAS_HEIGHT // CELL_SIZE
        num_cols = CANVAS_WIDTH // CELL_SIZE

        for row in range(num_rows):
            for col in range(num_cols):
                left_x = col * CELL_SIZE
                top_y = row * CELL_SIZE
                right_x = left_x + CELL_SIZE
                bottom_y = top_y + CELL_SIZE
                self.canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill='blue', outline='black')

    def create_eraser(self, event):
        if not self.eraser:
            self.eraser = self.canvas.create_rectangle(
                event.x, event.y,
                event.x + ERASER_SIZE,
                event.y + ERASER_SIZE,
                fill='pink'
            )
            self.animate()

    def update_mouse_position(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def erase_objects(self):
        if not self.eraser:
            return

        left_x = self.mouse_x
        top_y = self.mouse_y
        right_x = left_x + ERASER_SIZE
        bottom_y = top_y + ERASER_SIZE

        overlapping = self.canvas.find_overlapping(left_x, top_y, right_x, bottom_y)

        for obj in overlapping:
            if obj != self.eraser:
                self.canvas.itemconfig(obj, fill='white')

    def animate(self):
        if self.eraser:
            self.canvas.coords(
                self.eraser,
                self.mouse_x,
                self.mouse_y,
                self.mouse_x + ERASER_SIZE,
                self.mouse_y + ERASER_SIZE
            )
            self.erase_objects()
            self.root.after(50, self.animate)  # Call animate again after 50ms

def main():
    root = tk.Tk()
    app = EraserApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
