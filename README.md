# aws-data-pipeline

Serverless data pipeline built on AWS for ingesting, processing, and analyzing event data at scale.

## Architecture

```
S3 (Raw Data) → Lambda (Processor) → DynamoDB / RDS → API Gateway → Lambda (API) → Client
                     ↓
              CloudWatch Logs
                     ↓
              SNS Notifications
```

### Components

| Service | Purpose |
|---------|---------|
| **S3** | Raw event data storage (JSON/CSV) |
| **Lambda** | Event processing & API handlers |
| **DynamoDB** | Real-time event store |
| **RDS (PostgreSQL)** | Analytics & reporting database |
| **API Gateway** | REST API for querying processed data |
| **CloudWatch** | Monitoring, alarms & logging |
| **SNS** | Alert notifications |
| **EventBridge** | Scheduled processing rules |

## Project Structure

```
├── infrastructure/        # Terraform IaC
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── modules/
├── lambda/
│   ├── data_processor/    # S3 event processor
│   │   ├── handler.py
│   │   └── utils.py
│   └── api/               # API Gateway handlers
│       └── handler.py
├── sql/
│   ├── migrations/        # Schema migrations
│   └── queries/           # Analytics queries
├── config/                # Environment configs
├── scripts/               # Deployment & utility scripts
├── tests/                 # Unit & integration tests
└── docs/                  # Architecture & decision records
```

## Getting Started

### Prerequisites

- AWS CLI v2 configured with appropriate credentials
- Terraform >= 1.5
- Python 3.11+
- Docker (for local testing with LocalStack)

### Setup

```bash
# Clone and install dependencies
git clone https://github.com/gustipardo/aws-data-pipeline.git
cd aws-data-pipeline
pip install -r requirements.txt

# Initialize Terraform
cd infrastructure
terraform init
terraform plan -var-file="../config/dev.tfvars"

# Deploy to dev
terraform apply -var-file="../config/dev.tfvars"
```

### Running Tests

```bash
pytest tests/ -v --cov=lambda
```

## Environments

| Environment | Account | Region |
|------------|---------|--------|
| Development | `dev-123456` | us-east-1 |
| Staging | `stg-789012` | us-east-1 |
| Production | `prod-345678` | us-east-1, eu-west-1 |

## Data Flow

1. Raw event data lands in S3 (`s3://pipeline-raw-events/`)
2. S3 event triggers `data_processor` Lambda
3. Lambda validates, transforms, and enriches the data
4. Processed records are written to DynamoDB (real-time) and batched to RDS (analytics)
5. CloudWatch alarms monitor error rates and latency
6. API Gateway exposes query endpoints for downstream consumers

## Configuration

Environment-specific configuration is managed through `config/` directory.
See [docs/configuration.md](docs/configuration.md) for details.

## Contributing

1. Create a feature branch from `main`
2. Follow conventional commit messages
3. Ensure all tests pass
4. Submit a pull request

## License

MIT

<!-- Updated: 2026-03-02 -->

<!-- Updated: 2026-03-04 -->

<!-- Updated: 2026-03-05 -->

<!-- Updated: 2026-03-10 -->

<!-- Updated: 2026-03-12 -->

<!-- Updated: 2026-03-12 -->

<!-- Updated: 2026-03-13 -->

<!-- Updated: 2026-03-13 -->

<!-- Updated: 2026-03-14 -->

<!-- Updated: 2026-03-16 -->

<!-- Updated: 2026-03-17 -->

<!-- Updated: 2026-03-18 -->

<!-- Updated: 2026-03-20 -->

<!-- Updated: 2026-03-23 -->
