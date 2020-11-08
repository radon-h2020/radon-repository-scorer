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
                     clone_to: str):
    """
    Score a repository to identify well-engineered projects.

    :param host: the SVM hosting platform. That is, github or gitlab
    :param full_name: the full name of a repository (e.g., radon-h2020/radon-repository-scorer)
    :param clone_to: directory to clone the repository
    :return: a dictionary with a score for every indicator
    """

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

    path_to_repo = os.path.join(clone_to, full_name.split('/')[-1])

    history = commit_frequency(path_to_repo)
    community = core_contributors(path_to_repo)
    ci = has_continuous_integration(path_to_repo)
    license_ = has_license(path_to_repo)
    cloc, sloc = loc_info(path_to_repo)
    ratio_comments = cloc / (cloc + sloc) if (cloc + sloc) != 0 else 0
    ratio_iac = iac_ratio(path_to_repo)

    return {
        'has_ci': ci,
        'comments_ratio': round(ratio_comments, 4),
        'commit_frequency': round(history, 2),
        'core_contributors': community,
        'iac_ratio': round(ratio_iac, 4),
        'issue_frequency': round(issues, 2),
        'has_license': license_,
        'repository_size': sloc
    }
