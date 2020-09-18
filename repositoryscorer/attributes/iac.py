"""
The metric for the continuous integration dimension may be defined as a piecewise \
function that returns 1 if the repo has evidence of Continuous Integrations, \
identified by the presence of Travis CI, Hound, Appveyor, Shippable, MagnumCI, \
Solano, CircleCI, and Wercker files.
"""
from repositoryscorer.utility import get_files
import statistics


def iac_ratio(path_to_repo: str) -> float:
    """
    :param path_to_repo: the path to the repository to analyze
    :return: the ration [0, 1] of iac scripts in the repository
    """
    iac_files = [(file.endswith('.yml') or file.endswith('.yaml') or file.endswith('.j2'))
                 or (('cookbooks' in file or 'recipe' in file) and file.endswith('.rb'))
                 or file.endswith('.pp')
                 for file in get_files(path_to_repo)]

    ratio = 0
    if iac_files:
        ratio = statistics.mean(iac_files)

    return ratio
