"""Implementasjon av kubernetes prober for liveness og readiness."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/is_alive")
def alive() -> None:
    """Kubernetesspesifikk test som skal informere clustere vite om tjenesten
    har gått i stå og trenger å restarte."""
    pass


@router.get("/is_ready")
def ready() -> None:
    """Kubernetesspesifikk test som skal informere clustere om tjenesten er klar til å motta trafikk/forespørsler.

    Brukes f.eks. for automatisk skalering av tjenesten i k8s, hvis så konfigurert
    """
    # Fordi dette prosjektet ikke inneholder noe logikk av noe slag så har vi
    # heller ikke noe fornuftig å plassere i denne metoden, men her ville det
    # vært naturlig å sjekke at databaser svarer som de skal eller andre ting
    # som applikasjonen må ha tilgang til for at ting skal fungere som forventet
    pass
