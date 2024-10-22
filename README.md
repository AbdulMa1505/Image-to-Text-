## Image to Text Converter using Tesseract and Python
## Overview
This project is a Python-based script that uses Tesseract OCR (Optical Character Recognition) to extract text from images. The program utilizes the pytesseract library to interface with Tesseract, and Pillow to handle image processing. The extracted text from the image is printed out in the console.

## Features
--Convert Images to Text: Converts images into readable text using the Tesseract OCR engine
--Supports Multiple Image Formats: Works with common image formats such as PNG, JPG, and WEBP.
--Simple to Use: The script allows easy image-to-text conversion with minimal setup.
## Requirement
--Python 3.x
--Tesseract OCR installed on your machine.
Python libraries:pytesseract,Pillow and os

## Troubleshooting
TesseractNotFoundError: Ensure Tesseract is installed and added to the system's PATH correctly. Test with tesseract --version in the command line.
FileNotFoundError: Verify that the image path is correct and that the image exists.
contributing