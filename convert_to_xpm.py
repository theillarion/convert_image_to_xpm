from wand.image import Image
import os.path
from sys import argv
from pathlib import Path


def convert_image_to_xpm(srcPath: str) -> str:
	if os.path.isfile(srcPath):
		newImage = os.path.dirname(srcPath) + "/" + Path(srcPath).stem + ".xpm"
		with Image(filename=srcPath) as img:
			img.format = 'xpm'
			img.save(filename=newImage)
		return newImage
	return str()


def main():
	if len(argv) == 2:
		convert_image_to_xpm(argv[1])
	else:
		print("Error: invalid args")


if __name__ == '__main__':
	main()
