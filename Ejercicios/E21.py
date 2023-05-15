def copyfile(filename, *outputs):
    with open(filename) as input_file:
            content = input_file.readlines()
    for output in outputs:
        with open(output, 'w') as writer:
            writer.writelines(content)


copyfile('myfile.txt', 'copy1.txt', 'copy2.txt')