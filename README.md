# FastAPI på NAIS

Dette prosjektet inneholder en oppskrift på hvordan man kan bruke FastAPI på
NAIS for å lage en Python applikasjon. Selve implementasjonen inneholder ikke
noe spennende, men det er alt rundt som kanskje kan fungere som inspirasjon.

> [!TIP]
> For å starte å utvikle i dette prosjektet kjør `uv sync --frozen`, det vil
> installere avhengigheter og gjøre alt klart

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
