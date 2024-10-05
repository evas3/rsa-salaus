import unittest
from primes import Primes

class TestEncryptionKeys(unittest.TestCase):
    def setUp(self):
        pass

    def test_generate_prime_is_prime(self):
        prime = Primes().generate_prime()
        answer = Primes().check_if_prime(prime)
        self.assertEqual(True, answer)

    def test_generate_prime_large_enough(self):
        prime = Primes().generate_prime()
        self.assertGreater(prime, 1000)
        self.assertLess(prime, 10**10)

    def test_generate_prime_is_integer(self):
        prime = Primes().generate_prime()
        self.assertEqual(prime.is_integer(), True)

    def test_check_if_prime_not(self):
        non_primes = [6, 14, 7003, 7015, 5989]
        for i in non_primes:
            result = Primes.check_if_prime(self, int(i))
            self.assertEqual(False, result)

    def test_check_if_prime(self):
        primes = [7001, 7013, 7019, 7027, 7039, 7043, 7057, 7069, 7079, 7103, 5939, 5953, 5981, 5987, 6007]
        for i in primes:
            result = Primes.check_if_prime(self, int(i))
            self.assertEqual(True, result)

    def test_two_primes_differ(self):
        pair = Primes().two_primes()
        self.assertEqual((pair[0]==pair[1]), False)

    def test_two_primes_tuple(self):
        pair = Primes().two_primes()
        self.assertEqual(type(pair), tuple)
