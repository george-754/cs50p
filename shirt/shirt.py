# open a png/jpg file and overlay it over another png/jpg image file

import os, sys
from PIL import Image, ImageOps


def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Validate the file extension (.jpg, .jpeg, .png)
    f, e = os.path.splitext(sys.argv[1])
    ft, et = os.path.splitext(sys.argv[2])

    if e.lower() != ".jpg" and e.lower() != ".jpeg" and e.lower() != ".png":
        sys.exit("Invalid input")

    if et.lower() != ".jpg" and et.lower() != ".jpeg" and et.lower() != ".png":
        sys.exit("Invalid output")

    # Validate both file extensions are the same
    if e != et:
        sys.exit("Input and output have different extensions")
    
    convert(sys.argv[1], sys.argv[2])



def convert(img_orig, img_new):

    shirt = Image.open("shirt.png")
    size = shirt.size

    try:
        # get the original image
        img_original = Image.open(img_orig)
        # resize the original image to the size of the shirt image
        resized_image = ImageOps.fit(img_original, size)

        resized_image.paste(shirt, shirt)

        resized_image.save(img_new)

    except FileNotFoundError:
        sys.exit("Input does not exist")



if __name__=="__main__":
    main()