"""Reproduction test suite for telemetry formatter."""
import re
from datetime import datetime, timezone
import pytest
from telemetry_service.formatter import format_telemetry_event

def test_iso8601_strict_formatting():
    """Reproducible defect: Formatted timestamp must adhere to ISO-8601 standard."""
    dt = datetime(2026, 11, 25, 12, 30, 45, 123456, tzinfo=timezone.utc)
    res = format_telemetry_event("user_login", dt, {"user_id": "usr_99"})
    
    assert res["event"] == "user_login"
    ts = res["timestamp"]
    # ISO-8601 pattern: YYYY-MM-DDTHH:MM:SS(.microseconds)?(Z|+00:00)
    iso_pattern = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?(Z|\+00:00)$"
    assert re.match(iso_pattern, ts), f"Timestamp '{ts}' does not match strict ISO-8601 format"
