"""
FelipedelosH
2024

ENCRYPT ALL .txt
"""
import os
_root_path = os.getcwd()
_alphabet = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚabcdefghijklmnñopqrstuvwxyzáéíóú")
print("=======================STEP 01 of 04 READ FOLDERS===============================")
def list_directories():
    try:
        entries = os.listdir(_root_path)
        directories = [entry for entry in entries if os.path.isdir(os.path.join(_root_path, entry))]
        return directories
    except FileNotFoundError:
        print(f"El directorio {_root_path} no fue encontrado.")
        return []
    except PermissionError:
        print(f"No se tiene permiso para acceder al directorio {_root_path}.")
        return []
_directories = list_directories()
print(f"=======================STEP 02 of 04 COUNT:{len(_directories)}====================================")
def list_files(directory, extension):
    try:
        entries = os.listdir(directory)
        files = [entry for entry in entries if os.path.isfile(os.path.join(directory, entry)) and entry.endswith(extension)]
        return files
    except FileNotFoundError:
        print(f"El directorio {directory} no fue encontrado.")
        return []
    except PermissionError:
        print(f"No se tiene permiso para acceder al directorio {directory}.")
        return []
print("=======================STEP 03 of 04 READ FILES & ENCRYPT=======================")
def enigmaMachineEncrypt(plain_text):
    "'TIP: 1942 HH"
    ##
    _shift = 13
    encrypted_text = ''
    for char in plain_text:
        if char in _alphabet:
            index = (_alphabet.index(char) + _shift) % len(_alphabet)
            encrypted_text += _alphabet[index]
        else:
            encrypted_text += char
    return encrypted_text

for i in _directories:
    itter_path = f"{_root_path}\\{i}"
    _files_txt = list_files(itter_path, ".txt")
    
    for itterFilePath in _files_txt:
        try:
            _p = f"{itter_path}\\{itterFilePath}"
            _encrytedTXT = ""
            with open(_p, "r", encoding="UTF-8") as f:
                _encrytedTXT = enigmaMachineEncrypt(f.read())

            with open(_p, "w", encoding="UTF-8") as f:
                f.write(_encrytedTXT)
            print(f"FILE: {itterFilePath} >>>>>> ENCRYPTED & SAVE.")
        except:
            print(f"Error fatal: {itterFilePath} no se puede abrir")
print("=======================STEP 04 of 04 DAS ENDE TO ENCRYPT=======================")
        