import os
from pygount import ProjectSummary, SourceAnalysis
from reposcorer.utility import get_files


def loc_info(path_to_repo: str):
    """
    Return statistics on the lines of code
    :param path_to_repo: str - path to the repository to analyze
    :return: a tuple (cloc, sloc) where cloc and sloc are the number of commented and source lines of code, respectively
    """

    # Get all the files
    source_paths = get_files(path_to_repo)
    for root, _, filenames in os.walk(path_to_repo):
        if '.git' in root:
            continue

        for filename in filenames:
            path = os.path.join(root, filename)
            source_paths.add(path)

    # Analyze the files
    project_summary = ProjectSummary()
    for source_path in source_paths:
        try:
            source_analysis = SourceAnalysis.from_file(source_path, "pygount")
            project_summary.add(source_analysis)
        except (FileNotFoundError, TypeError, OSError):
            pass

    sloc = sum([summary.code_count for summary in project_summary.language_to_language_summary_map.values()])
    cloc = sum([summary.documentation_count for summary in project_summary.language_to_language_summary_map.values()])

    return cloc, sloc
