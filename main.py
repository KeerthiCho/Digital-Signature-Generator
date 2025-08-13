# digital_signature.py
from PIL import Image, ImageDraw, ImageFont

def generate_signature(name, output_file="digital_signature.png"):
    """
    Generate a digital signature image from the given name.
    """
    width, height = 400, 100
    image = Image.new("RGB", (width, height), color="white")

    draw = ImageDraw.Draw(image)
    try:
        font = ImageFont.truetype("arial.ttf", 48)  # Change to cursive font if available
    except:
        font = ImageFont.load_default()
    draw.text((10, 25), name, fill="black", font=font)

    image.save(output_file)
    print(f"Digital signature saved as '{output_file}'")

if __name__ == "__main__":
    name_input = input("Enter your name: ")
    generate_signature(name_input)
