import argparse

from PIL import Image


def user_input():

    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Remove metadata from an image file.")
    parser.add_argument("img", help="Path to the image file.")

    # Parse arguments
    args = parser.parse_args()

    return args.img


def clear_metadata(image_name: str) -> None:
    # Open the image
    with Image.open(image_name) as img:
        # Ensure img is of correct type
        if not isinstance(img, Image.Image):
            raise ValueError("The file could not be opened as an image.")

        # Read the image data, but exclude the metadata
        info = list(img.getdata())

        # Create a new image with the same data, minus the metadata
        image_no_meta = Image.new(img.mode, img.size)
        image_no_meta.putdata(info)

        # Overwrite the old image with the new one, thus erasing the original metadata
        image_no_meta.save(image_name)

    print(f"Metadata has been cleared from {image_name}")

# Request user input
path = user_input()

clear_metadata(path)
