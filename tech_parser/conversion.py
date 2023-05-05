from enum import Enum
import matplotlib
import numpy as np
import json


class ConverterMode(Enum):
    ToHEX = 1
    ToRGB = 2


def color_converter(colors, mode: ConverterMode):
    grid = np.zeros((len(colors), len(colors[0]), len(colors[0, 0])), dtype=tuple)
    for i in range(len(colors)):
        for j in range(len(colors[i])):
            for k in range(len(colors[i, j])):
                if mode == ConverterMode.ToRGB:
                    rgba = matplotlib.colors.to_rgb(colors[i, j, k])
                    grid[i, j, k] = [int(x*255) for x in rgba]
                if mode == ConverterMode.ToHEX:
                    rgba = to_rgba(colors[i, j, k])
                    grid[i, j, k] = matplotlib.colors.to_hex(rgba)

    return grid


def to_rgba(rgb):
    return [x/255 for x in rgb]


def change_color(name, old_color, new_color):
    filename = f'objects/{name}.json'

    # Преобразовываем к сравнимому виду
    old_color = to_rgba(old_color)
    old_color = matplotlib.colors.to_hex(old_color)

    new_color = to_rgba(new_color)
    new_color = matplotlib.colors.to_hex(new_color)

    with open(filename) as reader:
        data = json.load(reader)
        model = np.array(data['rgb'])

    hex_colors = color_converter(model, ConverterMode.ToHEX)

    for i in range(len(hex_colors)):
        for j in range(len(hex_colors[i])):
            for k in range(len(hex_colors[i, j])):
                if hex_colors[i, j, k] == old_color:
                    hex_colors[i, j, k] = new_color

    model = color_converter(hex_colors, ConverterMode.ToRGB)

    data = {
        'rgb': model.tolist()
    }

    with open(filename, 'w') as writer:
        json.dump(data, writer)



