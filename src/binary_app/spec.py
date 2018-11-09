from src.lib.validate import required
from src.lib.services.dropbox import list_folder


def is_key_exist(key):
    files = list_folder()
    filenames = [file.name for file in files]

    return key in filenames


def put():
    return {
        'key': [required],
        'data': [required],
    }


def delete():
    return {
        'key': [is_key_exist],
    }


def get():
    return {
        'key': [is_key_exist],
    }