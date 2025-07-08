"""
FelipedelosH
2025

WINDOWS
""" 
import os
from os import scandir

_alphabet = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚabcdefghijklmnñopqrstuvwxyzáéíóú")
_shift = 13

_path = str(os.path.dirname(os.path.abspath(__file__)))

_path_encrypfiles = _path.replace("\\RECURSOS\\DiaryDataDecryp", "")
_path_encrypfiles = f"{_path_encrypfiles}\\DATA\\DIARIO\\2025"

def getAllFilesInFolderByExt(path, ext):
    files = []
    
    try:
        for i in scandir(path):
            if i.is_file():
                if ext in i.name:
                    files.append(i.name)
    except:
        pass

    return files


def getTextInFile(path):
    text = ""

    with open(path, "r", encoding="UTF-8") as f:
        return f.read()


def enigmaMachineDecript(encrypted_text):
    """
    Remeber: NEW FAGOT CAN'T READ IT
    """
    decrypted_text = ''
    for char in encrypted_text:
        if char in _alphabet:
            index = (_alphabet.index(char) - _shift) % len(_alphabet)
            decrypted_text += _alphabet[index]
        else:
            decrypted_text += char
    return decrypted_text


def saveFile(path, txt):
    with open(path, "w", encoding="UTF-8") as f:
        f.write(txt)


print("=======================STEP 01 of 04 READ FOLDERS===============================")
_files = getAllFilesInFolderByExt(_path_encrypfiles, ".txt")
print(f"=======================STEP 02 of 04 COUNT:{len(_files)}====================================")

print("=======================STEP 03 of 04 READ FILES & DECRYPT=======================")
_decrypted = {}
for i in _files:
    full_path = os.path.join(_path_encrypfiles, i)
    encryptTxt = getTextInFile(full_path)
    decryptTxt = enigmaMachineDecript(encryptTxt)
    _decrypted[i] = decryptTxt
print("=======================STEP 04 of 04 SAVE FILES DECRYPT=======================")
for i in _decrypted:
    full_path = f"{_path}\\OUTPUT\\{i}"
    saveFile(full_path, _decrypted[i])
print("=======================  DAS ENDE  =======================")
