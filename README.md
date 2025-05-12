
          Here's a **complete example** of **number plate detection using OpenCV**, along with a **README.md file** suitable for a GitHub repository.

---

## 🚗 Number Plate Detection Using OpenCV

This project demonstrates how to detect vehicle number plates in images using **OpenCV** and **Haar Cascade Classifier**.

---

### ✅ Requirements

- Python 3.x
- OpenCV (`pip install opencv-python` or `opencv-python-headless`)
- Optional: `imutils` (for image resizing)

Install dependencies:

```bash
pip install opencv-python imutils
```

---

### 📁 Project Structure

```
number-plate-detection/
├── detect_plates.py
├── test_images/
│   └── car1.jpg
├── output/
│   └── (detected plates will be saved here)
└── README.md
```

---

### 🧠 Code: `detect_plates.py`

```python
import cv2
import os
from imutils import resize

# Load the pre-trained Haar Cascade classifier for license plates
plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')

# Input and output directories
input_folder = 'test_images/'
output_folder = 'output/'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def detect_plates(image_path, output_path):
    # Read image
    img = cv2.imread(image_path)
    if img is None:
        print(f"[ERROR] Unable to read image {image_path}")
        return

    # Resize for faster processing
    img = resize(img, width=600)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect plates
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around plates
    for (x, y, w, h) in plates:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi = img[y:y+h, x:x+w]
        cv2.imwrite(output_path, roi)

    # Save result
    result_path = os.path.join(output_folder, "detected_" + os.path.basename(image_path))
    cv2.imwrite(result_path, img)
    print(f"[INFO] Detected {len(plates)} license plate(s) in {image_path}. Saved to {result_path}")

# Process all images in input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        detect_plates(os.path.join(input_folder, filename), os.path.join(output_folder, filename))

print("[INFO] Processing complete.")
```

---

### 📄 Sample Test Image

Place an image like `car1.jpg` inside the `test_images/` directory.

---

### 📝 README.md

```markdown
# License Plate Detection using OpenCV

This project detects vehicle license plates from images using the **Haar Cascade Classifier** provided by OpenCV.

## 🔍 Features

- Detects license plates in images.
- Crops and saves detected license plates.
- Uses built-in `haarcascade_russian_plate_number.xml`.

## 🛠️ Requirements

Ensure you have the following installed:

- Python 3.x
- OpenCV (`pip install opencv-python`)
- Imutils (optional): `pip install imutils`

## 📦 Directory Structure

```
number-plate-detection/
├── detect_plates.py
├── test_images/
│   └── car1.jpg
├── output/
└── README.md
```

## ▶️ How to Run

1. Clone this repo:

```bash
git clone https://github.com/yourusername/number-plate-detection.git
cd number-plate-detection
```

2. Place your test images in the `test_images/` folder.

3. Run the script:

```bash
python detect_plates.py
```

4. Check the `output/` folder for results.

## 🖼️ Output

The script generates two outputs per image:
- A full image with detected plates highlighted.
- Cropped ROI (Region of Interest) of each detected license plate.

## 📌 Notes

- This model works best on frontal views of vehicles.
- Accuracy may vary depending on lighting, angle, and image quality.

## 📚 Credits

Uses [OpenCV's Haar Cascade for Russian license plates](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_russian_plate_number.xml).

## 📝 License

MIT License
```
