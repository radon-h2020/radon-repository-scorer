import github
from datetime import datetime


def issue_event_frequency(access_token: str,
                          repo_owner: str,
                          repo_name: str,
                          since: datetime = None,
                          until: datetime = None) -> float:
    """
    Return the average number of issue events per month
    :param access_token: Github personal token to query repositories
    :param repo_owner: the repository owner
    :param repo_name: the repository name
    :param since: look for events since this date
    :param until: look for events until this date
    :return: the monthly average number of issue events
    """

    g = github.Github(access_token)
    repo = g.get_repo(f'{repo_owner}/{repo_name}')

    if not since:
        since = repo.created_at
    if not until:
        until = repo.updated_at

    months = round((until - since).days / 30)

    events = 0

    for issue in repo.get_issues(sort='created'):
        if not issue:
            continue

        issue_events = issue.get_events()

        if not issue_events:
            continue

        for event in issue_events:
            if event.created_at <= until:
                events += 1

    if months == 0:
        return 0

    return events / months
