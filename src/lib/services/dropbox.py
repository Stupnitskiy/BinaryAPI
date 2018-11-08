import dropbox

from config import DROPBOX_ACCESS_TOKEN, DROPBOX_PROJECT_PATH

from src.lib.errors import BadRequest, Code

"""
This code was remaked from https://github.com/dropbox/dropbox-sdk-python/blob/master/example/updown.py
"""

# Create Dropbox API object. Needed for requests to Dropbox.
dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)

def list_folder():
    """List a folder.
    Return a dict mapping unicode filenames to
    FileMetadata|FolderMetadata entries.
    """
    path = DROPBOX_PROJECT_PATH

    try:
        res = dbx.files_list_folder(path)
    except dropbox.exceptions.ApiError as err:
        return {}
    else:
        return res.entries

def download(key):
    """Download a file.
    Return the bytes of the file, or None if it doesn't exist.
    """
    path = '%s/%s' % (DROPBOX_PROJECT_PATH, key)
    while '//' in path:
        path = path.replace('//', '/')
    try:
        metadata, res = dbx.files_download(path)
    except dropbox.exceptions.HttpError as err:
        raise BadRequest(Code.DOWNLOAD_FAILED)
    data = res.content
    return data

def upload(file, key, overwrite=False):
    """Upload a file.
    Return the request response, or None in case of error.
    """
    path = '%s/%s' % (DROPBOX_PROJECT_PATH, key)
    while '//' in path:
        path = path.replace('//', '/')

    mode = (dropbox.files.WriteMode.overwrite
            if overwrite
            else dropbox.files.WriteMode.add)

    try:
        res = dbx.files_upload(
            file, path, mode,
            mute=True
        )
    except dropbox.exceptions.ApiError as err:
        raise BadRequest(Code.UPLOAD_FAILED)

    return res
