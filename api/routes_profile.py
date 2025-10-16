from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.responses import JSONResponse
from models.profile_model import ProfileResponse, UserProfile
from services.cat_fact_service import get_cat_fact
from core.config import settings
from core.utils import get_utc_timestamp
from fastapi_limiter.depends import RateLimiter




router = APIRouter()

@router.get("/me", response_model=ProfileResponse, response_class=JSONResponse,dependencies=[Depends(RateLimiter(times=5, seconds=60))])
async def get_profile():
    """Return profile info along with a dynamic cat fact."""
    cat_fact = await get_cat_fact()

    profile = ProfileResponse(
        status="success",
        user=UserProfile(
            email=settings.EMAIL,
            name=settings.FULL_NAME,
            stack=settings.STACK,
        ),
        timestamp=get_utc_timestamp(),
        fact=cat_fact,
    )
    return JSONResponse(content=profile.model_dump(), media_type="application/json")
