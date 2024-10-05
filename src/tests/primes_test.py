import unittest
from primes import Primes

class TestEncryptionKeys(unittest.TestCase):
    def setUp(self):
        pass

    def test_generate_prime(self):
        prime = EncryptionKeys().generate_prime()
        answer = EncryptionKeys().check_if_prime(prime)
        self.assertEqual(True, answer)
        self.assertGreater(prime, 1000)
        self.assertLess(prime, 10**10)

    def test_check_if_prime(self):
        primes = [7001, 7013, 7019, 7027, 7039, 7043, 7057, 7069, 7079, 7103, 5939, 5953, 5981, 5987, 6007]
        for i in primes:
            result = EncryptionKeys.check_if_prime(self, int(i))
            self.assertEqual(True, result)

    def test_two_primes(self):
        pass