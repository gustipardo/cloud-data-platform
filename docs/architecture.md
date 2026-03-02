# Architecture

## System Overview

```
┌─────────────┐     ┌──────────────┐     ┌──────────────────┐
│   Clients   │────▶│ API Gateway  │────▶│  Lambda (API)    │
└─────────────┘     └──────────────┘     └────────┬─────────┘
                                                   │
                                                   ▼
┌─────────────┐     ┌──────────────┐     ┌──────────────────┐
│  Data Sources│────▶│   S3 Bucket  │────▶│ Lambda (Processor)│
└─────────────┘     └──────────────┘     └────────┬─────────┘
                                                   │
                                          ┌────────┴─────────┐
                                          ▼                  ▼
                                   ┌──────────┐      ┌──────────┐
                                   │ DynamoDB  │      │   RDS    │
                                   │(Realtime) │      │(Analytics)│
                                   └──────────┘      └──────────┘
```

## Design Decisions

### Why Serverless?

- **Cost efficiency**: Pay only for actual usage
- **Auto-scaling**: Handles traffic spikes without manual intervention
- **Reduced ops overhead**: No servers to manage or patch
- **Event-driven**: Natural fit for data pipeline patterns

### DynamoDB + RDS

We use a dual-database approach:

- **DynamoDB** for real-time event storage and low-latency queries
- **RDS (PostgreSQL)** for complex analytics, joins, and reporting

This separation allows optimizing each store for its access pattern.

### Event Processing

Events flow through a validation → transformation → storage pipeline:

1. **Validation**: Schema checks, type verification
2. **Transformation**: Timestamp normalization, type conversion, enrichment
3. **Storage**: Dual write to DynamoDB (real-time) and batch to RDS (analytics)

## Security

- All data encrypted at rest (S3 SSE, DynamoDB encryption, RDS encryption)
- Lambda functions use least-privilege IAM policies
- API Gateway with CORS restrictions in production
- VPC endpoints for DynamoDB and S3 access
- CloudTrail logging for API auditing

## Monitoring

- CloudWatch metrics for Lambda duration, errors, throttles
- Custom metrics for business KPIs
- SNS alerts for critical thresholds
- X-Ray tracing for end-to-end latency analysis

## Perf: Lambda Provisioned Concurrency for API functions
