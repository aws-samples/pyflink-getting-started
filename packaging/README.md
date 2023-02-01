# Packaging

### Ensure you have completed or understand all the content within [getting-started](../getting-started/README.md) before continuing.

Packaging your Pyflink application for deployment onto Kinesis Data Analytics for Apache Flink requires three things:

1. Python files `(getting-started.py)`
2. Any required dependencies such as `boto3`.   
3. Any included jar files `(lib/flink-sql-connector-kinesis_2.12-1.13.2)`

### Including Python dependencies
Before we can archive our files, we need to look at how to include python dependencies in our application.

The following tree structure showcases what your file structure should look like with dependencies:

```bash
my-pyflink-project
│   README.md
│   python-packages.py    
│
└───my_deps
       └───boto3
       │   │   session.py
       │   │   utils.py
       │   │   ...
       │   
       └───botocore
       │   │   args.py
       │   │   auth.py
       │    ...
       └───mynonpypimodule
       │   │   mymodulefile1.py
       │   │   mymodulefile2.py
            ...
└───lib
│    │ flink-sql-connector-kinesis_2.11-1.13.2.jar 
│    │ ...
...
```

*For PyPi dependencies*, copy the files and folders located within your python environment's `site-packages` folder as shown in the folder structure above. These instructions assume you are using [miniconda](https://docs.conda.io/en/latest/miniconda.html) for your environment management as described in [getting-started](../getting-started/README.md). 

The location of the `site-packages` folder for a `conda` environment is `~/miniconda3/envs/<<env-name>>/lib/python<<version>>/site-packages` Replace `<<env-name>>` with the name of your conda environment.

#### How do I avoid including unnecessary packages without missing transitive dependencies?
For example, if your application depends on [`boto3`](https://github.com/boto/boto3), it in turn references [`botocore`](https://github.com/boto/botocore). `botocore` is a *transitive dependency* of `boto3`. Accounting for this, we recommend the following approach:

1. Create a standalone Python environment (conda or similar) on your local machine.
2. Take note of the initial list of packages that your application requires.
3. Now, `pip install` all dependencies that your application requires.
4. Note the packages added to the `site-packages` folder after step 3 above. These are the folders you need to include in your package (under `my_deps` folder), organized as shown above. Essentially, you are capturing a **diff** of the packages between steps 2 and 3 above to identify the right package dependencies for your application.
5. Supply `my_deps/` as an argument for the `pyFiles` property in the `kinesis.analytics.flink.run.options` property group as described below for the `jarfiles` property. Flink also allows you to specify python dependencies using the [`add_python_file` function](https://nightlies.apache.org/flink/flink-docs-master/docs/dev/python/dependency_management/#python-dependencies), but it is important to specify one or the other of these options, ***not both***.

Lastly, you can also include your own dependencies via the same method--placing the corresponding Python files in `my_deps`. 

**Note:** You do not need to name your folder `my_deps`; the important piece is registering the dependencies using either `pyFiles` or `add_python_file`.


### Jar dependencies
If your application depends on a connector, be sure to include the connector jar (e.g. `flink-sql-connector-kinesis_2.11-1.13.2.jar`) in your package; under the lib folder in the tree structure shown above. Note that you don't have to name the folder lib, you just have to include it somewhere in your package and also ensure that you specify the jar dependency using the jarfile property as described below. Make sure the connector version corresponds to the appropriate Apache Flink version in your Kinesis Data Analytics application.

If you have multiple dependencies, you have to create a fat jar and then include it using the jarfile property as described below. This is a Flink requirement as described [here](https://nightlies.apache.org/flink/flink-docs-master/docs/dev/python/dependency_management/#jar-dependencies).

Important: In addition to including the jar dependency in your package, you have to specify dependencies using the jarfile property in the kinesis.analytics.flink.run.options property group when you create your application. Please see the "Configure the Application" section [here](https://docs.aws.amazon.com/kinesisanalytics/latest/java/gs-python-createapp.html#gs-python-7).



### Creating zip archive

What we need to do is `zip` these files into an archive, and then upload them to S3. 

**DON'T** use the compress tool in Finder or Windows Explorer, which will create an invalid code package for Kinesis Data Analytics.

| 📓 Add `.zip`  to your .gitignore to not mistakenly commit zip files to git.  |
|-----------------------------------------|

| ⚠️ Make sure you modify the sink back to _not_ use the print connector from Getting Started, and rather write to Kinesis since we'll be running on Kinesis Data Analytics and not locally. |
|-----------------------------------------|



<br><br>
From Pycharm, at the bottom of the IDE you should see a tab called `Terminal`. Click on that, and type `ls` to ensure you see this project.

```bash
ls
(my-new-environment) jdber@147dda1bd4b4 pyflink-training-session % ls
README.md               datagen                 img                     pyflink-examples
```

Next, type 

```bash
> cd pyflink-examples
> zip -r GettingStarted.zip pyflink-examples/GettingStarted



(my-new-environment) jdber@147dda1bd4b4 pyflink-training-session % zip -r GettingStarted.zip pyflink-examples/GettingStarted
  adding: pyflink-examples/GettingStarted/ (stored 0%)
  adding: pyflink-examples/GettingStarted/getting-started.py (deflated 68%)
  adding: pyflink-examples/GettingStarted/application_properties.json (deflated 56%)
  adding: pyflink-examples/GettingStarted/lib/ (stored 0%)
  adding: pyflink-examples/GettingStarted/lib/flink-sql-connector-kinesis_2.12-1.13.2 (deflated 8%)
```

This will create a file called `GettingStarted.zip` with the getting-started.py file, a lib folder with the kinesis connector, and an unused application_properties.json--you can choose to omit this if you'd like.


This is how you package a pyflink project for Kinesis Data Analytics for Apache Flink!

Now let's [Deploy](../deploying/) the application.