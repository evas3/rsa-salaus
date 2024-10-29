import math

class Decryption:
    """
    Luokka joka vastaa salauksen purkamisesta
    """

    def message_to_str(self, message):
        """
        Vastaa viestin muuntamisesta takaisin alkuperäiseen muotoon, palauttaa viestin
        alkuperäisessä muodossa. Ceil palauttaa pienimmän kokonaisluvun joka ei ole
        alle sille alletun arvon. Decode/encode käyttää UTF-8
        
        Args:
            message : viesti int muodossa
        """

        length = math.ceil((message.bit_length() / 8))
        return message.to_bytes(length, byteorder="big").decode()

    def decryption(self, encrypted_message, private_key_d, public_key_n):
        """
        Vastaa viestin salauksen purkamisesta. Palauttaa viestin siten että sen salaus on purettu.
        salaamaton viesti saadaan RSA-salauksessa kaavalla (salattu viesti)^{d} mod n jossa n on
        kahden suuren toisistaan eriävän alkuluvun (q ja p) tulo.

        Args:
            encrypted_message : purettava viesti numeroina
            private_key_d : salainen avain d. Positiivinen suuri kokonaisluku
            public_key_n : julkinen avain n. Positiivinen suuri kokonaisluku
        """

        decrypted_message = pow(encrypted_message, private_key_d, public_key_n)
        return decrypted_message
