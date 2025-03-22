"""
Write a program to convert an image to its color negative.
Subtract each color value from 255
"""

from graphics import *

def main():
    win = GraphWin("Convert to Negative", 1065, 1070)
    win.setCoords(0, 0, 100, 100)

    image_to_change = Image(Point(50, 50), "test_image.gif")
    image_to_change.draw(win)
    image_width = image_to_change.getWidth()
    image_height = image_to_change.getHeight()

    for x in range(image_width):
        win.update()
        for y in range(image_height):
            r, g, b = image_to_change.getPixel(x, y)
            image_to_change.setPixel(x, y, color_rgb(255-r, 255-g, 255-b))

    print(f"Image width is {image_width}, height is {image_height}")
    image_to_change.save("negative.png")
    win.getMouse()

main()