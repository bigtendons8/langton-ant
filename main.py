import simplegrid
import time

def main():

    grid = simplegrid.Grid(75, 75, "■ ")
    direction = 90
    grid.selected_x = 40
    grid.selected_y = 40

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


if __name__ == "__main__":
    main()

