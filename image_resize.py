import os.path
from PIL import Image
from sys import argv
from pathlib import Path


def resize_to(srcPath: str, destPath: str, listPixels: list, extension='.png') -> list:
    pathToFiles = []

    if (os.path.isfile(srcPath) or os.path.basename(srcPath).find(extension)) and os.path.isdir(destPath):
        img = Image.open(srcPath)

        for pixel in listPixels:
            resizeImage = img.resize((pixel, pixel), Image.ANTIALIAS)
            pathFile = f'{destPath}{"/" if destPath[len(destPath) - 1] != "/" else ""}{Path(srcPath).stem}_{str(pixel)}{extension}'
            resizeImage.save(pathFile)
            pathToFiles.append(pathFile)

    return pathToFiles


def main():
    pixelsImage = [64, 32, 16, 8]
    extension = ".png"

    if len(argv) == 3:
        srcPath = str(argv[1])
        destPath = str(argv[2])

        print(resize_to(srcPath, destPath, pixelsImage, extension))

    else:
        print("Error: invalid argv")


if __name__ == '__main__':
    main()
