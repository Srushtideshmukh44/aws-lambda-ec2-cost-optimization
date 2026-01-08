# AWS Cost Optimization using Lambda & SNS

## 📌 Project Overview
This project automatically stops unused EC2 instances to reduce AWS costs.
Before stopping instances, an email alert is sent using Amazon SNS.

## 🛠️ Services Used
- AWS Lambda
- Amazon EC2
- Amazon SNS
- Amazon EventBridge
- AWS IAM
- Amazon CloudWatch

## 🔁 Architecture Flow
1. EventBridge triggers Lambda every hour
2. Lambda checks running EC2 instances
3. SNS sends email alert
4. Lambda stops EC2 instances
5. Logs are stored in CloudWatch

## 🧠 Use Case
- Cost optimization
- Avoid unnecessary EC2 billing
- Automated infrastructure control

## 🔐 IAM Permissions
- EC2 Full Access
- SNS Publish Access
- CloudWatch Logs

## 🚀 Outcome
- Reduced AWS costs
- Fully automated solution
- Email alert before EC2 shutdown

## 📎 Author
**Srushti Deshmukh**  
DevOps / Cloud Engineer
