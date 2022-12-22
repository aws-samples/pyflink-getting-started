# -*- coding: utf-8 -*-

"""
streaming-firehose-sink.py
~~~~~~~~~~~~~~~~~~~
This module:
    1. Creates a table environment
    2. Creates a source table from a Kinesis Data Stream
    3. Creates a sink table writing to a Kinesis Data Firehose Stream
    4. Inserts the source table data into the sink table
"""

from pyflink.table import EnvironmentSettings, StreamTableEnvironment
import os
import json

# 1. Creates a Table Environment
env_settings = EnvironmentSettings.in_streaming_mode()
table_env = StreamTableEnvironment.create(environment_settings=env_settings)

APPLICATION_PROPERTIES_FILE_PATH = "/etc/flink/application_properties.json"  # on kda

is_local = (
    True if os.environ.get("IS_LOCAL") else False
)  # set this env var in your local environment

if is_local:
    # only for local, overwrite variable to properties and pass in your jars delimited by a semicolon (;)
    APPLICATION_PROPERTIES_FILE_PATH = "application_properties.json"  # local

    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    table_env.get_config().get_configuration().set_string(
        "pipeline.jars",
        "file:///" + CURRENT_DIR + "/target/aws-kinesis-analytics-python-apps-1.jar",
    )

def get_application_properties():
    if os.path.isfile(APPLICATION_PROPERTIES_FILE_PATH):
        with open(APPLICATION_PROPERTIES_FILE_PATH, "r") as file:
            contents = file.read()
            properties = json.loads(contents)
            return properties
    else:
        print('A file at "{}" was not found'.format(APPLICATION_PROPERTIES_FILE_PATH))


def property_map(props, property_group_id):
    for prop in props:
        if prop["PropertyGroupId"] == property_group_id:
            return prop["PropertyMap"]


def create_kinesis_table(table_name, stream_name, region, stream_initpos = None):
    init_pos = "\n'scan.stream.initpos' = '{0}',".format(stream_initpos) if stream_initpos is not None else ''

    return """ CREATE TABLE {0} (
                ticker VARCHAR(6),
                price DOUBLE,
                event_time TIMESTAMP(3)
              )
              WITH (
                'connector' = 'kinesis',
                'stream' = '{1}',
                'aws.region' = '{2}',{3}
                'format' = 'json',
                'json.timestamp-format.standard' = 'ISO-8601'
              ) """.format(table_name, stream_name, region, init_pos)

def create_firehose_table(table_name, stream_name, region):

    return """ CREATE TABLE {0} (
                ticker VARCHAR(6),
                price DOUBLE,
                event_time TIMESTAMP(3)
              )
              WITH (
                'connector' = 'firehose',
                'delivery-stream' = '{1}',
                'aws.region' = '{2}',
                'format' = 'json',
                'json.timestamp-format.standard' = 'ISO-8601'
              ) """.format(table_name, stream_name, region)


def main():
    # Application Property Keys
    input_property_group_key = "consumer.config.0"
    producer_property_group_key = "producer.config.0"

    input_stream_key = "input.stream.name"
    input_region_key = "aws.region"
    input_starting_position_key = "scan.stream.initpos"

    output_stream_key = "output.stream.name"
    output_region_key = "aws.region"

    # tables
    input_table_name = "ExampleInputStream"
    output_table_name = "ExampleOutputStream"

    # get application properties
    props = get_application_properties()

    input_property_map = property_map(props, input_property_group_key)
    output_property_map = property_map(props, producer_property_group_key)

    input_stream = input_property_map[input_stream_key]
    input_region = input_property_map[input_region_key]
    stream_initpos = input_property_map[input_starting_position_key]

    output_stream = output_property_map[output_stream_key]
    output_region = output_property_map[output_region_key]

    # 2. Creates a source table from a Kinesis Data Stream
    table_env.execute_sql(create_kinesis_table(input_table_name, input_stream, input_region, stream_initpos))

    # 3. Creates a sink table writing to a Kinesis Data Stream
    table_env.execute_sql(create_firehose_table(output_table_name, output_stream, output_region))

    # 4. Inserts the source table data into the sink table
    result = table_env.execute_sql("INSERT INTO {0} SELECT * FROM {1}".format(output_table_name, input_table_name))

    if is_local:
        result.wait()

if __name__ == "__main__":
    main()
