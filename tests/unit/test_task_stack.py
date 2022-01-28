import aws_cdk as core
import aws_cdk.assertions as assertions

from task.task_stack import TaskStack

# example tests. To run these tests, uncomment this file along with the example
# resource in task/task_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = TaskStack(app, "task")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
