"""
Tests for data processor utilities.
"""

import pytest
from decimal import Decimal
from lambda.data_processor.utils import (
    validate_event,
    transform_event,
    generate_event_id,
    normalize_timestamp,
    convert_floats,
    sanitize_string,
    calculate_ttl,
)


class TestValidateEvent:
    """Tests for event validation."""

    def test_valid_event(self):
        event = {
            "event_type": "user.signup",
            "payload": {"email": "test@example.com"},
            "timestamp": 1700000000,
        }
        assert validate_event(event) is True

    def test_missing_required_field(self):
        event = {
            "event_type": "user.signup",
            "payload": {},
        }
        assert validate_event(event) is False

    def test_invalid_event_type(self):
        event = {
            "event_type": "invalid.type",
            "payload": {},
            "timestamp": 1700000000,
        }
        assert validate_event(event) is False

    def test_non_dict_input(self):
        assert validate_event("not a dict") is False
        assert validate_event(None) is False
        assert validate_event([]) is False

    def test_payload_must_be_dict(self):
        event = {
            "event_type": "user.signup",
            "payload": "not a dict",
            "timestamp": 1700000000,
        }
        assert validate_event(event) is False


class TestTransformEvent:
    """Tests for event transformation."""

    def test_basic_transform(self):
        event = {
            "event_type": "order.created",
            "payload": {"amount": 99.99},
            "timestamp": 1700000000,
        }
        result = transform_event(event)

        assert result["event_type"] == "order.created"
        assert result["category"] == "order"
        assert result["action"] == "created"
        assert result["payload"]["amount"] == Decimal("99.99")

    def test_transform_with_user_id(self):
        event = {
            "event_type": "user.login",
            "payload": {},
            "timestamp": 1700000000,
            "user_id": 12345,
        }
        result = transform_event(event)
        assert result["user_id"] == "12345"

    def test_transform_with_metadata(self):
        event = {
            "event_type": "user.login",
            "payload": {},
            "timestamp": 1700000000,
            "metadata": {"ip": "192.168.1.1", "score": 0.95},
        }
        result = transform_event(event)
        assert result["metadata"]["score"] == Decimal("0.95")


class TestNormalizeTimestamp:
    """Tests for timestamp normalization."""

    def test_unix_epoch_int(self):
        assert normalize_timestamp(1700000000) == 1700000000

    def test_unix_epoch_float(self):
        assert normalize_timestamp(1700000000.123) == 1700000000

    def test_iso_format(self):
        result = normalize_timestamp("2023-11-14T22:13:20Z")
        assert isinstance(result, int)

    def test_invalid_timestamp(self):
        with pytest.raises(ValueError):
            normalize_timestamp("not a timestamp")


class TestConvertFloats:
    """Tests for float to Decimal conversion."""

    def test_simple_float(self):
        assert convert_floats(3.14) == Decimal("3.14")

    def test_nested_dict(self):
        result = convert_floats({"a": 1.5, "b": {"c": 2.5}})
        assert result["a"] == Decimal("1.5")
        assert result["b"]["c"] == Decimal("2.5")

    def test_list_with_floats(self):
        result = convert_floats([1.1, 2.2, 3.3])
        assert all(isinstance(x, Decimal) for x in result)

    def test_non_float_passthrough(self):
        assert convert_floats("hello") == "hello"
        assert convert_floats(42) == 42
        assert convert_floats(None) is None


class TestSanitizeString:
    """Tests for string sanitization."""

    def test_clean_string(self):
        assert sanitize_string("hello world") == "hello world"

    def test_removes_dangerous_chars(self):
        assert sanitize_string('<script>alert("xss")</script>') == "scriptalert(xss)/script"

    def test_strips_whitespace(self):
        assert sanitize_string("  hello  ") == "hello"


class TestCalculateTTL:
    """Tests for TTL calculation."""

    def test_default_90_days(self):
        ttl = calculate_ttl()
        import time
        expected_min = int(time.time()) + (89 * 86400)
        assert ttl > expected_min

    def test_custom_days(self):
        ttl_30 = calculate_ttl(30)
        ttl_90 = calculate_ttl(90)
        assert ttl_90 > ttl_30


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2


    def test_event_id_deterministic(self):
        event = {
            "event_type": "user.login",
            "payload": {"key": "value"},
            "timestamp": 1700000000,
        }
        result = transform_event(event)
        id1 = generate_event_id(result)
        id2 = generate_event_id(result)
        assert id1 == id2
