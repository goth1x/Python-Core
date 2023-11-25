import pathlib
path = pathlib.Path.cwd()

def parse_folder(path):
    files = []
    folders = []
    for i in path.iterdir():
        if i.is_dir():
            folders.append(i.name)
        elif i.is_file():
            files.append(i.name)   
    return files, folders

print(parse_folder(path))