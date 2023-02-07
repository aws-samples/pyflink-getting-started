# PyFlink local testing - adding file system support for S3 buckets

In order to test S3 file sink locally, please add S3 file system plugin to PyFlink `lib` directory.

1. Download S3 file system implementation such as S3 FS Hadoop from Maven repository [here](https://mvnrepository.com/artifact/org.apache.flink/flink-s3-fs-hadoop). (Please pick a version that matches your apache-flink version.)
2. Copy the downloaded jar file (e.g. flink-s3-fs-hadoop-1.15.2.jar) to PyFlink `lib` directory.
   1. For miniconda3, the directory is at `~/miniconda3/envs/local-kda-env/lib/python3.8/site-packages/pyflink/lib/`
