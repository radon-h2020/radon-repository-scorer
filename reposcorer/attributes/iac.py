from reposcorer.utility import get_files
import statistics


def iac_ratio(path_to_repo: str) -> float:
    """
    :param path_to_repo: the path to the repository to analyze
    :return: the ratio [0, 1] of iac scripts in the repository
    """
    iac_files = [(file.endswith('.yml') or file.endswith('.yaml') or file.endswith('.j2'))
                 or (('cookbooks' in file or 'recipe' in file) and file.endswith('.rb'))
                 or file.endswith('.pp')
                 for file in get_files(path_to_repo)]

    ratio = 0
    if iac_files:
        ratio = statistics.mean(iac_files)

    return ratio
