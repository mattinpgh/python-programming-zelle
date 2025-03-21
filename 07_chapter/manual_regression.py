"""
A graphical program for plotting a regression line from manually set points
"""

from graphics import Circle, GraphWin, Point, Rectangle, Text, Line


class Section:
    def __init__(self,
                 shape,
                 is_drawn=False,
                 name="",
                 left_bound=0,
                 bottom_bound=0,
                 right_bound=0,
                 top_bound=0,
                 fill_color="white",
                 outline_color="black"
                 ):
        self.shape = shape
        self.is_drawn = is_drawn
        self.name = name
        self.left_bound = left_bound
        self.bottom_bound = bottom_bound
        self.right_bound = right_bound
        self.top_bound = top_bound
        self.fill_color = fill_color
        self.outline_color = outline_color

    def draw_section(self, window, text=False):
        if self.is_drawn and hasattr(self.shape, 'undraw'):
            self.shape.undraw()
        self.shape = Rectangle(Point(self.left_bound, self.bottom_bound),
                          Point(self.right_bound, self.top_bound)
                          )
        self.shape.setFill(self.fill_color)
        self.shape.setOutline(self.outline_color)
        self.shape.draw(window)

        if text:
            shape_text = Text(Point((self.left_bound + self.right_bound) / 2,
                                    (self.bottom_bound + self.top_bound) / 2),
                            text)
            shape_text.draw(window)

    def point_in_section(self, point):
        x = point.getX()
        y = point.getY()

        if (x >= self.left_bound
            and x <= self.right_bound
            and y >= self.bottom_bound
            and y <= self.top_bound
        ):
            return True
        return False
        

"""def draw_buttons(window):
    win = window
    done_button = Rectangle(Point(0,0), Point(15,15))
    done_button.setOutline("black")
    done_button.draw(win)
    done_text = Text(Point(7.5,7.5), "Done")
    done_text.draw(win)

    rpt_button = Rectangle(Point(20,0), Point(35,15))
    rpt_button.setOutline("black")
    rpt_button.draw(win)
    rpt_text = Text(Point(27.5,7.5), "Start \nOver")
    rpt_text.draw(win)

    exit_button = Rectangle(Point(40,0), Point(55,15))
    exit_button.setOutline("black")
    exit_button.draw(win)
    exit_text = Text(Point(47.5,7.5), "Exit \nProgram")
    exit_text.draw(win)      


def get_click_within(point, ll_bound, ur_bound):
    left_bound = ll_bound.getX()
    right_bound = ur_bound.getX()
    top_bound = ur_bound.getY()
    bottom_bound = ll_bound.getY()

    x = point.getX()
    y = point.getY()

    if (x > left_bound and x < right_bound and 
        y > bottom_bound and y < top_bound):
        return True

    return False"""


def store_point(point, dct):
    x = point.getX()
    y = point.getY()
    dct["x_sum"] = dct.get("x_sum", 0) + x
    dct["y_sum"] = dct.get("y_sum", 0) + y
    dct["x_count"] = dct.get("x_count", 0) + 1
    dct["y_count"] = dct.get("y_count", 0) + 1
    dct["xy_sum"] = dct.get("xy_sum", 0) + (x * y)
    dct["sum_x_sq"] = dct.get("sum_x_sq", 0) + (x ** 2)


def draw_point(point, window, lst):
    win = window
    circle = Circle(point, 0.5)
    circle.setOutline("black")
    circle.setFill("black")
    circle.draw(win)
    lst.append(circle)


def reset_field(win, lst, dct):
    for item in lst:
        item.undraw()
    for key in dct:
        dct[key] = 0


def calculate_regression(dct):
    y_bar = dct.get("y_sum", 0) / dct.get("y_count", 1)
    x_bar = dct.get("x_sum", 0) / dct.get("x_count", 1)
    n = dct.get("x_count", 1)
    m_top = dct.get("xy_sum", 1) - (n * x_bar * y_bar)
    m_bottom = dct.get("sum_x_sq", 1) - (n * (x_bar ** 2))
    m = m_top / m_bottom
    return m


def get_leftmost_x(lst):
    leftmost_x = 200
    for item in lst:
        if item.getCenter().getX() <= leftmost_x:
            leftmost_x = item.getCenter().getX()

    return leftmost_x


def get_rightmost_x(lst):
    rightmost_x = 0
    for item in lst:
        if item.getCenter().getX() >= rightmost_x:
            rightmost_x = item.getCenter().getX()

    return rightmost_x    


def get_regression_line(left_x, right_x, dct):
    y_bar = dct.get("y_sum", 0) / dct.get("y_count", 1)
    x_bar = dct.get("x_sum", 0) / dct.get("x_count", 1)
    m = calculate_regression(dct)
    left_y = y_bar + (m * (left_x - x_bar))
    right_y = y_bar + (m * (right_x - x_bar))
    left_point = Point(left_x, left_y)
    right_point = Point(right_x, right_y)

    return Line(left_point, right_point)


def main():
    # Initialize graphical components
    win = GraphWin("Regression", 1280, 720)
    win.setCoords(0, 0, 200, 200)

    sidebar = Section("", False, "Sidebar", 140, 15, 200, 200, "lightgray", "black")
    footer = Section("", False, "Footer", 0, 0, 140, 15, "lightgray", "black")
    output = Section("", False, "Output", 140, 0, 200, 15, "lightblue", "black")
    sidebar.draw_section(win)
    footer.draw_section(win)
    output.draw_section(win)
    
    done_button = Section("", False, "Calculate", 0, 0, 15, 15, "white", "black")
    again_button = Section("", False, "Start Over", 20, 0, 35, 15, "white", "black")
    quit_button = Section("", False, "Exit Program", 40, 0, 55, 15, "white", "black")
    done_button.draw_section(win, done_button.name)
    again_button.draw_section(win, again_button.name)
    quit_button.draw_section(win, quit_button.name)


    
    finished = False
    point_list = []
    reg_line = Line(Point(0,0), Point(0,0))
    x_y_dict = {"x_sum": 0,
                "y_sum": 0,
                "x_count": 0,
                "y_count": 0,
                "xy_sum": 0,
                "sum_x_sq": 0,
                }

    # draw_buttons(win)

    while True:
        click_loc = win.getMouse()
        if done_button.point_in_section(click_loc) and finished is False:
        #if get_click_within(click_loc, Point(0,0), Point(10,6)) and finished is False:
            # Click the Done button to calculate the slope and draw the line
            reg_val = calculate_regression(x_y_dict)
            reg_line =  get_regression_line(
                get_leftmost_x(point_list),
                get_rightmost_x(point_list),
                x_y_dict)
            reg_line.draw(win)
            finished = True
            calc_text = (f"The slope of the regression line is: {reg_val:.4f}\n"
                         "Start Over or Exit Program?")
            output.draw_section(win, calc_text)
            print()
            print()

        elif again_button.point_in_section(click_loc):
        #elif get_click_within(click_loc, Point(11,0), Point(22,6)):
            # Click the Start Over button, erase the points, clear the lists
            reset_field(win, point_list, x_y_dict)
            reg_line.undraw()
            point_list = []
            finished = False

        elif quit_button.point_in_section(click_loc):
        #elif get_click_within(click_loc, Point(22,0), Point(32,6)):
            # Click the Exit Program button to quit
            break

        elif finished is False:
            # Otherwise, store and draw points
            store_point(click_loc, x_y_dict)
            draw_point(click_loc, win, point_list)

    print(x_y_dict)
    print(point_list)
    win.getMouse()

main()