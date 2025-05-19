import os
import urllib.request

# Create the uploads directory if it doesn't exist
upload_dir = 'static/uploads'
if not os.path.exists(upload_dir):
    os.makedirs(upload_dir)

# Sample MRI images URLs (these are example URLs, replace with actual MRI scan images)
sample_images = [
    {
        'url': 'https://www.researchgate.net/profile/Swe-Swe-Aung/publication/340266504/figure/fig2/AS:874510623846401@1585575260442/Axial-T1-weighted-MRI-brain-with-contrast-showing-homogeneously-enhancing-extra-axial.jpg',
        'filename': 'meningioma_sample.jpg',
        'type': 'Meningioma'
    },
    {
        'url': 'https://www.researchgate.net/profile/Swe-Swe-Aung/publication/340266504/figure/fig3/AS:874510623850497@1585575260526/Axial-T1-weighted-MRI-brain-with-contrast-showing-heterogeneously-enhancing-intra-axial.jpg',
        'filename': 'glioma_sample.jpg',
        'type': 'Glioma'
    },
    {
        'url': 'https://www.researchgate.net/profile/Swe-Swe-Aung/publication/340266504/figure/fig4/AS:874510623854593@1585575260608/Coronal-T1-weighted-MRI-brain-with-contrast-showing-homogeneously-enhancing-sellar-and.jpg',
        'filename': 'pituitary_sample.jpg',
        'type': 'Pituitary Tumor'
    }
]

# Download the sample images
for image in sample_images:
    try:
        print(f"Downloading {image['type']} sample image...")
        urllib.request.urlretrieve(image['url'], os.path.join(upload_dir, image['filename']))
        print(f"Downloaded {image['filename']}")
    except Exception as e:
        print(f"Error downloading {image['filename']}: {e}")

print("Sample download complete!")