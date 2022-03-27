from image_resize import resize_to
from convert_to_xpm import convert_image_to_xpm
from sys import argv


def main():
    pixelsImage = [64, 32, 16, 8]
    extension = ".png"

    if len(argv) == 3:
        srcPath = str(argv[1])
        destPath = str(argv[2])

        files = resize_to(srcPath, destPath, pixelsImage, extension)
        for file in files:
            convert_image_to_xpm(file)
        print("Complete: all")
    else:
        print("Error: invalid argv")



if __name__ == '__main__':
    main()
