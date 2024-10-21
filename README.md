# RSA-salaus

Algoritmit ja tekoäly harjoitustyö 2024

## Dokumentaatio

- [Määrittelydokumentti](https://github.com/evas3/rsa-salaus/blob/main/docs/maarittelydokumentti.md)

- [Toteutusdokumentti](https://github.com/evas3/rsa-salaus/blob/main/docs/toteutusdokumentti.md)

- [Testausdokumentti](https://github.com/evas3/rsa-salaus/blob/main/docs/testausdokumentti.md)

- Käyttöohje löytyy alempaa
  

## Viikkoraportit:

- [Viikkoraportti 1](https://github.com/evas3/rsa-salaus/blob/main/docs/viikkoraportti1.md)

- [Viikkoraportti 2](https://github.com/evas3/rsa-salaus/blob/main/docs/viikkoraportti2.md)

- [Viikkoraportti 3](https://github.com/evas3/rsa-salaus/blob/main/docs/viikkoraportti3.md)

- [Viikkoraportti 4](https://github.com/evas3/rsa-salaus/blob/main/docs/viikkoraportti4.md)

- [Viikkoraportti 5](https://github.com/evas3/rsa-salaus/blob/main/docs/viikkoraportti5.md)

- [Viikkoraportti 6](https://github.com/evas3/rsa-salaus/blob/main/docs/viikkoraportti6.md)

## Käyttöohje

Ensin käyttäjän tulee asentaa tarvittavat riippuvuudet komennolla

```
poetry install
```


Tämän jälkeen sovellus käynnistetään komennolla

```
poetry run invoke start
```


Käynnistämisen jälkeen käyttöliittymä opastaa käyttäjää ohjelman käytössä.

Ohjelmasta löytyy kolme toimintoa: viestin salaaminen automaattisesti generoitavilla avaimilla, viestin salauksen purkaminen ja lopeta. Toiminto valitaan syöttämällä käyttöliittymälle haluttua toimintoa vastaava numero. Kunkin toiminnon numero lukee sitä vastaavan toiminnnon edessä.

Viestiä salatessa ohjelmalle tulee syöttää salattava viesti ja se palauttaa tekstinä salatun viestin sekä salaamisen käytetyt, viestin purkamiseen vaaditut avaimet. Viestiksi sopii lyhyt merkkijono. 

Viestiä purettaessa ohjelmalle tulee syöttää salattu viesti sekä edellä mainitut avaimet viestin purkamista varten. Viestin täytyy olla salattu syötettyjä avaimia käyttäen sillä muuten salauksen purkaminen ei luonnollisesti toimi. Avaimet ovat suuria positiivisia kokonaislukuja. 

Lopeta toiminto lopettaa ohjelman suorittamisen.




Projektille on myös tehty valmiita testejä. Testit voi suorittaa käyttäen seuraavaa komentoa

```
poetry run invoke tests
```



Ja testikattavuusraportin saa luotua komennolla

```poetry run invoke coverage```
