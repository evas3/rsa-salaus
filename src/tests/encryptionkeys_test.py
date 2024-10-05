import unittest
from encryptionkeys import EncryptionKeys

class TestEncryptionKeys(unittest.TestCase):
    def setUp(self):
        pass

    def test_private_key_d(self):
        for i in [(3120, 17), (99, 23) , (76408, 345)]:
            d = EncryptionKeys().private_key_d(i[0], i[1])
            mod_mulp_inv = pow(i[1], -1, i[0])
            self.assertEqual(d, mod_mulp_inv)
            self.assertGreater(d, 0)
            self.assertEqual(d.is_integer(), True)

    def test_public_key_e(self):
        e = EncryptionKeys().public_key_e(70391)
        self.assertGreater(e, 2)
        self.assertLess(e, 70391)

    def test_public_key_e_integer(self):
        e = EncryptionKeys().public_key_e(70391)
        self.assertEqual(e.is_integer(), True)
