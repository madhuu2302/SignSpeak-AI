import pytesseract
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def extract_text(image):
    image = image.convert("RGB")
    width, height = image.size
    image = image.resize(
        (width * 3, height * 3)
    )

    image = ImageOps.grayscale(image)
    image = ImageEnhance.Contrast(image).enhance(2)
    image = image.filter(ImageFilter.SHARPEN)
    text = pytesseract.image_to_string(
        image,
        config="--psm 11"
    )

    return text.strip()
