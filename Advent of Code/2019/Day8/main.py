
#input
with open("input.txt","r") as file:
    pixels = [int(pixel) for pixel in str(file.read())];



width = 25;
height = 6;
numLayers = len(pixels) % (25*6);
layers = [];

for i in range(numLayers):
    layer = []
    row = []
    for i in range(width):
        row.append(pixels(i

