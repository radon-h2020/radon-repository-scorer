from pydriller import RepositoryMining


def commit_frequency(path_to_repo:str) -> float:
    """
    Return the average number of commit per month
    :param path_to_repo: the path to the repository to analyze
    :return: the average number of commits per month
    """

    commits = list(RepositoryMining(path_to_repo).traverse_commits())

    first_commit_date = commits[0].committer_date
    last_commit_date = commits[-1].committer_date
    months = round((last_commit_date - first_commit_date).days / 30)

    if months == 0:
        return 0

    return len(commits)/months
