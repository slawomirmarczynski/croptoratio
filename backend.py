from PIL import Image

def load_image(file_name):
    image = Image.open(file_name)
    return image

def crop_image(old_image, ratio=3 / 5):

    width = old_image.width
    height = old_image.height

    if width / height > ratio:
        new_width = int(height * ratio)
        new_height = height
        offset = (width - new_width) // 2
        new_image = old_image.crop((offset, 0, new_width + offset, new_height))
    elif width / height < ratio:
        new_width = width
        new_height = width / ratio
        offset = (height - new_height) // 2
        new_image = old_image.crop((0, offset, new_width, new_height + offset))
    else:
        new_image = old_image

    return new_image
