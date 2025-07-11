🔁 AWS Lambda + SQS Data Pipeline (Bulk Data Generation & Processing)

This project demonstrates a serverless event-driven architecture using AWS Lambda, Amazon SQS, and Python (with boto3 and random). The setup simulates a data ingestion pipeline where synthetic data is generated, queued, and processed efficiently.

📌 Project Workflow

Lambda Function 1 (Data Generator):

Uses the random library to generate bulk synthetic data (e.g., mock user info or transactions).

Publishes each generated record as a message to an Amazon SQS queue using the boto3 SDK.

Amazon SQS:

Acts as a decoupled message broker between the producer and consumer Lambda functions.

Stores and forwards messages reliably for asynchronous processing.

Lambda Function 2 (Data Processor):

Is triggered automatically when messages arrive in the queue.

Reads and processes each SQS message (e.g., logs, stores, transforms).

🛠️ Key Skills and AWS Services Used

AWS Lambda: Stateless compute for both producer and consumer functions.

Amazon SQS: Scalable message queue for decoupling and reliability.

Boto3: AWS SDK for Python used to send messages to the SQS queue.

Python random: Used for generating mock/bulk data.

IAM Roles & Policies: To allow Lambda → SQS publish and Lambda → SQS read access.

CloudWatch Logs: For monitoring, debugging, and validating function execution.

