# Stack-<NAME>

Service catalog <NAME> stack

Small description of the stack

# Architecture

<p align="center">
<img src="docs/diagram.jpeg" width="400">
</p>


  * **ALB**: Amazon application loadbalancer
  * **RDS** ...

# Requirements

In order to run this task, couple elements are required within the infrastructure:

  * Having a VPC with private & public subnets [Here](https://docs.aws.amazon.com/vpc/latest/userguide/getting-started-ipv4.html#getting-started-create-vpc)
  * Having an S3 bucket to store Terraform remote states [Here](https://docs.aws.amazon.com/quickstarts/latest/s3backup/step-1-create-bucket.html)
  * Having a bastion server to run Ansible like described [Here](https://docs.cycloid.io/advanced-guide/ansible-integration.html#standard-usage)

# Details

## Pipeline

> **Note** The pipeline contains a manual approval between terraform plan and terraform apply.
> That means if you trigger a terraform plan, to apply it, you have to go on terraform apply job
> and click on the `+` button to trigger it.

<img src="docs/pipeline.png" width="800">

**Jobs description**

  * `terraform-plan`: Terraform job that will simply make a plan of the stack.
  * `terraform-apply`: Terraform job similar to the plan one, but will actually create/update everything that needs to. Please see the plan diff for a better understanding.
  * `terraform-destroy`: :warning: Terraform job meant to destroy the whole stack - **NO CONFIRMATION ASKED**. If triggered, the full project **WILL** be destroyed. Use with caution.

**Params**

> Generate command
```
markdown-tabs-from-comments.py -f pipeline/variables.sample.yml
```

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-----:|:-----:|
| aws_region |  | string | `eu-west-1` | no |


## Terraform

> Generate commands
```

# Outputs
terraform-docs md outputs.tf

# Inputs
# For full role variables doc
terraform-docs md module-magento/

# For doc generated from the sample file
markdown-tabs-from-comments.py -f terraform/magento.tf.sample
```

**Inputs**

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-----:|:-----:|
| aws_region |  | string | `eu-west-1` | no |


**Outputs**

| Name | Description |
|------|-------------|
| cache_address |  |


## Ansible

> Generate command
```
markdown-tabs-from-comments.py -f ansible/environments/front.yml.sample
```

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-----:|:-----:|
| aws_region |  | string | `eu-west-1` | no |


# Troubleshooting

(Add it if there is content)


# Molecule tests

(Add it if there is ansible + molecule test we can run)

Requires a bucket which contains a build of magento sources and AWS accesskey

```
export AWS_SECRET_ACCESS_KEY=$(vault read -field=secret_key secret/$CUSTOMER/aws)
export AWS_ACCESS_KEY_ID=$(vault read -field=access_key secret/$CUSTOMER/aws)

export MAGENTO_DEPLOY_BUCKET_NAME=cycloid-deploy
export MAGENTO_DEPLOY_BUCKET_OBJECT_PATH=/catalog-magento/ci/magento.tar.gz
export MAGENTO_DEPLOY_BUCKET_REGION=eu-west-1

# Share if needed your ssh key to an ssh agent (used by molecule to clone dependencies)
eval $(ssh-agent )
ssh-add ~/.ssh/id_rsa

# Run molecule
molecule test
```

