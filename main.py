from image_resize import resize_to
from convert_to_xpm import convert_image_to_xpm
from paste_layers import paste_layers
from sys import argv
from pathlib import Path
import os

srcMainFile = "/home/illarion/test_image/png/Hull.png"
srcPath = "/home/illarion/test_image/png/"
destPath = "/home/illarion/test_image/result_png/"
destXpm = "/home/illarion/test_image/result_xpm/"


def main():
    pixelsImage = [64, 32, 16, 8, 4]

    resultResizeFile = []
    for root, dirs, files in os.walk(srcPath):
        for filename in files:
            resultResizeFile.append(resize_to(root + filename, destPath, pixelsImage))
    print("Complete: all")


if __name__ == '__main__':
    main()

 '''fullFiles = []
    nameMainFile = Path(srcMainFile).stem

    for i in range(0, len(resultResizeFile[0]) - 1):
        resizeFiles = [resultResizeFile[j][i] for j in range(len(resultResizeFile[i]) - 1)]
        for index, element in enumerate(resizeFiles):
            if file.find(nameMainFile) != -1:
                resizeFiles[0], resizeFiles[index] = resizeFiles[index, resizeFiles[0]
                break
        if not os.path.exists(srcPath + 'Full/'):
            os.mkdir(srcPath + 'Full/')
        fullFiles.append(paste_layers(resizeFiles[0], srcPath + 'Full/', resizeFiles[1:]))
        print(resizeFiles)'''