import httpx
import logging
from core.config import settings

logger = logging.getLogger(__name__)

async def get_cat_fact() -> str:
    """Fetch random cat fact from external API."""
    try:
        async with httpx.AsyncClient(timeout=settings.REQUEST_TIMEOUT) as client:
            response = await client.get(settings.CAT_FACT_URL)
            response.raise_for_status()
            data = response.json()
            return data.get("fact", "Cats are mysterious creatures.")
    except Exception as e:
        logger.error(f"Cat Fact API error: {e}")
        return "Cats are amazing, but the fact service is temporarily unavailable."
