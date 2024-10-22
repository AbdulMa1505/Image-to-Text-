import pytesseract
import os
from PIL import Image

# path to tesseract 
pytesseract.pytesseract.tesseract_cmd = r"C:\\Path\\To\\Tesseract-OCR\\tesseract.exe"

def Convert():
    img_path = r'OCR/pal'  # Replace with your image file path
    if os.path.exists(img_path):
        img = Image.open(img_path)
        text = pytesseract.image_to_string(img)
        print(text)
    else:
        print(f"Image not found: {img_path}")

if __name__ == "__main__":
    Convert()
