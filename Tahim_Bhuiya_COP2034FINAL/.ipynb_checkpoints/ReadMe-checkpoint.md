
# 🖼️ Image Filtering App using Streamlit

This is a simple and interactive image filtering web application built with **Python** and **Streamlit**. The app allows users to upload images (`.jpg`, `.jpeg`, or `.png`) and apply one of **14 different filters** to the uploaded image. After selecting a filter, the app displays the **original image** on the left and the **filtered version** on the right. Users can also **download** the filtered image with a single click.

---

## ✅ Features

- Upload image files (`.jpg`, `.jpeg`, `.png`)
- Apply 14 different image filters including:
  - Grayscale
  - Blur (with intensity control)
  - Canny, Sobel, Invert
  - Stylized (Cartoon, Pencil Sketches)
  - Color isolation filters (Red, Green, Blue, Yellow, Magenta, Turquoise)
- View original and filtered images side-by-side
- Download the filtered image directly

---

## 📦 Prerequisites

Make sure you have **Python 3** installed, along with the following libraries:

- `opencv-python`
- `streamlit`
- `numpy`
- `Pillow`

You can install them using pip:

```bash
pip install opencv-python streamlit numpy Pillow
```

---

## ▶️ Running the Application

1. Save the two necessary Python files:
   - `Tahim_Bhuiya_COP2034_app.py` (main Streamlit app)
   - `filters.py` (contains the filter logic)

2. Open a terminal or command prompt.

3. Navigate to the directory where the files are saved.

4. Run the Streamlit app:

```bash
streamlit run Tahim_Bhuiya_COP2034_app.py
```

> 🔁 If you renamed the main file, replace the filename accordingly:

```bash
streamlit run your_filename.py
```

Once executed, the app should open in your browser automatically. If not, Streamlit will provide a local URL that you can paste into your browser.

---

## 🧠 How to Use the App

1. **Upload an Image**  
   Click the uploader in the middle of the page and select a `.jpg`, `.jpeg`, or `.png` file.  
   (Sample images are available in the `Images_Folder` directory, if provided.)

2. **Choose a Filter**  
   Use the sidebar on the left to select a filter from the list using the radio buttons.

3. **Adjust Filter Intensity (Optional)**  
   If you select the **Blur** filter, an intensity slider will appear (range: 0–30). Adjust it as desired.

4. **View Results**  
   The original image will be shown on the left, and the filtered image on the right, both labeled accordingly.

5. **Download Filtered Image**  
   Below the filtered image, click the **"Download Filtered Image"** button. The image will be saved to the `Output_Folder`.

6. **Repeat**  
   You can upload and filter as many images as you'd like — one at a time.

---

## 👨‍💻 Creator

This app was developed by **Tahim Bhuiya** as a final project for the course **COP2034**.
