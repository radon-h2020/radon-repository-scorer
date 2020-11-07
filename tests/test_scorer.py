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
        scores = score_repository(host='github', full_name='UoW-CPC/COLARepo', clone_to=self.tmp_dir)

        self.assertAlmostEqual(scores['commit_frequency'], 4.5, 0)
        self.assertEqual(scores['issue_frequency'], 0)
        self.assertEqual(scores['core_contributors'], 3)
        self.assertFalse(scores['has_ci'])
        self.assertFalse(scores['has_license'])


if __name__ == '__main__':
    unittest.main()
