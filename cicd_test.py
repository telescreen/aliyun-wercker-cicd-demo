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

    def test_index(self):
        """
        テストケース1: '/' へアクセスするときに200を返さなければならない
        """
        rv = self.app.get('/')
        assert rv.status_code == 200

    def test_model_data(self):
        """
        テストケース2: モデルのデータサイズは2でなければならない
        """
        rv = cicd.model_data()
        assert len(rv) == 2

    #def test_newlayout(self):
    #    """
    #    テストケース3:
    #     + newlayoutへアクセスが正常でなければならない
    #     + SBCloud という文字を含まなければならない
    #    """
    #    rv = self.app.get('/')
    #    assert rv.status_code == 200
    #    assert b"SBCloud!" in rv.data

if __name__ == '__main__':
    unittest.main()
