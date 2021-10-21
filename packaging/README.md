# Packaging

### Ensure you have completed or understand all the content within [getting-started](../getting-started/README.md) before continuing.

packaging your Pyflink application for deployment onto Kinesis Data Analytics for Apache Flink requires two things:

1. Python files `(getting-started.py)`
2. Any included Library files `(lib/flink-sql-connector-kinesis_2.12-1.13.2)`



What we need to do is `zip` these files into an archive, and then upload them to S3.

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