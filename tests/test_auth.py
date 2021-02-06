import unittest

import sys
sys.path.append('./')
from base import BaseTestCase

class TestStuff(BaseTestCase):
    def test_1(self):
        self.assertEqual(True, True)
 
if __name__ == "__main__":
    unittest.main()
