#!/bin/bash
# Deploy script for data pipeline infrastructure
set -euo pipefail

ENV="${1:-dev}"
ACTION="${2:-plan}"

echo "=== Data Pipeline Deploy ==="
echo "Environment: $ENV"
echo "Action: $ACTION"
echo ""

if [[ ! "$ENV" =~ ^(dev|staging|prod)$ ]]; then
  echo "Error: Invalid environment. Use: dev, staging, prod"
  exit 1
fi

cd "$(dirname "$0")/../infrastructure"

terraform init -backend-config="key=data-pipeline/${ENV}/terraform.tfstate"

case $ACTION in
  plan)
    terraform plan -var-file="../config/${ENV}.tfvars" -out="tfplan"
    ;;
  apply)
    terraform apply -var-file="../config/${ENV}.tfvars" -auto-approve
    ;;
  destroy)
    echo "⚠️  WARNING: This will destroy all resources in $ENV"
    read -p "Are you sure? (yes/no): " confirm
    if [ "$confirm" = "yes" ]; then
      terraform destroy -var-file="../config/${ENV}.tfvars" -auto-approve
    fi
    ;;
  *)
    echo "Usage: $0 <env> <plan|apply|destroy>"
    exit 1
    ;;
esac
