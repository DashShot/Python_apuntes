import os

def get_file_extensions(directory):
    extensions = set()

    for filename in os.listdir(directory):
        _, ext = os.path.splitext(filename)
        if ext:
            extensions.add(ext)

    return extensions


directory = '/ruta/al/directorio'
extensions = get_file_extensions(directory)

print(extensions)
