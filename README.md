# Pyflink - The Python Apache Flink Interpreter


>  🚨 “August 30, 2023: Amazon Kinesis Data Analytics has been renamed to [Amazon Managed Service for Apache Flink](https://aws.amazon.com/managed-service-apache-flink).”

--------

This repository will include code examples and walkthroughs for the following common tasks:

### Table of Contents
1. 💻 &nbsp; &nbsp; [Local Development using Pyflink](getting-started/)
2. 📦 &nbsp; &nbsp; [Packaging your Pyflink Application for use with Amazon Managed Service for Apache Flink](packaging/)
3. 🚀 &nbsp; &nbsp;  [Deploying and running your Pyflink Application to Amazon Managed Service for Apache Flink](deploying/)
4. 📄 &nbsp; &nbsp; [Logging in a Pyflink Application, and where to see those logs in Amazon Managed Service for Apache Flink](logging/)
5. 🔧 &nbsp; &nbsp; [Basic Troubleshooting and Monitoring](troubleshooting/)

<br>

--------

> ### Thank you to [@kremrik](https://github.com/kremrik/python-template/blob/master/setup.md) for the helpful miniconda instructions below.


### Prerequisites

1. Install Miniconda with Dependencies

   1. Follow the instructions [here](https://docs.conda.io/en/latest/miniconda.html) to download to your machine.

      ```bash Miniconda3-latest-MacOSX-x86_64.sh```
      
      This is for my case, but verify yours!
   2. Ensure that you prepend miniconda to your PATH, in your `.bashrc` or elsewhere:
      ```bash
      export PATH=~/miniconda3/bin:$PATH
      ``` 

      Then type:
      ```bash
      source ~/.bashrc
      ```

   3. Verify your path has been setup correctly after sourcing your .bashrc by typing:
      ```bash
      which python
      > /home/$USER/miniconda3/bin/python
      ```
      
   4. Once installed, create a virtual environment to use for your flink environment:
      ```bash
      conda create -n my-new-environment pip python=3.8
      ```

      This creates a new conda environment with pip installed. The `pip` at the end of this documentation ensures that when running `pip install` commands, they are installed to the correct location.

      I've found that python 3.9 > doesn't play nicely with some of the Apache Flink dependencies, so just specify 3.8.

   1. After creating your new environment, activate it by typing:
      ```bash
      conda activate my-new-environment
      ```
      Then verify that the correct pip is being used:
      ```bash
      which pip
      > /home/$USER/miniconda3/envs/my-new-environment/bin/pip
      ```

      Once this is set up, installing modules like `apache-flink` is as simple as typing `pip install apache-flink`, which will install it into your miniconda environment.

      Go ahead and install apache-flink since we'll need it for the rest of this exercise.

      ```bash
      (my-new-environment) $ pip install apache-flink==1.15.2
      ```

Additional Note: Please validate that you are either using Java 8 or Java 11 when running examples. There are compatibility issues with later versions of Java due to the Py4j libary calling out to the Kinesis Connector.

```bash
(my-new-environment) jdber@147dda1bd4b4 ~ % java -version
openjdk version "11.0.9.1" 2020-11-04 LTS
OpenJDK Runtime Environment Corretto-11.0.9.12.1 (build 11.0.9.1+12-LTS)
OpenJDK 64-Bit Server VM Corretto-11.0.9.12.1 (build 11.0.9.1+12-LTS, mixed mode)
```

[Continue on to Getting Started](getting-started/)!

