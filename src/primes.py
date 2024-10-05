import random

class Primes:
    """Luokka vastaa alkulukujen generoimisesta"""

    def generate_prime(self):
        """Satunnaisten, toisistaan riippumattomien alkulukujen generoimiseen.
        Palauttaa alkuluvun"""

        while True:
            test = random.randrange(999, 10**10, 2)
            if self.check_if_prime(test):
                return test

    def check_if_prime(self, num):
        """
        Tarkistaa Miller-Rabin algoritmia käyttäen onko luku alkuluku.
        Palauttaa totuusarvon
        
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

    def two_primes(self):
        """
        Vastaa alkulukujen generoimisesta ja palauttaa tuplen joka sisältää
        kaksi toisistaan eriävää suurta alkulukua p ja q.
        """

        p = self.generate_prime()
        q = self.generate_prime()
        while p == q:
            q = self.generate_prime()
        return (p, q)
