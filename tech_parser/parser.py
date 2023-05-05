from shakalizator import compression, compression_test
import json
import trimesh



def parser(inp, outp, color, len_x=8, len_y=8, len_z=8):
    # grid = compression(filename, len_x, len_y, len_z)
    mesh = trimesh.load_mesh(inp)
    grid = compression_test(mesh, color, len_x, len_y, len_z)

    data = {
        'cube': grid.tolist()
    }

    with open(f'objects/{outp}.json', 'w') as writer:
        json.dump(data, writer)


model_name = 'Heart'
default_color = [66, 170, 255]

if __name__ == '__main__':
    # Путь до исходной модели
    filename = f'models/{model_name}.obj'

    parser(filename, model_name, default_color)


