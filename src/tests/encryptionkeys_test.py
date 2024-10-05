import unittest
from encryptionkeys import EncryptionKeys

class TestEncryptionKeys(unittest.TestCase):
    def setUp(self):
        pass

    def test_private_key_d(self):
        pass

    def test_public_key_e(self):
        e = EncryptionKeys().public_key_e(7039, 5953)
        e_less = (7039-1)*(5953-1)
        self.assertGreater(e, 2)
        self.assertLess(e, e_less)
