import colorgram

colors = colorgram.extract('image.jpg', 36)

palette = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    palette.append(rgb)

print(palette)