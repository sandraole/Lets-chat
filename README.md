# Lets-chat

## Let's Chat - Keskustelusovellus

Kaipaatko jutteluseuraa tai kaveria? Let's Chat mahdollistaa tämän kaiken sinulle!
Voit tehdä helposti oman käyttäjätunnuksen ja kirjautua sisään aina, kun siltä tuntuu.
Kun olet kirjautuneena sisälle, näet listan eri aiheita ja voit liittyä mieleiseesi keskusteluun.
Näet muiden kirjoittamat viestit kellontarkkaan, kun ne on lähetetty eli et jää mistään mielenkiintoisesta paitsi!
Voit myös halutessasi tehdä omalla huomiota herättävällä otsikolla keskustelun, mutta mikäli se ei miellytä
pystyt muokkaamaan luomaasi keskustelun otsikkoa tai lähetettyä sisältöä. Mikäli koko keskustelu tuntuu
typerältä, voit poistaa sen kokonaan. Jos et jaksa selata kaikkia keskusteluja läpi, pystyt
etsimään kaikki viestit valitsemalla avainsanalla. Lopuksi, kun olet valmis voit kirjautua ulos ja palata keskustelemaan
taas, kun kaipaat juttelukaveria.

Kaikkea tätä valvovat ahkerat ylläpitäjät. Kannattaa käyttäytyä kunnolla, sillä he voivat lisätä tai poistaa
keskusteluita. Tarvittaessa ylläpitäjä voi antaa harvoille ja valituille käyttäjille pääsyn salaiselle alueelle.


### Sovelluksen tulevia ominaisuuksia:

    * Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
    * Käyttäjä näkee sovelluksen etusivulla listan alueista sekä jokaisen alueen ketjujen ja viestien määrän ja viimeksi lähetetyn viestin ajankohdan.
    * Käyttäjä voi luoda alueelle uuden ketjun antamalla ketjun otsikon ja aloitusviestin sisällön.
    * Käyttäjä voi kirjoittaa uuden viestin olemassa olevaan ketjuun.
    * Käyttäjä voi muokata luomansa ketjun otsikkoa sekä lähettämänsä viestin sisältöä. Käyttäjä voi myös poistaa ketjun tai viestin.
    * Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana.
    * Ylläpitäjä voi lisätä ja poistaa keskustelualueita.

### Tämän hetken tilanne (05.05.2024):
    * Sivustolla kävijä näkee kuinka mones vierailija hän on.
    * Käyttäjä voi kirjautua sisään ja ulos, sekä luoda uuden tunnuksen.
    * Kirjautuessaan käyttäjä pääsee omaan profiiliin, josta hän pääsee lukemaan keskustelupalstan säännöt.
    * Käyttäjä pystyy tekemään keskustelun.
    * Käyttäjän profiilissa näkyvät lähetetyt viestit ja niistä pystyy hakusanalla etsimään haluttuja keskusteluja.
    * Käyttäjä pystyy tykkäämään keskustelusta. (Toiminnallisuudet valmiit, mutta tykkäys määritelty väärin profile.html:ssä ja sen vuoksi se ei näytä määrää.)
    * Sovelluksen ulkoasu on täysin valmis.
    * Tällä hetkellä 4 taulua.
    * Sovellus jäi kesken ja sen vuoksi moni toiminnallisuuksista puuttuu.


### Sovelluksen taulut:
    1. Users
    2. Visitors
    3. Messages


## Sovelluksen asentamisen ohjeet paikallisesti:

1. Kloonaa repositorio "Let's Chat" koneellesi:
   ```
   git clone https://github.com/taisteluvalmis/Lets-chat.git
   ```

2. Siirry oikeaan kansioon, josta sovellus löytyy:
   ```
   cd Lets-chat
   ```

3. Luo .env tiedosto kyseiseen kansioon ja lisää siihen seuraavat tiedot:
   ```
   DATABASE_URL=<database-local-address> (postgresql:///user)
   SECRET_KEY=<your_secret_key>
   ```

4. Käynnistä virtuaaliympäristö ja aja seuraavat käskyt:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

5. Asenna Flask:
   ```
   pip install flask
   ```

6. Asenna riippuvuudet:
   ```
   pip install -r ./requirements.txt
   ```

7. Avaa taustalle toinen terminaali ja aja käsky:
   ```
   start-pg.sh
   ```

8. Luo tietokanta psql:ssä:
   ```
   psql < schema.sql
   ```

9. Käynnistä sovellus:
   ```
   flask run
   ```