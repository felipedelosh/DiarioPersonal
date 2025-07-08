"""
FelipedelosH

2025
WINDOWS

PUT ALL FILES IN INPUT FOLDER AND ENCRYPT
"""
import os
from os import scandir
_root_path = os.getcwd()
_root_path = f"{_root_path}\\RECURSOS\\DiaryDataEncryp"
_alphabet = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚabcdefghijklmnñopqrstuvwxyzáéíóú")
_shift = 13 % len(_alphabet)
print("=======================STEP 01 of 04 READ FILES IN FOLDER===============================")
def readFilesTxtInFolder(path):
    _files = []
    try:
        for i in scandir(path):
            if i.is_file():
                if ".txt" in i.name:
                    _files.append(i.name)
    except:
        pass

    return _files
_files = readFilesTxtInFolder(f"{_root_path}\\INPUT")
print(f"=======================STEP 02 of 04 COUNT:{len(_files)}====================================")
print("=======================STEP 03 of 04 READ FILES & ENCRYPT=======================")
def enigmaMachineEncrypt(plain_text):
    "'TIP: 1942 HH"
    ##
    encrypted_text = ''
    for char in plain_text:
        if char in _alphabet:
            index = (_alphabet.index(char) + _shift) % len(_alphabet)
            encrypted_text += _alphabet[index]
        else:
            encrypted_text += char
    return encrypted_text

def getTextInFile(path):
    text = ""

    with open(path, "r", encoding="UTF-8") as f:
        return f.read()

_data = {}
for i in _files:
    full_path = f"{_root_path}\\INPUT\\{i}"
    txt = getTextInFile(full_path)
    encryptTXT = enigmaMachineEncrypt(txt)
    _data[i] = encryptTXT
print("=======================STEP 04 of 04 SAVE FILES=======================")
for i in _data:
    full_path = f"{_root_path}\\OUTPUT\\{i}"
    print(full_path)
    with open(full_path, "w", encoding="UTF-8") as f:
        f.write(_data[i])
