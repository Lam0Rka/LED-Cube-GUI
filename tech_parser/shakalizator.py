import multiprocessing
import trimesh
import numpy as np
import multiprocessing as mp
# from layer import layer
import matplotlib
# from . import conversion
from .conversion import color_converter, ConverterMode, to_rgba

# Функция для работы нескольких потоков
def layer(dict_value, i):

    # Создаем один из слоев в потоке
    lay = np.zeros((1, dict_value['len_y'], dict_value['len_z']), dtype=bool)

    for j in range(dict_value['len_y']):
        for k in range(dict_value['len_z']):
            # Вычисление координаты текущего кубика
            # Минимальная точка
            x_begin = dict_value['bbox'][0][0] + i * dict_value['step_x']
            y_begin = dict_value['bbox'][0][1] + j * dict_value['step_y']
            z_begin = dict_value['bbox'][0][2] + k * dict_value['step_z']

            # Максимальная точка
            x_end = x_begin + dict_value['step_x']
            y_end = y_begin + dict_value['step_y']
            z_end = z_begin + dict_value['step_z']

            # Проверка сколько объема фигуры находится в области кубика
            small_box = trimesh.creation.box(bounds=[[x_begin, y_begin, z_begin], [x_end, y_end, z_end]])
            inter = trimesh.boolean.intersection([dict_value['mesh'], small_box])
            main_volume = inter.volume

            print(f'{main_volume}: {i} {j} {k}')

            if main_volume >= dict_value['volume_part'] * dict_value['small_box_volume']:
                lay[0, j, k] = True

            dict_value[f'layer{i}'] = lay

def compression(path, len_x=8, len_y=8, len_z=8):
    # Загружаем модель
    mesh = trimesh.load_mesh(path)

    # Находим центр масс модели
    center = mesh.center_mass

    # Перемещаем модель так, чтобы центр масс совпадал с началом координат
    mesh.apply_translation(-center)

    # Пустой массив размером 8x8x8
    grid = np.zeros((len_x, len_y, len_z), dtype=bool)

    # Рамка ограничивающая модель
    bbox = mesh.bounding_box.bounds

    # Учитываем масштаб фигуры
    min_coord = min(bbox[0])
    max_coord = max(bbox[1])
    new_bbox = np.array([[min_coord] * 3, [max_coord] * 3])

    # Размер шага для каждой оси
    step_x = (new_bbox[1][0] - new_bbox[0][0]) / len_x
    step_y = (new_bbox[1][1] - new_bbox[0][1]) / len_y
    step_z = (new_bbox[1][2] - new_bbox[0][2]) / len_z

    # Проходим по каждой точке сетки
    for i in range(len_x):
        for j in range(len_y):
            for k in range(len_z):

                # Вычисление координаты текущего кубика
                x_begin = new_bbox[0][0] + i * step_x
                y_begin = new_bbox[0][1] + j * step_y
                z_begin = new_bbox[0][2] + k * step_z

                # Проверка, находится ли точка внутри сетки
                if mesh.contains(np.array([[x_begin, y_begin, z_begin]])):
                    grid[i, j, k] = True

    return grid


def compression_test(mesh, color, len_x=8, len_y=8, len_z=8):
    # Находим центр масс модели
    center = mesh.center_mass
    print(center)

    # Перемещаем модель так, чтобы центр масс совпадал с началом координат
    mesh.apply_translation(-center)

    # Рамка ограничивающая модель
    bbox = mesh.bounding_box.bounds

    # Учитываем масштаб фигуры
    min_coord = min(bbox[0])
    max_coord = max(bbox[1])
    new_bbox = np.array([[min_coord] * 3, [max_coord] * 3])

    # Размер шага для каждой оси
    step_x = (new_bbox[1][0] - new_bbox[0][0]) / len_x
    step_y = (new_bbox[1][1] - new_bbox[0][1]) / len_y
    step_z = (new_bbox[1][2] - new_bbox[0][2]) / len_z

    # Считаем объем кубика
    small_box = trimesh.creation.box(bounds=[[new_bbox[0][0], new_bbox[0][1], new_bbox[0][2]],
                                       [new_bbox[0][0] + step_x, new_bbox[0][1] + step_y, new_bbox[0][2] + step_z]])

    big_box = trimesh.creation.box(bounds=new_bbox)
    volume_part = mesh.volume / big_box.volume

    # Задаем массив с данными для передачи потокам
    manager = multiprocessing.Manager()
    dict_value = manager.dict({
        'bbox': new_bbox,
        'step_x': step_x,
        'step_y': step_y,
        'step_z': step_z,
        'mesh': mesh,
        'volume_part': volume_part,
        'small_box_volume': small_box.volume,
        'len_x': len_x,
        'len_y': len_y,
        'len_z': len_z,
    })

    print(f'part:{volume_part} small_box:{small_box.volume} model: {mesh.volume} big_box: {big_box.volume}')

    # Проходим по каждой точке сетки
    threads = []
    for i in range(len_x):
        th = mp.Process(target=layer, args=(dict_value, i, ))
        th.start()
        threads.append(th)

    for th in threads:
        th.join()

    # Собираем все слои в одну сетку
    grid = dict_value['layer0']
    for i in range(1, 8):
        grid = np.vstack([grid, dict_value[f'layer{i}']])

    # Сохраним цвет в формате RGB
    hex_black = '#000000'
    rgba = to_rgba(color)
    hex_color = matplotlib.colors.to_hex(rgba)
    facecolors = np.where(grid, hex_color, hex_black)
    rgb_format = color_converter(facecolors, ConverterMode.ToRGB)

    return rgb_format

compression("tech_parser/sphere.obj")