from typing import Union

from repositoryscorer.attributes.community import core_contributors
from repositoryscorer.attributes.continuous_integration import has_continuous_integration
from repositoryscorer.attributes.history import commit_frequency
from repositoryscorer.attributes.iac import iac_ratio
from repositoryscorer.attributes.issues import issue_event_frequency
from repositoryscorer.attributes.licensing import has_license
from repositoryscorer.attributes.loc_info import loc_info


def score_repository(path_to_repo: str,
                     access_token: str,
                     full_name_or_id: Union[str, int]):
    """
    Score a repository to identify well-engineered projects.

    :param path_to_repo: path to the local repository
    :param access_token: Github access token
    :param full_name_or_id: the full name of a repository or its id (e.g., radon-h2020/radon-repository-scorer)
    :return: a dictionary with a score for every indicator
    """

    history = commit_frequency(path_to_repo)
    community = core_contributors(path_to_repo)
    ci = has_continuous_integration(path_to_repo)
    issues = issue_event_frequency(access_token, full_name_or_id)
    license = has_license(path_to_repo)
    cloc, sloc = loc_info(path_to_repo)
    ratio_comments = cloc / (cloc + sloc) if (cloc + sloc) != 0 else 0
    ratio_iac = iac_ratio(path_to_repo)

    return {
        'continuous_integration': ci,
        'percent_comment': round(ratio_comments, 4),
        'commit_frequency': round(history, 2),
        'core_contributors': community,
        'iac_ratio': round(ratio_iac, 4),
        'issue_frequency': round(issues, 2),
        'license': license,
        'repository_size': sloc
    }
