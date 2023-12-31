# start with the provider

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  # # Comment this backend s3 part out IF starting from scratch
  backend "s3" {
    bucket = "cloud-portfolio-2"
    key    = "terraform_create_s3_bucket/terraform.tfstate"
    region = "us-east-1"
    dynamodb_table = "terraform-remote-state-dynamo"
    encrypt = true
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}

# Creating all the S3 bucket neccessities to hold the DynamoDB table containing the lock file
resource "aws_s3_bucket" "terraform_state" {
  bucket = var.bucket_name
  force_destroy = true
}

resource "aws_s3_bucket_versioning" "bucket_version" {
  bucket = var.bucket_name
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "bucket_sse" {
  bucket = var.bucket_name
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# Creating all the DynamoDB table neccessities to hold the lock file
resource "aws_dynamodb_table" "terraform_locks" {
  name         = var.table_name
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"
  attribute {
    name = "LockID"
    type = "S"
  }
}

# Create the RDS instance 
resource "aws_db_instance" "backup_pg_instance" {
  allocated_storage    = 20
  db_name              = var.my_db
  engine               = var.db_engine
  engine_version       = var.engine_version
  instance_class       = var.db_ic 
  username             = var.db_username
  password             = var.db_password
  # parameter_group_name = "default.mysql5.7" This is optional
  # skip_final_snapshot  = true this is also optional
}

