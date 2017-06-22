import os
import unittest
import tempfile
import cicd
from datetime import datetime

class CICDTest(unittest.TestCase):
    def setUp(self):
        cicd.app.config['TESTING'] = True
        self.app = cicd.app.test_client()

    def test_get_day_left(self):
        now = datetime(2017,7,10,12,0,10)
        target = datetime(2017,7,20,0,0,0)
        assert cicd.get_day_left(now, target) == 10

if __name__ == '__main__':
    unittest.main()
