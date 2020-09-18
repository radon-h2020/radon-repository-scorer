import os
import unittest

from dotenv import load_dotenv
from pathlib import Path
from pydriller import GitRepository

from repositoryscorer.attributes.community import core_contributors
from repositoryscorer.attributes.continuous_integration import has_continuous_integration
from repositoryscorer.attributes.history import commit_frequency
from repositoryscorer.attributes.iac import iac_ratio
from repositoryscorer.attributes.issues import issue_event_frequency
from repositoryscorer.attributes.licensing import has_license
from repositoryscorer.attributes.loc_info import loc_info

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
    def test_issue_event_frequency():
        assert round(issue_event_frequency(PATH_TO_REPO, os.getenv('GITHUB_ACCESS_TOKEN'), 'ANXS', 'postgresql'), 1) == 5.1

    @staticmethod
    def test_has_license():
        assert has_license(PATH_TO_REPO)

    @staticmethod
    def test_loc_info():
        cloc, sloc = loc_info(PATH_TO_REPO)
        assert cloc == 343
        assert sloc == 1345


if __name__ == '__main__':
    unittest.main()
