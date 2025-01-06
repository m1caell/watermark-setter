# Image Watermarking with EXIF Orientation Handling

This Python script adds a watermark to images in a specified folder and ensures that the image is rotated according to its EXIF orientation metadata (if available). The script supports multiple image formats and processes all images in the input folder, saving the output with watermarks to a specified output folder.

## Features

- Adds a watermark to images.
- Automatically handles image orientation based on EXIF metadata.
- Processes multiple image formats (PNG, JPG, JPEG, BMP, GIF).
- Resizes the watermark to a percentage of the base image's width.
- Places the watermark in the bottom-right corner with a margin.

## How to use
- Create a folder named 'images' in the same directory as the main file. When you start the script, it will look for images in this folder and create a new folder called 'images-with-watermark' containing the processed images with watermarks.
- Ensure that there is a PNG image named 'watermark' in the same directory structure, as this image will be used as the watermark.

## Requirements

- Python 3.x
- [Pillow](https://pillow.readthedocs.io/en/stable/) library for image processing.

## Installation

1. Clone the repository or download the script files.
   
2. Install the required dependencies:
   ```bash
   pip install -r ./requirements
   ```

## Build

```bash
pyinstaller --onefile main.py
```