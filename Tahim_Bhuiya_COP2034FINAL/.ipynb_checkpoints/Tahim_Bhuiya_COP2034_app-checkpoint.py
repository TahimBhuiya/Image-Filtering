# Import required libraries
import cv2                         # OpenCV for image processing
import streamlit as st             # Streamlit for creating the web app UI
import numpy as np                 # NumPy for numerical operations
from PIL import Image              # Pillow for handling image file formats
from filters import apply_filter   # Custom function to apply selected image filters

# Create a three-column layout: left, center, and right
left_column, mid_column, right_column = st.columns([1, 2, 1])  

# Load and display the FAU logo in the rightmost column
fau = Image.open("FAULOGO2.png")  # Load the FAU logo image
right_column.image(fau, caption="Florida Atlantic University")  # Display the logo with a caption

# Display project details in the center of the page
st.title('Tahim Bhuiya')                  # Student name
st.title('Final Project COP2034')         # Course/project title
st.title('05/03/2023')                    # Submission date



#Add sidebar with info
#Adding a text in the sidebar
st.sidebar.title('Image Filtering Web Application') #title
with st.sidebar.expander("Web App Description"): #add expander for description
    st.write("This image filtering application will be utilized to help pick and choose how you would like to filter your uploaded images with the filter options given after uploading!! If you would like to download the filtered image, you will also be given the option to do so!! Note that this app only accpets 'jpg, 'jpeg', and 'png' files!!") #App description!!!
    
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"]) #file uploader with the type being specified for image type files.
if uploaded_file is not None:
    # Read the image using OpenCV
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
 

    # Define a list of filter names
    filter_names = ["Grayscale", "Blur", "Canny", "Sobel", "Invert","Cartoon","Normal Pencil Sketch","Colored Pencil Sketch","Red","Blue","Green","Yellow","Magenta","Turquoise"]

    # Add radio buttons for selecting a filter
    filter_choice = st.sidebar.radio("Select a filter", filter_names)

    # Add intensity slider for the Blur filter
    if filter_choice == "Blur":
        intensity = st.sidebar.slider("Blur Intensity", min_value=0, max_value=30, step=1, value=5)
    else:
        intensity = 0

    # Apply the selected filter to the image
    filtered_img = apply_filter(filter_choice, img, intensity)
    
    
#Define a function to save the image
    def save_image(image, filename):
        filepath = f'Output_Folder/{filename}'
        image.save(filepath)
        st.success(f'Saved {filename} to {filepath}')
    
    
    
    
    left_colu, right_colu = st.columns(2) #will be used to have the download button under the filtered image

# Display the first image in the left column
    with left_colu:
        st.image([img],caption=["Original"], use_column_width=True)

# Display the second image in the right column
    with right_colu:
        st.image([filtered_img],caption=[filter_choice], use_column_width=True)
    # Add a button under the second image
        if st.button("Download Filtered Image"):
            filtered_pil = Image.fromarray(filtered_img)
            save_image(filtered_pil, f'{filter_choice}_{uploaded_file.name}.png') #calling the save_image fucntion and pplying to the selected filtered image
            #created the correct file name which will help identify which photo is which
