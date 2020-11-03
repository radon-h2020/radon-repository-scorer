import os
import github, gitlab
from datetime import datetime
from typing import Union


def github_issue_event_frequency(full_name_or_id: Union[str, int],
                                 since: datetime = None,
                                 until: datetime = None) -> float:
    """
    Return the average number of issue events per month
    :param full_name_or_id: the full name of a repository or its id (e.g., radon-h2020/radon-repository-scorer)
    :param since: look for events since this date
    :param until: look for events until this date
    :return: the monthly average number of issue events
    """

    gh = github.Github(os.getenv('GITHUB_ACCESS_TOKEN'))
    repo = gh.get_repo(full_name_or_id)

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
            if since <= event.created_at <= until:
                events += 1

    if months == 0:
        return 0

    return events / months


def gitlab_issue_event_frequency(full_name_or_id: Union[str, int],
                                 since: datetime = None,
                                 until: datetime = None) -> float:
    """
    Return the average number of issue events per month
    :param full_name_or_id: the full name of a repository or its id (e.g., radon-h2020/radon-repository-scorer)
    :param since: look for events since this date
    :param until: look for events until this date
    :return: the monthly average number of issue events
    """

    gl = gitlab.Gitlab('http://gitlab.com', os.getenv('GITLAB_ACCESS_TOKEN'))
    project = gl.projects.get(full_name_or_id)

    if not since:
        since = datetime.strptime(project.created_at, '%Y-%m-%dT%H:%M:%S.%fZ')
    if not until:
        until = datetime.strptime(project.last_activity_at, '%Y-%m-%dT%H:%M:%S.%fZ')

    months = round((until - since).days / 30)
    events = 0

    for issue in project.issues.list(all=True):
        for note in issue.notes.list(all=True, as_list=False, sort='asc'):
            if since <= datetime.strptime(note.created_at, '%Y-%m-%dT%H:%M:%S.%fZ') <= until:
                events += 1
            else:
                break

    if months == 0:
        return 0
    print(events, months)
    return events / months
