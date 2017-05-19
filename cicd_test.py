import os
import unittest
import tempfile
import cicd

class CICDTest(unittest.TestCase):
    def setUp(self):
        cicd.app.config['TESTING'] = True
        self.app = cicd.app.test_client()

    def tearDown(self):
        pass

    def test_hello(self):
        rv = self.app.get('/hello')
        assert b'Hello world' in rv.data

    def test_index(self):
        pass

if __name__ == '__main__':
    unittest.main()
