import os
import shutil
import unittest

from dotenv import load_dotenv
from reposcorer.scorer import score_repository


class AttributesTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        load_dotenv()
        cls.tmp_dir = os.path.join('test_data', 'tmp')
        os.mkdir(cls.tmp_dir)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp_dir)

    def test_score_repository(self):
        scores = score_repository(
            host='github',
            full_name='UoW-CPC/COLARepo',
            clone_to=self.tmp_dir,
            calculate_comments_ratio= True,
            calculate_commit_frequency=True,
            calculate_core_contributors = True,
            calculate_has_ci=True,
            calculate_has_license = True,
            calculate_iac_ratio=True,
            calculate_issue_frequency=True,
            calculate_repository_size=True
        )

        self.assertAlmostEqual(scores['commit_frequency'], 4.5, 0)
        self.assertEqual(scores['issue_frequency'], 0)
        self.assertEqual(scores['core_contributors'], 3)
        self.assertFalse(scores['has_ci'])
        self.assertFalse(scores['has_license'])


if __name__ == '__main__':
    unittest.main()
