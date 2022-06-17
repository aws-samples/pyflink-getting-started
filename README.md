# Pyflink - The Python Apache Flink Interpreter

This repository will include code examples and walkthroughs for the following common tasks:


> ### Thank you to [@kremrik](https://github.com/kremrik/python-template/blob/master/setup.md) for the helpful miniconda instructions below.


<br>

### Table of Contents
1. 💻 &nbsp; &nbsp; [Local Development using Pyflink](getting-started/)
2. 📦 &nbsp; &nbsp; [Packaging your Pyflink Application for use with Kinesis Data Analytics for Apache Flink](packaging/)
3. 🚀 &nbsp; &nbsp;  [Deploying and running your Pyflink Application to Kinesis Data Analytics for Apache Flink](deploying/)
4. 📄 &nbsp; &nbsp; [Logging in a Pyflink Application, and where to see those logs in Kinesis Data Analytics for Apache Flink](logging/)
5. 🔧 &nbsp; &nbsp; [Basic Troubleshooting and Monitoring](troubleshooting/)

<br>

--------


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
      (my-new-environment) $ pip install apache-flink==1.13.6
      ```


[Continue on to Getting Started](getting-started/)!

