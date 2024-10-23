import random

class EncryptionKeys:
    """
    Luokka vastaa viestin salaamisesta vaadittavista avaimista
    """

    def public_key_e(self, phi):
        """
        Julkisen avaimen e osan laskemiseen. Palauttaa e osan.
        e osa on satunnainen kokonaisluku väliltä [2, phi-2]

        Args:
            phi : (prime_p - 1) * (prime_q - 1). Alkuluvut p ja q ovat
            toisistaan riippumattomia alkulukuja jotka ovat erisuuret ja 1030 bittiä
        """

        return random.randint(2, phi-1)

    def private_key_d(self, phi, e):
        """
        Salaisen avaimen eksponenttiosan d laskemiseen. Palauttaa salaisen avaimen d osan
        d on modulaariaritmetiikan käänteisluku e modulo phi
        
        Args:
            phi : (prime_p - 1) * (prime_q - 1). Alkuluvut p ja q ovat
            toisistaan riippumattomia alkulukuja jotka ovat erisuuret ja 1030 bittiä
            e : satunnainen kokonaisluku väliltä [2, phi-2]
        """

        d = pow(e, -1, phi)
        return d
