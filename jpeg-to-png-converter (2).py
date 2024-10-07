import os
from PIL import Image

def convert_jpeg_to_png(input_path, output_path):
    try:
        # Open the JPEG image
        with Image.open(input_path) as img:
            # Save as PNG
            img.save(output_path, 'PNG')
        print(f"Successfully converted {input_path} to {output_path}")
    except Exception as e:
        print(f"Error converting image: {e}")

def main():
    print("JPEG to PNG Converter")
    
    # Get input file path
    input_path = input("Enter the path to the JPEG file: ")
    
    # Check if file exists and is a JPEG
    if not os.path.exists(input_path):
        print("File does not exist.")
        return
    
    if not input_path.lower().endswith(('.jpg', '.jpeg')):
        print("File is not a JPEG.")
        return
    
    # Generate output file path
    output_path = os.path.splitext(input_path)[0] + ".png"
    
    # Convert JPEG to PNG
    convert_jpeg_to_png(input_path, output_path)

if __name__ == "__main__":
    main()
