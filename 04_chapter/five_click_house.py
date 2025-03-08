from graphics import GraphWin, Rectangle, Point, Polygon


def draw_frame(win, frame_ul, frame_lr):
    frame = Rectangle(frame_ul, frame_lr)
    frame.setOutline("black")
    frame.draw(win)


def get_door_width(frame_ul, frame_lr):
    house_width = abs(frame_ul.getX() - frame_lr.getX())
    door_width = house_width * 0.2
    return door_width


def draw_door(win, frame_ul, frame_lr, door_center):
    door_mod = get_door_width(frame_ul, frame_lr) * 0.5
    ulx = door_center.getX() - door_mod
    uly = door_center.getY()
    lrx = door_center.getX() + door_mod
    lry = frame_lr.getY()
    door = Rectangle(Point(ulx, uly), Point(lrx, lry))
    door.setOutline("black")
    door.draw(win)


def draw_window(win, width, center):
    mod = width / 2
    ulx = center.getX() - mod
    uly = center.getY() + mod
    lrx = center.getX() + mod
    lry = center.getY() - mod
    window = Rectangle(Point(ulx, uly), Point(lrx, lry))
    window.setOutline("black")
    window.draw(win)


def get_window_width(door_width):
    return door_width * 0.5


def draw_roof(win, f1, f2, peak):
    roof = Polygon(f1, Point(f2.getX(), f1.getY()), peak)
    roof.setOutline("black")
    roof.draw(win)


def main():
    win = GraphWin("Five-Click House", 1280, 1200)
    win.setCoords(-10, -10, 10, 10)

    f1 = win.getMouse()
    f2 = win.getMouse()
    draw_frame(win, f1, f2)

    door_center = win.getMouse()
    draw_door(win, f1, f2, door_center)

    window_center = win.getMouse()
    draw_window(win, get_window_width(get_door_width(f1, f2)), window_center)

    peak = win.getMouse()
    draw_roof(win, f1, f2, peak)

    win.getMouse()
    win.close()


main()
