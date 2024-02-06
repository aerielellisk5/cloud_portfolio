# start with the provider

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  # Comment this backend s3 part out IF starting from scratch
  backend "s3" {
    bucket         = "cloud-portfolio-2"
    key            = "terraform_create_s3_bucket/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-remote-state-dynamo"
    encrypt        = true
  }
}

# Configure the AWS Provider
provider "aws" {
  region = "us-east-1"
}

# Creating all the S3 bucket neccessities to hold the DynamoDB table containing the lock file
resource "aws_s3_bucket" "terraform_state" {
  bucket        = var.bucket_name
  force_destroy = false
  lifecycle {
    prevent_destroy = true
  }
}

resource "aws_s3_bucket_versioning" "bucket_version" {
  bucket = var.bucket_name
  versioning_configuration {
    status = "Enabled"
  }
  lifecycle {
    prevent_destroy = true
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "bucket_sse" {
  bucket = var.bucket_name
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
  lifecycle {
    prevent_destroy = true
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
  deletion_protection_enabled = true
}

# Create the RDS instance 
# resource "aws_db_instance" "backup_pg_instance" {
#   allocated_storage = 20
#   db_name           = var.my_db
#   engine            = var.db_engine
#   engine_version    = var.engine_version
#   instance_class    = var.db_ic
#   username          = var.db_username
#   password          = var.db_password
#   # parameter_group_name = "default.mysql5.7" This is optional
#   skip_final_snapshot = true
#   apply_immediately   = true
# }

#Create the S3 bucket to hold the files for my website

resource "aws_s3_bucket" "cpterraformae" {
  # name of the actual bucket
  bucket = "cpterraformae"

  tags = {
    Name = "cpterraformae"
  }
}

#check versioning
resource "aws_s3_bucket_versioning" "versioning_example" {
  bucket = aws_s3_bucket.cpterraformae.id
  versioning_configuration {
    status = "Enabled"
  }
}

# give the s3 bucket the ability to be a website
resource "aws_s3_bucket_website_configuration" "example" {
  bucket = aws_s3_bucket.cpterraformae.id

  index_document {
    suffix = "index.html"
  }

  # this might actually be 404.html?
  error_document {
    key = "error.html"
  }
}

#adding documents to my s3 bucket
resource "aws_s3_object" "html" {
  bucket = aws_s3_bucket.cpterraformae.id
  for_each = toset(var.html_files_to_upload)
  key    = each.value
  source = each.value
  content_type = "text/html"
}



























#Creating the Certificate
# resource "aws_acm_certificate" "cert" {
#   domain_name       = "example.com"
#   validation_method = "DNS"

#   tags = {
#     Environment = "test"
#   }

#   lifecycle {
#     create_before_destroy = true
#   }

#   validation_option {
#     domain_name       = "testing.example.com"
#     validation_domain = "example.com"
#   }
# }

#creating the route53 record
# resource "aws_route53_record" "www" {
#   zone_id = aws_route53_zone.primary.zone_id
#   name    = "www.example.com"
#   type    = "A"
#   ttl     = 300
#   records = [aws_eip.lb.public_ip]
# }



