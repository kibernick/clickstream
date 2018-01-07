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

## Quickstart

See the `make` commands in ![Makefile](./Makefile) for running the services locally.

## Troubleshooting

### `java.lang.NullPointerException` when running `spark-shell`

Spark is incompatible with Java 9, which is the version brew cask install java will install if it is up to date. If you did install Java 9, what you need to do is install Java 8 instead:

```bash
$ brew cask uninstall java
$ brew tap caskroom/versions
$ brew cask search java
$ brew cask install java8
```
