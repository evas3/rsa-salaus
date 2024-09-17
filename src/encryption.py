import random
import math

class Encryption:
    """Luokka vastaa viestin salaamisesta ja salauksen purkamisesta"""

    def __init__(self):
        """p ja q jotka muodostavat julkisen avaimen n osuuden"""

        self.p = None
        self.q = None

    def generate_prime(self):
        """Satunnaisten, toisistaan riippumattomien alkulukujen generoimiseen. Palauttaa alkuluvun"""

        while True:
            test = random.randrange(999, 10**10, 2)
            if self.check_if_prime(test):
                return test

    def check_if_prime(self, num):
        """
        Tarkistaa Miller-Rabin algoritmia käyttäen onko luku alkuluku. Palauttaa totuusarvon
        
        Args:
            num : kokonaisluku joka tarkastetaan
        """

        e = num - 1
        while e % 2 == 0:
            e = int(e / 2)
        for i in range(10):
            a = random.randint(2, num-1)
            pow_unbroken = True
            if pow(a, e, num) == 1:
                continue
            while e < num-1:
                if pow(a, e, num) == num-1:
                    pow_unbroken = False
                    break
                e = e*2
            if pow_unbroken:
                return False
        return True

    def public_key_n(self):
        """Julkisen avaimen n osan laskemiseen"""

        p = self.generate_prime()
        self.p = p
        q = self.generate_prime()
        self.q = q
        n = p * q
        return n

    def public_key_e(self):
        """Julkisen avaimen e osan laskemiseen"""

        e_smaller_than = (self.p-1)*(self.q-1)
        e = random.randint(2, e_smaller_than-1)
        return e
