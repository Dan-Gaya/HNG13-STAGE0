import sys
import os
import pytest
import redis.asyncio as redis
from httpx import AsyncClient, ASGITransport
from fastapi_limiter import FastAPILimiter

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app


@pytest.mark.asyncio
async def test_root_endpoint():
    #Test the root (/) endpoint which has rate limiting enabled.
    # Ensures Redis and FastAPILimiter are initialized before the request.
    
    # Connect to Redis and initialize FastAPILimiter manually
    redis_client = await redis.from_url("redis://localhost:6379", encoding="utf8", decode_responses=True)
    await FastAPILimiter.init(redis_client)

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/")
    
    assert response.status_code == 200
    assert response.json()["message"] == "Welcome to the Profile API"


@pytest.mark.asyncio
async def test_me_endpoint():

    # Test the /me endpoint.
    
    #Ensure Redis connection exists before testing
    redis_client = await redis.from_url("redis://localhost:6379", encoding="utf8", decode_responses=True)
    await FastAPILimiter.init(redis_client)

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/me")

    assert response.status_code in (200, 401, 404)
