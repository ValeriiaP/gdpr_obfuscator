# `gdpr_obfuscator`

## Project Description

   ### **Purpose:**

   This tool is designed to help with the obfuscation of personal data in compliance with GDPR regulations.

   It ensures that sensitive information is anonymized in datasets, making it safe to use for analysis and processing without compromising privacy.

   ### **Storage:**

   The data is stored in an AWS S3 bucket, so this tool requires proper AWS configuration.

## Installation

1. **Clone the repository**
   git clone [GitHub Pages](https://github.com/ValeriiaP/gdpr_obfuscator)

2. **Navigate into the project directory**

   ```
   cd gdpr_obfuscator
   ```

3. **Activate your virtual environment:**

   ```
   source venv/bin/activate # macOS/Linux
   .\venv\Scripts\activate # Windows
   ```

4. **Install dependencies:**

   ```
   pip install -r requirements.txt
   ```

## Usage

**To use the `gdpr_obfuscator` tool, follow these steps:**

1. Ensure your data is in CSV, JSON, or parquet format and stored in an AWS S3 bucket.
2. Make sure your AWS credentials are configured as described in the Configuration section.
3. The obfuscate() function expects a dictionary with two keys:
   + **file_to_obfuscate**: the path to the file in an S3 bucket.
   + **pii_fields**: a list of fields that contain Personally Identifiable Information (PII) to be obfuscated.
4. Example usage:

   ```
   from gdpr_obfuscator import obfuscate

   obfuscate({
   "file_to_obfuscate": "s3://example-bucket/file.csv",
   "pii_fields": ["name", "email"]
   })
   ```

5. Example input:

   ```
   student_id,name,course,cohort,graduation_date,email
   91a3283711,Jane Smith,Mathematics,2023,2023-04-10,janesmith@example.com
   7f76b4d212,David Lee,Physics,2022,2021-07-29,davidlee@example.com
   ```

6. Example output:

   ```
   student_id,name,course,cohort,graduation_date,email
   91a3283711,***,Mathematics,2023,2023-04-10,***
   7f76b4d212,***,Physics,2022,2021-07-29,***
   ```

## Configuration

**AWS Credentials Configuration**

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
