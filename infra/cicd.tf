resource "aws_iam_user" "github_actions" {
  name = "github-actions-user"
}

resource "aws_iam_user_policy_attachment" "ecr_power_user" {
  user       = aws_iam_user.github_actions.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryPowerUser"
}

resource "aws_iam_access_key" "github_actions_key" {
  user = aws_iam_user.github_actions.name
}

output "aws_access_key_id" {
  value     = aws_iam_access_key.github_actions_key.id
  sensitive = true
}

output "aws_secret_access_key" {
  value     = aws_iam_access_key.github_actions_key.secret
  sensitive = true
}