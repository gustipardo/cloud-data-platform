output "api_endpoint" {
  description = "API Gateway endpoint URL"
  value       = aws_apigatewayv2_api.main.api_endpoint
}

output "raw_events_bucket" {
  description = "S3 bucket for raw event data"
  value       = aws_s3_bucket.raw_events.id
}

output "dynamodb_table" {
  description = "DynamoDB events table name"
  value       = aws_dynamodb_table.events.name
}

output "processor_function" {
  description = "Data processor Lambda function name"
  value       = aws_lambda_function.data_processor.function_name
}

output "api_function" {
  description = "API Lambda function name"
  value       = aws_lambda_function.api.function_name
}
