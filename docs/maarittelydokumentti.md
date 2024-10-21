# Määrittelydokumentti
Opinto-ohjelma johon kuulun on tietojenkäsittelytieteen kandidaatti. 

Dokumentaatiossa on käytetty suomea.

Projektissa käytän ohjelmointikielenä Pythonia. Myös vertaisarviointeja varten toivoisin projektia jossa on käytetty ohjelmointikielenä Pythonia.

## Projektista

Projektissa toteutan ohjelman joka kykenee salaamaan käyttäjän antamia viestejä RSA-salausta käyttäen sekä purkamaan salauksen jos ohjelmalle annetaan RSA:ta käyttäen salattu viesti sekä kyseisen viestin salaamiseen käytetyt avaimet.

## RSA-salaus
RSA salauksessa viestin salaamisessa ja purkamisessa käytetään kahta eri avainta. Toinen avaimista on julkinen avain viestin salaamista varten. Tämä avain on nimensä mukaisesti julkinen eikä sitä tarvitse pitää salassa. Toinen salauksen purkamiseen vaadittava avain on pidettävä ulkopuolisilta salassa ja sitä kutsutaankin yksityiseksi tai salaiseksi avaimeksi. 

Julkinen avain muodostuu kahdesta osasta (projektissa e ja n). Osa n on kahden suuren toisistaan eriävän alkuluvun (projektissa p ja q) tulo eli n=p\*q. Eksponenttiosa e on satunnainen, ykköstä suurempi kokonaisluku joka on kuitenkin pienempi kuin (p-1)\*(q-1). Tyypillisesti tässä käytetään lukua 65 537 joten sitä on käytetty myös tässä projektissa.

Yksityinen avain saadaan edellä mainitusta n osasta sekä yksityisestä eksponenttikertoimesta (projektissa d). Osa d lasketaan laajennetun Eukleideen algoritmin avulla.

Varsinainen viestin salaus noudattaa yksinkertaista kaavaa. Viestiä salatessa siis salattu viesti saadaan laskemalla (Viesti)^{e} mod n. Alkuperäinen viesti saadaan laskemalla (Salattu viesti){d} mod n.
	
## Projektin algoritmit ja tietorakenteet

Projekti edellyttää vähintään Python versiota 3.10. Projekti vaatii suurten alkulukujen generoimista ja tässä apuna on käytetty Miller-Rabin algoritmia

## Lähteet

- [Geeks for geeks: Miller-Rabin algoritmi](https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/)
- [Nordvpn: RSA-salaus](https://nordvpn.com/fi/blog/rsa-kryptografiaan/?srsltid=AfmBOoq3sBepL1Bt-WEpLxLvOlyZU2wl7qBCpCthOW7znRup1dARmhXZ)

