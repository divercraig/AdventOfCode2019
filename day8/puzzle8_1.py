from day8.space_image import SpaceImage

test_image = SpaceImage(filename='test_input.txt', width=3, height=2)
print("TEST Image checksum = {}".format(test_image.checksum()))

image = SpaceImage(filename='input.txt')
print("Image checksum = {}".format(image.checksum()))