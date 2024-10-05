import random

class EncryptionKeys:
    """Luokka vastaa viestin salaamisesta vaadittavista avaimista"""

    def public_key_e(self, p, q):
        """
        Julkisen avaimen e osan laskemiseen. Palauttaa e osan
        
        Args:
            p ja q : toisistaan riippumattomia alkulukuja jotka ovat erisuuret ja > 1000
        """

        e_smaller_than = (p-1)*(q-1)
        e = random.randint(2, e_smaller_than-1)
        return e

    def private_key_d(self, p, q, e):
        """
        Salaisen avaimen eksponenttiosan d laskemiseen. Palauttaa salaisen avaimen d osan
        
        Args:
            p ja q : toisistaan riippumattomia alkulukuja jotka ovat erisuuret ja > 1000
        """

        k = 1
        on = (p-1)*(q-1)
        while True:
            value = (1+k*on)/e
            if value.is_integer():
                return int(value)
            k += 1
