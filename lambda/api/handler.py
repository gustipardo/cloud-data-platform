"""
API Lambda Handler

REST API for querying processed event data from DynamoDB.
Exposed via API Gateway HTTP API.
"""

import json
import logging
import os
from datetime import datetime, timezone
from typing import Any

import boto3
from boto3.dynamodb.conditions import Key, Attr

logger = logging.getLogger()
logger.setLevel(os.environ.get("LOG_LEVEL", "INFO"))

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])


def lambda_handler(event: dict, context: Any) -> dict:
    """Route API Gateway requests to appropriate handlers."""
    method = event.get("requestContext", {}).get("http", {}).get("method", "GET")
    path = event.get("rawPath", "/")

    logger.info(f"{method} {path}")

    routes = {
        ("GET", "/events"): get_events,
        ("GET", "/events/stats"): get_event_stats,
        ("GET", "/health"): health_check,
    }

    handler = routes.get((method, path))

    if handler is None:
        return response(404, {"error": "Not found"})

    try:
        return handler(event)
    except Exception as e:
        logger.error(f"Handler error: {e}")
        return response(500, {"error": "Internal server error"})


def get_events(event: dict) -> dict:
    """Query events by type with optional time range."""
    params = event.get("queryStringParameters") or {}

    event_type = params.get("type")
    limit = min(int(params.get("limit", 50)), 100)

    if event_type:
        result = table.query(
            IndexName="EventTypeIndex",
            KeyConditionExpression=Key("event_type").eq(event_type),
            ScanIndexForward=False,
            Limit=limit,
        )
    else:
        result = table.scan(Limit=limit)

    items = convert_decimals(result.get("Items", []))
    return response(200, {"events": items, "count": len(items)})


def get_event_stats(event: dict) -> dict:
    """Get aggregated event statistics."""
    result = table.scan(
        Select="COUNT",
    )

    return response(200, {
        "total_events": result["Count"],
        "scanned": result["ScannedCount"],
        "timestamp": datetime.now(timezone.utc).isoformat(),
    })


def health_check(event: dict) -> dict:
    """Health check endpoint."""
    return response(200, {
        "status": "healthy",
        "environment": os.environ.get("ENVIRONMENT", "unknown"),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    })


def response(status_code: int, body: dict) -> dict:
    """Build API Gateway response."""
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "X-Request-Time": datetime.now(timezone.utc).isoformat(),
        },
        "body": json.dumps(body, default=str),
    }


def convert_decimals(items: list) -> list:
    """Convert DynamoDB Decimal types back to int/float for JSON serialization."""
    from decimal import Decimal

    def convert(obj):
        if isinstance(obj, Decimal):
            return int(obj) if obj == int(obj) else float(obj)
        elif isinstance(obj, dict):
            return {k: convert(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert(i) for i in obj]
        return obj

    return [convert(item) for item in items]

# Pagination: use cursor-based pagination next iteration

# Pagination: use cursor-based pagination next iteration

# Pagination: use cursor-based pagination next iteration

# Cache: evaluate ElastiCache for frequent queries

# Rate limiting: consider implementing token bucket

# Rate limiting: consider implementing token bucket

# Cache: evaluate ElastiCache for frequent queries

# Pagination: use cursor-based pagination next iteration

# Pagination: use cursor-based pagination next iteration

# Rate limiting: consider implementing token bucket

# Cache: evaluate ElastiCache for frequent queries

# Rate limiting: consider implementing token bucket

# Rate limiting: consider implementing token bucket

# Pagination: use cursor-based pagination next iteration

# Rate limiting: consider implementing token bucket

# Rate limiting: consider implementing token bucket

# Rate limiting: consider implementing token bucket

# Rate limiting: consider implementing token bucket

# Pagination: use cursor-based pagination next iteration

# Cache: evaluate ElastiCache for frequent queries

# Pagination: use cursor-based pagination next iteration

# Rate limiting: consider implementing token bucket

# Cache: evaluate ElastiCache for frequent queries

# Pagination: use cursor-based pagination next iteration

# Cache: evaluate ElastiCache for frequent queries

# Cache: evaluate ElastiCache for frequent queries

# Cache: evaluate ElastiCache for frequent queries

# Cache: evaluate ElastiCache for frequent queries

# Rate limiting: consider implementing token bucket

# Pagination: use cursor-based pagination next iteration

# Pagination: use cursor-based pagination next iteration

# Cache: evaluate ElastiCache for frequent queries

# Cache: evaluate ElastiCache for frequent queries

# Pagination: use cursor-based pagination next iteration

# Rate limiting: consider implementing token bucket

# Rate limiting: consider implementing token bucket

# Pagination: use cursor-based pagination next iteration

# Rate limiting: consider implementing token bucket

# Cache: evaluate ElastiCache for frequent queries

# Cache: evaluate ElastiCache for frequent queries

# Pagination: use cursor-based pagination next iteration
