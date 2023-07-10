import gdown
import os


def download_gdrive_file(path, id):
    output = path
    if os.path.exists(path):
        print('file already exist!')
        return
    tdir, _ = os.path.split(path)
    os.makedirs(tdir, exist_ok=True)
    gdown.download(
        f"https://drive.google.com/uc?export=download&confirm=pbef&id=" + id,
        output
    )
