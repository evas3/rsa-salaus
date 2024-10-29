# Projektin toteutus

## Ohjelman yleinen rakenne
index.py käynnistää käyttöliittymän (ui.py) joka toteuttaa salauksen sekä salauksen purkamisen käyttäeen apuna Encryption, Decryption ja EncryptionKeys luokkia. Encryption luokka puolestaan hyödyntää Primes luokkaa alkulukujen generoimiseen. Primes luokka siis generoi suurta toisistaan eriävää alkulukua (q ja p). Encryption luokan avulla käyttäjän syöte esitetään kokonaislukuna joka saadaan salattua luokan encryption funktion avulla. Tätä salausta varten tarvittavat avaimet e ja d laskee EncryptionKeys-luokka. Decryption luokka vastaa nimensä mukaisesti viestin purkamisesta. Siitä löytyy funktio numeerisessa muodossa olevan viestin muuttamiseksi takaisin merkkijonoksi sekä decryption funktio varsinaista salauksen purkamista varten sille annetuilla avaimilla. 

Alkulukujen yhteydessä käytetään Miller-Rabin alkulukutestiä. Kyseinen algoritmi testaa onko sille annettu luku suurella todennäköisyydellä alkuluku. Koska Miller-Rabin testi on hidas, käytetään myös Erastothenen seulaa pienempien alkulukujen etsimiseen. Yksityinen avain d lasketaan alkuperäisen Eulerin φ-funktion sijasta laskemalla λ(n). Tässä käytetään Eukleideen algoritmia. RSA-salausta on avattu lyhyesti [määrittelydokumentissa](https://github.com/evas3/rsa-salaus/blob/main/docs/maarittelydokumentti.md) ja syvemmin siihen tai käytettäviin algoritmeihin voi tutustua esimerkiksi alla olevista lähteistä.


## Aikavaativuus
Erityisesti aikavaativuus aiheuttaa ongelmia suurten alkulukujen generoimisen kohdalla sillä suurten parittomien lukujen testaaminen alkuluvuiksi on hidasta. Jos tarkasteltava luku ei ole alkuluku tulee valita uusi satunnaisluku ja testataa uudelleen onko kyseessä alkuluku niin kauan kunnes löydetään kaksi suurta toisistaan eriävää alkulukua.

Reseachgatesta löytämäni julkaisun mukaan RSA-algoritmin aikavaativuus on O((log_{2}x))^{3}. Miller-Rabin alkulukutestin aikavaativuudeksi sanotaan yleisesti Wikipediassa O(k log^{3} n). Jottei ohjelman tarvitsisi käyttää hidasta Miller-Rabin alkulukutestiä jokaisen testattavan luvun kohdalla, lasketaan lista pienempiä alkulukuja käyttäen Erastothenen seulaa. Wikiperian mukaan kyseisen algoritmin aikavaativuus on O(n log log n) eli algoritmi on huomattavasti Miller-Rabin algoritmia nopeampi. Lisäksi heti alkuun karsitaan kaikki parilliset luvut. Ohjelman viestin salauksen ja salauksen purkamisen yhteydessä käyttämä pow-funktio on aikavaativuudeltaan O(log n). Eukleideen algoritmin aikavaativuus on O(n) luokkaa. 

## Parannuksia
Ohjelmassa voisi olla vaihtoehtona että käyttäjä voisi syöttää ohjelmalle itse avaimet joita käyttäen hän haluaa salata viestin. Tällöin myös eksponentti e voisi olla satunnaisluku ja ohjelma tarkastaisi sopivatko avaimet viestin salaamiseen.

RSA-salaukseen kuuluisi myös padding sillä salaus ei ole ilman sitä turvallinen. Lisäksi random kirjastoa ei tulisi käyttää salausohjelmissa. Ohjelmaa voisi siis parantaa toteuttamalla paddingin jolloin viestiin lisättäisiin satunnaista dataa salauksen murtamisen hankaloittamiseksi.

Käyttöliittymä voisi olla helpompi käyttää avainten kopioinnin osalta ja aikavaativuutta voisi varmasti vielä parantaa

## Laajojen kielimallien käyttö
Projektissa on käytetty muutamaan otteeseen OpenAi:n ChatGPT kielimallia. Kielimallia ei ole käytetty ohjelman rakenteen tai algoritmien ideointiin. Sitä ei ole myöskään hyödynnetty koodin, testien tai dokumentaation tuottamisessa vaan käyttö on rajoittunut googlettamisen kaltaisiin kyselyihin bugien ratkaisemiseksi. 


## Viitteet
- [Wikipedia: RSA](https://fi.wikipedia.org/wiki/RSA)

- [Naukri: pow](https://www.naukri.com/code360/library/math-pow)

- [Researchgate: RSA aikavaativuudesta](https://www.researchgate.net/figure/The-time-complexity-of-RSA-and-ECC_fig4_330832141#:~:text=5%2C%20the%20time%20complexity%20of,decryption%20is%20slower%20%5B15%5D.)

- [Wikipedia: Miller-Rabin alkulukutesti](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#:~:text=return%20%E2%80%9Cprobably%20prime%E2%80%9D-,Complexity,efficient%2C%20polynomial%2Dtime%20algorithm.)

- [Wikipedia: Erastothenen seula](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

- [Wikipedia: Eukleiden algoritmi](https://en.wikipedia.org/wiki/Euclidean_algorithm)

- [Geeks for geeks: Eukleiden algoritmin aikavaativuudesta](https://www.geeksforgeeks.org/time-complexity-of-euclidean-algorithm/)
