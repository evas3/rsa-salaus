import random

class EncryptionKeys:
    """Luokka vastaa viestin salaamisesta vaadittavista avaimista"""

    def public_key_e(self, phi):
        """
        Julkisen avaimen e osan laskemiseen. Palauttaa e osan
        
        Args:
            phi : (prime_p - 1) * (prime_q - 1). Alkuluvut ovat
            toisistaan riippumattomia alkulukuja jotka ovat erisuuret ja > 1000
        """

        return random.randint(2, phi-1)

    def private_key_d(self, phi, e):
        """
        Salaisen avaimen eksponenttiosan d laskemiseen. Palauttaa salaisen avaimen d osan
        
        Args:
            phi : (prime_p - 1) * (prime_q - 1). Alkuluvut ovat
            toisistaan riippumattomia alkulukuja jotka ovat erisuuret ja > 1000
            e : satunnainen kokonaisluku väliltä [2, phi-2]
        """

        d = pow(e, -1, phi)
        return d
