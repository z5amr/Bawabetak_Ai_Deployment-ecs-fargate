resource "aws_ecs_cluster" "main" {
  name = "${var.service_name}-cluster"
}

resource "aws_ecs_service" "main" {
  name            = "${var.service_name}-service"
  cluster         = aws_ecs_cluster.main.id
  task_definition = aws_ecs_task_definition.app.arn
  desired_count   = 1
  launch_type     = "FARGATE"

  network_configuration {
    subnets          = [aws_subnet.public_1.id]
    security_groups  = [aws_security_group.ecs_sg.id]
    assign_public_ip = true
  }
}