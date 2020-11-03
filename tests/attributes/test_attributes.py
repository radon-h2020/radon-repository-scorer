import os
import unittest

from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path
from pydriller import GitRepository

from reposcorer.attributes.comments import comments_ratio
from reposcorer.attributes.community import core_contributors
from reposcorer.attributes.continuous_integration import has_continuous_integration
from reposcorer.attributes.history import commit_frequency
from reposcorer.attributes.iac import iac_ratio
from reposcorer.attributes.issues import github_issue_event_frequency, gitlab_issue_event_frequency
from reposcorer.attributes.licensing import has_license
from reposcorer.attributes.loc_info import loc_info

ROOT = os.path.realpath(__file__).rsplit(os.sep, 3)[0]
PATH_TO_REPO = str(Path(os.path.join(ROOT, 'test_data', 'ANXS', 'postgresql')))


class AttributesTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        load_dotenv()
        cls.git_repo = GitRepository(PATH_TO_REPO)
        cls.git_repo.reset()
        cls.git_repo.checkout('d8fc0d3316aa7ed099f23ce3a5546a74734aef8d')

    @classmethod
    def tearDownClass(cls):
        cls.git_repo.reset()

    @staticmethod
    def test_commit_frequency():
        assert round(commit_frequency(PATH_TO_REPO)) == 7

    @staticmethod
    def test_core_contributors():
        assert core_contributors(PATH_TO_REPO) == 14

    @staticmethod
    def test_has_continuous_integration():
        assert has_continuous_integration(PATH_TO_REPO)

    @staticmethod
    def test_iac_ratio():
        assert round(iac_ratio(PATH_TO_REPO), 2) == 0.67

    @staticmethod
    def test_github_issue_event_frequency():
        issue_frequency = github_issue_event_frequency(full_name_or_id='ANXS/postgresql',
                                                       since=None,
                                                       until=datetime(year=2020, month=10, day=20))

        assert round(issue_frequency, 1) == 5.0

    @staticmethod
    def test_gitlab_issue_event_frequency():
        issue_frequency = gitlab_issue_event_frequency(full_name_or_id='commonshost/ansible',
                                                       since=None,
                                                       until=datetime(year=2020, month=10, day=20))

        assert round(issue_frequency, 1) == 2.1

    @staticmethod
    def test_has_license():
        assert has_license(PATH_TO_REPO)

    @staticmethod
    def test_loc_info():
        cloc, sloc = loc_info(PATH_TO_REPO)
        assert cloc == 343
        assert sloc == 1345

    @staticmethod
    def test_comments_ratio():
        assert comments_ratio(PATH_TO_REPO) == 343 / (343 + 1345)


if __name__ == '__main__':
    unittest.main()
