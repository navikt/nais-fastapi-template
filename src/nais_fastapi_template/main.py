"""Hovedinngangen for FastAPI applikasjonen"""

import importlib.metadata
from typing import Any

from fastapi import FastAPI, Security
from fastapi.responses import RedirectResponse

from .nais.auth import VerifyOauth2Token
from .nais.probes import router as nais_router

TOKEN_VERIFICATION = VerifyOauth2Token()
"""Instans for å verifisere OAuth2 token på NAIS"""

app = FastAPI(
    title="NAIS FastAPI template",
    summary="Eksempel på hvordan å sette opp en FastAPI applikasjon på NAIS med autentisering",
    version=importlib.metadata.version("nais_fastapi_template"),
)
# Legg til router for NAIS/Kubernetes endepunkter
app.include_router(nais_router, tags=["nais"])


@app.get("/")
async def redirect_main() -> RedirectResponse:
    """Redirect brukere til dokumentasjonen."""
    # Hvis prosjektet bare eksponerer et HTTP/REST grensesnitt så kan det være
    # behjelpelig å omdirigere bruker fra `/` til `/docs` gjennom
    # innloggingsportalen
    return RedirectResponse("/oauth2/login?redirect=/docs")


@app.get("/api/v1/test_verification", tags=["api"])
async def test_verification(
    token: dict[str, Any] = Security(TOKEN_VERIFICATION.verify),
) -> dict[str, Any]:
    """Endepunkt som verifiserer at bruker er logget inn."""
    # MERK: Selv om det ser ut til at denne funksjonen ikke gjør noe så vil
    # bruker bli verifisert gjennom `Security` avhengigheten til denne metoden.
    return token
