# Development Notes

> Working notes, ideas and technical debt tracking.

## TODO

- [ ] Add pagination to events API endpoint
- [ ] Implement batch processing with SQS
- [ ] Set up CI/CD pipeline with GitHub Actions
- [ ] Add integration tests with LocalStack
- [ ] Implement data partitioning strategy for S3
- [ ] Add OpenAPI spec for API Gateway
- [ ] Set up Grafana dashboard for monitoring
- [ ] Implement retry logic for transient DynamoDB errors

## Notes

### Performance observations

- Lambda cold starts averaging ~800ms with current package size
- DynamoDB query latency consistently < 10ms for single-key lookups
- Batch writer handles up to ~500 items efficiently before throttling

### Useful commands

```bash
# Check Lambda logs
aws logs tail /aws/lambda/data-pipeline-processor-dev --follow

# Query DynamoDB
aws dynamodb scan --table-name data-pipeline-events-dev --max-items 10

# Upload test event
aws s3 cp test_event.json s3://data-pipeline-raw-events-dev/incoming/

# Invoke Lambda directly
aws lambda invoke --function-name data-pipeline-processor-dev \
  --payload file://test/fixtures/s3_event.json output.json
```

### 2026-03-02 15:57:34

- Reviewed CloudWatch Logs Insights queries for debugging

### 2026-03-06 15:54:37

- Reviewed CloudWatch Logs Insights queries for debugging

### 2026-03-10 16:16:34

- Analyzed error patterns, most failures are transient

### 2026-03-11 20:02:09

- Tested batch processing with SQS FIFO queue

### 2026-03-12 03:12:47

- Tested VPC endpoint latency vs public endpoint

### 2026-03-13 03:09:43

- Reviewed CloudWatch Logs Insights queries for debugging

### 2026-03-16 03:36:07

- Reviewed CloudWatch Logs Insights queries for debugging

### 2026-03-16 11:55:11

- Reviewed CloudWatch Logs Insights queries for debugging

### 2026-03-17 11:53:02

- Reviewed DynamoDB capacity metrics, current usage within limits

### 2026-03-17 16:19:05

- Investigated cold start optimization with provisioned concurrency

### 2026-03-18 03:21:32

- Reviewed DynamoDB capacity metrics, current usage within limits

### 2026-03-18 16:19:18

- Profiled Lambda memory usage, 512MB optimal for current workload

### 2026-03-18 20:03:01

- Tested VPC endpoint latency vs public endpoint

### 2026-03-22 03:21:42

- Analyzed error patterns, most failures are transient

### 2026-03-28 03:17:02

- Evaluated EventBridge Pipes as alternative to S3 notifications

### 2026-03-28 19:55:05

- Investigated cold start optimization with provisioned concurrency

### 2026-04-02 20:04:51

- Reviewed CloudWatch Logs Insights queries for debugging

### 2026-04-04 15:47:56

- Benchmarked JSON vs Parquet for S3 storage

### 2026-04-05 11:41:51

- Benchmarked JSON vs Parquet for S3 storage

### 2026-04-06 11:56:30

- Explored Step Functions for complex event workflows

### 2026-04-06 16:03:04

- Investigated cold start optimization with provisioned concurrency
