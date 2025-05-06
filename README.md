# 🧹 AWS Lambda: EBS Snapshot Cleaner

A Python AWS Lambda function that automatically deletes old and unused Amazon EBS snapshots to save costs and maintain a clean environment.

---

## ✅ Features

* Deletes EBS snapshots **older than 6 months**
* Skips snapshots **used in AMIs**
* Logs all actions and errors
* Written in **Python using Boto3**

---

##

---

## 🧠 Technologies Used

* **AWS Lambda**
* \*\*Python \*\*
* **Boto3 (AWS SDK for Python)**
* **Amazon EC2 & EBS**

---

## 🚀 How It Works

1. Fetches all snapshots and AMIs owned by your account.
2. Skips snapshots that are part of an AMI.
3. Deletes snapshots that are older than 6 months and not in use.

---

## 🔐 IAM Permissions Required

Make sure your Lambda execution role has the following permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeSnapshots",
        "ec2:DescribeImages",
        "ec2:DeleteSnapshot"
      ],
      "Resource": "*"
    }
  ]
}
```
