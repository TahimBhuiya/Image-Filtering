import cv2  # Import the OpenCV library for image processing

# Define a function to apply a specified filter to an image with a given intensity
def apply_filter(filter_name, img, intensity):
    if filter_name == "Grayscale":
        # Convert the image from BGR (OpenCV default) to RGB for consistency
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Convert the RGB image to grayscale
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


        elif filter_name == "Blur":
            # Apply Gaussian blur to the image
            # The kernel size is calculated based on the intensity value: it must be odd, so we use (intensity * 2 + 1)
            # A higher intensity results in a stronger blur effect
            img = cv2.GaussianBlur(img, (int(intensity)*2 + 1, int(intensity)*2 + 1), 0)

        elif filter_name == "Canny":
            # Convert image from BGR to RGB before edge detection for consistency
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Apply Canny edge detection with fixed threshold values (100 for lower, 200 for upper)
            # This highlights edges and outlines in the image
            img = cv2.Canny(img, 100, 200)


    
        elif filter_name == "Sobel":
            # Convert image from BGR to RGB before applying Sobel filter
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Apply the Sobel filter to detect edges in the horizontal (x) direction
            # cv2.CV_8U specifies the output image depth
            # dx=1, dy=0 applies the derivative in the x-direction only
            img = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)

        elif filter_name == "Invert":
            # Convert image from BGR to RGB before inverting colors
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Create a copy of the image to avoid modifying the original
            img = img.copy()

            # Invert each color channel manually by subtracting from 255
            for i in range(3):
                img[:, :, i] = 255 - img[:, :, i]

            # Note: The same effect could also be achieved using:
            # img = cv2.bitwise_not(img)


    
        elif filter_name == "Red":
            # Convert image from BGR to RGB format
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Create a copy of the image to avoid modifying the original
            img = img.copy()

            # Set the Green and Blue channels to 0, keeping only the Red channel active
            img[:, :, 1:3] = 0  # Produces a red-tinted image

        elif filter_name == "Blue":
            # Convert image from BGR to RGB format
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Create a copy of the image to avoid modifying the original
            img = img.copy()

            # Set the Red and Green channels to 0, keeping only the Blue channel active
            img[:, :, 0:2] = 0  # Produces a blue-tinted image

            
            
        elif filter_name == "Green":
            # Convert image from BGR to RGB format
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Create a copy to preserve the original image
            img = img.copy()

            # Set the Red (0) and Blue (2) channels to 0, keeping only the Green channel active
            img[:, :, [0, 2]] = 0  # Produces a green-tinted image

        elif filter_name == "Yellow":
            # Convert image from BGR to RGB format
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Create a copy to preserve the original image
            img = img.copy()

            # Set the Blue channel (index 2) to 0, leaving Red and Green active to produce yellow
            img[:, :, 2:3] = 0  # Produces a yellow-tinted image (Red + Green)


    
            
        elif filter_name == "Magenta":
            # Convert image from BGR to RGB format
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Create a copy to avoid modifying the original image
            img = img.copy()

            # Set the Green channel (index 1) to 0, keeping Red and Blue active
            # This results in a magenta-tinted image (Red + Blue)
            img[:, :, 1:2] = 0  # Produces a magenta filter

        elif filter_name == "Turquoise":
            # Convert image from BGR to RGB format
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Create a copy to avoid modifying the original image
            img = img.copy()

            # Set the Red channel (index 0) to 0, keeping Green and Blue active
            # This results in a turquoise/cyan-tinted image (Green + Blue)
            img[:, :, 0:1] = 0  # Produces a turquoise filter

            
        
        elif filter_name == "Cartoon":
            # Convert the original image to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Apply median blur to reduce image noise
            gray = cv2.medianBlur(gray, 5)

            # Detect edges using adaptive thresholding
            edges = cv2.adaptiveThreshold(
                gray, 255,
                cv2.ADAPTIVE_THRESH_MEAN_C,
                cv2.THRESH_BINARY,
                blockSize=9,
                C=9
            )

            # Apply bilateral filter to smooth colors while preserving edges
            color = cv2.bilateralFilter(img, d=9, sigmaColor=250, sigmaSpace=250)

            # Combine the smoothed color image with the detected edges to produce a cartoon effect
            img = cv2.bitwise_and(color, color, mask=edges)

            # Cartoon effect inspired by technique referenced from 'Final Project Supporting Material'

            
        elif filter_name=="Normal Pencil Sketch":
            img,cartoon_image2  = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.5, shade_factor=0.02)   #making pencil sketch filter with aid of provided website in 'Final Project Supporting Material'
            
        elif filter_name=="Colored Pencil Sketch":
            cartoon_image1,img  = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.5, shade_factor=0.02)   #making colored pencil sketch filter with aid of provided website in 'Final Project Supporting Material'
            
        return img #returning img no matter which filter is being used and will be displayed to the user
