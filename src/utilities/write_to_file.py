import os


def write_to_file(path, filename, content):
    if not os.path.exists(path):
        os.makedirs(path)

    with open(path + filename, "w") as new_file:
        new_file.write(content)
