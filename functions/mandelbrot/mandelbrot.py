import io
import numpy as np
import matplotlib.pyplot as plt

# def sample(c, max_iters):
#     """
#     Figures out if a given complex number 'c' is part of the set or not
#     Either returns the number of iterations required for divergence
#     or zero if the point does not diverge
#     """
#     z = 0.; n = 0
#     while abs(z) <= 2. and n < max_iters:
#         z = z**2+c
#         n += 1
#     return n if n != max_iters else 0


def sample_area(real_start, real_end, imag_start, image_end, max_iters, width, height):
    """
    Loops over an area and assigns points to the Mandelbrot set
    Thanks chatGPT for this vectorized version (although it was wrong to begin with)
    """
    x, y = np.meshgrid(np.linspace(real_start, real_end, width),
                       np.linspace(imag_start, image_end, height))
    mandelbrot_set = np.zeros((height, width))
    c = x + y * 1j       # Map x, y to their complex values
    z = np.zeros_like(c)  # Initialise the value of 'z' at each location
    for i in range(max_iters):
        z = z**2 + c              # Iterate
        mask = np.abs(z) > 2.     # Select points that are diverging
        # Set the value of the set to the number of iterations for divergence
        mandelbrot_set[mask] = i
        z[mask], c[mask] = 0., 0.  # Reset the diverging point so that it will not diverge in future
    return mandelbrot_set


def create_image(real_start, real_end, imag_start, image_end, max_iters, width, height,
                 cmap="cubehelix", figsize=(8, 8), dpi=150):
    """
    Create a png and return it as a binary
    """
    array = sample_area(real_start, real_end, imag_start,
                        image_end, max_iters, width, height)
    plt.subplots(figsize=figsize, dpi=dpi, frameon=False)
    plt.imshow(array, cmap=cmap)
    plt.xticks([])
    plt.yticks([])
    plt.tight_layout()
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png", bbox_inches='tight',
                pad_inches=0)  # Place the png as a binary in memory
    return buffer.getvalue()  # Return the png binary (avoids saving to disk)


# if __name__ == "__main__":

#     # Parameters for part of set
#     rmin, rmax = -1.5, 0.5
#     imin, imax = -1., 1.
#     max_iters = 50
#     width, height = 2000, 2000
#     file_name = "mandelbrot.png"

#     # Display an image on screen and simulatanouesly save it
#     create_image(rmin, rmax, imin, imax, max_iters, width, height)
#     plt.savefig("static/"+file_name, bbox_inches='tight', pad_inches=0)
#     plt.show()
#     plt.close()
