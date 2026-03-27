from PIL import Image
from pillow_heif import register_heif_opener
import os

def heic_to_jpg(input_file, count_all, count):

    print(f"Converting: {input_file} ({count}/{count_all})")

    register_heif_opener()

    img = Image.open(input_file)

    output_file = os.path.splitext("photos_input/" + os.path.basename(input_file))[0] + ".jpg"

    img.convert('RGB').save(
        output_file, 
        "JPEG", 
        quality=100, 
        subsampling=0, 
        icc_profile=img.info.get("icc_profile")
    )

    os.remove(input_file)