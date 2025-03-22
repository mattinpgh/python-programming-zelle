"""
A graphical program for plotting a regression line from manually set points
"""

from graphics import Circle, GraphWin, Point, Rectangle, Text, Line


class Section:
    """
    A class used to represent a graphical section in the manual regression plotting program.

    Attributes
    ----------
    shape : graphics object
        The graphical shape of the section.
    is_drawn : bool
        Indicates whether the section is currently drawn.
    name : str
        The name of the section.
    left_bound : int
        The left boundary of the section.
    bottom_bound : int
        The bottom boundary of the section.
    right_bound : int
        The right boundary of the section.
    top_bound : int
        The top boundary of the section.
    fill_color : str
        The fill color of the section.
    outline_color : str
        The outline color of the section.

    Methods
    -------
    draw_section(window, text=False):
        Draws the section on the given window. Optionally adds text to the section.
    point_in_section(point):
        Checks if a given point is within the section boundaries.
    """
    def __init__(self,
                 left_bottom = Point,
                 right_top = Point,
                 fill = "white",
                 outline = "black"
                 ):
        self.shape = ""
        self.is_drawn = False
        self.name = ""
        self.bound = {"left": left_bottom.getX(),
                      "bottom": left_bottom.getY(),
                      "right": right_top.getX(),
                      "top": right_top.getY()}
        self.colors = {"fill": fill,
                       "outline": outline}

    def draw_section(self, window, text=False):
        """
        Draws the section on the given window. Optionally adds text to the section.

        Parameters
        ----------
        window : GraphWin
            The window where the section will be drawn.
        text : str, optional
            The text to be displayed in the section (default is False).
        """
        if self.is_drawn and hasattr(self.shape, 'undraw'):
            self.shape.undraw()
            self.is_drawn = False
        self.shape = Rectangle(Point(self.bound['left'], self.bound['bottom']),
                          Point(self.bound['right'], self.bound['top'])
                          )
        self.shape.setFill(self.colors['fill'])
        self.shape.setOutline(self.colors['outline'])
        self.shape.draw(window)
        self.is_drawn = True

        if text:
            shape_text = Text(Point(
                (self.bound['left'] + self.bound['right']) / 2,
                (self.bound['bottom'] + self.bound['top']) / 2),
                              text)
            shape_text.draw(window)

    def point_in_section(self, point):
        """
        Checks if a given point is within the section boundaries.

        Parameters
        ----------
        point : Point
            The point to be checked.

        Returns
        -------
        bool
            True if the point is within the section boundaries, False otherwise.
        """
        x = point.getX()
        y = point.getY()

        return (self.bound['left'] <= x <= self.bound['right'] and
                self.bound['bottom'] <= y <= self.bound['top'])


    def set_name(self, text):
        """
        Sets the name of the section.

        Parameters
        ----------
        text : str
            The name to be set for the section.
        """
        self.name = text
        return self


def store_point(point, dct):
    """
    Stores the coordinates of a given point and updates the provided 
    dictionary with sums and counts.

    Parameters
    ----------
    point : Point
        The point whose coordinates are to be stored.
    dct : dict
        A dictionary to store the sums and counts of the coordinates. 
        The dictionary should have the following keys:
        - "x_sum": Sum of all x-coordinates.
        - "y_sum": Sum of all y-coordinates.
        - "n": Count of points.
        - "xy_sum": Sum of the product of x and y coordinates.
        - "sum_x_sq": Sum of the squares of x-coordinates.
    """
    x = point.getX()
    y = point.getY()
    dct["x_sum"] += x
    dct["y_sum"] += y
    dct["n"] += 1
    dct["xy_sum"] += (x * y)
    dct["sum_x_sq"] += (x ** 2)


def draw_point(point, window, lst):
    """
    Draws a point on the given window and adds it to the list of drawn points.

    Parameters
    ----------
    point : Point
        The point to be drawn.
    window : GraphWin
        The window where the point will be drawn.
    lst : list
        A list to store the drawn point (as a Circle object).
    """
    win = window
    circle = Circle(point, 0.5)
    circle.setOutline("black")
    circle.setFill("black")
    circle.draw(win)
    lst.append(circle)


def reset_field(lst, dct):
    """
    Resets the drawing field by undrawing all items in the list and resetting 
    the dictionary values.

    Parameters
    ----------
    win : GraphWin
        The window where the items are drawn.
    lst : list
        A list of drawable items (e.g., Circle objects) to be undrawn.
    dct : dict
        A dictionary to reset the sums and counts of the coordinates. 
        The dictionary should have the following keys:
        - "x_sum": Sum of all x-coordinates.
        - "y_sum": Sum of all y-coordinates.
        - "n": Count of points.
        - "xy_sum": Sum of the product of x and y coordinates.
        - "sum_x_sq": Sum of the squares of x-coordinates.
    """
    for item in lst:
        item.undraw()
    for key in dct:
        dct[key] = 0


def calculate_regression(dct, sec, window):
    """
    Calculates the slope of the regression line based on the provided data.

    Parameters
    ----------
    dct : dict
        A dictionary containing the sums and counts of the coordinates. 
        The dictionary should have the following keys:
        - "x_sum": Sum of all x-coordinates.
        - "y_sum": Sum of all y-coordinates.
        - "n": Count of points.
        - "xy_sum": Sum of the product of x and y coordinates.
        - "sum_x_sq": Sum of the squares of x-coordinates.
    sec : Section
        The section where any warning messages will be displayed.
    window : GraphWin
        The window where the section will be drawn.

    Returns
    -------
    float or None
        The slope of the regression line if calculation is successful, 
        None if there is a division by zero error.
    """
    n = dct["n"]
    y_bar = dct["y_sum"] / n
    x_bar = dct["x_sum"] / n
    m_top = dct["xy_sum"] - (n * x_bar * y_bar)
    m_bottom = dct["sum_x_sq"] - (n * (x_bar ** 2))

    if m_bottom == 0:
        sec.draw_section(window, ("WARNING: Divison by Zero inevitable.\n"
                                  "Hit 'Start Over' to reenter your points."))
        return None
    m = m_top / m_bottom
    return m


