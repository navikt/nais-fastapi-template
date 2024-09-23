# Fiks feil og formater kode med ruff
fix:
    uv run ruff check --fix .
    uv run ruff format .

# Sjekk at alt ser bra ut med pre-commit
lint:
    uv run pre-commit run --all-files --color always

# Server FastAPI applikasjonen lokalt
serve:
    uv run fastapi dev ./src/nais_fastapi_template/main.py --port 8080

# Kjør tester med PyTest
# test:
#    uv run pytest -rs tests/
