from aws_cdk.assertions import Template, Match

from ddb.dynamodb import DynamoDb
from tests import app

stack_ = DynamoDb(app, 'DynamoDb')
template = Template.from_stack(stack_)
DYNAMODB_TABLE = 'AWS::DynamoDB::Table'

def test_keyschema():
    template.has_resource_properties(
        DYNAMODB_TABLE,
        {'KeySchema': Match.array_equals(
            [{'AttributeName': 'pytest', 'KeyType': 'HASH'}]
        )}
    )

def test_resource_count():
    template.resource_count_is(DYNAMODB_TABLE, 1)

def test_table_name():
    template.has_resource_properties(
        DYNAMODB_TABLE,
        {'TableName': Match.exact('pytest')}
    )

# creating creating