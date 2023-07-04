# Ansible Role: RDS Create Instance
This Ansible role creates an RDS instance from a snapshot using the rds module.

### Requirements
This role requires the boto3 Python package to be installed on the target host. You can install it using the pip package manager:

```
    pip install boto3
```

### Role Variables
The following variables are defined in defaults/main.yml:
```
    aws_region: us-east-1
    rds_instance_name: my-rds-instance
    rds_snapshot_name: my-rds-snapshot
    rds_subnet_group: my-rds-subnet-group
    rds_security_group: my-rds-security-group
    rds_instance_type: db.t2.micro
    rds_master_username: my-rds-user
    rds_master_password: my-rds-password
    rds_engine: mysql
    rds_port: 3306
```

### Dependencies
None.

### Example Playbook

```
    - hosts: localhost
      roles:
        - role: rds_create_instance
```

### Author Information
This role was created by Vivek Bangare