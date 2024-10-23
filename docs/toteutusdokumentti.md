# Projektin toteutus

## Ohjelman yleinen rakenne
index.py käynnistää käyttöliittymän (ui.py) joka toteuttaa salauksen sekä salauksen purkamisen käyttäeen apuna Encryption, Decryption ja EncryptionKeys luokkia. Encryption luokka puolestaan hyödyntää Primes luokkaa alkulukujen generoimiseen. Primes luokka siis generoi suurta toisistaan eriävää alkulukua (q ja p). Encryption luokan avulla käyttäjän syöte esitetään kokonaislukuna joka saadaan salattua luokan encryption funktion avulla. Tätä salausta varten tarvittavat avaimet e ja d laskee EncryptionKeys-luokka. Decryption luokka vastaa nimensä mukaisesti viestin purkamisesta. Siitä löytyy funktio numeerisessa muodossa olevan viestin muuttamiseksi takaisin merkkijonoksi sekä decryption funktio varsinaista salauksen purkamista varten sille annetuilla avaimilla.


## Aikavaativuus
Erityisesti aikavaativuus aiheuttaa ongelmia suurten alkulukujen generoimisen kohdalla sillä suurten parittomien lukujen testaaminen alkuluvuiksi on hidasta. Jos tarkasteltava luku ei ole alkuluku tulee valita uusi satunnaisluku ja testataa uudelleen onko kyseessä alkuluku niin kauan kunnes löydetään kaksi suurta toisistaan eriävää alkulukua.

Reseachgatesta löytämäni julkaisun mukaan RSA-algoritmin aikavaativuus on O((log_{2}x))^{3}. Miller-Rabin alkulukutestin aikavaativuudeksi sanotaan yleisesti Wikipediassa O(k log^{3} n). Geeks for geeksistä löytyvän algoritmin aikavaativuudeksi on merkattu O(k log n) ja tilavaativuus on O(1). Jottei ohjelman tarvitsisi käyttää hidasta Miller-Rabin alkulukutestiä jokaisen luvun kohdalla, lasketaan lista pienempiä alkulukuja käyttäen Erastothenen seulaa. Wikiperian mukaan kyseisen algoritmin aikavaativuus on O(n log log n) eli algoritmi on huomattavasti Miller-Rabin algoritmia nopeampi. Ohjelman viestin salauksen ja salauksen purkamisen yhteydessä käyttämä pow-funktio on aikavaativuudeltaan O(log n).

## Parannuksia
Ohjelmassa voisi olla vaihtoehtona että käyttäjä voisi syöttää ohjelmalle itse avaimet joita käyttäen hän haluaa salata viestin. Tällöin myös eksponentti e voisi olla satunnaisluku ja ohjelma tarkastaisi sopivatko avaimet viestin salaamiseen.

RSA-salaukseen kuuluisi myös padding sillä salaus ei ole ilman sitä turvallinen. Lisäksi random kirjastoa ei tulisi käyttää salausohjelmissa. Ohjelmaa voisi siis parantaa toteuttamalla paddingin jolloin viestiin lisättäisiin satunnaista dataa salauksen murtamisen hankaloittamiseksi.

Käyttöliittymä voisi olla helpompi käyttää avainten kopioinnin osalta ja aikavaativuutta voisi varmasti vielä parantaa

## Laajojen kielimallien käyttö
Projektissa on käytetty muutamaan otteeseen OpenAi:n ChatGPT kielimallia. Kielimallia ei ole käytetty ohjelman rakenteen ideointiin tai koodin, testien tai dokumentaation tuottamiseen vaan käyttö on rajoittunut googlettamisen kaltaisiin kyselyihin bugien ratkaisemiseksi. 


## Viitteet
- [Wikipedia: RSA](https://fi.wikipedia.org/wiki/RSA)

- [Geeks for Geeks: Miller-Rabin alkulukutesti](https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/)

- [Naukri: pow](https://www.naukri.com/code360/library/math-pow)

- [Researchgate: RSA aikavaativuudesta](https://www.researchgate.net/figure/The-time-complexity-of-RSA-and-ECC_fig4_330832141#:~:text=5%2C%20the%20time%20complexity%20of,decryption%20is%20slower%20%5B15%5D.)

- [Wikipedia: Miller-Rabin alkulukutesti](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#:~:text=return%20%E2%80%9Cprobably%20prime%E2%80%9D-,Complexity,efficient%2C%20polynomial%2Dtime%20algorithm.)

- [Wikipedia: Erastothenen seula](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
