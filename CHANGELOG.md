# Changelog

All notable changes to this project will be documented in this file.

## [0.4.0] - 2025-07-15

### Added
- EventBridge rules for scheduled batch processing
- Dead letter queue for failed Lambda invocations
- X-Ray tracing for end-to-end request tracking

### Changed
- Increased processor Lambda memory to 512MB
- Updated DynamoDB GSI for better query performance

### Fixed
- Race condition in batch writer when processing large files
- Timestamp parsing for ISO 8601 formats with timezone offset

## [0.3.0] - 2025-05-20

### Added
- API Gateway HTTP API with CORS configuration
- `/events/stats` endpoint for aggregated statistics
- Health check endpoint at `/health`
- Session duration tracking and analytics

### Changed
- Migrated from REST API to HTTP API (lower latency, cost)
- Improved error handling in data processor

## [0.2.0] - 2025-04-10

### Added
- PostgreSQL analytics schema with migrations
- Daily aggregation tables
- Funnel analysis queries
- CloudWatch alarms for error rate monitoring
- SNS notifications for critical alerts

### Changed
- Switched DynamoDB to PAY_PER_REQUEST billing
- Added point-in-time recovery

## [0.1.0] - 2025-03-01

### Added
- Initial project setup
- S3 bucket for raw event ingestion
- Lambda data processor with validation and transformation
- DynamoDB event store with GSI
- Basic Terraform infrastructure
- Unit tests for core utilities

- Update dependency versions

- Improve API response caching

- Add retry logic for transient failures
