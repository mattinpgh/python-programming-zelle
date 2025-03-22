"""
Access an image, convert it to grayscale using a weighted average per pixel
"""

from graphics import *

def main():
    win = GraphWin("Convert to Grayscale", 1065, 1070)
    win.setCoords(0, 0, 100, 100)

    image_to_change = Image(Point(50, 50), "test_image.gif")
    image_to_change.draw(win)
    image_width = image_to_change.getWidth()
    image_height = image_to_change.getHeight()

    for x in range(image_width):
        win.update()
        for y in range(image_height):
            r, g, b = image_to_change.getPixel(x, y)
            brightness = int(round(0.299 * r + 0.587 * g + 0.114 * b))
            image_to_change.setPixel(x, y, color_rgb(brightness, brightness, brightness))

    print(f"Image width is {image_width}, height is {image_height}")
    image_to_change.save("haha.gif")
    win.getMouse()

main()
