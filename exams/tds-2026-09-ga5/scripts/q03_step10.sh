# Since I cannot 'look' at the PNG file, I will use tesseract to OCR the number from the ROI.
tesseract roi.png output
cat output.txt
