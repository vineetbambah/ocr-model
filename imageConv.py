from pdf2image import convert_from_path
from PIL import Image, ImageOps, ImageEnhance
from pathlib import Path
images = convert_from_path('./pdfs/input.pdf')
for i, image in enumerate(images):
    image.save(f'./images/page_{i}.png', 'PNG')


for file in Path('./images').iterdir():
    if file.is_file():
        img = Image.open(file)
        img = ImageOps.invert(img)
        img = ImageEnhance.Contrast(img).enhance(1.2)
        print(f'./images/inverted/inverted_{file.name}')
        img.save(f'./images/inverted/inverted_{file.name}', 'PNG')

