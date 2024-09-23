# FastAPI på NAIS

Dette prosjektet inneholder en oppskrift på hvordan man kan bruke FastAPI på
NAIS for å lage en Python applikasjon. Selve implementasjonen inneholder ikke
noe spennende, men det er alt rundt som kanskje kan fungere som inspirasjon.

> [!TIP]
> For å starte å utvikle i dette prosjektet kjør `uv sync --frozen`, det vil
> installere avhengigheter og gjøre alt klart

## NAIS oppsett

For å kunne lansere en applikasjon på NAIS må NAIS først vite hvordan vi ønsker
at denne applikasjonen fungerer. Dette spesifiseres i en, eller flere, YAML
filer i `.nais/` mappen.

For dette prosjektet har vi en minimal FastAPI applikasjon med autentisering på
NAIS, men vi anbefaler å se over [`app.yaml`](.nais/app.yaml) og lese
[dokumentasjonen til
NAIS](https://docs.nais.io/workloads/application/reference/application-spec/)
for å se hvordan variablene henger sammen.

## Verktøy

Dette prosjektet inneholder flere verktøy hvor ikke alle er like nødvendige.
Hvis du finner et verktøy som ikke er nevnt her betyr det at verktøyet er
valgfritt.

> [!NOTE]
> Når det er snakk om verktøy som Python har ansvar for har disse blitt
> installert av `uv` med `uv add <pakke_navn> --dev` slik at de blir med som
> utvikler avhengigheter og ikke blir installert f.eks. når vi bygger Docker
> bildet.

> [!TIP]
> For å lage `.gitignore` brukte vi
> [gitignore.io](https://www.toptal.com/developers/gitignore) og spesifiserte
> `Python`.

### Bygging med `uv`

Dette prosjektet bruker [`uv`](https://docs.astral.sh/uv/) for å bygge og
håndtere avhengigheter.

For å komme i gang:

```bash
uv sync --frozen
```

> [!NOTE]
> Dette prosjektet ble opprettet av `uv` som et bibliotek, dette er ikke strengt
> tatt nødvendig når man utvikler FastAPI med `uv` for NAIS, men er et valg vi
> har tatt for at koden skal være organisert under `src/`.

### Formatering og kodesjekk

For å passe på at koden ser ordentlig ut hvis det er flere utviklere som
samarbeider bruker vi i dette prosjektet [`ruff`](https://docs.astral.sh/ruff/).
`ruff` er konfigurert i [`ruff.toml`](./ruff.toml). `ruff` passer på at vi
skriver "riktig" Python kode og kan samtidig formatere koden slik at det ser
ganske likt ut.

Kjør `ruff` med:
```bash
# Hvis ruff bare skal rapportere feil
uv run ruff check .
uv run ruff format --diff .
# Eller hvis ruff får lov til å endre filer
uv run ruff check --fix .
uv run ruff format .
```

### `pre-commit` (Valgbar)

> [!TIP]
> `pre-commit` er et verktøy som kjører hver gang før vi legger til kode i
> `git`. Det kan derfor være et fint verktøy fordi det er vanskelig å glemme å
> kjøre, men samtidig kan det komme litt i veien. Vi har derfor markert dette
> som **Valgbar**.

`pre-commit` kan hjelp å sjekke at koden er riktig før vi legge til koden i
`git`. Det kan være et fint verktøy for å håndheve at verktøyene nevnt her
faktisk brukes. Vi har inkludert et eksempel med `ruff` og `mypy` som håndhever
kodestandard og sjekker at koden vår faktisk gjør det den skal. Her kan man
selvsagt fjerne verktøy i `pre-commit` hvis man ikke ønsker f.eks. `mypy`.

Se [`.pre-commit-config.yaml`](.pre-commit-config.yaml) for oppsett. Hvis det er
ønskelig å bruke `pre-commit` er det viktig at alle utviklere installerer
`pre-commit` for seg selv med:

```bash
uv run pre-commit install
```

Deretter kan man manuelt kjøre:

```bash
uv run pre-commit run --all-files
```

Eller la `git` håndtere dette.

### `justfile` (Valgbar)

Dette prosjektet inneholder en [`justfile`](https://just.systems/man/en/) som er
en moderne tolkning av `make`.  Denne filen inneholder nyttige kommandoer som
gjør det enklere å kjøre ofte brukte ting (spesielt når man ofte trenger `uv
run`).

Vi har inkludert noen enkle kommandoer, som `just fix` som kjører `ruff` og
`just lint` som kjører `pre-commit`.

Bruk `just --list` for å se alle oppskrifter og beskrivelser.

## Docker

For å kunne lansere applikasjonen på NAIS trenger vi å bygge et [Docker
bilde](https://docs.docker.com/get-started/). Man kan tenke på et Docker bildet
som en privat virtuell maskin som inneholder bare de pakkene vi trenger.

I dette prosjektet bygger vi applikasjonen i to steg. Først installerer vi
avhengigheter uten å installere selve prosjektet. Dette gjøres for å forbedre
tiden det tar å bygge Docker bilder, neste gang vi bygger Docker bildet vil
Docker huske at vi har installert avhengigheter og hvis ikke noe har forandret
seg så kopierer Docker det vi bygget før. Deretter installerer vi applikasjonen,
denne forandrer seg ofte så her hjelper det lite å huske hva som er gjort før.

Det neste steget i bygging av Docker bildet er å starte et nytt bygg fra et
`distroless` bilde. Vi bruker `distroless` for å minimere antall eksterne
avhengigheter som er installert i Docker og dette burde gi færre sårbarheter. Vi
kopierer så inn det vi bygget i det første steget og har nå laget et nytt
minimalt Docker bilde.

> [!TIP]
> Filen `.dockerignore` inneholder en liste med alle filene og mappene som
> Docker skal overse når vi kopierer inn til Docker bildet. Denne filen gjør at
> vi enkelt kan si at vi vil kopiere alt i nåværende mappe uten å måtte
> spesifisere akkurat hvilke ting vi vil ha med.
