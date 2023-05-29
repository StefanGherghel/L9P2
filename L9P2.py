import os.path


def path_filter(paths):
    for path in paths:
        file_name, file_extension = os.path.splitext(path)
        if(file_extension == ".txt"):
            print('Nume :' + file_name)
            yield path


def number_of_lines(paths):
    for path in paths:
      file1 = open(path, 'r')
      yield len(file1.readlines())


def print_it(nr_lines):
    for nr in nr_lines:
        yield  'Numarul de randuri din fisier: ' + str(nr)



if __name__ == '__main__':
    print('Am inceput programul' + "\n")
    paths = ["/home/student/AplicatiiPy/Laborator9/Aplicatie2/Folder2/fisiertext0", "/home/student/AplicatiiPy/Laborator9/Aplicatie2/Folder1/fisiertext1.txt", "/home/student/AplicatiiPy/Laborator9/Aplicatie2/Folder1/fisiertext2.txt"]
    pipeline = print_it(number_of_lines(path_filter(paths)))
    for path in pipeline:
        print(path + "\n")
