# AWS CloudFormation POC - Wibix Consulting

## Overview

This project includes:

- A CloudFormation template (`readonly-access.yaml`) that creates an IAM role with ReadOnly access.
- A Python script (`fetch_inventory.py`) that retrieves resource details from the specified CloudFormation stack.

## Deployment

### 1. Launch CloudFormation Stack

Use the following URL to launch the stack:

[Launch Stack](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?templateURL=https://raw.githubusercontent.com/neiilvsm/aws-cloudformation-poc/main/readonly-access.yaml)

> Replace `neiilvsm` with your actual GitHub username if you fork or copy this repo.

### 2. Run Python Script

Ensure you have the necessary permissions (e.g., running on an EC2 instance with an appropriate IAM role).

```bash
python fetch_inventory.py <stack-name>
```

Replace `<stack-name>` with the name of your CloudFormation stack.

## Notes

- The Python script uses default AWS credentials (e.g., from instance profile).
- No AWS credentials are hardcoded in the script.
