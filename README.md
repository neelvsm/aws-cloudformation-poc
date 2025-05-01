# AWS Internship POC - Wibix Consulting

## Overview

This Proof of Concept includes:
- A CloudFormation template (`readonly-access.yaml`) to create a ReadOnly IAM role.
- A Python script (`fetch_inventory.py`) to fetch inventory info from the CloudFormation stack.

## Steps to Use

### 1. Launch the CloudFormation Stack

Upload the `readonly-access.yaml` file to a GitHub repo, and use this format to launch it:

```
https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?templateURL=https://raw.githubusercontent.com/<your-username>/aws-cloudformation-poc/main/readonly-access.yaml
```

Replace https://console.aws.amazon.com/cloudformation/home#/stacks/create/review?templateURL=https://raw.githubusercontent.com/neelvsm/aws-cloudformation-poc/main/readonly-access.yaml
 with your GitHub username.

### 2. Run the Python Script

```bash
python fetch_inventory.py <stack-name>
```

Make sure this script runs inside an AWS environment that has proper permissions (like an EC2 instance with an IAM role).

No AWS credentials are hardcoded.

## Deliverables

- GitHub Repository: Contains the files
- CloudFormation Launch URL (based on raw file link)
- README (this file) for documentation
