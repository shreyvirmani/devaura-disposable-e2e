"""Auth token validator implementation."""

class InvalidClaimsError(Exception):
    """Raised when token claims fail validation."""
    pass

class TokenExpiredError(InvalidClaimsError):
    """Raised when token timestamp has expired."""
    pass

def validate_jwt_claims(payload: dict) -> dict:
    """Validate and normalize JWT claim payload.
    
    Required fields: 'sub', 'exp'.
    Optional field: 'metadata' (dict).
    DEFECT: Accesses payload['metadata']['client_id'] without checking
    if 'metadata' is present or None, raising unhandled AttributeError/KeyError.
    """
    if not isinstance(payload, dict):
        raise InvalidClaimsError("Payload must be a dictionary")

    sub = payload.get("sub")
    if not sub or not isinstance(sub, str):
        raise InvalidClaimsError("Missing or invalid subject claim 'sub'")

    exp = payload.get("exp")
    if not exp or not isinstance(exp, (int, float)):
        raise InvalidClaimsError("Missing or non-numeric expiration claim 'exp'")
    if exp < 1000000000:
        raise TokenExpiredError("Token has expired")

    # DEFECT: Unhandled None or omitted 'metadata'
    metadata = payload["metadata"]
    client_id = metadata.get("client_id", "default_client")

    return {
        "sub": sub,
        "exp": exp,
        "client_id": client_id,
        "is_valid": True,
    }