def get_leftmost_x(lst):
    """
    Finds the leftmost x-coordinate from a list of drawable items.

    Parameters
    ----------
    lst : list
        A list of drawable items (e.g., Circle objects).

    Returns
    -------
    float
        The leftmost x-coordinate.
    """
    leftmost_x = 200
    for item in lst:
        leftmost_x = min(leftmost_x, item.getCenter().getX())

    return leftmost_x


def get_rightmost_x(lst):
    """
    Finds the rightmost x-coordinate from a list of drawable items.

    Parameters
    ----------
    lst : list
        A list of drawable items (e.g., Circle objects).

    Returns
    -------
    float
        The rightmost x-coordinate.
    """
    rightmost_x = 0
    for item in lst:
        rightmost_x = max(rightmost_x, item.getCenter().getX())

    return rightmost_x


def get_regression_line(left_x, right_x, dct, sec, window):
    """
    Calculates the regression line based on the provided data and returns 
    it as a Line object.

    Parameters
    ----------
    left_x : float
        The leftmost x-coordinate.
    right_x : float
        The rightmost x-coordinate.
    dct : dict
        A dictionary containing the sums and counts of the coordinates. The 
        dictionary should have the following keys:
        - "x_sum": Sum of all x-coordinates.
        - "y_sum": Sum of all y-coordinates.
        - "n": Count of points.
        - "xy_sum": Sum of the product of x and y coordinates.
        - "sum_x_sq": Sum of the squares of x-coordinates.
    sec : Section
        The section where any warning messages will be displayed.
    window : GraphWin
        The window where the section will be drawn.

    Returns
    -------
    Line or None
        A Line object representing the regression line if calculation is 
        successful, None if there is a division by zero error.
    """
    n = dct["n"]
    y_bar = dct["y_sum"] / n
    x_bar = dct["x_sum"] / n
    m = calculate_regression(dct, sec, window)
    if m is None:
        return None
    left_y = y_bar + (m * (left_x - x_bar))
    right_y = y_bar + (m * (right_x - x_bar))
    left_point = Point(left_x, left_y)
    right_point = Point(right_x, right_y)

    return Line(left_point, right_point)


def main():
    """
    Runs the main loop for the manual regression plotting program.
    Initializes the graphical components and handles user interactions.
    """
    # Initialize graphical components
    win = GraphWin("Regression", 1280, 720)
    win.setCoords(0, 0, 200, 200)

    sidebar = Section(Point(140, 15), Point(200, 200), "lightgray", "black")
    footer = Section(Point(0, 0), Point(140, 15), "lightgray", "black")
    output = Section(Point(140, 0), Point(200, 15), "lightblue", "black")
    sidebar.draw_section(win)
    footer.draw_section(win)
    output.draw_section(win, "Enter at least 10 points, then hit 'Calculate'")
    done_button = Section(Point(0, 0), Point(15, 15), "white", "black")
    again_button = Section(Point(20, 0), Point(35, 15), "white", "black")
    quit_button = Section(Point(40, 0), Point(55, 15), "white", "black")
    done_button.set_name("Calculate").draw_section(win, done_button.name)
    again_button.set_name("Start Over").draw_section(win, again_button.name)
    quit_button.set_name("Exit Program").draw_section(win, quit_button.name)

    # Initialize variables
    point_list = []
    x_y_dict = {"x_sum": 0,
                "y_sum": 0,
                "n": 0,
                "xy_sum": 0,
                "sum_x_sq": 0,
                }
    # Main logic for drawing points and registering click events
    while True:
        click_loc = win.getMouse()
        if done_button.point_in_section(click_loc):
            # Click the Done button to calculate the slope and draw the line
            if x_y_dict["n"] < 10:
                output.draw_section(
                    win,
                    (f"Enter at least {10 - x_y_dict["n"]} more points before"
                     " hitting 'Calculate'")
                )
                continue
            reg_val = calculate_regression(x_y_dict, output, win)
            reg_line =  get_regression_line(
                get_leftmost_x(point_list),
                get_rightmost_x(point_list),
                x_y_dict, output, win)
            reg_line.draw(win)
            calc_text = (f"The slope of the regression line is: {reg_val:.4f}\n"
                         "Start Over or Exit Program?")
            output.draw_section(win, calc_text)

        elif again_button.point_in_section(click_loc):
            # Click the Start Over button, erase the points, clear the lists
            reset_field(point_list, x_y_dict)
            try:
                reg_line.undraw()
            except UnboundLocalError:
                print("reg_line not yet set")
            point_list = []

        elif quit_button.point_in_section(click_loc):
            # Click the Exit Program button to quit
            output.draw_section(win, "Hit 'Exit' again to close the window.")

            if quit_button.point_in_section(win.getMouse()):
                break

            output.draw_section(win, "Enter your points, then hit 'Calculate'")
            continue

        else:    # Otherwise, store and draw points
            store_point(click_loc, x_y_dict)
            draw_point(click_loc, win, point_list)
            n_points = x_y_dict["n"]
            if n_points < 10:
                op_text = f"Enter at least {10 - n_points} more points, then hit 'Calculate'"
            else:
                op_text = "Finish entering your points, then hit 'Calculate'"
            output.draw_section(win, op_text)

    win.close()

if __name__ == "__main__":
    main()
