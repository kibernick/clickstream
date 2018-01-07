zookeeper:
	zkserver start

kafka:
	kafka-server-start ./config/server.properties

create_topic:
	kafka-topics --zookeeper localhost:2181 --create --topic clickstream --replication-factor 1 --partitions 1

purge_topic:
	kafka-topics --zookeeper localhost:2181 --delete --topic clickstream

sample_data:
	python kafka_producer.py data/sample.csv

production_data:
	python kafka_producer.py data/production.csv

check_topic:
	kafka-console-consumer --zookeeper localhost:2181 --topic clickstream --from-beginning

spark_read:
	spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 spark_read.py localhost 9092

spark_categories:
	spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 spark_categories.py localhost 9092
