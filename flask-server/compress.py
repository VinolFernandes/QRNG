from PIL import Image
import sys

arguments=sys.argv

image_path = arguments[1]
output_path = arguments[2]

def compress_image(image_path, output_path):
    # Open the image
    image = Image.open(image_path)
    
    # Resize the image while maintaining aspect ratio
    image.thumbnail((1000, 1000))
    
    # Save the resized image with compression
    image.save(output_path, optimize=True, quality=85)

# Example usage
compress_image(image_path, output_path)