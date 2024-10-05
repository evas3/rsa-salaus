import sys
from encryption import Encryption
from decryption import Decryption

class Ui:
    """Luokka vastaa ohjelman käyttöliittymäpuolesta ja käyttäjän ohjeistamisesta ohjelman
    käytössä."""

    def __init__(self):
        pass

    def start(self):
        """Funktio käynnistää salausohjelman."""

        print("\nRSA-salaus")
        print("----------\n\n")
        self.menu()

    def menu(self):
        """Funktio näyttää käyttäjälle aloitusvalikon."""

        print("Toiminnot:")
        print("1 : Salaa viesti automaattisesti generoitavilla avaimilla")
        print("2 : Pura viestin salaus")
        print("3 : Lopeta")
        print("")
        func = input("Syötä toimintoa vastaava numero: ")
        try:
            func = int(func)
        except ValueError:
            print("\nSinun täytyy syöttää toimintoa vastaava numero\n")
            self.menu()
        if func == 1:
            self.encrypt()
        elif func == 2:
            self.decrypt()
        elif func == 3:
            self.close()
        else:
            print("\nSinun täytyy syöttää toimintoa vastaava numero\n")
            self.menu()

    def encrypt(self):
        """Funktio viestin salaamisen käyttöliittymäpuolta varten."""

        message = input("\nSyötä viesti jonka haluat salata: ")
        try:
            e = 65537
            message_int = Encryption().message_to_int(message)
            encrypted_info= Encryption().encryption(message_int, e)
            print("\nSalattu viesti on:", str(encrypted_info[0]))
            print("Viesti on salattu käyttäen seuraavaa julkista avainta n:", str(encrypted_info[1]))
            print("Sekä seuraavaa salaista avainta d:", str(encrypted_info[2]))
            print("Huomioi että salainen avain ei saa päätyä ulkopuolisille!\n")
            self.menu()
        except ValueError:
            print("Jotain meni vikaan")
            self.encrypt()

    def decrypt(self):
        """Funktio viestin salauksen purkamisen käyttöliittymäpuolta varten."""

        print("Salauksen purkaminen vaatii kyseisen viestin salaukseen käytetyn salaisen avaimen d ja julkisen avaimen n")
        private_key_d = input("\nSyötä salainen avain d: ")
        public_key_n = input("Syötä julkinen avain n: ")
        encrypted_message = input("Syötä annetuilla avaimilla salattu viesti: ")
        error = "\nSalaisen ja julkisen avaimen tulee olla positiivisia kokonaislukuja.\n"
        try:
            if int(private_key_d) > 0 and int(public_key_n) > 0:
                private_key_d = int(private_key_d)
                public_key_n = int(public_key_n)
                encrypted_message = int(encrypted_message)
                decrypted_message = Decryption().decryption(encrypted_message, private_key_d, public_key_n)
                print("3", decrypted_message)
                original_message = Decryption().message_to_str(decrypted_message)
                print("\nViesti on salaamattomana:", str(original_message)+"\n")
                self.menu()
            else:
                print(error)
                self.decrypt()
        except ValueError:
            print(error)
            self.decrypt()

    def close(self):
        """Funktio joka lopettaa ohjelman suorittamisen."""

        print("\n\nKiitos ja näkemiin!\n")
        sys.exit()
