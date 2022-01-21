import builtins

from aws_cdk import aws_dynamodb as ddb
from aws_cdk import core as cdk

class DynamoDb(cdk.Stack):

    def __init__(self, scope: cdk.Construct, id_: builtins.str):

        super().__init__(scope, id_)

        pk = ddb.Attribute(
            name='pytest',
            type=ddb.AttributeType.STRING
        )
        table = ddb.Table(
            self,
            'Table',
            partition_key=pk,
            table_name='pytest'
        )
        cdk.CfnOutput(self, 'TableName', value=table.table_name)
        cdk.CfnOutput(self, 'TableArn', value=table.table_arn)