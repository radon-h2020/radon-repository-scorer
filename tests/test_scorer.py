import os
import shutil
import unittest

from dotenv import load_dotenv
from reposcorer.scorer import score_repository


class AttributesTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        load_dotenv()
        cls.path_to_repo = os.path.join('test_data', 'ANXS', 'postgresql')

    def test_score_repository(self):
        scores = score_repository(
            path_to_repo=self.path_to_repo,
            host='github',
            full_name='ANXS/postgresql',
            calculate_comments_ratio=True,
            calculate_commit_frequency=True,
            calculate_core_contributors=True,
            calculate_has_ci=True,
            calculate_has_license=True,
            calculate_iac_ratio=True,
            calculate_issue_frequency=False,
            calculate_repository_size=True
        )
        self.assertAlmostEqual(scores['commit_frequency'], 6.5, 0)
        # self.assertEqual(scores['issue_frequency'], 0)
        self.assertEqual(scores['core_contributors'], 14)
        self.assertTrue(scores['has_ci'])
        self.assertTrue(scores['has_license'])


if __name__ == '__main__':
    unittest.main()
