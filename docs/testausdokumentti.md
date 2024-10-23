# Testausdokumentti

Testaaminen on toteutettu Unittestiä käyttäen automaattisilla yksikkötesteillä. Testit testaavat EncryptionKeys-luokkaa, Encryption-luokkaa, Decryption-luokkaa sekä Primes-luokkaa. Lisäksi käyttöliittymää on testattu manuaalisesti.

## Ykköstestit

Luokkan EncryptionKeys osalta testataan yksityisen avaimen ja julkisen avaimen luomista. Yksityisen avaimen d osalta tarkastetaan muutamalla phii, e, parilla että d:n arvo on oikeanlainen. Satunnaisesta eksponentista e tarkastetaan että se on positiivinen kokonaisluku joka on suurempi kuin 2 mutta pienempi kuin annettu luku.

Encryption_tests testaa sekä Encryption että Decryption luokkaa. Se testaa että viestin muuttaminen merkeistä numeroihin ja takaisin toimii halutulla tavalla eli että kun viesti muunnetaan numeeriseen muotoon, saadaan alkuperäinen viesti kääntämällä numeerinen muoto takaisin merkeiksi. Testaamisessa on käytetty erikoismerkkejä ja numeroita sisältävää merkkijonoa, sekä tyhjää merkkijonoa. Lisäksi on testattu että varsinainen salaaminen toimii eli että salattu viesti saadaan purettua takaisin alkuperäiseen muotoon. Tässäkin on käytetty kirjaimia, numeroita ja erikoismerkkejä sisältävää merkkijonoa, suurta lukua sekä tyhjää merkkijonoa. Käyttäjä voi antaa ainoastaan str muoroisia syötteitä joten muilla syötteillä ohjelmaa ei ole testattu.

Primes_test testaa Primes luokkaa. Se tarkastaa että two_primes funktio antaa tuplen joka sisältää kaksi toisistaan eroavaa alkulukua. Lisäksi se testaa että annettu alkuluku on tarpeeksi suuri eli sen pituus bitteinä on yli 1024. Testeissä tarkastetaan että Erastotheneen seulan avulla luotu lista alkuluvuista välillä [2, 5000] vastaa totuutta. Miller-Rabin algoritmia testataan listalla suuria alkulukuja ja toisella listalla lukuja jotka eivät ole alkulukuja.

## Testien ajaminen
Testit voi ajaa käyttäen komentoa

```
poetry run invoke tests
```


Testikattavuusraportin saa luotua komennolla

```
poetry run invoke coverage
```

## Testikattavuus
Testikattavuus näyttää tältä

![alt text](https://github.com/evas3/rsa-salaus/blob/main/docs/testikattavuus.png)

Testejä on vain 19 kappaletta. Kaikki testit menevät läpi mutta testien läpikäyntiin kuluu jonkin verran aikaa. Testien haarautumiskattavuus on 98%. Tiedoston primes.py 61 rivi jää siis testikattavuuden ulkopuolelle. Kyseisellä rivillä funktio two_primes varmistaa että generoidut alkuluvut p ja q eivät ole sama luku. Jos ne ovat samat niin alkuluku q generoidaan uudestaan niin monta kertaa kunnes alkuluvut ovat erisuuret ennen kun ne sisältävä tuple palautetaan. 

## Käyttöliittymän testaus
Annettaessa alkuvalikkoon tyhjä merkkojono, merkkijono tai numero joka ei vastaa toimintoa, käyttöliittymä kysyy uudelleen haluttua toimintoa. 

Toiminnolla 1 käyttäjä voi salata viestin. Jos viesti on liian pitkä eli yli 256 tavua, käyttöliittymä huomauttaa tästä ja kysyy uudelleen viestiä. Jos kentän jättää tyhjäksi eli ohjelmalle antaa tyhjän merkkijonon ohjelma salaa sen. Salattu viesti on tällöin 0 mutta kun salaus puretaan saadaan alkuperäinen viesti eli tyhjä merkkijono. Kun viesti on tavurajoituksen puitteissa se salataan ja käyttäjälle tulostetaan salattu viesti sekä viestin salaamiseen käytetyt avaimet n ja d.

Toiminnolla 2 käyttäjä voi purkaa viestin salauksen. Käyttäjän tulee syöttää salainen avain d, julkinen avain n sekä salattu viesti. Ohjelma kysyy nämä kaikki ennen kun ilmoittaa käyttäjän syötteen olevan mahdollisesti virheellinen. Jos yksi tai useampi käyttäjän antamista arvoista on virheellinen (viesti on tyhjä merkkijono, toinen tai molemmat avaimet ovat merkkijonoja tai tyhjiä merkkijonoja, toinen tai molemmat avaimet ovat nolla, negatiivisia lukuja tai desimaalilukuja tai jos avaimet eivät vastaa salattua viestiä) niin käyttöliittymä ilmoittaa käyttäjälle etteivät avaimet vastaa viestiä ja kysyy kaikkia arvoja uudelleen.

Toiminto 3 sulkee ohjelman.
