import os


def get_files(path_to_repo: str):
    files = set()

    for root, _, filenames in os.walk(path_to_repo):
        if '.git' in root:
            continue
        for filename in filenames:
            path = os.path.join(root, filename)
            files.add(path)

    return files
