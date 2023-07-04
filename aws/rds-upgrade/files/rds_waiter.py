#To use this script, you will need to have the boto3 library installed. You can install it using the following command:
#pip install boto3

import boto3
import sys
import time

def wait_for_available(db_instance_identifier, region):
    client = boto3.client('rds', region_name=region)
    while True:
        response = client.describe_db_instances(DBInstanceIdentifier=db_instance_identifier)
        db_instance = response['DBInstances'][0]
        if db_instance['DBInstanceStatus'] == 'available':
            break
        time.sleep(5)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: rds_waiter.py DB_INSTANCE_IDENTIFIER REGION')
        sys.exit(1)
    db_instance_identifier = sys.argv[1]
    region = sys.argv[2]
    wait_for_available(db_instance_identifier, region)
