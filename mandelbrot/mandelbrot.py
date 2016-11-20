from cImage import EmptyImage, ImageWin, Pixel


###########################################################################
# Given a pixel, calculate and return its intensity (ie, Red + Green + Blue).
###########################################################################
def instensity(pixel):
    return sum(pixel.getColorTuple())


###########################################################################
# Given an integer n, generate a list of n RGB colors,
# sorted by intensity.  Return a list of Pixels named 'color_list'
###########################################################################
def generate_random_color_table(n):
    from random import randint
    color_list = [Pixel(randint(0, 255), randint(0, 255), randint(0, 255))
                  for i in range(n)]
    color_list.sort(key=lambda p: instensity(p), reverse=True)
    return color_list


###########################################################################
# Check if the point (x,y) is close to the image's border.
###########################################################################
def is_close_to_border(x, y):
    threshold = 10
    return not (
        threshold < x < (window_size - threshold) and
        threshold < y < (window_size - threshold)
    )


###########################################################################
# The Mandelbrot function returns the escape value for a complex number c.
# If the algorithm does not escape within N iterations, return N.
# Do not modify this function.
###########################################################################
def escape_value(c, N):
    z = 0
    for n in range(N):
        if abs(z) > 2:
            return n
        z = z * z + c
    return N


###########################################################################
# Input:
#    img: the image to be modified
#    lower_x: the lower x bound of the Mandelbrot range
#    upper_x: the upper x bound of the Mandelbrot range
#    lower_y: the lower y bound of the Mandelbrot range
#    upper_y: the upper y bound of the Mandelbrot range
#
#    Determine the color of each pixel in the image, according to the
#    Mandelbrot set. You will need to scale x and y values into the
#    Mandelbrot range, and supply a complex number c
#    to escape_value(c, N), whose return value
#    will indicate which color should be chosen.
###########################################################################
def draw_at(img, lower_x, upper_x, lower_y, upper_y):
    black = Pixel(0, 0, 0)

    for i in range(window_size):
        for j in range(window_size):
            x = lower_x + i * Lx / window_size
            y = lower_y + j * Ly / window_size

            c = complex(x, y)
            value = escape_value(c, N)
            img.setPixel(i, j, black if value == N else color_list[value])


###########################################################################
# Main function
# You will need to create an initial Mandelbrot image with the initial range
# Specified here.  Your program should also allow the user to zoom up to
# three times: each zoom scales the image by a factor of 2, and will centre
# the new image on the location clicked in the previous step.  After 3 zooms,
# a click will close the image.  If the user clicks too close to the edge
# of the image, the image will close.
###########################################################################
def main():
    global N, window_size, color_list, Lx, Ly
    # settings
    window_size = 200
    N = 150
    color_list = []

    # initial mandelbrot set range
    lower_x = -3
    upper_x = 1
    lower_y = -2
    upper_y = 2

    zoom_factor = 2.0
    zoom_max_times = 3

    Lx = (upper_x - lower_x) * 1.0
    Ly = (upper_y - lower_y) * 1.0

    win = ImageWin('Mandelbrot', window_size, window_size)
    image = EmptyImage(window_size, window_size)
    color_list = generate_random_color_table(N)

    # init draw
    draw_at(image, lower_x, upper_x, lower_y, upper_y)
    image.draw(win)

    # click to zoom in
    count = 0
    while count < zoom_max_times:
        count += 1
        x, y = win.getMouse()

        if is_close_to_border(x, y):
            break

        mx = lower_x + x * Lx / window_size
        my = lower_y + y * Ly / window_size

        Lx, Ly = Lx / 2, Ly / 2

        lower_x = mx - Lx / zoom_factor
        upper_x = mx + Lx / zoom_factor
        lower_y = my - Ly / zoom_factor
        upper_y = my + Ly / zoom_factor

        draw_at(image, lower_x, upper_x, lower_y, upper_y)
        image.draw(win)

    if count == zoom_max_times:
        win.exitOnClick()
    else:
        win._close()


if __name__ == '__main__':
    main()
