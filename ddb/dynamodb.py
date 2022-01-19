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
        ddb.Table(
            self,
            'Table',
            partition_key=pk,
            table_name='pytest'
        )