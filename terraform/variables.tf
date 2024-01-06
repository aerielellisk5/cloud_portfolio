variable "bucket_name" {
  description = "The name of the S3 bucket. Must be globally unique."
  type        = string
  default = "cloud-portfolio-2"
}

variable "table_name" {
  description = "The name of the DynamoDB table. Must be unique in this AWS account."
  type        = string
  default = "terraform-remote-state-dynamo"
}

variable "my_db" {
  description = "the name of the db"
  type        = string
  default = "cloud_portfolio"
}

variable "db_engine" {
  description = "the type of db engine being used"
  type        = string
  default = "postgres"
}

variable "engine_version" {
  description = "the version of the engine being used"
  type        = string
  default = "13.11"
}

variable "db_ic" {
  description = "the instance class of the db"
  type        = string
  default = "db.t3.micro"
}

variable "db_username" {
  description = "the username for the postgres instance"
  type        = string
  default = "postgres"
}

variable "db_password" {
  description = "the password for the postgres instance"
  type        = string
  default = "password123"
}