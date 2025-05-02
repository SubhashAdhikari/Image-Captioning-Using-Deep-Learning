from model.blip_model import load_model, generate_caption
from utils.image_upload import load_image

# Choose one:
# For local file:
# image_path = "data/sample_image.jpg"

# For online image:
image_path = "https://images.unsplash.com/photo-1533450718592-29d45635f0a9?fm=jpg&q=60"

# Load image
image = load_image(image_path)

# Load model
model, processor, device = load_model()

# Generate caption
caption = generate_caption(model, processor, image, device)
print("Caption:", caption)
