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
