# rem_img_metadata.py

Rem_img_metadata.py is a Python application that removes metadata from images. This can be helpful when uploading images to a blog, for example, as EXIF metadata increases the size of the image. The smaller the image is, the faster the page can load, thus resulting in an SEO improvement.

A tool like this can also help maintain some level of privacy on social media by removing location metadata when uploading images. However, this tool has been created for learning purposes only and should thus not be used for real-world purposes.

Below is the program's source code. Scroll down to see a [line-by-line explanation](#code-explanation) of what the code is doing.

```python
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
```


## Code Explanation

### User Input

Before the metadata can be stripped, first the user must point the program to the right file. This is achieved through `argparse`, which allows the user to give the path as an argument in the terminal.

```python
parser = argparse.ArgumentParser(description="Remove metadata from an image file.")
```

The code above sets up the argument parsing.

```python
parser.add_argument("img", help="Path to the image file.")
```

Once argument parsing has been set up, we need to provide it with possible arguments. In this case, there is only one possible argument: the path to the image.

```python
args = parser.parse_args()
    return args.img
```

The arguments are then parsed, and the path to the image is returned to the main block variable `path = user_input()`

### The Path

```python
clear_metadata(path)
```

Once the path has been determined, the `clear_metadata(path)` function will be called, and the path is passed along.

### Clear Metadata

```python
def clear_metadata(image_name: str) -> None:
```

First, let us examine the function itself. `: str` tells the compiler that `image_name` is expected to be a string, whilst `-> None` signifies that the function does not return anything.

```python
with Image.open(image_name) as img:
```

The code above opens the actual image.

```python
if not isinstance(img, Image.Image):
            raise ValueError("The file could not be opened as an image.")
```

The code above checks if the file provided is an actual image. If not, it raises an error.

```python
info = list(img.getdata())
```

Once we've confirmed that the file is an image, we get the image and put it into the variable `info`, except for its metadata. Some metadata, such as file resolution, will remain.

```python
image_no_meta = Image.new(img.mode, img.size)
        image_no_meta.putdata(info)
```

The code above creates a new image with the image data from the initial file minus the metadata.

```python
image_no_meta.save(image_name)
```

This overwrites the original image with the newer metadata-free image.

```python
print(f"Metadata has been cleared from {image_name}")
```

Once the operation has finished, the above message is output to the terminal.

## Quality Assurance

### Image Provided

**Input**
```bash
python3 rem_img_metadata.py "Metadata has been cleared from /Users/admin/Desktop/image.jpeg"
```

**Output**
```
Metadata has been cleared from /Users/admin/Desktop/image.jpeg
```

Upon examination, most metadata has been removed from the image, except for core metadata, such as the image resolution and some other data.

### Audio File Provided

**Input**
```bash
python3 rem_img_metadata.py "/Users/admin/Desktop/file.wav"
```

**Output**
```
Traceback (most recent call last): File "/Users/admin/vim/learning/python/rem_img_metadata/re m_img_metadata.py", line 40, in <module> clear_metadata(path) File "/Users/admin/vim/learning/python/rem_img_metadata/re m_img_metadata.py", line 20, in clear_metadata with Image.open(image_name) as img: ^^^^^^^^^^^^^^^^^^^^^^ File "/Users/admin/vim/learning/python/rem_img_metadata/ve nv/lib/python3.12/site-packages/PIL/Image.py", line 3498, in open raise UnidentifiedImageError(msg) PIL.UnidentifiedImageError: cannot identify image file '/Use rs/admin/Desktop/file.wav"
```

As expected, when the file is not an image, an error occurs.
