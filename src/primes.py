import secrets
import random

class Primes:
    """
    Luokka vastaa salaukseen vaadittavien alkulukujen generoimisesta
    """

    def generate_prime(self):
        """
        Satunnaisten, toisistaan riippumattomien alkulukujen generoimiseen.
        Palauttaa todennäköisen alkuluvun. Secrets kirjaston randbits palauttaa
        satunnaisen luvun jossa on spesifoitu määrä bittejä.
        """

        while True:
            test = secrets.randbits(1030)
            if self.check_if_prime(test):
                return test

    def check_if_prime(self, num):
        """
        Tarkistaa Miller-Rabin algoritmia ja pienten alkulukujen listaa käyttäen onko
        luku todennäköisesti alkuluku. Palauttaa totuusarvon.

        Args:
            num : kokonaisluku joka tarkastetaan
        """

        for i in Primes().small_primes():
            if num % i == 0:
                return False

        #Miller-Rabin alkulukutesti
        e = num - 1
        while e % 2 == 0:
            e = int(e // 2)
        for i in range(40):
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

    def small_primes(self):
        """
        Palauttaa listan pienimmistä alkuluvuista jottei aina tarvitse käyttää
        Miller-Rabin algoritmia. Käyttää listan luomiseen Erastotheneen seulaa.
        """

        num_list = [True for num in range(5000)]
        primes = []
        p = 2
        while p**2 <= 4999:
            if num_list[p]:
                #p:llä kerrolliset luvut eivät ole alkulukuja
                for i in range(p**2, 5000, p):
                    num_list[i] = False
            p += 1

        for i in range(2, 5000):
            if num_list[i]:
                primes.append(i)
        return primes
