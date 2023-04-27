# Image Filtering App Made with Streamlit

This is an image filtering app created using the Python language that consists of help with several diffeent modules and libraries. The app allows for the user to upload a file, which must be a 'JPG','JPEG', or a 'PNG' file. After the image is uploaded by the user, there are several different filter options that are provided for the user to choose from (14 filters total). The original image is displayed under the file uploader on the left-hand side of the page. The newly created filtered imaged is displayed to right of the original image and has a caption referring to which filter was applied to the image. Under the filtered image lies a 'Download Filtered Image' button that will can be used if the user wishes to save and download the filtered version of the uploaded image.

# Prerequisites

Python 3
OpenCV
Streamlit
Numpy
Pillow


# Running the Appication

In order to run this application, the user has to download the required libraries that were listed in the prerequisites. Next, the contents of the 'Tahim_Bhuiya_COP2034_app.py' file will need to be saved as well as the 'filters.py' file which are extremely crucial for the funcionality of this app as the 'Tahim_Bhuiya_COP2034_app.py' is the main file for running the streamlit app and the 'filters.py' file contains all of the filters for the app. The user will then have to open up the terminal and find their way to the directory where the file is saved and run the followng code: 

'streamlit run Tahim_Bhuiya_COP2034_app.py'

if the user saved the contents of 'Tahim_Bhuiya_COP2034_app.py' to another .py file, then they would run a similar code but replace the file name with whatever file name the user gave the new .py file:

'streamlit run filename.py'

The page may automatically open up in the user's browser or a URL will be given to transition to the running app.

# How to Use the App Once Up and Running

Once the app is open in the browser, the user will finally be able to use the app to their liking by following the steps below:
1. Upload a 'JPG','JPEG', or a 'PNG' image file by clicking on the image uploader in the middle of the page under the creator's name, project, and date. If the user simply wants to try the app out, there are several sample images in the 'Images_Folder' folder.
2. Select which filter the user would like to use on the left sidebar using the radio button located beneath the app description.
3. Certain filters, such as the 'Blur' filter have the option to change the intensity at which the filter operates with the use of a slider ranging from 0-30 in intensity. Adjust this to your liking.
4. The filtered image will be displayed alongside the original image under the file uploader with captions allowing for the user to differentiate between the original and the newly filtered image. The filtered image is on the right side and the original image is on the left side.
5. Below the filtered image, there is a 'Download Filtered Image' button that can be used to download the new image if the user would like to do so. This image will be downloaded in the 'Output_Folder' folder which is within the same folder of your other files.
6. The user could do this with as many photos as they would like but each photo will be filtered one at a time.


# Creators of App
This app was created by Tahim Bhuiya as a part of a final project for COP2034
