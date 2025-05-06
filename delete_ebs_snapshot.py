import boto3
from datetime import datetime, timezone, timedelta

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Get current time and 6 months ago
    now = datetime.now(timezone.utc)
    six_months_ago = now - timedelta(days=180)

    # Get all snapshots owned by this account
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']
    print(f"Found {len(snapshots)} snapshots.")

    # Get all AMIs owned by this account
    images = ec2.describe_images(Owners=['self'])['Images']
    image_snapshot_ids = set()

    # Collect snapshot IDs used in AMIs
    for image in images:
        for device in image.get('BlockDeviceMappings', []):
            if 'Ebs' in device and 'SnapshotId' in device['Ebs']:
                image_snapshot_ids.add(device['Ebs']['SnapshotId'])

    deleted_count = 0

    for snapshot in snapshots:
        snapshot_id = snapshot['SnapshotId']
        start_time = snapshot['StartTime']

        if snapshot_id in image_snapshot_ids:
            continue  # Don't delete if used in AMI

        if start_time < six_months_ago:
            try:
                ec2.delete_snapshot(SnapshotId=snapshot_id)
                print(f"Deleted snapshot: {snapshot_id} (Created: {start_time})")
                deleted_count += 1
            except Exception as e:
                print(f"Failed to delete snapshot {snapshot_id}: {e}")

    return {
        'statusCode': 200,
        'body': f"Deleted {deleted_count} old and unused snapshots."
    }

