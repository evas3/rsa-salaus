import random
import math

class EncryptionKeys:
    """Luokka vastaa viestin salaamisesta vaadittavista avaimista"""

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

    def public_key_n(self p, q):
        """
        Julkisen avaimen n osan laskemiseen. Palauttaa n osan
        
        Args:
            p ja q : toisistaan riippumattomia alkulukuja jotka ovat > 1000
        """

        n = p * q
        return n

    def public_key_e(self, p, q):
        """
        Julkisen avaimen e osan laskemiseen. Palauttaa e osan
        
        Args:
            p ja q : toisistaan riippumattomia alkulukuja jotka ovat > 1000
        """

        e_smaller_than = (p-1)*(q-1)
        e = random.randint(2, e_smaller_than-1)
        return e
