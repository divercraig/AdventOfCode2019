from day8.space_image import SpaceImage

print("IMAGE")
image = SpaceImage(filename='input.txt')
image.print()

print("NEGATIVE")
image.print(negative=True)
