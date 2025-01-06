import os
from PIL import Image
from PIL.ExifTags import TAGS

input_folder = "./images"
output_folder = "./images-with-watermark"
watermark_image_path = "./watermark.png"

os.makedirs(output_folder, exist_ok=True)

def apply_exif_orientation(image):
    try:
        exif_data = image.getexif()

        if exif_data:
            for tag, value in exif_data.items():
                if TAGS.get(tag) == 'Orientation':
                    exif_orientation = value
                    if exif_orientation == 3:
                        image = image.rotate(180, expand=True)
                    elif exif_orientation == 6:
                        image = image.rotate(270, expand=True)
                    elif exif_orientation == 8:
                        image = image.rotate(90, expand=True)
                    break
                
    except (AttributeError, KeyError, IndexError):
        pass
    return image

def add_watermark(image_path, output_path, watermark_path):
    base_image = Image.open(image_path).convert("RGBA")
    base_image = apply_exif_orientation(base_image)
    watermark = Image.open(watermark_path).convert("RGBA")

    base_width, base_height = base_image.size
    watermark_width = int(base_width * 0.8)
    watermark_aspect_ratio = watermark.size[1] / watermark.size[0]
    watermark_height = int(watermark_width * watermark_aspect_ratio)
    watermark = watermark.resize((watermark_width, watermark_height), Image.Resampling.LANCZOS)

    x = (base_width - watermark_width) // 2
    y = (base_height - watermark_height) // 2

    transparent_layer = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
    transparent_layer.paste(watermark, (x, y), watermark)

    combined_image = Image.alpha_composite(base_image, transparent_layer)

    combined_image = combined_image.convert("RGB")
    combined_image.save(output_path)

def process_images():
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            output_path = os.path.join(output_folder, filename)
            add_watermark(input_path, output_path, watermark_image_path)
            print(f"Processed: {output_folder}/{filename}")

if __name__ == "__main__":
    process_images()