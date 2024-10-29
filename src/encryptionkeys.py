import random

class EncryptionKeys:
    """
    Luokka vastaa viestin salaamisesta vaadittavista avaimista
    """

    def public_key_e(self, lam):
        """
        Julkisen avaimen e osan laskemiseen. Palauttaa e osan.
        e osa on satunnainen kokonaisluku väliltä [2, lam-2].
        Lisäksi eksponentti e ja lam ovat keskenään jaottomia.

        Args:
            lam : λ(n) = lcm(p-1, q-1). Alkuluvut p ja q ovat
            toisistaan riippumattomia alkulukuja jotka ovat erisuuret ja 1030 bittiä
        """

        while True:
            e = random.randint(2, lam-1)
            if EncryptionKeys().gcd(e, lam) == 1:
                break
        return e

    def private_key_d(self, p, q, e):
        """
        Salaisen avaimen eksponenttiosan d laskemiseen. Palauttaa salaisen avaimen d osan
        d on modulaariaritmetiikan käänteisluku e modulo lam. Lam saadaan λ(n) = lcm(p-1, q-1).
        Alkuluvut p ja q ovat toisistaan riippumattomia alkulukuja jotka ovat erisuuret ja 1030
        bittiä
        
        Args:
            lam : λ(n) = lcm(p-1, q-1). Alkuluvut p ja q ovat
            toisistaan riippumattomia alkulukuja jotka ovat erisuuret ja 1030 bittiä
            e : satunnainen kokonaisluku väliltä [2, lam-2], e ja lam ovat keskenään jaottomia
        """

        #lmc(a, b) = (abs(ab)/gcd(a, b))
        lcm = abs((p-1)*(q-1)) // EncryptionKeys().gcd(p-1, q-1)
        d = pow(e, -1, lcm)
        return d

    def gcd(self, a, b):
        """
        Eukleideen algoritmi selvittää kahden kokonaisluvun suurimman yhteisen jakajan. Tätä
        tarvitaan salaisen avaimen laskemista varten. Tämän avulla saadaan laskettua pienin
        yhteinen kerroin (lcm) sillä λ(n) = lcm(p-1, q-1). Lisäksi tällä tarkastetaan että
        eksponentti e ja λ(n) ovat keskenään jaottomia. Palauttaa annettujen lukujen suurimman
        yhteisen jakajan

        Args:
            a: positiivinen kokonaisluku
            b: positiivinen kokonaisluku
        """

        if b == 0:
            return a
        return self.gcd(b, a % b)
