"""
The metric for the continuous integration dimension may be defined as a piecewise \
function that returns 1 if the repo has evidence of Continuous Integrations, \
identified by the presence of Travis CI, Hound, Appveyor, Shippable, MagnumCI, \
Solano, CircleCI, Wercker, and Jenkinsfile files.
If none is present, check if .github/workflows/ exists and is not empty
"""
import os


def has_continuous_integration(path_to_repo: str) -> bool:
    """
    :param path_to_repo: the path to the repository to analyze
    :return: True if the repository contains evidence of a continuous integration practice. False otherwise
    """
    ci_services = {'.travis.yml', '.hound.yml', 'appveyor.yml', '.magnum.yml', 'circle.yml', '.ci', '.circle',
                   'shippable.yml', 'solano.yml', 'wercker.yml', 'Jenkinsfile'}

    has_ci = any(service in os.listdir(path_to_repo) for service in ci_services)

    if not has_ci:
        github_workflow_dir = os.path.join(path_to_repo, '.github', 'workflows')
        has_ci = os.path.isdir(github_workflow_dir) and len(os.listdir(github_workflow_dir))

    return has_ci
