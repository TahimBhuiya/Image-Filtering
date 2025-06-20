import cv2  # Import the OpenCV library for image processing

# Define a function to apply a specified filter to an image with a given intensity
def apply_filter(filter_name, img, intensity):
    if filter_name == "Grayscale":
        # Convert the image from BGR (OpenCV default) to RGB for consistency
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Convert the RGB image to grayscale
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    
        elif filter_name == "Blur":
            img = cv2.GaussianBlur(img, (int(intensity)*2+1, int(intensity)*2+1), 0) #using GaussianBlur to blur the image given and will be provided with an intensity setter which is in the main file
        elif filter_name == "Canny":
            img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            img = cv2.Canny(img, 100, 200)  #uses canny
        elif filter_name == "Sobel":
            img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            img = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3) #uses sobel
        elif filter_name == "Invert":
            img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            img=img.copy() #inverting the images colors
            for i in range(3):
                img[:,:,i]=255-img[:,:,i]
            # img = cv2.bitwise_not(img) could've also been used here.
        elif filter_name == "Red":
            img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #making red filter
            img=img.copy()
            img[::,::,1:3]=0

        elif filter_name == "Blue":
            img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            img=img.copy()
            img[::,::,0:2]=0  #making blue filter
            
            
        elif filter_name == "Green":
            img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            img=img.copy()
            img[::,:,[0,2]] = 0  #making green filter
            
        elif filter_name == "Yellow":
            img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            img=img.copy()
            img[::,::,2:3]=0  #making yellow filter
            
        elif filter_name == "Magenta":
            img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            img=img.copy()
            img[::,::,1:2]=0  #making magenta filter
            
        elif filter_name == "Turquoise":
            img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            img=img.copy()
            img[::,::,0:1]=0  #making Turquoise filter
        
        elif filter_name == "Cartoon":
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 5)
            edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
            color = cv2.bilateralFilter(img, 9, 250, 250)
            img = cv2.bitwise_and(color, color, mask=edges)  #making cartoon filter with aid of provided website in 'Final Project Supporting Material'
            
        elif filter_name=="Normal Pencil Sketch":
            img,cartoon_image2  = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.5, shade_factor=0.02)   #making pencil sketch filter with aid of provided website in 'Final Project Supporting Material'
            
        elif filter_name=="Colored Pencil Sketch":
            cartoon_image1,img  = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.5, shade_factor=0.02)   #making colored pencil sketch filter with aid of provided website in 'Final Project Supporting Material'
            
        return img #returning img no matter which filter is being used and will be displayed to the user
