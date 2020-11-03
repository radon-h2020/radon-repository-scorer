"""
Core contributors is the cardinality of the smallest set of contributors whose \
total number of commits to a source code repository accounts for 80% or more of \
the total contributions.
"""

from pydriller import RepositoryMining


def core_contributors(path_to_repo: str) -> int:
    """
    Return the number of developers that contributed more than 80% to the code
    :param path_to_repo: the path to the repository to analyze
    :return: the number of core contributors
    """

    total_commits = 0
    contributors = dict()

    for commit in RepositoryMining(path_to_repo).traverse_commits():
        total_commits += 1
        contributors[commit.committer.email] = contributors.get(commit.committer.email, 0) + 1

    contributions = [v for k, v in sorted(contributors.items(), key=lambda item: item[1], reverse=True)]

    i = 0
    core_contribution = 0
    core_contributors_ = 0

    while i < len(contributions) and core_contribution < round(.8 * total_commits):
        core_contribution += contributions[i]
        core_contributors_ += 1
        i += 1

    return core_contributors_
