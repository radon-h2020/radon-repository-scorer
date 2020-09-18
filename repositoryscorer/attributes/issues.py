import github
import os


def issue_event_frequency(path_to_repo: str, access_token: str, repo_owner:str, repo_name:str) -> float:
    """
    Return the average number of issue events per month
    :param path_to_repo: the path to the repository to analyze
    :param access_token: Github personal token to query repositories
    :param repo_owner: the repository owner
    :param repo_name: the repository name
    :return: the monthly average number of issue events
    """

    g = github.Github(access_token)
    repo = g.get_repo(f'{repo_owner}/{repo_name}')
    months = round((repo.updated_at - repo.created_at).days / 30)

    events = 0

    for issue in repo.get_issues(sort='created'):
        if not issue:
            continue

        issue_events = issue.get_events()

        if not issue_events:
            continue

        events += issue_events.totalCount

    if months == 0:
        return 0

    return events / months
