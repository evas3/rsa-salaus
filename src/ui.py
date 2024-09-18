import sys
from encryptionkeys import EncryptionKeys

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

    def decrypt(self):
        """Funktio viestin salauksen purkamisen käyttöliittymäpuolta varten."""
        
        private_key_d = input("\nSyötä salainen avain d:")
        public_key_n = input("Syötä julkinen avain n: ")
        encrypted_message = input("Syötä annetuilla avaimilla salattu viesti: ")

    
    def close(self):
        """Funktio joka lopettaa ohjelman suorittamisen."""
        
        print("\n\nKiitos ja näkemiin!\n")
        sys.exit()
