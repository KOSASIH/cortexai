import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import random

# Create the uploads directory if it doesn't exist
upload_dir = 'static/uploads'
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

# Function to create a placeholder MRI image
def create_mri_placeholder(filename, tumor_type):
    # Create a grayscale image (512x512 pixels)
    width, height = 512, 512
    img = Image.new('L', (width, height), color=0)
    draw = ImageDraw.Draw(img)
    
    # Draw a circle representing the brain
    brain_radius = 200
    draw.ellipse(
        (width//2 - brain_radius, height//2 - brain_radius, 
         width//2 + brain_radius, height//2 + brain_radius), 
        fill=100
    )
    
    # Add some random noise to make it look more like an MRI
    pixels = np.array(img)
    noise = np.random.normal(0, 10, (height, width))
    pixels = np.clip(pixels + noise, 0, 255).astype(np.uint8)
    img = Image.fromarray(pixels)
    draw = ImageDraw.Draw(img)
    
    # Draw a "tumor" based on the type
    if tumor_type == "Meningioma":
        # Draw a tumor at the edge of the brain
        tumor_x = width//2 + int(brain_radius * 0.7 * np.cos(np.pi/4))
        tumor_y = height//2 + int(brain_radius * 0.7 * np.sin(np.pi/4))
        tumor_radius = 40
        draw.ellipse(
            (tumor_x - tumor_radius, tumor_y - tumor_radius,
             tumor_x + tumor_radius, tumor_y + tumor_radius),
            fill=200
        )
    elif tumor_type == "Glioma":
        # Draw an irregular tumor inside the brain
        tumor_x = width//2 - 50
        tumor_y = height//2 + 30
        points = []
        for i in range(8):
            angle = 2 * np.pi * i / 8
            r = random.uniform(30, 60)
            points.append((tumor_x + int(r * np.cos(angle)), 
                          tumor_y + int(r * np.sin(angle))))
        draw.polygon(points, fill=180)
    elif tumor_type == "Pituitary Tumor":
        # Draw a small tumor in the center-bottom of the brain
        tumor_x = width//2
        tumor_y = height//2 + 100
        tumor_radius = 25
        draw.ellipse(
            (tumor_x - tumor_radius, tumor_y - tumor_radius,
             tumor_x + tumor_radius, tumor_y + tumor_radius),
            fill=220
        )
    
    # Add text label
    try:
        # Try to load a font, use default if not available
        font = ImageFont.truetype("arial.ttf", 20)
    except IOError:
        font = ImageFont.load_default()
    
    draw.text((10, 10), f"Sample {tumor_type} MRI", fill=255, font=font)
    
    # Save the image
    img.save(os.path.join(upload_dir, filename))
    print(f"Created {filename}")

# Create sample MRI images
samples = [
    {"filename": "meningioma_sample.jpg", "type": "Meningioma"},
    {"filename": "glioma_sample.jpg", "type": "Glioma"},
    {"filename": "pituitary_sample.jpg", "type": "Pituitary Tumor"}
]

for sample in samples:
    create_mri_placeholder(sample["filename"], sample["type"])

print("Sample creation complete!")