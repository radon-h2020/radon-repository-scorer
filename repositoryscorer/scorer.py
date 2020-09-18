from repositoryscorer.attributes.community import core_contributors
from repositoryscorer.attributes.continuous_integration import has_continuous_integration
from repositoryscorer.attributes.history import commit_frequency
from repositoryscorer.attributes.iac import iac_ratio
from repositoryscorer.attributes.issues import issue_event_frequency
from repositoryscorer.attributes.licensing import has_license
from repositoryscorer.attributes.loc_info import loc_info


def score_repository(path_to_repo: str,
                     access_token: str,
                     repo_name: str,
                     repo_owner: str):
    """
    Score a repository to identify well-engineered projects.

    :param path_to_repo: path to the local repository
    :param access_token: Github access token
    :param repo_owner: the repository owner
    :param repo_name: the repository name
    :return: a dictionary with a score for every indicator
    """

    history = commit_frequency(path_to_repo)
    community = core_contributors(path_to_repo)
    ci = has_continuous_integration(path_to_repo)
    issues = issue_event_frequency(path_to_repo, access_token, repo_name, repo_owner)
    license = has_license(path_to_repo)
    cloc, sloc = loc_info(path_to_repo)
    ratio_comments = cloc / (cloc + sloc) if (cloc + sloc) != 0 else 0
    ratio_iac = iac_ratio(path_to_repo)

    return {
        'repository': path_to_repo,
        'continuous_integration': ci,
        'percent_comment': round(ratio_comments, 4),
        'commit_frequency': round(history, 2),
        'core_contributors': community,
        'iac_ratio': round(ratio_iac, 4),
        'issue_frequency': round(issues, 2),
        'license': license,
        'repository_size': sloc
    }
