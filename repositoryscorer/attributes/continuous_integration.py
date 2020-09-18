"""
The metric for the continuous integration dimension may be defined as a piecewise \
function that returns 1 if the repo has evidence of Continuous Integrations, \
identified by the presence of Travis CI, Hound, Appveyor, Shippable, MagnumCI, \
Solano, CircleCI, and Wercker files.
"""
from os import listdir


def has_continuous_integration(path_to_repo: str) -> bool:
    """
    :param path_to_repo: the path to the repository to analyze
    :return: True if the repository contains evidence of a continuous integration practice. False otherwise
    """
    ci_services = {'.travis.yml', '.hound.yml', 'appveyor.yml', '.magnum.yml', 'circle.yml', 'shippable.yml',
                   'solano.yml',
                   'wercker.yml'}

    return any(service in listdir(path_to_repo) for service in ci_services)
