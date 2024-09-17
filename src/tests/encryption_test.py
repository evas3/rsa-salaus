import unittest
from encryption import Encryption

class TestEncryption(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_check_if_prime(self):
        primes = [7001, 7013, 7019, 7027, 7039, 7043, 7057, 7069, 7079, 7103, 5939, 5953, 5981, 5987, 6007]
        for i in primes:
            result = Encryption.check_if_prime(self, int(i))
            self.assertEqual(True, result)
