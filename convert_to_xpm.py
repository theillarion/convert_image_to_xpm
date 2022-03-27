from wand.image import Image
import os.path
from sys import argv
from pathlib import Path


def convert_image_to_xpm(srcPath: str, destPath: str) -> str:
	if os.path.isfile(srcPath) and os.path.isdir(destPath):
		newImage = f'{destPath}{"/" if destPath[len(destPath) - 1] != "/" else ""}{Path(srcPath).stem}.xpm'
		with Image(filename=srcPath) as img:
			img.format = 'xpm'
			img.save(filename=newImage)
		return newImage
	return str()


def get_all_file_dir(dir: str) -> list:
	result = []

	if os.path.isdir(dir):
		for root, dirs, files in os.walk(dir):
			for filename in files:
				result.append(root + filename)

	return result



def main():
	srcImage = '/home/illarion/test_image/result_png/Dirt/'
	dstImage = '/home/illarion/test_image/result_xpm/'

	if not os.path.exists(dstImage):
		os.mkdir(dstImage)

	allFiles = get_all_file_dir(srcImage)

	for file in allFiles:
		convert_image_to_xpm(file, dstImage)

	print("Complete: all")


if __name__ == '__main__':
	main()
