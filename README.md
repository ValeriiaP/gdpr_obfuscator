## Project Description

`gdpr_obfuscator` is a tool designed to help with the obfuscation of personal data in compliance with GDPR regulations. It ensures that sensitive information is anonymized in datasets, making it safe to use for analysis and processing without compromising privacy. Data is stored in CSV-, JSON-, or parquet-formatted files in an AWS S3 bucket.

## Installation

1. Clone the repository
   git clone https://github.com/ValeriiaP/gdpr_obfuscator

2. Navigate into the project directory
   cd gdpr_obfuscator

3. Create and activate a virtual environment:
   pip install virtualenv
   virtualenv venv
   source venv/bin/activate # macOS/Linux
   OR
   .\venv\Scripts\activate # Windows

4. Install dependencies:
   pip install -r requirements.txt

## Usage

???

## Configuration

AWS Credentials Configuration

This project requires AWS credentials to interact with AWS services like S3, EC2, or DynamoDB. Below are several ways to configure your AWS credentials.

Option 1: AWS CLI

1. Install the AWS CLI
2. Run `aws configure` and follow the prompts to enter your AWS Access Key, Secret Access Key, and Default Region.

Option 2: Environment Variables

Set AWS credentials using environment variables:

```bash
export AWS_ACCESS_KEY_ID=your-access-key-id
export AWS_SECRET_ACCESS_KEY=your-secret-access-key
export AWS_DEFAULT_REGION=your-region
```
