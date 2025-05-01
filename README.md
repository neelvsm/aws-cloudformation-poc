# AWS Internship POC - Wibix Consulting

## Overview

This Proof of Concept includes:

- A CloudFormation template (`readonly-access.yaml`) to create a ReadOnly IAM role.
- A Python script (`fetch_inventory.py`) to fetch inventory info from the CloudFormation stack.

## Steps to Use

### 1. Launch the CloudFormation Stack

Click the link below to launch the stack:

[Launch CloudFormation Stack](https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?templateURL=https://raw.githubusercontent.com/neelvsm/aws-cloudformation-poc/main/readonly-access.yaml)

> This will deploy a ReadOnlyAccess IAM role using your AWS Console.

### 2. Run the Python Script

```bash
python fetch_inventory.py <stack-name>
