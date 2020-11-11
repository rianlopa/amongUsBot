from PIL import ImageGrab
import pytesseract



img = ImageGrab.grab(bbox=(400,-30,2000,600))

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'
word = pytesseract.image_to_string(img)

img.show()
print(word)

