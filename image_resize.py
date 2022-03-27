import os.path
from PIL import Image
from sys import argv
from pathlib import Path


def get_slash(string: str) -> str:
    if string[len(string) - 1] != '/':
        return '/'
    else:
        return ''


def resize_to(pathToFile: str, pathToDirResult: str, listPixels: list) -> list:
    pathToFiles = []

    if os.path.isfile(pathToFile) and os.path.isdir(pathToDirResult):
        img = Image.open(pathToFile)

        for pixel in listPixels:
            resizeImage = img.resize((pixel, pixel), Image.ANTIALIAS)

            nameFile = Path(pathToFile).stem
            pathResultFile = pathToDirResult + get_slash(pathToDirResult) + nameFile + '/'

            if not os.path.exists(pathResultFile):
                os.mkdir(pathResultFile)

            pathResultFile += get_slash(pathResultFile) + nameFile + '_' + str(pixel) + Path(pathToFile).suffix

            resizeImage.save(pathResultFile)
            pathToFiles.append(pathResultFile)

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
