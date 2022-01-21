import json
import re

from aws_cdk.assertions import Capture, Match, Template
import pytest

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

@pytest.fixture
def test_outputs():
    outputs_values = Capture()
    return template.find_outputs('*', props=outputs_values)


def test_outputs_logical_ids(test_outputs):
    found = []
    for output in test_outputs:
        found.append(re.search('(TableName|TableArn)', output))
    assert all(found)

def test_outputs_values(test_outputs):
    found = []
    for output in test_outputs.values():
        value = output['Value']
        value_toassert = json.dumps(value)
        found.append(re.search('(Ref|Arn)', value_toassert))

    assert all(found)