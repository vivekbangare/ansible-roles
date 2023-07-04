# Ansible Role: RDS Upgrade
This Ansible role upgrades an RDS instance using the rds module.

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
    rds_instance_type: db.t3.small
```

### Dependencies
None.

### Example Playbook
```
    - hosts: localhost
      roles:
        - role: rds_upgrade
```
