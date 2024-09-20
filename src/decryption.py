class Decryption:
    """Luokka joka vastaa salauksen purkamisesta"""

    def decryption(self, encrypted_message, private_key_d, public_key_n):
        """
        Vastaa viestin salauksen purkamisesta. Palauttaa viestin siten että sen salaus on purettu.

        Args:
            encrypted_message : purettava viesti numeroina
            private_key_d : salainen avain d. Positiivinen kokonaisluku
            public_key_n : julkinen avain n. Positiivinen kokonaisluku

        """

        decrypted_message = pow(encrypted_message, private_key_d, public_key_n)
        return decrypted_message
