# Clickstream

Sample project that processes clickstream data using Kafka and Apache Spark.

Install `scala`, `kafka` and `apache-spark` using homebrew.

```bash
export JAVA_HOME="$(/usr/libexec/java_home)"
export PATH=$JAVA_HOME:$PATH

export SCALA_HOME="/usr/local/Cellar/scala/2.12.4"  # find it using `brew info`
export PATH=$SCALA_HOME/bin:$PATH
```

Make sure that `/usr/local/bin` is also added to your `$PATH`.

Use `pyenv` or similar to manage your python versions and virtual environments. After creating a virtual environment, install dependencies with: `pip install -r requirements.txt`.

To use production data, copy the CSV file into `data/production.csv`.

## Quickstart

See the `make` commands in ![Makefile](./Makefile) for running the services locally.

### iterm walkthrough

1. Start Zookeeper: `make zookeeper`
2. Start Kafka: `make kafka`
3. New tab, create the `clickstream` topic with `make create_topic` (unless it already exists).
4. Start the simple Spark stream that monitors the `clickstream` topic and prints the messages to the command line: `make spark_read`
5. New tab, stream some sample data to Kafka: `make sample_data`
6. The sample data should appear in the simple stream in the previous tab.
7. Make sure that your production data (a really big CSV) is found under `data/production.csv`
8. Start importing production data with `make production_data`
9. Start the categories stream with `make spark_categories`
10. The categories should appear counted, with the sliding interval of 10 seconds.
11. The output of the previous stream should also appear writen to the file system in the `output` directory.

## TODO

* Remove log4j logs! Could not find a way to use the ![log4j.properties](./config/log4j.properties) with the `spark-submit` command.
* Continue with setting up Docker. Likely by creating a new Docker image, with Spark and Python3 on it.
