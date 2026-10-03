import pytesseract
from PIL import Image, ImageEnhance, ImageFilter, ImageOps


# Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def extract_text(image):

    # Convert image to RGB
    image = image.convert("RGB")

    # Get original size
    width, height = image.size

    # Increase image size for better OCR
    image = image.resize(
        (width * 3, height * 3)
    )

    # Convert to grayscale
    image = ImageOps.grayscale(image)

    # Improve contrast
    image = ImageEnhance.Contrast(image).enhance(2)

    # Sharpen image
    image = image.filter(ImageFilter.SHARPEN)

    # OCR
    text = pytesseract.image_to_string(
        image,
        config="--psm 11"
    )

    return text.strip()