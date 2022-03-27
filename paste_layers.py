import os
from PIL import Image
from pathlib import Path


def paste_layers(pathToImage: str, pathToResultImage: str, pathToLayers: list) -> str:
	pathOutputFile = str()

	if not os.path.exists(pathToResultImage):
		os.mkdir(pathToResultImage)
	if os.path.isfile(pathToImage) and os.path.isdir(pathToResultImage):
		image = Image.open(pathToImage)

		for layer in pathToLayers:
			if os.path.isfile(layer):
				imageLayer = Image.open(layer)
				image.paste(imageLayer, (0, 0), imageLayer)

		slash = "/" if pathToResultImage[len(pathToResultImage) - 1] != "/" else ""
		nameFile = 'Full'

		tempList = pathToImage.split('_')
		if len(tempList) == 1:
			suffix = Path(pathToImage).suffix
		else:
			suffix = '_' + tempList[len(tempList) - 1]

		pathToResultImage = pathToResultImage + slash + nameFile + suffix

		image.save(pathToResultImage)

	return pathOutputFile


def get_all_file_dir(dir: str) -> list:
	result = []

	if os.path.isdir(dir):
		for root, dirs, files in os.walk(dir):
			for filename in files:
				result.append(root + filename)

	return result


def main():
	srcImage = '/home/illarion/test_image/result_png/Dirt/'
	destImage = '/home/illarion/test_image/result_png/Full/'
	srcLayers = ["/home/illarion/test_image/result_png/Hull/", "/home/illarion/test_image/result_png/Gun/"]

	allImage = get_all_file_dir(srcImage)
	allLayersHull = get_all_file_dir(srcLayers[0])
	allLayersGun = get_all_file_dir(srcLayers[1])

	allImage.sort()
	allLayersHull.sort()
	allLayersGun.sort()

	for i in range(0, len(allImage) - 1):
		paste_layers(allImage[i], destImage, [allLayersHull[i], allLayersGun[i]])
	print("Complete: all")


if __name__ == '__main__':
	main()