import os
import unittest

from dotenv import load_dotenv
from pathlib import Path
from pydriller import GitRepository

from repositoryscorer.scorer import score_repository

ROOT = os.path.realpath(__file__).rsplit(os.sep, 2)[0]
PATH_TO_REPO = str(Path(os.path.join(ROOT, 'test_data', 'ANXS', 'postgresql')))


class ScoreRepositoryTestCase(unittest.TestCase):

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
    def test_score_repository():

        report = score_repository(PATH_TO_REPO,
                                  os.getenv('GITHUB_ACCESS_TOKEN'),
                                  'ANXS',
                                  'postgresql')

        assert report == {'repository': PATH_TO_REPO,
                          'continuous_integration': True,
                          'percent_comment': 0.2032,
                          'commit_frequency': 6.51,
                          'core_contributors': 14,
                          'iac_ratio': 0.6709,
                          'issue_frequency': 5.1,
                          'license': True,
                          'repository_size': 1345
                          }


if __name__ == '__main__':
    unittest.main()
