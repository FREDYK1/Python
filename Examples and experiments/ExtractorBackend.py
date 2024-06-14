import zipfile


def extract_archive(archive_file, dest_file):
    with zipfile.ZipFile(archive_file, 'r') as archive:
        archive.extractall(dest_file)

