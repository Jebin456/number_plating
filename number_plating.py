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
