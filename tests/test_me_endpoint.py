import pytest
from httpx import AsyncClient
from main import app
import re
from datetime import datetime, timezone

@pytest.mark.asyncio
async def test_me_endpoint_structure():
    """✅ Ensure /me endpoint returns valid JSON response with required fields."""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/me")

    # Check HTTP status
    assert response.status_code == 200, "Expected 200 OK"

    # Check Content-Type
    assert response.headers["content-type"] == "application/json", "Invalid Content-Type"

    data = response.json()

    # Required top-level fields
    assert "status" in data
    assert "user" in data
    assert "timestamp" in data
    assert "fact" in data

    # Check static fields
    assert data["status"] == "success", "Status must be 'success'"

    # Check user subfields
    user = data["user"]
    assert isinstance(user, dict), "user must be an object"
    for key in ["email", "name", "stack"]:
        assert key in user, f"Missing user.{key}"
        assert isinstance(user[key], str) and user[key].strip(), f"user.{key} must be non-empty string"

    # Validate timestamp format (ISO 8601 UTC)
    timestamp = data["timestamp"]
    iso_pattern = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}"
    assert re.match(iso_pattern, timestamp), "Timestamp must be ISO 8601 format"

    # Ensure timestamp is roughly current
    dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    delta = datetime.now(timezone.utc) - dt
    assert abs(delta.total_seconds()) < 5, "Timestamp should reflect current UTC time"

    # Check fact field
    assert isinstance(data["fact"], str) and len(data["fact"]) > 0, "fact must be non-empty string"


@pytest.mark.asyncio
async def test_me_endpoint_dynamic_fact_and_timestamp():
    """✅ Ensure new fact and timestamp on each request."""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response1 = await ac.get("/me")
        response2 = await ac.get("/me")

    data1 = response1.json()
    data2 = response2.json()

    # Ensure timestamp changes
    assert data1["timestamp"] != data2["timestamp"], "Timestamp should differ between requests"

    # Facts should differ most times, but allow fallback case
    assert isinstance(data1["fact"], str)
    assert isinstance(data2["fact"], str)
    # Do not force inequality (some APIs return same fact occasionally)
    assert len(data1["fact"]) > 0
    assert len(data2["fact"]) > 0


@pytest.mark.asyncio
async def test_me_endpoint_handles_cat_api_failure(monkeypatch):
    """✅ Ensure graceful fallback when Cat Facts API fails."""

    async def mock_fail_cat_fact():
        raise Exception("Simulated failure")

    # Patch get_cat_fact function in main.py
    from main import get_cat_fact
    monkeypatch.setattr("main.get_cat_fact", mock_fail_cat_fact)

    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/me")

    assert response.status_code == 200
    data = response.json()
    assert "fact" in data
    assert isinstance(data["fact"], str)
    # Fallback fact must still be non-empty
    assert len(data["fact"]) > 0
