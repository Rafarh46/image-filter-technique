import cvlib
import cv2
import numpy as np

def apply_filters(image):
    """
    Applies median, average, and Gaussian filters to the given image.
    """
    median = cv2.medianBlur(image, 5)
    average = cv2.blur(image, (5, 5))
    gaussian = cv2.GaussianBlur(image, (5, 5), 0)
    return median, average, gaussian

if __name__ == "__main__":
    # Load and read an example image

    image = cvlib.read_image("newcastle-beach.jpeg")

    # Apply filters
    median, average, gaussian = apply_filters(image)

    # Visualize original and filtered images
    cvlib.visualise_image(image,"Original")
    cvlib.visualise_image(median,"Median fliter")
    cvlib.visualise_image(average,"Average filter")
    cvlib.visualise_image(gaussian, "gaussian filter")