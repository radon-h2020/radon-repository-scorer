"""
The metric for the license dimension may be defined as a piecewise function \
that returns 1 if the repository has a license, 0 otherwise
"""

import os


def has_license(path_to_repo: str) -> bool:
    return any('license' in name.lower() or 'licence' in name.lower() for name in os.listdir(path_to_repo))
