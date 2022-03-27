from image_resize import resize_to
from convert_to_xpm import convert_image_to_xpm
from sys import argv

srcPath = "/home/illarion/test_image/png/linux.png"
destPng = "/home/illarion/test_image/test_png/"
destXpm = "/home/illarion/test_image/test_xpm/"

def main():
    pixelsImage = [64, 32, 16, 8]
    extension = ".png"

    files = resize_to(srcPath, destPng, pixelsImage, extension)
    print("Complete: resize")

    for file in files:
        convert_image_to_xpm(file, destXpm)

    print("Complete: all")


if __name__ == '__main__':
    main()
