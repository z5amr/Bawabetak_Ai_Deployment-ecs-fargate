terraform {
  required_version = ">= 1.10.0" 

  backend "s3" {
    bucket       = "bawabetak-tf-state-amr-2026"
    key          = "ecs-fargate/terraform.tfstate"
    region       = "us-east-1"
    encrypt      = true
    use_lockfile = true
  }
}