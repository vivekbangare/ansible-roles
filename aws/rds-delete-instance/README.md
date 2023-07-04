# RDS Delete Instance Ansible Role
This Ansible role is designed to facilitate the deletion of Amazon RDS instances. It provides a simple and automated way to remove RDS instances from your infrastructure.

### Features
Deletes Amazon RDS instances.
Allows specification of multiple instances to be deleted.
Supports both single instance deletion and deletion of instances in a Multi-AZ deployment.
Supports specifying the deletion of instances with final snapshots or without snapshots.
Provides customizable options for handling instance deletion errors.

### Requirements
Ansible 2.10 or higher
Boto3 library (installed on the Ansible control node)

### Role Variables
The following variables can be customized in the role:

aws_access_key (required): AWS access key for authentication.
aws_secret_key (required): AWS secret key for authentication.
region (required): AWS region where the RDS instances are located.
instance_ids (required): A list of RDS instance IDs to delete.
final_snapshot_identifier (optional): The identifier for the final snapshot of the deleted instances. If not provided, no final snapshots will be created.
skip_final_snapshot (optional): Set this to true if you want to delete the instances without creating a final snapshot.
force_failover (optional): Set this to true if you want to force a failover to the standby replica before deleting the instances.
delete_automated_backups (optional): Set this to true if you want to delete any automated backups associated with the instances.
wait_timeout (optional): Timeout duration (in seconds) for waiting for instance deletion to complete.
ignore_errors (optional): Set this to true if you want to ignore any errors that occur during instance deletion.

### Example Playbook
Here's an example playbook that uses the rds-delete-instance role:

```
- name: Delete RDS Instances
  hosts: localhost
  gather_facts: false

  vars:
    aws_access_key: "your_aws_access_key"
    aws_secret_key: "your_aws_secret_key"
    region: "us-east-1"
    instance_ids:
      - "instance-1"
      - "instance-2"

  roles:
    - rds-delete-instance

```

### Author Information
This role was created by Vivek Bangare