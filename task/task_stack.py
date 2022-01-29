from aws_cdk import (
    Duration,
    Stack,
   CfnOutput,
   aws_sqs as sqs,
   aws_s3 as s3
)
from constructs import Construct


class TaskStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        queue = sqs.Queue(
            self, "StaticappQueue",
            visibility_timeout=Duration.seconds(300),
         )

        bucket = s3.Bucket(self,"sitebucket",bucket_name="bukd4323",public_read_access=True,
        website_index_document="index.html")

       