"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: Original image.
    :return: New image.
    """
    new_img = SimpleImage.blank(img.width, img.height)                      # Create blank image.
    for y in range(img.height):
        for x in range(img.width):
            pixel = new_img.get_pixel(x, y)                                 # Get (x, y)'s pixel.
            total_red = 0
            total_blur = 0
            total_green = 0
            total_num = 0
            for a in range(x-1, x+2):                                       # Get (x, y)'s surrounding location.
                if a > 0 and a < img.width - 1:
                    for b in range(y-1, y+2):
                        if b > 0 and b < img.height - 1:
                            total_red += img.get_pixel(a, b).red
                            total_blur += img.get_pixel(a, b).blue
                            total_green += img.get_pixel(a, b).green
                            total_num += 1
            pixel.red = total_red / total_num                               # To assign blur RGB value for new img.
            pixel.green = total_green / total_num
            pixel.blue = total_blur / total_num
    return new_img


def main():
    """
    To blur the original image.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
