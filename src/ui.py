import sys
from encryption import Encryption
from decryption import Decryption

class Ui:
    """
    Luokka vastaa ohjelman käyttöliittymäpuolesta ja käyttäjän ohjeistamisesta ohjelman
    käytössä.
    """

    def start(self):
        """
        Funktio käynnistää salausohjelman.
        """

        print("\n----------")
        print("RSA-salaus")
        print("----------\n\n")
        self.menu()

    def menu(self):
        """
        Funktio tulostaa käyttäjälle aloitusvalikon. Käyttäjän tulee syöttää
        ohjelmalle haluttua toimintoa vastaava numero. Jos numero ei vastaa
        mitään toimintoa, sitä kysytään uudestaan
        """

        print("Toiminnot:")
        print("1 : Salaa viesti automaattisesti generoitavilla avaimilla")
        print("2 : Pura viestin salaus")
        print("3 : Lopeta\n")
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
        """
        Funktio viestin salaamisen käyttöliittymäpuolta varten. Käyttäjän tulee
        syöttää ohjelmalle salattava viesti. Jos viesti on alle 256 tavua pitkä,
        ohjelma tulostaa käyttäjälle viestin salattuna sekä julkisen avaimen n
        ja salaisen avaimen d palaten valikkoon. Muutoin viestiä kysytään uudelleen
        """

        message = input("\nSyötä viesti jonka haluat salata (viestin täytyy olla alle 256 tavua): ")
        e = 65537
        try:
            message_int = Encryption().message_to_int(message)
            encrypted_info= Encryption().encryption(message_int, e)
            #Testaa ettei viesti ole liian pitkä ja että se on purettavissa
            test_decryption = Decryption().decryption(encrypted_info[0], encrypted_info[2], encrypted_info[1])
            test_msg_to_str = Decryption().message_to_str(test_decryption)
            print("\n\nSalattu viesti on:", str(encrypted_info[0]),"\n")
            print("Viesti on salattu käyttäen seuraavaa julkista avainta n:", str(encrypted_info[1]),"\n")
            print("Sekä seuraavaa salaista avainta d:", str(encrypted_info[2]),"\n")
            print("Huomioi että salainen avain ei saa päätyä ulkopuolisille!\n\n")
            self.menu()

        except ValueError:
            print("Salattavan viestin tulee olla alle 256 tavua pitkä")
            self.encrypt()

    def decrypt(self):
        """
        Funktio viestin salauksen purkamisen käyttöliittymäpuolta varten.
        Käyttäjän tulee syöttää ohjelmalle salattu viesti sekä salainen avain d
        ja julkinen avain n joita käytäen viesti on salattu. Avainten tulee vastata
        salattua viestiä, muutoin ohjelma huomauttaa tästä. Jos avaimet ja viesti
        täsmäävät tulostetaan viesti salaamattomana ja palataan valikkoon
        """

        print("\nSalauksen purkaminen vaatii kyseisen viestin salaukseen käytetyn salaisen avaimen d ja julkisen avaimen n")
        private_key_d = input("\nSyötä salainen avain d: ")
        public_key_n = input("\nSyötä julkinen avain n: ")
        encrypted_message = input("\nSyötä annetuilla avaimilla salattu viesti: ")

        try:
            if int(private_key_d) > 0 and int(public_key_n) > 0 and int(private_key_d).bit_length() > 2047 and int(public_key_n).bit_length() > 2047:
                private_key_d = int(private_key_d)
                public_key_n = int(public_key_n)
                encrypted_message = int(encrypted_message)
                decrypted_message = Decryption().decryption(encrypted_message, private_key_d, public_key_n)
                original_message = Decryption().message_to_str(decrypted_message)
                print("\n\nViesti on salaamattomana:", str(original_message)+"\n\n")
                self.menu()
            else:
                print("\nAvainten tulee olla positiivisia kokonaislukuja joiden pituus bitteinä on vähintään 2048")
                self.decrypt()

        except ValueError:
            print("\nAvainten tulee olla ne avaimet joilla annettu viesti on salattu\n")
            self.decrypt()

    def close(self):
        """
        Funktio joka lopettaa ohjelman suorittamisen.
        """

        print("\n\nKiitos ja näkemiin!\n")
        sys.exit()
