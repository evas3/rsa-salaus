from encryptionkeys import EncryptionKeys

class Encryption:
    """Luokka vastaa viestin salaamisesta"""

    def __init__(self):
        """Konstruktori avaimia varten"""

        self.p = EncryptionKeys().generate_prime()
        self.q = EncryptionKeys().generate_prime()
        while self.p == self.q:
            self.q = EncryptionKeys().generate_prime()
        self.n = EncryptionKeys().public_key_n(self.p, self.q)

    def encryption(self, message_as_numbers, public_key_e):
        """
        Vastaa viestin salaamisesta. Palauttaa salatun viestin.

        Args:
            message_as_numbers : salattava viesti numeroina
            public_key_e : julkinen avain e. Positiivinen kokonaisluku

        """

        encrypted_message = pow(message_as_numbers, public_key_e, self.n)
        return encrypted_message
