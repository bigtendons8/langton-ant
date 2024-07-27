import simplegrid
import time

grid = simplegrid.Grid(30, 30, "■ ")
direction = 90
grid.selected_x = 16
grid.selected_y = 16

while True:
    if grid.read_here() == "■ ":
        grid.change_here("□ ")
        direction += 90
    else:
        grid.change_here("■ ")
        direction -= 90

    normalised = direction % 360
    if normalised == 90:
        grid.move(1, 0)
    elif normalised == 180:
        grid.move(0, 1)
    elif normalised == 270:
        grid.move(-1, 0)
    elif normalised == 0:
        grid.move(0, -1)

    print(grid, flush=True)
    time.sleep(0.01)
