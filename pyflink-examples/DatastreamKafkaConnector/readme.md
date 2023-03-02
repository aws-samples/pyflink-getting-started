# kafka datastream connector example for pyflink

Flink version - 1.15.2

Required libraries to add
* flink-connector-kafka-1.15.2.jar ,
* kafka-clients-3.3.1.jar

In order to run from local, download the above to jar,  add it other lib folder and then refer the path in code.
However, to run on KDA, we need to create a UBER jar with these two jars and refer to that at `jarfile` key of property group `kinesis.analytics.flink.run.options`

This example demonstrates 
* How to consume & produce records using pyflink datastream connector for kafka. 
* Serialize/Deserialize Json data
* Use of value state

