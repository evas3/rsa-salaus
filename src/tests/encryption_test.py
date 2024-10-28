import unittest
from encryption import Encryption
from decryption import Decryption

class TestEncryption(unittest.TestCase):
    def setUp(self):
        pass

    def test_message_to_int_txt_input(self):
        message = "Hello This Is ä message to you all!-*/32312"
        encoded = Encryption().message_to_int(message)
        decoded = Decryption().message_to_str(encoded)
        self.assertEqual(decoded, message)
    
    def test_message_to_int_txt_input_long(self):
        message = "Hello This Text Is A Litle Bit Longer Than The One Before :D! Less Than 2048 Bits Tho"
        encoded = Encryption().message_to_int(message)
        decoded = Decryption().message_to_str(encoded)
        self.assertEqual(decoded, message)

    def test_message_to_int_txt_input_special_char(self):
        message = "ÄÅÖø´`<@|-_'*/$#!#¤%Y/)=??@£$‚{[]}"
        encoded = Encryption().message_to_int(message)
        decoded = Decryption().message_to_str(encoded)
        self.assertEqual(decoded, message)

    def test_message_to_int_int_input(self):
        message = "34748735453846387366385743658376475365"
        encoded = Encryption().message_to_int(message)
        decoded = Decryption().message_to_str(encoded)
        self.assertEqual(decoded, message)

    def test_message_to_int_empty_input(self):
        message = ""
        encoded = Encryption().message_to_int(message)
        decoded = Decryption().message_to_str(encoded)
        self.assertEqual(decoded, message)

    def test_message_to_int_is_int(self):
        message = "Hello This Is ä message to you all!-*/32312"
        encoded = Encryption().message_to_int(message)
        self.assertEqual(encoded.is_integer(), True)

    def test_encryption_is_integer(self):
        message = 34748735453846387366385743658376475365
        encrypted = Encryption().encryption(message, 65537)
        self.assertEqual(encrypted[0].is_integer(), True)

    def test_encryption_num(self):
        message = 34748735453846387366385743658376475365
        encrypted_info = Encryption().encryption(message, 65537)
        decrypted = Decryption().decryption(encrypted_info[0], encrypted_info[2], encrypted_info[1])
        self.assertEqual(message, decrypted)

    def test_encryption_txt(self):
        message = "Hello This Is ä message to you all!-*/32312"
        encoded = Encryption().message_to_int(message)
        encrypted_info = Encryption().encryption(encoded, 65537)
        decrypted = Decryption().decryption(encrypted_info[0], encrypted_info[2], encrypted_info[1])
        decoded = Decryption().message_to_str(decrypted)
        self.assertEqual(message, decoded)

    def test_encryption_empty(self):
        message = ""
        encoded = Encryption().message_to_int(message)
        encrypted_info = Encryption().encryption(encoded, 65537)
        decrypted = Decryption().decryption(encrypted_info[0], encrypted_info[2], encrypted_info[1])
        decoded = Decryption().message_to_str(decrypted)
        self.assertEqual(message, decoded)
    
    def test_encryption_longer_txt(self):
        message = "Hello This Text Is A Litle Bit Longer Than The One Before :D! Less Than 2048 Bits Tho"
        encoded = Encryption().message_to_int(message)
        encrypted_info = Encryption().encryption(encoded, 65537)
        decrypted = Decryption().decryption(encrypted_info[0], encrypted_info[2], encrypted_info[1])
        decoded = Decryption().message_to_str(decrypted)
        self.assertEqual(message, decoded)

    def test_encryption_special_chars(self):
        message = "ÄÅÖø´`<@|-_'*/$#!#¤%Y/)=??@£$‚{[]}"
        encoded = Encryption().message_to_int(message)
        encrypted_info = Encryption().encryption(encoded, 65537)
        decrypted = Decryption().decryption(encrypted_info[0], encrypted_info[2], encrypted_info[1])
        decoded = Decryption().message_to_str(decrypted)
        self.assertEqual(message, decoded)
