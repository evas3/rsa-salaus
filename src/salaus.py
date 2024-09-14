import random
import math

class Salaus:
    """Luokka vastaa viestin salaamisesta ja salauksen purkamisesta"""

    def __init__(self):
        """p ja q jotka muodostavat julkisen avaimen n osuuden"""
        
        self.p = None
        self.q = None

    def generate_prime(self):
        """Satunnaisten, toisistaan riippumattomien alkulukujen generoimiseen"""

        pass

    def public_key_n(self):
        """Julkisen avaimen n osan laskemiseen"""

        p = self.generate_prime()
        self.p = 12
        q = self.generate_prime()
        self.q = 13
        n = p * q
        return n

    def public_key_e(self):
        """Julkisen avaimen e osan laskemiseen"""

        e_smaller_than = (self.p-1)*(self.q-1)
        e = random.randint(2, e_smaller_than-1)
        return e
