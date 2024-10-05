import math

class Decryption:
    """Luokka joka vastaa salauksen purkamisesta"""

    def message_to_str(self, message):
        """
        Vastaa viestin muuntamisesta takaisin alkuperäiseen muotoon, palauttaa tämän
        
        Args:
            message : viesti int muodossa
        """

        length = math.ceil((message.bit_length() / 8))
        return message.to_bytes(length, byteorder="big").decode()

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
