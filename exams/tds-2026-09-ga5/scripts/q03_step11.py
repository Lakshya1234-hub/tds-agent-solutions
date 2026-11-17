# Use PIL to read pixel values or detect number manually if possible
from PIL import Image
import pytesseract # Just in case it's actually installed as a library, if not I'll print color data

try:
    img = Image.open("roi.png")
    # Instead of OCR, print the image as a grid of values if small
    # But for a red ball number, usually just reading the center is enough
    print(list(img.getdata()))
except Exception as e:
    print(f"Error: {e}")
