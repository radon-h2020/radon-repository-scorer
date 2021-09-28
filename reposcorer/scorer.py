import git
import os

from typing import Union

from reposcorer.attributes.community import core_contributors
from reposcorer.attributes.continuous_integration import has_continuous_integration
from reposcorer.attributes.history import commit_frequency
from reposcorer.attributes.iac import iac_ratio
from reposcorer.attributes.issues import github_issue_event_frequency, gitlab_issue_event_frequency
from reposcorer.attributes.licensing import has_license
from reposcorer.attributes.loc_info import loc_info


def score_repository(host: str,
                     full_name: Union[str, int],
                     clone_to: str,
                     calculate_comments_ratio: bool = False,
                     calculate_commit_frequency: bool = False,
                     calculate_core_contributors: bool = False,
                     calculate_has_ci: bool = False,
                     calculate_has_license: bool = False,
                     calculate_iac_ratio: bool = False,
                     calculate_issue_frequency: bool = False,
                     calculate_repository_size: bool = False):
    """
    Score a repository to identify well-engineered projects.

    :param host: the SVM hosting platform. That is, github or gitlab
    :param full_name: the full name of a repository (e.g., radon-h2020/radon-repository-scorer)
    :param clone_to: directory to clone the repository
    :param comments_ratio: if calculate this attribute
    :param commit_frequency: if calculate this attribute
    :param core_contributors: if calculate this attribute
    :param has_ci: if calculate this attribute
    :param has_license: if calculate this attribute
    :param iac_ratio: if calculate this attribute
    :param issue_frequency: if calculate this attribute
    :param repository_size: if calculate this attribute
    :return: a dictionary with a score for every indicator
    """

    scores = {}
    path_to_repo = os.path.join(clone_to, full_name.split('/')[-1])

    if calculate_issue_frequency:

        issues = 0
        if host == 'github':
            issues = github_issue_event_frequency(full_name)

            if not os.path.isdir(full_name):
                git.Git(clone_to).clone(f'https://github.com/{full_name}.git')

        elif host == 'gitlab':
            issues = gitlab_issue_event_frequency(full_name)
            if not os.path.isdir(full_name):
                git.Git(clone_to).clone(f'https://github.com/{full_name}.git')
        else:
            raise ValueError(f'{host} not supported. Please select github or gitlab')

        scores.update({'issue_frequency': round(issues, 2)})

    if calculate_commit_frequency:
        scores.update({'commit_frequency': round(commit_frequency(path_to_repo), 2)})

    if calculate_core_contributors:
        scores.update({'core_contributors': core_contributors(path_to_repo)})

    if calculate_has_ci:
        scores.update({'has_ci': has_continuous_integration(path_to_repo)})

    if calculate_has_license:
        scores.update({'has_license': has_license(path_to_repo)})

    if calculate_iac_ratio:
        scores.update({'iac_ratio': round(iac_ratio(path_to_repo), 4)})

    if calculate_comments_ratio or calculate_repository_size:
        cloc, sloc = loc_info(path_to_repo)
        ratio_comments = cloc / (cloc + sloc) if (cloc + sloc) != 0 else 0

        if calculate_comments_ratio:
            scores.update({'comments_ratio': round(ratio_comments, 4)})

        if calculate_repository_size:
            scores.update({'repository_size': sloc})

    return scores
