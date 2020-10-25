from .loc_info import loc_info


def comments_ratio(path_to_repo: str) -> float:
    """
    :param path_to_repo: the path to the repository to analyze
    :return: the ratio [0, 1] of comments in the repository
    """
    cloc, sloc = loc_info(path_to_repo)
    ratio_comments = cloc / (cloc + sloc) if (cloc + sloc) != 0 else 0

    return ratio_comments
