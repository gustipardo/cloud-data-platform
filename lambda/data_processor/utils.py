"""
Utility functions for data processing pipeline.

Provides validation, transformation, and helper functions
for the event processing Lambda.
"""

import hashlib
import re
from datetime import datetime, timezone
from decimal import Decimal
from typing import Optional


REQUIRED_FIELDS = ["event_type", "payload", "timestamp"]

VALID_EVENT_TYPES = [
    "user.signup",
    "user.login",
    "user.logout",
    "order.created",
    "order.updated",
    "order.completed",
    "order.cancelled",
    "payment.processed",
    "payment.failed",
    "notification.sent",
    "notification.clicked",
    "session.start",
    "session.end",
    "error.reported",
]


def validate_event(event: dict) -> bool:
    """
    Validate that an event has all required fields and valid types.

    Args:
        event: Raw event dictionary

    Returns:
        True if event is valid, False otherwise
    """
    if not isinstance(event, dict):
        return False

    for field in REQUIRED_FIELDS:
        if field not in event:
            return False

    if event.get("event_type") not in VALID_EVENT_TYPES:
        return False

    if not isinstance(event.get("payload"), dict):
        return False

    return True


def transform_event(event: dict) -> dict:
    """
    Transform raw event data into the canonical format for storage.

    Handles type conversions (floats to Decimals for DynamoDB),
    timestamp normalization, and data enrichment.

    Args:
        event: Validated raw event dictionary

    Returns:
        Transformed event ready for DynamoDB storage
    """
    transformed = {
        "event_type": event["event_type"],
        "timestamp": normalize_timestamp(event["timestamp"]),
        "payload": convert_floats(event["payload"]),
    }

    if "user_id" in event:
        transformed["user_id"] = str(event["user_id"])

    if "metadata" in event and isinstance(event["metadata"], dict):
        transformed["metadata"] = convert_floats(event["metadata"])

    category, action = event["event_type"].split(".", 1)
    transformed["category"] = category
    transformed["action"] = action

    return transformed


def generate_event_id(event: dict) -> str:
    """
    Generate a deterministic event ID based on event content.
    Uses SHA-256 hash of key fields to ensure idempotency.
    """
    key_string = f"{event['event_type']}:{event['timestamp']}:{str(event.get('payload', {}))}"
    return hashlib.sha256(key_string.encode()).hexdigest()[:16]


def normalize_timestamp(ts) -> int:
    """
    Normalize various timestamp formats to Unix epoch (integer).

    Supports:
        - Unix epoch (int/float)
        - ISO 8601 strings
        - Common datetime formats
    """
    if isinstance(ts, (int, float)):
        return int(ts)

    if isinstance(ts, str):
        for fmt in [
            "%Y-%m-%dT%H:%M:%S.%fZ",
            "%Y-%m-%dT%H:%M:%SZ",
            "%Y-%m-%dT%H:%M:%S%z",
            "%Y-%m-%d %H:%M:%S",
        ]:
            try:
                dt = datetime.strptime(ts, fmt)
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                return int(dt.timestamp())
            except ValueError:
                continue

    raise ValueError(f"Unable to parse timestamp: {ts}")


def convert_floats(obj):
    """
    Recursively convert float values to Decimal for DynamoDB compatibility.
    DynamoDB does not support Python float type.
    """
    if isinstance(obj, float):
        return Decimal(str(obj))
    elif isinstance(obj, dict):
        return {k: convert_floats(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_floats(i) for i in obj]
    return obj


def sanitize_string(value: str) -> str:
    """Remove potentially dangerous characters from string values."""
    return re.sub(r'[<>"\';]', '', value).strip()


def calculate_ttl(days: int = 90) -> int:
    """Calculate TTL timestamp for DynamoDB item expiration."""
    now = datetime.now(timezone.utc)
    ttl = now.timestamp() + (days * 86400)
    return int(ttl)


def format_event_summary(event: dict) -> str:
    """Format event for logging output."""
    etype = event.get('event_type', 'unknown')
    eid = event.get('event_id', 'no-id')
    return f"[{etype}] {eid}"


def format_event_summary(event: dict) -> str:
    """Format event for logging output."""
    etype = event.get('event_type', 'unknown')
    eid = event.get('event_id', 'no-id')
    return f"[{etype}] {eid}"


def format_event_summary(event: dict) -> str:
    """Format event for logging output."""
    etype = event.get('event_type', 'unknown')
    eid = event.get('event_id', 'no-id')
    return f"[{etype}] {eid}"


def format_event_summary(event: dict) -> str:
    """Format event for logging output."""
    etype = event.get('event_type', 'unknown')
    eid = event.get('event_id', 'no-id')
    return f"[{etype}] {eid}"


def format_event_summary(event: dict) -> str:
    """Format event for logging output."""
    etype = event.get('event_type', 'unknown')
    eid = event.get('event_id', 'no-id')
    return f"[{etype}] {eid}"


def format_event_summary(event: dict) -> str:
    """Format event for logging output."""
    etype = event.get('event_type', 'unknown')
    eid = event.get('event_id', 'no-id')
    return f"[{etype}] {eid}"


def format_event_summary(event: dict) -> str:
    """Format event for logging output."""
    etype = event.get('event_type', 'unknown')
    eid = event.get('event_id', 'no-id')
    return f"[{etype}] {eid}"


def format_event_summary(event: dict) -> str:
    """Format event for logging output."""
    etype = event.get('event_type', 'unknown')
    eid = event.get('event_id', 'no-id')
    return f"[{etype}] {eid}"


def format_event_summary(event: dict) -> str:
    """Format event for logging output."""
    etype = event.get('event_type', 'unknown')
    eid = event.get('event_id', 'no-id')
    return f"[{etype}] {eid}"


def format_event_summary(event: dict) -> str:
    """Format event for logging output."""
    etype = event.get('event_type', 'unknown')
    eid = event.get('event_id', 'no-id')
    return f"[{etype}] {eid}"


def format_event_summary(event: dict) -> str:
    """Format event for logging output."""
    etype = event.get('event_type', 'unknown')
    eid = event.get('event_id', 'no-id')
    return f"[{etype}] {eid}"


def format_event_summary(event: dict) -> str:
    """Format event for logging output."""
    etype = event.get('event_type', 'unknown')
    eid = event.get('event_id', 'no-id')
    return f"[{etype}] {eid}"


def format_event_summary(event: dict) -> str:
    """Format event for logging output."""
    etype = event.get('event_type', 'unknown')
    eid = event.get('event_id', 'no-id')
    return f"[{etype}] {eid}"


def format_event_summary(event: dict) -> str:
    """Format event for logging output."""
    etype = event.get('event_type', 'unknown')
    eid = event.get('event_id', 'no-id')
    return f"[{etype}] {eid}"
