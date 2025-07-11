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



# Add a sidebar section for app information and controls
st.sidebar.title('Image Filtering Web Application')  # Sidebar title

# Create an expandable section in the sidebar to display app description
with st.sidebar.expander("Web App Description"):
    st.write(
        "This image filtering application allows you to upload an image and choose from various filters to apply. "
        "After applying a filter, you can download the filtered image if desired. "
        "Supported file formats are 'jpg', 'jpeg', and 'png'."
    )

# File uploader widget to allow users to upload images of specific types
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert the uploaded file to a numpy array of bytes
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)

    # Decode the image bytes into an OpenCV image (BGR format)
    img = cv2.imdecode(file_bytes, 1)

    # Convert the OpenCV image from BGR to RGB color format for proper display
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

 

    # List of all available filter options for the user to choose from
    filter_names = [
        "Grayscale", "Blur", "Canny", "Sobel", "Invert",
        "Cartoon", "Normal Pencil Sketch", "Colored Pencil Sketch",
        "Red", "Blue", "Green", "Yellow", "Magenta", "Turquoise"
    ]
    
    # Sidebar radio buttons to allow the user to select one filter from the list
    filter_choice = st.sidebar.radio("Select a filter", filter_names)
    
    # If the selected filter is 'Blur', provide a slider to control blur intensity
    # For all other filters, intensity is set to zero (not used)
    if filter_choice == "Blur":
        intensity = st.sidebar.slider("Blur Intensity", min_value=0, max_value=30, step=1, value=5)
    else:
        intensity = 0
    
    # Apply the selected filter with the specified intensity to the uploaded image
    filtered_img = apply_filter(filter_choice, img, intensity)
    
    # Function to save the filtered image to the 'Output_Folder' directory
    def save_image(image, filename):
        filepath = f'Output_Folder/{filename}'
        image.save(filepath)  # Save the PIL Image object to disk
        st.success(f'Saved {filename} to {filepath}')  # Notify user of successful save

    
    
    
    
    # Create two equal-width columns for displaying images side-by-side
    left_colu, right_colu = st.columns(2)  
    
    # Display the original uploaded image in the left column with caption
    with left_colu:
        st.image([img], caption=["Original"], use_column_width=True)
    
    # Display the filtered image in the right column with caption of the filter applied
    with right_colu:
        st.image([filtered_img], caption=[filter_choice], use_column_width=True)
    
        # Provide a button below the filtered image to allow the user to download it
        if st.button("Download Filtered Image"):
            # Convert the filtered NumPy image array back to a PIL Image for saving
            filtered_pil = Image.fromarray(filtered_img)
            # Save the filtered image with a descriptive filename including filter name and original filename
            save_image(filtered_pil, f'{filter_choice}_{uploaded_file.name}.png')

