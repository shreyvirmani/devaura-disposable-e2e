"""Telemetry event formatter implementation."""
from datetime import datetime, timezone

def format_telemetry_event(event_name: str, timestamp: datetime, payload: dict) -> dict:
    """Format an event with strict ISO-8601 UTC timestamp and structured payload.
    
    DEFECT:
    Uses strftime('%Y-%m-%d %H:%M:%S') which strips timezone offset and microseconds,
    violating strict ISO-8601 formatting required by downstream log ingestion.
    """
    if not event_name:
        raise ValueError("Event name cannot be empty")
        
    # DEFECT: Non-compliant datetime formatting lacking ISO-8601 'T' and timezone indicator
    ts_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    
    return {
        "event": event_name,
        "timestamp": ts_str,
        "data": payload or {},
    }
