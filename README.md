# AWS EBS Snapshot Cleanup Lambda Function

## Overview

This Lambda function is designed to clean up **unused** EBS snapshots in AWS. It does so by identifying snapshots that are no longer attached to active EC2 instances or are associated with unattached EBS volumes.

The function performs the following tasks:

1. Fetches all EBS snapshots created by the AWS account.
2. Fetches all running EC2 instances.
3. Checks if each snapshot is associated with an active EC2 instance.
4. Deletes snapshots that are no longer associated with any volume or where the associated volume is not attached to any running instance.

## Prerequisites

* AWS account with the required permissions to describe EC2 instances, snapshots, and volumes.
* Lambda function with permissions to use **EC2** services.

## How it Works

1. **EC2 Snapshots**: The function begins by fetching all EBS snapshots owned by the account.
2. **Running EC2 Instances**: It then fetches the list of running EC2 instances.
3. **Snapshot Deletion**:

   * The function checks each snapshot to see if it is associated with an EBS volume.
   * If the volume is not attached to any instance, the snapshot is deleted.
   * If the volume is attached to a non-running instance or the volume itself doesn't exist (due to deletion), the snapshot is also deleted.

## Permissions Required

Ensure that the Lambda function has the following IAM permissions:

* `ec2:DescribeSnapshots`
* `ec2:DescribeInstances`
* `ec2:DescribeVolumes`
* `ec2:DeleteSnapshot`


