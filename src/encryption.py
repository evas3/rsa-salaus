from encryptionkeys import EncryptionKeys
from primes import Primes

class Encryption:
    """Luokka vastaa viestin salaamisesta"""

    def message_to_int(self, message):
        """
        Muuttaa viestin int muotoon ja palauttaa int muotoisen viestin.
        
        Args:
            message : käyttäjän antama salattava viesti
        """

        return int.from_bytes(message.encode(), byteorder="big")

    def encryption(self, message_as_numbers, public_key_e):
        """
        Vastaa viestin salaamisesta. Palauttaa tuplen jonka ensimmäinen elementti on
        salattu viesti, toinen elementti julkinen avain n ja viimeinen salainen avain d.

        Args:
            message_as_numbers : salattava viesti numeroina
            public_key_e : julkinen avain e. Positiivinen kokonaisluku

        """

        primes = Primes().two_primes()
        prime_p = primes[0]
        prime_q = primes[1]
        n = prime_p * prime_q
        phi =  (prime_p - 1) * (prime_q - 1)
        encrypted_message = pow(message_as_numbers, public_key_e, n)
        private_key_d = EncryptionKeys().private_key_d(phi, public_key_e)
        return (encrypted_message, n, private_key_d)
