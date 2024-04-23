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


### Sovelluksen ominaisuuksia:

    * Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
    * Käyttäjä näkee sovelluksen etusivulla listan alueista sekä jokaisen alueen ketjujen ja viestien määrän ja viimeksi lähetetyn viestin ajankohdan.
    * Käyttäjä voi luoda alueelle uuden ketjun antamalla ketjun otsikon ja aloitusviestin sisällön.
    * Käyttäjä voi kirjoittaa uuden viestin olemassa olevaan ketjuun.
    * Käyttäjä voi muokata luomansa ketjun otsikkoa sekä lähettämänsä viestin sisältöä. Käyttäjä voi myös poistaa ketjun tai viestin.
    * Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana.
    * Ylläpitäjä voi lisätä ja poistaa keskustelualueita.
    * Ylläpitäjä voi luoda salaisen alueen ja määrittää, keillä käyttäjillä on pääsy alueelle.


### Tämän hetken tilanne (23.04.2024):
    * Käyttäjä voi tehdä käyttäjätunnuksen ja kirjautua sisään.
    * Sivustolla kävijä näkee kuinka mones vierailija hän on.
    * Sovelluksen html tiedostot ja ulkoasu ovat käytännössä valmiit. Puuttuu vain muutama html.
    * Sovelluksen toiminnallisuudet on vielä vaiheessa. Seuraavaksi aloitan keskutelupalstan tekemisen.
 

### Sovelluksen taulut:
    1. Users
    2. Visitors


## Sovelluksen asentamisen ohjeet paikallisesti:

1. Tallenna tästä sovelluksesta löytyvät tiedostot samaan kansioon. (**Huomaa** tiedoston requirement.txt vaadittavat paketit ja lataa ne)

2. Luo .env tiedosto kyseiseen kansioon ja lisää siihen seuraavat tiedot:
   ```
   DATABASE_URL=<database-local-address> (postgresql:///user)
   SECRET_KEY=<your_secret_key>
   ```

3. Avaa terminaali, aktivoi virtuaaliympäristö ja aja seuraavat käskyt:
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install -r ./requirements.txt
   ```

4. Luo tietokanta psql:ssä:
   ```
   psql < schema.sql
   ```

6. Käynnistä sovellus:
   ```
   flask run
   ```
