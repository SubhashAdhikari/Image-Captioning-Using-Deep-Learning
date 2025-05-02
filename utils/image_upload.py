from PIL import Image
import requests
import io
import os

def load_image(image_path):
    # If the path starts with http or https, treat it as a URL
    if image_path.startswith("http://") or image_path.startswith("https://"):
        try:
            response = requests.get(image_path)
            response.raise_for_status()  # Raises HTTPError if the download failed
            image = Image.open(io.BytesIO(response.content)).convert("RGB")
            return image
        except Exception as e:
            raise RuntimeError(f"Failed to load image from URL: {e}")
    
    # If it's a local file path
    elif os.path.exists(image_path):
        try:
            image = Image.open(image_path).convert("RGB")
            return image
        except Exception as e:
            raise RuntimeError(f"Failed to load image from file: {e}")
    
    # If neither a valid URL nor a local file
    else:
        raise FileNotFoundError(f"No valid image found at: {image_path}")
