"""Reproduction test suite for auth token validation."""
import pytest
from auth_service.token_validator import validate_jwt_claims, InvalidClaimsError

def test_valid_token_with_metadata():
    payload = {"sub": "user_123", "exp": 2000000000, "metadata": {"client_id": "custom_app"}}
    res = validate_jwt_claims(payload)
    assert res["sub"] == "user_123"
    assert res["client_id"] == "custom_app"
    assert res["is_valid"] is True

def test_missing_optional_metadata():
    """Reproducible defect: Metadata is optional, but omitting it raises KeyError."""
    payload = {"sub": "user_456", "exp": 2000000000}
    res = validate_jwt_claims(payload)
    assert res["sub"] == "user_456"
    assert res["client_id"] == "default_client"
    assert res["is_valid"] is True
