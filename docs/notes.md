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

### 2026-04-09 20:27:45

- Benchmarked JSON vs Parquet for S3 storage

### 2026-04-14 03:43:57

- Analyzed error patterns, most failures are transient

### 2026-04-15 16:16:20

- Reviewed CloudWatch Logs Insights queries for debugging

### 2026-04-16 03:48:00

- Investigated cold start optimization with provisioned concurrency

### 2026-04-16 16:50:20

- Analyzed error patterns, most failures are transient

### 2026-04-16 20:25:23

- Profiled Lambda memory usage, 512MB optimal for current workload

### 2026-04-24 16:13:23

- Benchmarked JSON vs Parquet for S3 storage

### 2026-04-25 03:33:21

- Evaluated EventBridge Pipes as alternative to S3 notifications

### 2026-05-05 12:11:08

- Benchmarked JSON vs Parquet for S3 storage

### 2026-05-08 20:36:40

- Tested batch processing with SQS FIFO queue

### 2026-05-09 20:22:59

- Benchmarked JSON vs Parquet for S3 storage

### 2026-05-09 20:23:08

- Reviewed DynamoDB capacity metrics, current usage within limits

### 2026-05-10 12:00:40

- Tested VPC endpoint latency vs public endpoint

### 2026-05-11 17:31:39

- Reviewed DynamoDB capacity metrics, current usage within limits

### 2026-05-11 21:04:12

- Benchmarked JSON vs Parquet for S3 storage

### 2026-05-14 13:02:08

- Reviewed CloudWatch Logs Insights queries for debugging

### 2026-05-18 20:54:00

- Analyzed error patterns, most failures are transient

### 2026-05-20 04:38:08

- Tested batch processing with SQS FIFO queue

### 2026-05-20 21:19:43

- Evaluated EventBridge Pipes as alternative to S3 notifications

### 2026-05-21 14:17:07

- Benchmarked JSON vs Parquet for S3 storage

### 2026-05-25 17:16:32

- Explored Step Functions for complex event workflows

### 2026-05-26 14:09:32

- Analyzed error patterns, most failures are transient

### 2026-05-27 14:33:01

- Tested batch processing with SQS FIFO queue

### 2026-05-27 18:08:15

- Reviewed DynamoDB capacity metrics, current usage within limits

### 2026-05-27 18:08:24

- Tested VPC endpoint latency vs public endpoint

### 2026-06-01 05:17:34

- Evaluated EventBridge Pipes as alternative to S3 notifications

### 2026-06-01 19:58:39

- Reviewed DynamoDB capacity metrics, current usage within limits

### 2026-06-01 22:22:47

- Tested VPC endpoint latency vs public endpoint

### 2026-06-02 18:55:18

- Analyzed error patterns, most failures are transient

### 2026-06-04 17:57:04

- Profiled Lambda memory usage, 512MB optimal for current workload

### 2026-06-04 21:15:38

- Profiled Lambda memory usage, 512MB optimal for current workload

### 2026-06-06 04:29:46

- Tested batch processing with SQS FIFO queue

### 2026-06-06 04:30:09

- Tested VPC endpoint latency vs public endpoint

### 2026-06-08 05:02:32

- Benchmarked JSON vs Parquet for S3 storage

### 2026-06-08 18:08:44

- Explored Step Functions for complex event workflows

### 2026-06-09 21:21:20

- Benchmarked JSON vs Parquet for S3 storage

### 2026-06-10 04:50:02

- Reviewed DynamoDB capacity metrics, current usage within limits

### 2026-06-11 04:59:53

- Analyzed error patterns, most failures are transient

### 2026-06-11 14:52:01

- Reviewed CloudWatch Logs Insights queries for debugging

### 2026-06-11 14:52:12

- Reviewed CloudWatch Logs Insights queries for debugging

### 2026-06-12 21:17:52

- Explored Step Functions for complex event workflows

### 2026-06-16 22:01:22

- Analyzed error patterns, most failures are transient

### 2026-06-17 21:31:06

- Evaluated EventBridge Pipes as alternative to S3 notifications

### 2026-06-18 14:19:10

- Benchmarked JSON vs Parquet for S3 storage

### 2026-06-19 05:26:21

- Tested VPC endpoint latency vs public endpoint

### 2026-06-23 17:21:39

- Analyzed error patterns, most failures are transient

### 2026-06-24 13:27:18

- Profiled Lambda memory usage, 512MB optimal for current workload

### 2026-06-25 13:24:13

- Reviewed CloudWatch Logs Insights queries for debugging

### 2026-06-26 21:08:03

- Investigated cold start optimization with provisioned concurrency

### 2026-06-28 16:37:35

- Reviewed CloudWatch Logs Insights queries for debugging

### 2026-07-02 20:43:44

- Analyzed error patterns, most failures are transient

### 2026-07-08 16:51:04

- Tested VPC endpoint latency vs public endpoint

### 2026-07-10 04:16:11

- Tested batch processing with SQS FIFO queue
