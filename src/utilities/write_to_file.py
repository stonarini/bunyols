def write_to_file(path, filename, content):
    with open(path + filename, "w") as new_file:
        new_file.write(content)
