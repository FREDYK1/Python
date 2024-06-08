import zipfile
import pathlib


def zip_maker(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "CompressorApp.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname= filepath.name)

