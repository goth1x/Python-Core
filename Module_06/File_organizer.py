import sys
import re
from shutil import unpack_archive, copyfile
from pathlib import Path


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}

structure = {'Images': ['JPEG', 'PNG', 'JPG', 'SVG'],
             'Video': ['AVI', 'MP4', 'MOV', 'MKV'],
             'Documents': ['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'],
             'Audio': ['MP3', 'OGG', 'WAV', 'AMR'],
             'Archives': ['ZIP', 'GZ', 'TAR'],
             '3D models': ['3DS', 'STEP', 'STP', 'OBJ', 'FBX', 'IGS', 'MB']}

list_name = []


def copy_file(file_path):  # File copying to new directory
    if (file_path.suffix[1:]).upper() in structure['Archives']:
        unpack_archive(file_path, create_folder(file_path) / normalize(
            file_path)[:str(file_path.name).rfind('.')])  # Archives without suffix
    else:
        copyfile(file_path, create_folder(
            file_path) / normalize(file_path))


def create_folder(file_path):  # Create folder using file-format as folder name
    new_directory = Path(
        f'Organized/{create_volume(file_path) or "Other"}/{(file_path.suffix[1:]).upper()}')
    new_directory.mkdir(parents=True, exist_ok=True)
    return new_directory


# Find file-format in Dictionary and return Key as a folder name
def create_volume(file_path):
    for key, value in structure.items():
        for suffix in value:
            if (file_path.suffix[1:]).upper() == suffix:
                return key


def normalize(file_path):
    # Filename without suffix
    name = file_path.name[:str(file_path.name).rfind('.')]
    new_name = re.sub(r'\W', '_', name.translate(TRANS)
                      )  # New filename - transliterated
    file_name = f'{new_name}{file_path.suffix}'  # New filename with suffix
    list_name.append(file_name)  # Add to global list with filenames
    if list_name.count(file_name) > 1:
        # Add NUMBER to filename if filename already exist
        new_name = f'{new_name}({list_name.count(file_name) - 1})'
    return f'{new_name}{file_path.suffix}'


def parse_folder(path):  # Iter in the directory
    for element in path.iterdir():
        if element.is_dir():
            parse_folder(element)  # Recursion
            if element.name in structure.keys():
                continue
            else:
                try:
                    element.rmdir()    # Delete empty folder
                except:
                    pass
        else:
            copy_file(element)


for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


if __name__ == '__main__':
    path = Path(sys.argv[1])
    parse_folder(path)
    print(path, '  Done')