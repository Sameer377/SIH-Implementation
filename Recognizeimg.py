import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import openai

# Set OpenAI API key for text generation (replace with your actual key)


# Load CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Function to recognize image using CLIP
def recognize_image(image_path):
    image = Image.open(image_path)

    # Preprocess the image
    inputs = processor(images=image, return_tensors="pt", padding=True)
    
    # Extract the image features
    outputs = model.get_image_features(**inputs)
    
    # Return the features (usually we compare them with text embeddings for more specific recognition)
    return outputs

# Generate text description based on image recognition
def generate_description(recognized_objects):
    # Use GPT-based model to generate a description based on recognized objects
    prompt = f"This image contains: {recognized_objects}. Can you generate a short description of this scene?"

    # Generate a response using OpenAI GPT-3/4 API
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=100
    )
    
    return response.choices[0].text.strip()

# Example usage
if __name__ == "__main__":
    image_path = "D:\\OneDrive\\Desktop\\raw\\sameer.jpg" # Replace with the actual image file path

    # Recognize objects in the image
    recognized_objects = recognize_image(image_path)
    
    # Generate description based on recognized objects
    description = generate_description("a detailed representation of objects or features")

    # Output the description
    print("Generated Description: ", description)
